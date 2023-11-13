from django.urls import path
from . import views

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('content/', views.content, name="content"),
    path('descripe_statistic/', views.descripe_statistic, name="descripe_statistic"),
]