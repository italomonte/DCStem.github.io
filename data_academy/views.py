from django.shortcuts import render
from django.http import JsonResponse
import io
import sys
import pandas as pd
import csv
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home (request):
    return render(request, 'data_academy/pages/home.html')

def login (request):
    return render(request, 'data_academy/pages/login.html')

def content(request):

    if request.method == 'POST':
        code = request.POST.get('code', '')
        # Execute o código aqui e capture a saída
        # Crie um objeto StringIO para coletar a saída
        output = io.StringIO()
        sys.stdout = output  # Redirecione a saída padrão
        df = pd.read_csv("data_academy/media/data_academy/csv/airline-safety.csv")
        try:
            exec(code)
        except Exception as e:
            output.write(f'Erro: {str(e)}')

        # Restaure a saída padrão original
        sys.stdout = sys.__stdout__
        responseData = {'code': code, 'output': output.getvalue()}
        return JsonResponse(responseData)

    def highlight_bg(val):
        return f'background-color: white'

    df = pd.read_html("data_academy/media/data_academy/html/table.html")
    df = df.head()

    html_table = df.to_html()
  

    
    return render(request, 'data_academy/pages/content.html', {'html_table': html_table})

def table (request):
    return render(request, 'data_academy/pages/table.html')
    
