from flask import Blueprint, render_template, request, flash, redirect, url_for, abort, send_from_directory, session
from app import db
from models import *
from flask_login import current_user, login_required, current_user
from sqlalchemy import func
from tools import ImageSaver
from auth import permission_check
import markdown
import bleach
from datetime import datetime, timedelta

bp = Blueprint('plastinkas', __name__, url_prefix='/plastinkas')


PLASTINKA_PARAMS = [
    'name', 'author', 'year', 'description', 'publisher', 'volume', 'genres'
]

def params():
    plastinka_params = { p: request.form.get(p) for p in PLASTINKA_PARAMS }
    genre_ids = request.form.getlist('genres')
    genres = Genre.query.filter(Genre.id.in_(genre_ids)).all()
    plastinka_params['genres'] = genres
    return plastinka_params




@bp.route('/add_plastinka', methods=['GET', 'POST'])
@login_required
@permission_check("create")
def add_plastinka():
    genres = Genre.query.all()
    plastinka = Plastinka()  # Создание нового экземпляра пластинки
    if request.method == 'POST':
        return redirect(url_for('plastinkas.create_plastinka'))
    return render_template('add_plastinka.html', genres=genres, plastinka=plastinka)



@bp.route('/create_plastinka', methods=['POST'])
@login_required
@permission_check("create")
def create_plastinka():
    try:
        f = request.files.get('background_img')
        if f and f.filename:
            img = ImageSaver(f).save()
            image_id = img.id  # Получение идентификатора сохраненного изображения
        
                # Проверка наличия обязательных полей
        if not request.form.get('name') or not request.form.get('author') or not request.form.get('genres') or \
           not request.form.get('year') or not request.form.get('description') or not request.form.get('publisher'):
            flash('Заполните все обязательные поля.', 'danger')
            return redirect(url_for('index'))



        genre_name = request.form.get('genres')  # Получение выбранного названия жанра

        # Проверка наличия жанра и его добавление к книге
        if genre_name:
            genre = Genre.query.filter_by(name=genre_name).first()
            if genre:
                plastinka_genre = PlastinkaGenre(plastinka=plastinka, genre=genre)  # Создание записи в связующей таблице
                db.session.add(plastinka_genre)

        plastinka = Plastinka(**params(), id_image=image_id)

        description = bleach.clean(request.form.get('description'))
        plastinka.description = description

        bleach.clean(plastinka.description) 

        db.session.add(plastinka)
        db.session.commit()

        flash(f'пластинка {plastinka.name} была успешно добавлена!', 'success')
        return redirect(url_for('index'))

    except:
        db.session.rollback()
        flash('При сохранении данных возникла ошибка. Проверьте корректность введенных данных.', 'danger')
        return redirect(url_for('index'))







    # try:
    #     img = ImageSaver(f).save()
    #     id_image = img.id
    # except Exception as e:
    #     # Обработка ошибки сохранения изображения
    #     print(f"Ошибка сохранения изображения: {e}")

    # try:
    #     plastinka = Plastinka(**params(), id_image=id_image)
    #     db.session.add(plastinka)
    #     db.session.commit()
    # except Exception as e:
    #     # Обработка ошибки создания и сохранения пластинки
    #     print(f"Ошибка создания и сохранения пластинки: {e}")

@bp.route('<int:plastinka_id>/edit', methods=['GET', 'POST'])
@login_required
@permission_check("edit_plastinka")
def edit_plastinka(plastinka_id):
    # Получение пластинки из базы данных по идентификатору
    plastinka = Plastinka.query.get(plastinka_id)
    genres = Genre.query.all()

    if not plastinka:
        flash('пластинка не найдена', 'danger')
        return redirect(url_for('plastinkas'))

    try:    
        if request.method == 'POST':

            # Проверка наличия обязательных полей
            if not request.form.get('name') or not request.form.get('author') or not request.form.get('genres') or \
            not request.form.get('year') or not request.form.get('description') or not request.form.get('publisher'):
                flash('Заполните все обязательные поля.', 'danger')
                return redirect(url_for('add_plastinka'))

            # Извлечение данных из формы редактирования пластинки
            name = request.form.get('name')
            author = request.form.get('author')
            year = request.form.get('year')
            description = request.form.get('description')
            selected_genre_ids = request.form.getlist('genres')
            publisher = request.form.get('publisher')
            volume = request.form.get('volume')



            # bleach.clean(plastinka.description) 
            description = bleach.clean(request.form.get('description'))
            plastinka.description = description


            # Обновление данных пластинки в базе данных
            plastinka.name = name
            plastinka.author = author
            plastinka.year = year
            plastinka.description = description
            plastinka.genres = Genre.query.filter(Genre.id.in_(selected_genre_ids)).all()
            plastinka.publisher = publisher
            plastinka.volume = volume
            
            bleach.clean(plastinka.description)    
            # Сохранение изменений в базе данных
            
            db.session.commit()
            flash('пластинка успешно обновлена', 'success')
            return redirect(url_for('index'))
    except:
        db.session.rollback()
        flash('Ошибка загрузки данных', 'danger')
        return redirect(url_for('index'))

        

        # flash('пластинка успешно обновлена', 'success')
        # return redirect(url_for('index'))

    # Рендеринг шаблона редактирования пластинки
    return render_template('edit_plastinka.html', plastinka=plastinka, genres=genres)







