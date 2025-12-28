from flask import Blueprint, render_template

visitor_bp = Blueprint("visitor", __name__)

@visitor_bp.route("/")
def home():
    # Datos fake para la demo inicial
    departments = [
        {
            "id": "1",
            "title": "Departamento Centro",
            "address": "Av. Principal 123",
            "price": 350
        },
        {
            "id": "2",
            "title": "Departamento Norte",
            "address": "Calle Secundaria 456",
            "price": 420
        }
    ]

    return render_template(
        "visitor/departments.html",
        departments=departments
    )
