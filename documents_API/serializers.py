from rest_framework.serializers import Serializer, FileField, ModelSerializer, ListField, DictField, IntegerField, BooleanField, CharField
from .models import DocumentsInfo
from pandas import read_csv
from json import dumps

class DocumentSerializer(Serializer):
    """Сериализатор загружаемы документов"""
    document_file = FileField()

    #Обработка загрузки данных в БД
    def create(self, validated_data):
        open_file = read_csv(validated_data['document_file'])
        headings = dumps(open_file.columns.to_list())
        new_documents = DocumentsInfo.objects.create(document_file=validated_data['document_file'], 
                                                     headings=headings)
        return new_documents
    
class AllDocumentsSerializer(ModelSerializer):
    """Сериализатор для отобрадения всех документов"""
    class Meta:
        model = DocumentsInfo
        fields = '__all__'

class FilesWorkSerialize(Serializer):
    """Сериализатор для работы с csv файлами"""
    #Имена столбцов по которым будет осуществлён поиск
    columns_name = ListField(child=CharField(), 
                             required=False)
    #Значение искомые в стобцах выше
    columns_filter = ListField(required=False)

    #Имена стобцов по которым будет осуществлена сортировка
    sorting_column = ListField(required=False)
    #Нужно ли сортировать по возрастанию
    sort_ascending = ListField(child=BooleanField(), 
                               required=False)
    
    #Колличество записей которые нужно вывести
    item_count = IntegerField(min_value=1,
                              required=False)
    