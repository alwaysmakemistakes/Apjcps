import os

SECRET_KEY = 'secret-key'


#phpmyadmin от ПОЛИТЕХА
# SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://std_1865_sokap:12345678@std-mysql.ist.mospolytech.ru/std_1865_sokap'


#локалка постгрес
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345678@localhost:5432/sok'

#локалка mysql
SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://admin:123456@localhost:3306/test'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

ADMIN_ROLE_ID = 1
MODER_ROLE_ID = 2

LOGS_PER_PAGE = 10

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')


