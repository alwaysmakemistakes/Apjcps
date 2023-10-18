from flask import Blueprint, render_template, request
from flask_login import login_required
from app import db, app
from models import PlastinkaVisits, Plastinka
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