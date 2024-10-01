from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from . import auth_bp
from models import db
from logger.log import LogClass

# Inicializa a classe de log
log = LogClass() 


# Rota para a página de login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Verifica se os campos email e senha foram preenchidos
        if not email or not password:
            flash('Preencha todos os campos!')
            return render_template('login.html')

        # Processa o login
        user = User.query.filter_by(email=email).first()

        # Verifica se o usuário existe e se a senha está correta
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['role'] = user.role
            
            log.add_log(f"Usuário {user.email} logou.")
            
            return redirect('/dashboard')
        else:
            log.add_log(f"Tentativa de login falha no email: {email}.")
            flash('Email ou senha inválida. Tente novamente!.')
    
    return render_template('login.html')

# Rota para deslogar
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    return redirect('/')


# Rota para registro de alunos
@auth_bp.route('/register_student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        # Cria um novo objeto User(model criado anteriormente) para o aluno
        new_student = User(name=name, email=email, password=password, role='student')
        db.session.add(new_student) # Adiciona o novo aluno  à sessão do banco de dados
        db.session.commit() # Confirma a adição no banco de dados
        
        log.add_log(f"Novo aluno registrado: {email}.")
        
        return redirect('/')
    return render_template('add_student.html')


# Rota para registro de professores
@auth_bp.route('/register_teacher', methods=['GET', 'POST'])
def register_teacher():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
         # Cria um novo objeto User para o professor
        new_teacher = User(name=name, email=email, password=password, role='teacher')
        db.session.add(new_teacher) # Adiciona o novo professor à sessão do banco de dados
        db.session.commit() # Confirma a adição no banco de dados
        
        log.add_log(f"Novo professor registrado: {email}.")
        
        return redirect('/')
    return render_template('add_teacher.html')
