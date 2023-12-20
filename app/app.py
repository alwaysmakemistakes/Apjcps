from flask import Flask, Blueprint, render_template, abort, send_from_directory, request, session, flash, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user
from datetime import datetime, timedelta
#урааааааааааа cooommiiit
#урааа коммиттт 2узадсвщзхсбцщзхвуч
#test3

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from auth import bp as auth_bp, init_login_manager, permission_check, login_required
from plastinkas import bp as plastinka_bp

app.register_blueprint(auth_bp)
app.register_blueprint(plastinka_bp)


from logs import bp as logs_bp
app.register_blueprint(logs_bp)


init_login_manager(app)

from models import Plastinka, Image, Genre, Review, PlastinkaVisits, User
from tools import PlastinkaFilter
PER_PAGE = 10

def search_params():
    return {
        'name': request.args.get('name'),
        'genre_ids': request.args.getlist('gennre_ids'),
    }


# # Сортировка по убыванию
# def sort_pagination(query, page):
#     query = query.order_by(Plastinka.year.desc())
#     return query

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    query = Plastinka.query

    plastinkas = PlastinkaFilter(**search_params()).perform()

    # Фильтрация по параметрам поиска    
    name = request.args.get('name')
    genre_ids = request.args.getlist('genre_id')
    year = request.args.get('year')
    min_volume = request.args.get('min_volume')
    max_volume = request.args.get('max_volume')
    author = request.args.get('author')

    if name:
        # Применение фильтрации по названию пластинки (поиск с учетом регистра без учета регистра)
        query = query.filter(Plastinka.name.ilike(f'%{name}%'))
    if genre_ids:
        # Применение фильтрации по идентификаторам жанров (пластинки должны иметь хотя бы один из указанных жанров)
        query = query.filter(Plastinka.genres.any(Genre.id.in_(genre_ids)))
    if year:
        # Применение фильтрации по году выпуска пластинки
        query = query.filter(Plastinka.year == year)
    if min_volume:
        # Применение фильтрации по минимальному объему пластинки
        query = query.filter(Plastinka.volume >= min_volume)
    if max_volume:
        # Применение фильтрации по максимальному объему пластинки
        query = query.filter(Plastinka.volume <= max_volume)
    if author:
        # Применение фильтрации по автору пластинки (поиск с учетом регистра без учета регистра)
        query = query.filter(Plastinka.author.ilike(f'%{author}%'))

# Формирование списка годов исходя из содержимого БД
    years = db.session.query(Plastinka.year.distinct()).order_by(Plastinka.year).all()
    years = [str(year[0]) for year in years]

#  DISTINC нужен для получения уникальных занчений
    # query = sort_pagination(query, page)

    # Создание объекта пагинации и получение списка книг для текущей страницы
    pagination = query.paginate(page, PER_PAGE, error_out=False)
    plastinkas = pagination.items

    images = Image.query.all()
    genres = Genre.query.all()

    return render_template('index.html',  plastinkas=plastinkas, images=images, genres=genres, years=years, pagination=pagination, search_params=search_params())

# коммент

@app.route('/image/<image_id>')
def image(image_id):
    # Получение объекта изображения по идентификатору
    image = Image.query.get(image_id)
    if image is None:
        # Если объект изображения не найден, возвращается HTTP-ошибка 404
        abort(404)
    # Отправка файла изображения из указанной директории на сервере
    return send_from_directory(app.config['UPLOAD_FOLDER'], image.storage_filename)






































# @app.route('/logs/logsbase')
# def logsbase():
#     return render_template('logs/logsbase.html')

# @app.route('/logs/users_statistics')
# def user_statistics():
#     return render_template('logs/users_statistics.html')

# @app.route('/logs/plastinkas_statistics')
# def plastinkas_statistics():
#     return render_template('logs/plastinkas_statistics.html')













# #  Создание логов для книги
# def creating_plastinka_visits(user_id, plastinka_id):
#     try:
#         visit_log_params = {
#             'user_id': user_id,
#             'plastinka_id': plastinka_id,
#         }
#         db.session.add(PlastinkaVisits(**visit_log_params))
#         db.session.commit()
#     except:
#         db.session.rollback()


# def creating_last_plastinka_log(plastinka_id, user_id):
#     new_log = None

#     # Извлекаем данные, когда пользователь последний раз получал доступ
#     plastinka_log = (LastPlastinkaVisits.query
#                    # Фильтруем по конкретной книге
#                    .filter_by(plastinka_id=plastinka_id)  
#                    # Фильтруем по конкретному пользователю
#                    .filter_by(user_id=current_user.id) 
#                    .first())
#     if plastinka_log:
#         # У найденой записи обновляем время доступа
#         plastinka_log.created_at = db.func.now()
#     # Если пользователь еще не получал доступа к книге,
#     # то создаем новую запись
#     else:
#         new_log = LastPlastinkaVisits(plastinka_id=plastinka_id, user_id=user_id)
   
#     # Если была создана запись
#     if new_log:
#         try:
#             db.session.add(new_log)
#             db.session.commit()
#         except:
#             db.session.rollback()


# def save_last_plastinkas(plastinka_id):
#     data_from_cookies = session.get('last_plastinkas')

#     if data_from_cookies:
#         if plastinka_id in data_from_cookies:
#             data_from_cookies.remove(plastinka_id)
#             data_from_cookies.insert(0, plastinka_id)
#         else:
#             data_from_cookies.insert(0, plastinka_id)
    
#     # Если логов ранее не было сохранено
#     if not data_from_cookies:
#         data_from_cookies = [plastinka_id]

#     session['last_plastinkas'] = data_from_cookies



# @app.before_request
# @login_required
# @permission_check("create")
# def loger():
#     if (request.endpoint == 'static'
#         or request.endpoint == 'image'
#             or request.endpoint == 'users_statistics'):
#         return
#     if request.endpoint == 'show':
#         # Если пользователь анонимен, то необходимо
#         # лог запись сохранять в куки
#         if current_user.is_anonymous:
#             save_last_plastinkas(request.view_args.get('plastinka_id'))
#         if current_user.is_authenticated:
#             creating_last_plastinka_log(request.view_args.get('plastinka_id'),
#                                    current_user.id)
#         plastinka_visit_logs_params = {
#             'user_id': current_user.get_id(),
#             'plastinka_id': request.view_args.get('plastinka_id'),
#         }
#         start = datetime.now() - timedelta(days=1)
#         today_visits = (PlastinkaVisits.query
#                         .filter_by(plastinka_id=request.view_args.get('plastinka_id'))
#                         .filter(start <= PlastinkaVisits.created_at))
#         if current_user.is_authenticated:
#             today_visits = today_visits.filter_by(
#                 user_id=current_user.get_id())
#         else:
#             today_visits = today_visits.filter(PlastinkaVisits.user_id.is_(None))
#         today_visits_int = len(today_visits.all())
#         # < 10, т.к. нумерация идет с 0
#         if today_visits_int < 10:
#             try:
#                 db.session.add(PlastinkaVisits(**plastinka_visit_logs_params))
#                 db.session.commit()
#             except:
#                 db.session.rollback()
