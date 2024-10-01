from flask import Blueprint


# Inicializa/Cria as blueprints da aplicação
auth_bp = Blueprint('auth', __name__)
class_bp = Blueprint('class', __name__)
dashboard_bp = Blueprint('dashboard', __name__)
menu_bp = Blueprint('menu', __name__) 