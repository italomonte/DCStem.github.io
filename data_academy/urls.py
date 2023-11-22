from django.urls import path
from . import views

app_name = 'data_academy'

urlpatterns = [
    path('', views.home, name="home"),
    path('content/', views.content, name="content"),
    path('content_road/', views.content_road, name="content_road"),
    path('login/', views.login, name="login"),
    path('task1_1/', views.task1_1, name="task1_1"),
    path('task1_2/', views.task1_2, name="task1_2"),
    path('task1_3/', views.task1_3, name="task1_3"),
    path('task1_4/', views.task1_4, name="task1_4"),
    path('task1_5/', views.task1_5, name="task1_5"),
]