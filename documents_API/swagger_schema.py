from drf_yasg import openapi
from rest_framework import status


#Определяем схемы для swagger

document_POST_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'document_file': openapi.Schema(type=openapi.TYPE_FILE, description='Файл CSV для загрузки на сервер'),
    },
    required=['document_file']
)

file_GET_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'columns_name': openapi.Schema(type=openapi.TYPE_OBJECT, description='Массив (список) столбцов, которые мы будем фильтровать'),
        'columns_filter': openapi.Schema(type=openapi.TYPE_OBJECT, description='Массив (список) значений столбцов которые мы ищем'),
        'sorting_column': openapi.Schema(type=openapi.TYPE_OBJECT, description='Массив (список) столбцов по которым будет осуществлена сортировка '),
        'sort_ascending': openapi.Schema(type=openapi.TYPE_OBJECT, description='Массив (список) значений bool для определения делать ли сортировку по возрастанию'),
        'item_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='Колличество выводимых строк из CSV'),
    },
)

document_GET_one_responce = {
    status.HTTP_200_OK: openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID'),
            'document_file': openapi.Schema(type=openapi.TYPE_FILE, description='Путь к файлу'),
            'headings': openapi.Schema(type=openapi.TYPE_OBJECT, description='Заголовки файла'),
        },
        read_only = ['id']
    ),
}
