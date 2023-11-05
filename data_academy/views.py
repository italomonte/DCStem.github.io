from django.shortcuts import render, HttpResponse

# Create your views here.


def home (request):
    return render(request, 'data_academy/pages/home.html')

def content (request):
    return render(request, 'data_academy/pages/content.html')

def login (request):
    return render(request, 'data_academy/pages/login.html')

