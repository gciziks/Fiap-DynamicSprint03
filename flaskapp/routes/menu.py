from flask import render_template
from . import menu_bp

# Rota inicial da aplicação - Menu Principal
@menu_bp.route('/')
def menu():
    return render_template('menu.html')
