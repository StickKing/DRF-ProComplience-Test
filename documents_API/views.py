from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from pandas import read_csv
from .serializers import DocumentSerializer, AllDocumentsSerializer, FilesWorkSerialize
from .models import *
from .swagger_schema import *

class OneDocumentView(RetrieveDestroyAPIView):
    """Представление для вывода каждого по отдельности
    документа и для удаления"""
    
    #Указываем параметры авторизации
    permission_classes = [permissions.IsAuthenticated]
    #Указываем аутентификацию через JWT
    authentication_classes = [JWTAuthentication]

    #Метод GET
    @swagger_auto_schema(responses=document_GET_one_responce)
    def get(self, requests, pk):
        """Метод GET для вывода данных об одном документе"""
        #Проверяем есть ли данный объект в БД
        try:
            document = DocumentsInfo.objects.get(pk=pk)
        except:
            return Response({"Error": "Объект не найден"})
        serializer = AllDocumentsSerializer(document)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    #Метод DELETE 
    def delete(self, requests, pk):
        """Метод DELETE для удаления данных из БД"""
        #Проверяем есть ли данный объект в БД
        try:
            document = DocumentsInfo.objects.get(pk=pk)
        except:
            return Response({"Error": "Объект не найден"})
        #Удаляем файл из базы
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DocumentView(ListCreateAPIView):
    """Представление для вывода информации обо всех документах"""
    
    #Указываем параметры авторизации
    permission_classes = [permissions.IsAuthenticated]
    #Указываем аутентификацию через JWT
    authentication_classes = [JWTAuthentication]

    queryset = DocumentsInfo.objects.all()
    serializer_class = AllDocumentsSerializer
    #Метод POST
    @swagger_auto_schema(request_body=document_POST_request)
    def post(self, request):
        """Метод загрузки нового файла в базу.
        В данном методе происходит проверка на формат загружаемого файла,
        если файл не явялется CSV то он будет отклонён"""
        #Передаём полученные данные в сериализатор
        serializer = DocumentSerializer(data=request.data)
        #Проверяем валидность полученных данных
        serializer.is_valid(raise_exception=True)
        #Проверка на формат
        if request.data['document_file'].name[-4:].lower() == '.csv':
            #Сохраняем данные
            serializer.save()
            #Возвращаем статус 200 и загруженную информацию
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"Error": 'Неверный формат файла'}, status=status.HTTP_400_BAD_REQUEST)

class FilesWorkView(CreateAPIView):
    """Представление для реализации сортировки и фильтрации"""

    #Указываем параметры авторизации
    permission_classes = [permissions.IsAuthenticated]
    #Указываем аутентификацию через JWT
    authentication_classes = [JWTAuthentication]

    #Метод POST
    @swagger_auto_schema(request_body=file_GET_request)
    def post(self, requests, pk):

        """Метод для вывода информации из файлов
        Если пользователь передаёт параметры sorting_column и sort_ascending
        то в ответ получит информацию отсортированную согласно указанным параметрам.
        Если пользотель передаст параметры columns_name, columns_filter 
        то получит ответ отфильтрованный согласно данным параметрам.
        Когда ни один параметр не указан будет выведено содержимое всего файла"""

        #Проверяем объект на существование
        try:
            document = DocumentsInfo.objects.get(pk=pk)
            document_file = document.document_file
        except:
            return Response({"Error": "Объект не найден"})
        #Проверяем корректность полуденных данных
        serializer = FilesWorkSerialize(data=requests.data)
        serializer.is_valid(raise_exception=True)
        open_file = read_csv(document_file)

        #Проверяем какие параметры указал пользователь
        columns_name = serializer.data.get('columns_name', None)
        columns_filter = serializer.data.get('columns_filter', None)
        sorting_column = serializer.data.get('sorting_column', None)
        sort_ascending = serializer.data.get('sort_ascending', True)
        item_count = serializer.data.get('item_count', None)

        #Если есть данные для сортировки то сортируем по указанным столбцам
        if sorting_column:
            try:
                if type(sort_ascending) == bool:
                    sort_ascending = [sort_ascending] * len(sorting_column)
                open_file = open_file.sort_values(by=sorting_column, ascending=sort_ascending)
            except:
                return Response(data={"Error": "Ошибка сортировки"}, status=status.HTTP_400_BAD_REQUEST)
        
        #Если указаны данные для фильтрации то фильтруем
        if columns_filter and columns_name:
            try:
                #Поскольку в списке только строки, то необходимо цифровые элементы преобразовать в INT
                columns_filter = [int(i) if i.isdigit() else i for i in columns_filter]
                for i in range(len(columns_filter)):
                    open_file = open_file[open_file[columns_name[i]] == columns_filter[i]]
            except:
                return Response(data={"Error": "Ошибка фильтрации"}, status=status.HTTP_400_BAD_REQUEST)
                
        #Если указаны ограничения по колличетву элементов то выводим нужное колличестов
        if item_count:
            open_file = open_file.iloc[:int(item_count)]
        
        #Если не указан ни один параметр то возвращаем весь файл
        return Response(data=open_file.to_json(), status=status.HTTP_202_ACCEPTED)


        