# from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
# from models import User
# from users_policy import UsersPolicy

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models import User
from users_policy import UsersPolicy
from functools import wraps








bp = Blueprint('auth', __name__, url_prefix='/auth')


def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации.'
    login_manager.login_message_category = 'warning'
    login_manager.user_loader(load_user)
    login_manager.init_app(app)


class UserMix(UserMixin):
    def __init__(self, user_id, user_login, role_id):
        self.id = user_id
        self.login = user_login
        self.role_id = role_id

    def is_admin(self):
        return self.role_id == current_app.config['ADMIN_ROLE_ID']

    def can(self, action, record = None):
        users_policy = UsersPolicy(record)
        method = getattr(users_policy, action, None)
        if method:
            return method()
        return False

def load_user(user_id):
    user = User.query.get(user_id)
    return user




@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login and password:
            user = User.query.filter_by(login=login).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Вы успешно аутентифицированы.', 'success')
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash('Введены неверные логин и/или пароль.', 'danger')
    return render_template('login.html')

from models import Plastinka, Image, Genre, Review, PlastinkaVisits, User, Role
from tools import PlastinkaFilter

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

def permission_check(action):
    def decor(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            user_id = kwargs.get('user_id')
            user = None
            if user_id:
                user = load_user(user_id)
            if not current_user.can(action, user):
                flash('Недостаточно прав', 'warning')
                return redirect(url_for('index'))
            return function(*args, **kwargs)
        return wrapper
    return decor







from app import db


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        role_id = request.form.get('role')

        # Проверка на существующего пользователя по логину
        existing_user = User.query.filter_by(login=login).first()
        if existing_user:
            flash('Пользователь с таким логином уже существует.', 'danger')
        else:
            # Создание нового пользователя и сохранение в базе данных
            user = User(login=login, last_name=last_name, first_name=first_name, middle_name=middle_name, role_id=role_id)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Регистрация успешно завершена. Вы можете войти в систему.', 'success')
            return redirect(url_for('auth.login'))
    
    # Отображение страницы регистрации
    return render_template('newuser/add_user.html')


@bp.route('/lk')
@login_required
def lk():
    reviews = Review.query.filter_by(user_id=current_user.id).all()

    # Получите объект роли пользователя из базы данных
    user_role = Role.query.get(current_user.role_id)

    return render_template('lk.html', reviews=reviews, user=current_user, user_role=user_role)


from flask import request, flash, redirect, url_for
from werkzeug.security import check_password_hash

@bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if not current_password or not new_password or not confirm_password:
            flash('Заполните все поля.', 'danger')
        elif not check_password_hash(current_user.password_hash, current_password):
            flash('Неверный текущий пароль.', 'danger')
        elif new_password != confirm_password:
            flash('Пароли не совпадают.', 'danger')
        else:
            # Обновите пароль пользователя в базе данных
            current_user.set_password(new_password)
            db.session.commit()
            flash('Пароль успешно изменен.', 'success')
            return redirect(url_for('auth.lk'))

    return render_template('change_password.html')

@bp.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)

    if request.method == 'POST':
        new_login = request.form['login']
        # Проверка на уникальность логина
        existing_user = User.query.filter(User.login == new_login).filter(User.id != user_id).first()
        if existing_user:
            flash('Логин уже занят. Выберите другой логин.', 'danger')
        else:
            user.first_name = request.form['first_name']
            user.last_name = request.form['last_name']
            user.middle_name = request.form['middle_name']
            user.login = new_login  # Обновляем логин после проверки на уникальность
            db.session.commit()
            flash('Профиль обновлен успешно', 'success')
            return redirect(url_for('auth.lk'))

    # Если метод запроса не POST, покажите форму редактирования
    return render_template('edit_user.html', user=user)

@bp.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    if request.method == 'POST':
        user = User.query.get(current_user.id)
        if user:
            # Удаление пользователя и всех связанных данных
            db.session.delete(user)
            db.session.commit()
            flash('Ваш аккаунт был успешно удален.', 'success')
            logout_user()  # Разлогинивание пользователя
            return redirect(url_for('auth.login'))

    return render_template('delete_account.html')

