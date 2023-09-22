from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('abp/', views.abp),
    path('login/', views.login),
    path('estatistica/', views.estatistica_python),
    path('problema/', views.problema),
]