from django.contrib import admin
from django.urls import path
from documents_API.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', DocumentView.as_view()),
    path('documents/<int:pk>/', OneDocumentView.as_view()),
    path('documents/file/<int:pk>/', FilesWorkView.as_view())
]
