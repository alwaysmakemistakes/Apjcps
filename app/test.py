# import unittest
# from app import app, db  # Импортируйте ваш объект Flask приложения и объект БД

# SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:12345678@localhost:3306/test'

# class FlaskAppTestCase(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Использование временной БД для тестов
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

#     def test_index_route(self):
#         # Тестирование главной страницы
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
#         # Добавьте дополнительные проверки, например, наличие ожидаемого содержимого в ответе

#     def test_image_route(self):
#         # Тестирование маршрута изображений
#         response = self.app.get('/image/1')
#         self.assertEqual(response.status_code, 404)  # Проверка HTTP-ошибки 404 для несуществующего изображения

#     # Другие тесты для функций вашего приложения
#     # Тесты для функций логирования и работы с базой данных


# from app import app, db  # Импортируйте ваш объект Flask приложения и объект БД
# from auth import bp as auth_bp, User

# class AuthBlueprintTestCase(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Использование временной БД для тестов
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()


#     def test_login_route(self):
#         # Тестирование маршрута входа в систему
#         response = self.app.post('/auth/login', data=dict(
#             login='testuser',
#             password='testpassword'
#         ), follow_redirects=True)
#         self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера после аутентификации
       
#     def test_logout_route(self):
#         # Тестирование маршрута выхода из системы
#         with self.app:
#             # Аутентифицируем пользователя перед выходом из системы
#             self.app.post('/auth/login', data=dict(
#                 login='testuser',
#                 password='testpassword'
#             ))
#             response = self.app.get('/auth/logout', follow_redirects=True)
#             self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера после выхода из системы
        



# from app import app, db  # Импортируйте ваш объект Flask приложения и объект БД
# from plastinkas import bp as plastinkas_bp

# class PlastinkasBlueprintTestCase(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Использование временной БД для тестов
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

#     def test_add_plastinka_route(self):
#         # Тестирование маршрута добавления пластинки
#         with self.app:
#             # Аутентифицируем пользователя
#             self.app.post('/auth/login', data=dict(
#                 login='testuser',
#                 password='testpassword'
#             ))
#             response = self.app.get('/plastinkas/add_plastinka', follow_redirects=True)
#             self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
#             # Добавьте дополнительные проверки для страницы добавления пластинки

#     def test_edit_plastinka_route(self):
#         # Тестирование маршрута редактирования пластинки
#         with self.app:
#             # Аутентифицируем пользователя
#             self.app.post('/auth/login', data=dict(
#                 login='testuser',
#                 password='testpassword'
#             ))
#             response = self.app.get('/plastinkas/1/edit', follow_redirects=True)
#             self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
#             # Добавьте дополнительные проверки для страницы редактирования пластинки

#     # Другие тесты для функций из plastinkas.py







# from app import app, db  # Импортируйте ваш объект Flask приложения и объект БД
# from logs import bp as logs_bp, User, PlastinkaVisits, Plastinka, Role

# class LogsBlueprintTestCase(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
        
#         app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Использование временной БД для тестов
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

#     def test_users_statistics_route(self):
#         # Тестирование маршрута статистики по пользователям
#         with self.app:
#             # Аутентифицируем пользователя
#             self.app.post('/auth/login', data=dict(
#                 login='testuser',
#                 password='testpassword'
#             ))
#             response = self.app.get('/logs/users_statistics', follow_redirects=True)
#             self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
#             # Добавьте дополнительные проверки для страницы статистики по пользователям
        
#     def test_plastinkas_statistics_route(self):
#         # Тестирование маршрута статистики по пластинкам
#         with self.app:
#             # Аутентифицируем пользователя
#             self.app.post('/auth/login', data=dict(
#                 login='testuser',
#                 password='testpassword'
#             ))
#             response = self.app.get('/logs/plastinkas_statistics', follow_redirects=True)
#             self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
#             # Добавьте дополнительные проверки для страницы статистики по пластинкам

#     # Другие тесты для функций из logs.py

# import unittest

# if __name__ == '__main__':
#     unittest.main()










import unittest
from app import app, db  # Импорт объекта Flask приложения и объекта БД

# Указание настройки для подключения к тестовой базе данных
# SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:12345678@localhost:3306/test'

# Класс для тестирования базового функционала Flask приложения
class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Установка параметров тестирования Flask приложения
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Использование временной БД для тестов
        self.app = app.test_client()
        db.create_all()  # Создание всех таблиц в тестовой БД

    def tearDown(self):
        db.session.remove()  # Закрытие сессии БД
        db.drop_all()  # Очистка структуры БД

    # Тестирование главной страницы
    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера

    # Тестирование маршрута изображений
    def test_image_route(self):
        response = self.app.get('/image/1')
        self.assertEqual(response.status_code, 404)  # Проверка HTTP-ошибки 404 для несуществующего изображения


from app import app, db  # Импорт объекта Flask приложения и объекта БД
from auth import bp as auth_bp, User