def calc_plastinka_rating(plastinka_id):
    # Получаем объект курса из базы данных по указанному идентификатору course_id
    plastinka = Plastinka.query.get(plastinka_id)

    # Получаем сумму рейтингов курса
    rating_sum = plastinka.rating_sum

    # Получаем количество рейтингов курса
    rating_num = plastinka.rating_num

    # Проверяем, если количество рейтингов равно нулю, чтобы избежать деления на ноль
    if rating_num == 0:
        return 0

    # Вычисляем и возвращаем средний рейтинг курса, разделяя сумму рейтингов на количество рейтингов
    return rating_sum / rating_num
























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




@login_required
def loger():
    if (request.endpoint == 'static'
        or request.endpoint == 'image'
            or request.endpoint == 'users_statistics'):
        return
    if request.endpoint == 'show':
        # Если пользователь анонимен, то необходимо
        # лог запись сохранять в куки
        plastinka_visit_logs_params = {
            'user_id': current_user.get_id(),
            'plastinka_id': request.view_args.get('plastinka_id'),
        }
        start = datetime.now() - timedelta(days=1)
        today_visits = (PlastinkaVisits.query
                        .filter_by(plastinka_id=request.view_args.get('plastinka_id'))
                        .filter(start <= PlastinkaVisits.created_at))
        if current_user.is_authenticated:
            today_visits = today_visits.filter_by(
                user_id=current_user.get_id())
        else:
            today_visits = today_visits.filter(PlastinkaVisits.user_id.is_(None))
        today_visits_int = len(today_visits.all())
        # < 10, т.к. нумерация идет с 0
        if today_visits_int < 10:
            try:
                db.session.add(PlastinkaVisits(**plastinka_visit_logs_params))
                db.session.commit()
            except:
                db.session.rollback()


@bp.route('/<int:plastinka_id>')
@login_required
def show(plastinka_id):

    # Создайте запись о посещении книги перед вызовом loger()
    creating_plastinka_visits(user_id=current_user.get_id(), plastinka_id=plastinka_id)
    
    loger()
    # Получение информации о книге по её идентификатору
    plastinka = Plastinka.query.get(plastinka_id)
    # Получение всех отзывов для данной пластинки, отсортированных по дате создания
    reviews_all = Review.query.filter_by(plastinka_id=plastinka_id).order_by(Review.created_at.desc()).all()
    
    plastinka.description = markdown.markdown(plastinka.description)
    # Вычисление среднего рейтинга для пластинки
    plastinka_rating = calc_plastinka_rating(plastinka_id)

    # Получение списка всех пользователей
    users = User.query.all()

    images = Image.query.all()

    # Флаг, указывающий, оставил ли текущий пользователь отзыв для данной пластинки
    flag = False
    for review in reviews_all:
        # установим маркдаун
        review.text = markdown.markdown(review.text)
        try:
            if review.user_id == current_user.id:
                flag = True
        except:
            pass

    # Получение последних 5 отзывов для отображения на странице, уже исправлено
    reviews_lim5 = Review.query.filter_by(plastinka_id=plastinka_id).order_by(Review.created_at.desc()).all()

    # Отображение страницы с информацией о книге и отзывами
    return render_template('show.html', plastinka=plastinka, reviews_all=reviews_all, reviews_lim5=reviews_lim5, users=users, images=images, flag=flag, plastinka_id=plastinka_id, plastinka_rating=plastinka_rating)



#  Создание логов для книги
def creating_plastinka_visits(user_id, plastinka_id):
    try:
        visit_log_params = {
            'user_id': user_id,
            'plastinka_id': plastinka_id,
        }
        db.session.add(PlastinkaVisits(**visit_log_params))
        db.session.commit()
    except:
        db.session.rollback()













@bp.route('<int:plastinka_id>/delete', methods=['POST'])
@login_required
@permission_check("delete")
def delete_plastinka(plastinka_id):
    plastinka = Plastinka.query.get(plastinka_id)
    if not plastinka:
        flash('пластинка не найдена', 'danger')
        return redirect(url_for('plastinkas'))

    try:
        db.session.delete(plastinka)
        db.session.commit()
        flash('пластинка успешно удалена', 'success')
    except:
        db.session.rollback()
        flash('При удалении пластинки возникла ошибка', 'danger')

    return redirect(url_for('index'))































