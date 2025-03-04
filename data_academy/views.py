
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import io
import sys
import os
# Create your views here.

def home (request):
    return render(request, 'data_academy/pages/home.html')

def content(request):
    return render(request, 'data_academy/pages/content.html')

def content_road(request):
    return render(request, 'data_academy/pages/content_road.html')

def login (request):
    return render(request, 'data_academy/pages/login.html')

def task1_1 (request):
    return render(request, 'data_academy/pages/task1_1.html')

def task1_2 (request):
    return render(request, 'data_academy/pages/task1_2.html')

def task1_3 (request):
    
    df = pd.read_csv("/home/italomonte/Data_Academy/data_academy/static/data_academy/csv/BD_Refrigerante.csv")
    #df = pd.read_csv("data_academy/static/data_academy/csv/BD_Refrigerante.csv")
    html_table = df.to_html().replace("<table", '<table id="example" class="table table-striped" style="width:100%"')

    return render(request, 'data_academy/pages/task1_3.html', {"table": html_table})

def task1_4 (request):
    return render(request, 'data_academy/pages/task1_4.html')

def task1_5(request):

    if request.method == 'POST':
        code = request.POST.get('code', '')
        # Execute o código aqui e capture a saída
        # Crie um objeto StringIO para coletar a saída
        output = io.StringIO()
        sys.stdout = output  # Redirecione a saída padrão
        df = pd.read_csv("/home/italomonte/Data_Academy/data_academy/static/data_academy/csv/BD_Refrigerante.csv")
        #df = pd.read_csv("data_academy/static/data_academy/csv/BD_Refrigerante.csv")
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

        try:
            exec(code)
        except Exception as e:
            output.write(f'Erro: {str(e)}')

        # Restaure a saída padrão original
        sys.stdout = sys.__stdout__
        responseData = {'code': code, 'output': output.getvalue()}
        return JsonResponse(responseData)
    

    return render(request, 'data_academy/pages/task1_5.html')
