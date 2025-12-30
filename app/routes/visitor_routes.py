from flask import Blueprint, render_template, current_app

visitor_bp = Blueprint("visitor", __name__)

@visitor_bp.route("/")
def home():
    service = current_app.extensions["container"]["department_service"]
    departments = service.list_public()
    return render_template(
        "visitor/departments.html",
        departments=departments
    )
