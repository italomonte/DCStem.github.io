from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('content/', views.content, name="content"),
    path('login/', views.login, name="login"),
    path('grafh/', views.grafh, name="grafh"),
    path('slide/', views.slide, name="slide"),
]