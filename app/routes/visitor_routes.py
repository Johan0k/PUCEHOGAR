<<<<<<< HEAD
from flask import Blueprint, render_template, current_app
=======
from flask import Blueprint, render_template
>>>>>>> parent of 5d29c1f (Project Updated)

visitor_bp = Blueprint("visitor", __name__)

@visitor_bp.route("/")
def home():
<<<<<<< HEAD
    service = current_app.extensions["container"]["department_service"]
    departments = service.list_public()
=======
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

>>>>>>> parent of 5d29c1f (Project Updated)
    return render_template(
        "visitor/departments.html",
        departments=departments
    )