# Класс для тестирования функционала аутентификации
class AuthBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Использование временной БД для тестов
        self.app = app.test_client()
        db.create_all()  # Создание всех таблиц в тестовой БД

    def tearDown(self):
        db.session.remove()  # Закрытие сессии БД
        db.drop_all()  # Очистка структуры БД

    # Тестирование маршрута входа в систему
    def test_login_route(self):
        response = self.app.post('/auth/login', data=dict(
            login='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера после аутентификации

    # Тестирование маршрута выхода из системы
    def test_logout_route(self):
        with self.app:
            self.app.post('/auth/login', data=dict(
                login='testuser',
                password='testpassword'
            ))
            response = self.app.get('/auth/logout', follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера после выхода из системы


from app import app, db  # Импорт объекта Flask приложения и объекта БД
from plastinkas import bp as plastinkas_bp

# Класс для тестирования функционала работы с пластинками
class PlastinkasBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Использование временной БД для тестов
        self.app = app.test_client()
        db.create_all()  # Создание всех таблиц в тестовой БД

    def tearDown(self):
        db.session.remove()  # Закрытие сессии БД
        db.drop_all()  # Очистка структуры БД

    # Тестирование маршрута добавления пластинки
    def test_add_plastinka_route(self):
        with self.app:
            self.app.post('/auth/login', data=dict(
                login='testuser',
                password='testpassword'
            ))
            response = self.app.get('/plastinkas/add_plastinka', follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
    
    def test_add_plastinka_route(self):
        with self.app:
            self.app.post('/auth/login', data=dict(
                login='testuser',
                password='testpassword'
            ))
            response = self.app.get('/plastinkas/add_plastinka', follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера

            # Теперь добавим тест на создание пластинки
            response = self.app.post('/plastinkas/add_plastinka', data=dict(
                name='Test Plastinka',
                author='Test Author',
                genres='Test Genre',
                year='2023',
                description='12',
                publisher='31'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера

            # Добавим дополнительную проверку, чтобы убедиться, что пластинка была создана
            
    # Тестирование маршрута редактирования пластинки
    def test_edit_plastinka_route(self):
        with self.app:
            self.app.post('/auth/login', data=dict(
                login='testuser',
                password='testpassword'
            ))
            response = self.app.get('/plastinkas/1/edit', follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера


from app import app, db  # Импорт объекта Flask приложения и объекта БД
from logs import bp as logs_bp, User, PlastinkaVisits, Plastinka, Role

# Класс для тестирования функционала работы с логами
class LogsBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Использование временной БД для тестов
        self.app = app.test_client()
        db.create_all()  # Создание всех таблиц в тестовой БД

    def tearDown(self):
        db.session.remove()  # Закрытие сессии БД
        db.drop_all()  # Очистка структуры БД

    # Тестирование маршрута статистики по пользователям
    def test_users_statistics_route(self):
        with self.app:
            self.app.post('/auth/login', data=dict(
                login='testuser',
                password='testpassword'
            ))
            response = self.app.get('/logs/users_statistics', follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера
        
    # Тестирование маршрута статистики по пластинкам
    def test_plastinkas_statistics_route(self):
        with self.app:
            self.app.post('/auth/login', data=dict(
                login='testuser',
                password='testpassword'
            ))
            response = self.app.get('/logs/plastinkas_statistics', follow_redirects=True)
            self.assertEqual(response.status_code, 200)  # Проверка успешного ответа сервера


            
# from flask import Flask, url_for
# from unittest import TestCase

# class TestAddPlastinka(TestCase):
#     def setUp(self):
#         self.app = Flask(__name__)
#         self.app.config['TESTING'] = True
#         self.app.config['WTF_CSRF_ENABLED'] = False

#     def test_add_plastinka(self):
#         with self.app.test_request_context('/add_plastinka', method='POST'):
#             request_url = url_for('plastinkas.add_plastinka')  # Попробуйте обновить имя маршрута для Blueprint
#   # Получаем URL для маршрута add_plastinka
#             self.assertEqual(request_url, '/add_plastinka')  # Проверяем URL

#             with self.app.test_client() as client:
#                 response = client.post(request_url, data=dict(
#                     name='TestPlastinka',
#                     author='TestAuthor',
#                     genres='TestGenre',
#                     year='2023',
#                     description='21',
#                     publisher='12'
#                 ), follow_redirects=True)
                
#                 self.assertEqual(response.status_code, 200)



# import unittest
# from flask import Flask

from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from app import app, db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        data = {
            'login': 'testuser',
            'password': 'testpassword',
            'last_name': 'Test',
            'first_name': 'User',
            'middle_name': 'Middle',
            'role': 1  # Замените на соответствующий ID роли
        }

        response = self.app.post('/auth/register', data=data, follow_redirects=True)

        # Проверка кода ответа
        self.assertEqual(response.status_code, 200)

        # Проверка, что успешно зарегистрированного пользователя перенаправляют на страницу входа


import unittest

if __name__ == '__main__':
    unittest.main()
