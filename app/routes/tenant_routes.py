from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from datetime import datetime

from .auth_routes import require_auth
from ..domain.enums import UserRole, PaymentStatus

tenant_bp = Blueprint("tenant", __name__)


def get_services():
    """Helper para obtener servicios desde el contexto de la app"""
    from flask import current_app
    return current_app.config.get('deps', {})


def get_current_user_id():
    """Obtiene el ID del usuario actual desde la sesión"""
    return session.get('user_id')


@tenant_bp.route("/dashboard")
@require_auth
def dashboard():
    """Panel del inquilino"""
    user_id = get_current_user_id()
    deps = get_services()
    
    payment_service = deps.get('payment_service')
    report_service = deps.get('report_service')
    
    payments = []
    reports = []
    
    if payment_service:
        payments = payment_service.get_payments_by_tenant(user_id)
    
    if report_service:
        reports = report_service.get_reports_by_tenant(user_id)
    
    return render_template(
        "tenant/dashboard.html",
        payments=payments,
        reports=reports
    )


@tenant_bp.route("/payment/new", methods=["GET", "POST"])
@require_auth
def new_payment():
    """Crear un nuevo pago"""
    user_id = get_current_user_id()
    deps = get_services()
    
    if request.method == "POST":
        amount = request.form.get("amount")
        month = request.form.get("month")
        notes = request.form.get("notes", "")
        
        # Obtener department_id del usuario
        auth_service = deps.get('auth_service')
        if auth_service:
            user = auth_service.get_user_by_id(user_id)
            if not user or not user.department_id:
                flash("No tienes un departamento asignado", "error")
                return redirect(url_for("tenant.dashboard"))
            
            department_id = user.department_id
            payment_service = deps.get('payment_service')
            
            try:
                payment = payment_service.create_payment(
                    tenant_id=user_id,
                    department_id=department_id,
                    amount=float(amount),
                    month=month,
                    notes=notes
                )
                flash("Pago registrado correctamente. Sube el comprobante para completar.", "success")
                return redirect(url_for("tenant.upload_receipt", payment_id=payment.id))
            except ValueError as e:
                flash(str(e), "error")
            except Exception as e:
                flash(f"Error al crear el pago: {str(e)}", "error")
    
    # GET: mostrar formulario
    return render_template("tenant/new_payment.html")


@tenant_bp.route("/payment/<payment_id>/receipt", methods=["GET", "POST"])
@require_auth
def upload_receipt(payment_id: str):
    """Subir comprobante de pago"""
    user_id = get_current_user_id()
    deps = get_services()
    payment_service = deps.get('payment_service')
    
    # Verificar que el pago pertenece al usuario
    payment = payment_service.get_payment_by_id(payment_id)
    if not payment or payment.tenant_id != user_id:
        flash("Pago no encontrado", "error")
        return redirect(url_for("tenant.dashboard"))
    
    if request.method == "POST":
        if 'receipt' not in request.files:
            flash("No se seleccionó ningún archivo", "error")
            return render_template("tenant/upload_receipt.html", payment=payment)
        
        file = request.files['receipt']
        if file.filename == '':
            flash("No se seleccionó ningún archivo", "error")
            return render_template("tenant/upload_receipt.html", payment=payment)
        
        try:
            file_content = file.read()
            if len(file_content) == 0:
                flash("El archivo está vacío", "error")
                return render_template("tenant/upload_receipt.html", payment=payment)
            
            # Validar tamaño (máx 10MB)
            max_size = 10 * 1024 * 1024  # 10MB
            if len(file_content) > max_size:
                flash("El archivo es demasiado grande. Máximo 10MB", "error")
                return render_template("tenant/upload_receipt.html", payment=payment)
            
            updated_payment = payment_service.upload_receipt(
                payment_id=payment_id,
                file_content=file_content,
                file_name=file.filename
            )
            if updated_payment:
                flash("Comprobante subido correctamente", "success")
                return redirect(url_for("tenant.dashboard"))
            else:
                flash("Error al subir el comprobante", "error")
        except Exception as e:
            flash(f"Error: {str(e)}", "error")
    
    return render_template("tenant/upload_receipt.html", payment=payment)


@tenant_bp.route("/report/new", methods=["GET", "POST"])
@require_auth
def new_report():
    """Crear un nuevo reporte"""
    user_id = get_current_user_id()
    deps = get_services()
    
    auth_service = deps.get('auth_service')
    if not auth_service:
        flash("Error en el servicio", "error")
        return redirect(url_for("tenant.dashboard"))
    
    user = auth_service.get_user_by_id(user_id)
    if not user or not user.department_id:
        flash("No tienes un departamento asignado", "error")
        return redirect(url_for("tenant.dashboard"))
    
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        
        report_service = deps.get('report_service')
        try:
            report = report_service.create_report(
                tenant_id=user_id,
                department_id=user.department_id,
                title=title,
                description=description
            )
            flash("Reporte creado correctamente", "success")
            return redirect(url_for("tenant.dashboard"))
        except ValueError as e:
            flash(str(e), "error")
        except Exception as e:
            flash(f"Error al crear el reporte: {str(e)}", "error")
    
    return render_template("tenant/new_report.html")
