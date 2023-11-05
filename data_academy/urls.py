from django.urls import path
from . import views

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="inicio"),
    path('conteudos/', views.conteudos, name="conteudos"),
    path('login/', views.login, name="login"),
]