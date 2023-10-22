# from flask import Blueprint, render_template, request
# from flask_login import login_required

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from app import db, app
from models import PlastinkaVisits, Plastinka, User, Review
from auth import permission_check

bp = Blueprint('logs', __name__, url_prefix='/logs')


# Статистика по пользователям
@bp.route('/users_statistics')
@login_required
@permission_check('get_logs')
def users_statistics():
    page = request.args.get('page', 1, type=int)
    logs = PlastinkaVisits.query.order_by(PlastinkaVisits.created_at.desc())
    pagination = logs.paginate(page=page, per_page=app.config['LOGS_PER_PAGE'])
    logs = pagination.items
    return render_template('logs/users_statistics.html',
                           logs=logs,
                           pagination=pagination)


# Статистика по пластинкам
@bp.route('/plastinkas_statistics')
@login_required
@permission_check('get_logs')
def plastinkas_statistics():
    page = request.args.get('page', 1, type=int)
    plastinkas_stat_data = db.session.query(PlastinkaVisits.plastinka_id, db.func.count(PlastinkaVisits.id)).group_by(PlastinkaVisits.plastinka_id).order_by(db.func.count(PlastinkaVisits.id).desc())
    pagination = plastinkas_stat_data.paginate(page=page, per_page=app.config['LOGS_PER_PAGE'])
    plastinkas_stat_data = pagination.items
    data_for_render = []
    for plastinka_id, count in  plastinkas_stat_data:
        data_for_render.append((Plastinka.query.get(plastinka_id), count))

    print(data_for_render)
    
    return render_template('logs/plastinkas_statistics.html',
                           logs=data_for_render,
                           pagination=pagination)


@bp.route('/list_users')
@login_required
@permission_check('list_users') 
def list_users():
    # Получите список всех пользователей из базы данных
    users = User.query.all()

    # Отобразите список пользователей на странице
    return render_template('logs/users.html', users=users)



@bp.route('/view_user/<int:user_id>')
@login_required
@permission_check('view_user') 
def view_user(user_id):
    user = User.query.get(user_id)
    if user:
        reviews = Review.query.filter_by(user_id=user.id).all()
        return render_template('logs/view_user.html', user=user, reviews=reviews)
    else:
        flash('Пользователь не найден', 'danger')
        return redirect(url_for('logs/view_user.html'))

# @bp.route('/delete_user/<int:user_id>', methods=['POST'])
# @login_required
# def delete_user(user_id):
#     user = User.query.get(user_id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         flash('Пользователь успешно удален.', 'success')
#     else:
#         flash('Пользователь не найден.', 'danger')
#     return redirect(url_for('logs.users'))

