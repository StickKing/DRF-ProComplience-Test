# Данная работы является тестовым заданием
## Основная информация
Данная работы представляет из себя API сервис построенный на Django Rest Framework с PostgreSQL, аутентификацией по JWT и документацией сделаной с помощью Swagger.
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
2. После этого устанавливаем в файле ___docker-compose.yml___ логин и пароль от БД
3. Установить Docker если его нет и убедиться, что сервисов с такими же именами нет (db, web) если есть удалить их
4. Запускаем ___docker-compose up___
5. После успешного запуска приостонавливаем работу контейнеров с помощью CTRL + C
6. С помощью ___docker-compose run web python manage.py createsuperuser___ создаём админа
7. Запускаем ___docker-compose up___ снова \
Теперь можно пользоваться API

## Использование API
Для начала необходимо получить Token для работы с API делается это командой:\
``` bash
curl  \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "username", "password": "password"}' \
  http://0.0.0.0:8000/token/ 
```
В ответ будет передано два токена access и refresh, первый как раз будет использоваться для доступа к API\

Далее, чтобы получить информацию обовсех файлах и их заголовках необходимо выполнить команду: \
``` bash
curl -X GET\
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/
```

Слудущей командой мы можем получить информациб о конкретном файле и его заголовках: \
``` bash
curl -X GET\
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/<id>/
```

Для получения информации из самих файлов нужно использовать команду:
``` bash
curl -X POST\
    -H "Authorization: Bearer <your token>" \
    -F 'item_count=<count>' -F 'item_count=<item_count>' -F 'sorting_column=<column name>' -F 'sort_ascending=<True or False>' -F 'columns_name=<column name>' -F 'columns_filter=<columns_filter>'   http://0.0.0.0:8000/documents/file/<id>/
```

Небольшие примеры работы с API можно найти в файлах: *example.sh* для linux и в *example.ps1* для пользователей Windows (PowerShell)
