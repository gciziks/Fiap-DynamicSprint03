from flask import Flask
from models import db
from routes.auth import auth_bp
from routes.class_routes import class_bp
from routes.dashboard import dashboard_bp
from routes.menu import menu_bp

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando as blueprints criadas
app.register_blueprint(auth_bp)
app.register_blueprint(class_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(menu_bp)

# Executando a aplicação

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
