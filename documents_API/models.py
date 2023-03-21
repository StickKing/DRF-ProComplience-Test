from django.db import models

class DocumentsInfo(models.Model):
    """Модель хранящая загружаемые документы"""
    #Поле документа
    document_file = models.FileField(upload_to='uploads_file/')
    #Поле для хранения заголовков
    headings = models.JSONField()

    def __str__(self) -> str:
        return f"{self.document_file.path}"
