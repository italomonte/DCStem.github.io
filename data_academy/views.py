from django.shortcuts import render, HttpResponse

# Create your views here.


def home (request):
    return render(request, 'data_academy/pages/home.html')

def conteudos (request):
    return render(request, 'data_academy/pages/abp.html')

def login (request):
    return render(request, 'data_academy/pages/login.html')

