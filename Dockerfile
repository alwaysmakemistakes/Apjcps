FROM ubuntu:22.04 

ENV TZ=Europe/Moscow 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 

#Обновляем систему
RUN apt-get update -y && apt upgrade -y

#Устанавливаем необходимые пакеты
RUN apt-get install python3-pip build-essential python3-dev default-libmysqlclient-dev pkg-config gunicorn -y

#Создаем дикректорию для проекта
RUN mkdir /project

#Копируем все файлы из текущей директории в папку с проектом
COPY . /project

#Устанавливаем папку проекта в качестве рабочей директории
WORKDIR /project

#Устанавливаем зависимости для проекта
RUN pip3 install -r requirements.txt

#Устанавливаем папку с wsgi приложением в качестве рабочей директории
WORKDIR /project/app

#Задаем команду для запуска
CMD flask run -p 5000 -h 0.0.0.0
