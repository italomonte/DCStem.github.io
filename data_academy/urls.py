from django.urls import path
from . import views

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('abp/', views.abp, name="abp"),
    path('login/', views.login, name="login"),
    path('estatistica/', views.estatistica_python, name="estatistica"),
    path('problema/', views.problema, name="problema"),
]