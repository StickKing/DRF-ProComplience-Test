from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from documents_API.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="Client Weather and other API",
      default_version='v1',
      description="Тестовое задание",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mainsample@yandex.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documents/', DocumentView.as_view()),
    path('documents/<int:pk>/', OneDocumentView.as_view()),
    path('documents/file/<int:pk>/', FilesWorkView.as_view())
]
