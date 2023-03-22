# Данная работы является тестовым заданием
## Основная информация
Данная работы представляет из себя API сервис построенный на Django Rest Framework с PostgreSQL.
Всё это развёрнуто в docker-контейнерах.
Используемые библиотеки (указаны в __requirements.txt__):
- django
- djangorestframework
- djangorestframework-simplejwt
- drf-yasg
- psycopg2
- pandas
## Установка - Install
1. Клонируем репозиторий - git clone https://github.com/StickKing/DRF-ProComplience-Test.git
2. После этого устанавливаем в файле __docker-compose.yml__ логин и пароль от БД
3. Установить Docker если его нет
4. Запускаем __docker-compose up__
5. После успешного запуска приостонавливаем работу контейнеров с помощью CTRL + C
6. С помощью __docker-compose run web python .\manage.py createsuperuser__ создаём админа
7. Запускаем ___docker-compose up___ снова
Теперь можно пользоваться API


