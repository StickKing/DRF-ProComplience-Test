# Данная работы является тестовым заданием
## Основная информация
Данная работа представляет из себя API сервис построенный на Django Rest Framework с PostgreSQL, аутентификацией по JWT и документацией сделаной с помощью Swagger. \
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
Теперь можно открыть http://0.0.0.0:8000/ и ознакомиться с документацией сделаной с помощью swagger.

## Использование API
Для начала необходимо получить Token для работы с API делается это командой:\
``` bash
curl  \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "<your username>", "password": "<your password>"}' \
  http://0.0.0.0:8000/token/ 
```
В ответ будет передано два токена access и refresh, первый как раз будет использоваться для доступа к API\

Далее, чтобы получить информацию обовсех файлах и их заголовках необходимо выполнить команду: \
``` bash
curl -X GET \
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/
```

Слудущей командой мы можем получить информацию о конкретном файле и его заголовках: \
``` bash
curl -X GET \
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/<id>/
```

Для удаления файла из БД можно использовать:
``` bash
curl -X DELETE \
  -H "Authorization: Bearer <your token>" \
  http://0.0.0.0:8000/documents/<id>/
```

Для получения информации из самих файлов нужно использовать команду:
``` bash
curl -X POST \
    -H "Authorization: Bearer <your token>" \
    -F 'item_count=<count>' -F 'item_count=<item_count>' -F 'sorting_column=<column name>' -F 'sort_ascending=<True or False>' -F 'columns_name=<column name>' -F 'columns_filter=<columns_filter>'   http://0.0.0.0:8000/documents/file/<id>/
```

Небольшие примеры работы с API можно найти в файлах: *example.sh* для linux и в *example.ps1* для пользователей Windows (PowerShell)

## Пояснения по поводу вывода информации из файлов
POST запрос documents/file/id/ принимает на вход следующие параметры:
  - columns_name — Массив (список) столбцов в которых мы будем искать значения из *columns_filter*
  - columns_filter — Массив (список) значений искомых в стобцах *columns_name*
  - sorting_column — Массив (список) столбцов по которым будет произведена сортировка
  - sort_ascending — Массив (список) значений Bool где True означает что нужно производить сортировку по возрастанию, а False наоборот
  - item_count — Значение типа INT указывает сколько необходимо вывести строк из файла \
Все указанные выше параметры являются необязательными, если ни один из них указан не будет то выведется вся информация из файла \
Параметр *sort_ascending* по умолчанию имеет значение True.

### Условные примеры того как работает запрос
Если в запросе указан следующий набор данных: \
  *columns_name = ['name', 'age', 'gender']* \
  *columns_filter = ['Андрей', 12, 'Мужчина']* \
То выведутся все строки в которых name = 'Андрей', age = 12, gender = Мужчина \
\
Если в запросе указан следующий набор данных: \
  *sorting_column = ['name', 'age', 'gender']* \
  *sort_ascending = [True, False, True]* \
То выведется вся информация из файла отсортированная по трём столбцам 'name', 'age', 'gender' из которых name и gender отсортированы по возрастанию, а age по убыванию. \
  \
  Для большей гибкости можно указывать все эти параметры вместе.
