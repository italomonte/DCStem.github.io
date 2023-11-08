from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('content/', views.content, name="content"),
    path('login/', views.login, name="login"),
    path('show_csv_header/<str:file_path>/', views.show_csv_header, name='show_csv_header'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)