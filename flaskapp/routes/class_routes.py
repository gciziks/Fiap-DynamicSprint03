from flask import render_template, request, redirect, url_for, session, flash
from models.classm import ClassM, ClassStudent
from models.user import User
from . import class_bp
from models import db
from logger.log import LogClass

# Inicializa a classe de log
log = LogClass()

# Rota para criar turma
@class_bp.route('/create_class', methods=['GET', 'POST'])
def create_class():
    if session.get('role') != 'teacher':
        return redirect('/dashboard')
    
    if request.method == 'POST':
        class_name = request.form['class_name']

        # Cria um novo objeto ClassM(model criado anteriormente) para a turma 
        new_class = ClassM(name=class_name, teacher_id=session['user_id'])
        
        db.session.add(new_class)
        db.session.commit()
        
        log.add_log(f"Nova turma '{class_name}' criada pelo professor de ID: {session['user_id']}.")
        
        return redirect('/dashboard')
    
    return render_template('create_class.html')

# Rota para gerenciar a turma
@class_bp.route('/manage_class/<int:class_id>')
def manage_class(class_id):
    if session.get('role') != 'teacher':
        return redirect('/dashboard')
    
    class_ = ClassM.query.get(class_id) # Query para pegar o ID da turma que será gerenciada
    return render_template('manage_classes.html', class_=class_)

# Rota para adicionar aluno a turma
@class_bp.route('/add_student_to_class/<int:class_id>', methods=['POST'])
def add_student_to_class(class_id):
    if session.get('role') != 'teacher':
        return redirect('/dashboard')

    student_email = request.form['student_email']
    student = User.query.filter_by(email=student_email, role='student').first()

    if student:
        class_ = ClassM.query.get(class_id)
        class_.students.append(student)
        db.session.commit()
        
        log.add_log(f"Aluno {student_email} adicionado a turma de ID: {class_id}.")
        
        return redirect('/dashboard')
    else:
        log.add_log(f"Tentativa falha de adicionar aluno {student_email} a turma de ID: {class_id}. (Email inválido)")
        flash('Aluno não encontrado.')
        return redirect(f'/manage_class/{class_id}')

