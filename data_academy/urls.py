from django.urls import path
from . import views

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('content/', views.content, name="content"),
    path('login/', views.login, name="login"),
    path('task/', views.task, name="task"),
    path('content_road/', views.content_road, name="content_road"),
]