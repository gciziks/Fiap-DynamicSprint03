from flask import render_template, session, redirect
from models.user import User
from models.classm import ClassM
from . import dashboard_bp

# Rota para acessar o dashboard (Do professor)
@dashboard_bp.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect('/')
    
    user = User.query.get(session['user_id'])
    if user.role == 'teacher':
        classes = ClassM.query.filter_by(teacher_id=user.id).all()
        return render_template('dashboard.html', classes=classes, role=user.role)
    else:
        student_classes = user.classes
        return render_template('dashboard.html', classes=student_classes, role=user.role)