@bp.route('/<int:plastinka_id>/reviews', methods=['GET'])
def reviews(plastinka_id):
    plastinka = Plastinka.query.get(plastinka_id)

    # Пагинация - получение номера текущей страницы отзывов
    page = request.args.get('page', 1, type=int)
    five_per_page = 5  # Количество отзывов, отображаемых на одной странице

    # Фильтр - определение порядка сортировки отзывов
    sort_by = request.args.get('sort_by', 'new', type=str)
    if sort_by == 'positive':
        order_by = Review.rating.desc()  # Сортировка по возрастанию рейтинга
    elif sort_by == 'negative':
        order_by = Review.rating.asc()  # Сортировка по убыванию рейтинга
    else:
        order_by = Review.created_at.desc()  # Сортировка по дате создания (новые сверху)

    # Получение отфильтрованных и отсортированных отзывов с пагинацией
    reviews_all = Review.query.filter_by(plastinka_id=plastinka_id)\
        .join(User)\
        .add_columns(User.login)\
        .add_columns(User.last_name)\
        .add_columns(User.first_name)\
        .order_by(order_by)\
        .paginate(page, five_per_page, error_out=False)
    
    # text = bleach.clean(request.form.get('text'))
    # reviews_all.text = text

    # Проверка, вошел ли пользователь в аккаунт или нет
    if current_user.is_authenticated:
        flag = False
        existing_review = Review.query.filter_by(plastinka_id=plastinka_id, user_id=current_user.id).first()
        if existing_review:
            flag = True  # У пользователя уже есть отзыв для данного курса
    else:
        flag = None  # Пользователь не вошел в аккаунт

    # Отображение страницы с отзывами
    return render_template('reviews.html', plastinka=plastinka, reviews_all=reviews_all, flag=flag,  sort_by=sort_by, per_page=five_per_page, page=page)


@bp.route('/<int:plastinka_id>/add_review', methods=['POST'])
@login_required
def add_review(plastinka_id):
    try:
        # Проверяем, вошел ли пользователь в аккаунт или нет
        if not current_user.is_authenticated:
            flash('Для оставления отзыва необходимо войти в свой аккаунт.', 'warning')
            return redirect(url_for('auth.login'))
        
        if not request.form.get('text'):
            flash('Напишите отзыв, почему вы не написали ', 'danger')
            return redirect(url_for('plastinkas.reviews', plastinka_id=plastinka_id))

        # Получаем оценку и текст отзыва из формы
        rating = int(request.form['rating'])
        text = request.form['text']

        # Проверяем допустимость оценки (должна быть в диапазоне от 0 до 5)
        if rating < 0 or rating > 5:
            flash('Недопустимая оценка', 'danger')
            return redirect(url_for('plastinkas.review', plastinka_id=plastinka_id))

        # Проверяем, оставлял ли пользователь уже отзыв для данного курса
        existing_review = Review.query.filter_by(plastinka_id=plastinka_id, user_id=current_user.id).first()
        if existing_review:
            flash('Вы уже оставили отзыв для этого курса.', 'danger')
            return redirect(url_for('plastinkas.show', plastinka_id=plastinka_id))

        # Создаем новый отзыв
        review = Review(rating=rating, text=text, created_at=func.now(), plastinka_id=plastinka_id, user_id=current_user.id)
        db.session.add(review)
        db.session.commit()

        # Обновляем информацию о курсе: увеличиваем количество рейтингов и общую сумму рейтинга
        plastinka = Plastinka.query.get(plastinka_id)
        plastinka.rating_num += 1
        plastinka.rating_sum += rating
        db.session.add(plastinka)
        db.session.commit()

        # Отображаем сообщение об успешном добавлении отзыва
        flash('Отзыв успешно добавлен.', 'success')

        # Перенаправляем пользователя на страницу курса
        return redirect(url_for('plastinkas.show', plastinka_id=plastinka_id, rating=rating))
    except:
        db.session.rollback()
        flash('При сохранении данных возникла ошибка. Проверьте корректность введенных данных.', 'danger')
        return redirect(url_for('plastinkas.show', plastinka_id=plastinka_id))


@bp.route('/<int:plastinka_id>/reviews', methods=['GET'])
def view_reviews(plastinka_id):
    plastinka = Plastinka.query.get(plastinka_id)

    # Получение всех отзывов для данного курса, отсортированных по дате создания (новые сверху)
    reviews = Review.query.filter_by(plastinka_id=plastinka_id).order_by(Review.created_at.desc())


    # Получение списка всех пользователей
    users = User.query.all()

    # Отображение страницы с отзывами
    return render_template('reviews.html', plastinka=plastinka, reviews=reviews, users=users)
