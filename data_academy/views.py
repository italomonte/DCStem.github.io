from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import plotly.express as px
import io
import sys
import pandas as pd
import csv

# Create your views here.


def home (request):
    return render(request, 'data_academy/pages/home.html')

def login (request):
    return render(request, 'data_academy/pages/login.html')

def content(request):
    return render(request, 'data_academy/pages/content.html')

def descripe_statistic(request):

    if request.method == 'POST':
        code = request.POST.get('code', '')
        # Execute o código aqui e capture a saída
        # Crie um objeto StringIO para coletar a saída
        output = io.StringIO()
        sys.stdout = output  # Redirecione a saída padrão
        df = pd.read_csv("data_academy\static\data_academy\csv\BD_Refrigerante.csv")
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

    df = pd.read_csv("data_academy\static\data_academy\csv\BD_Refrigerante.csv")
    html_table = df.to_html().replace("<table", '<table id="example" class="table table-striped" style="width:100%"')

    return render(request, 'data_academy/pages/descripe_statistic.html', {"table": html_table})

def grafh(request):
    df = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [30, 40, 15, 25]
    })

    fig = px.bar(df, x='Categoria', y='Valores', title='Exemplo de Gráfico de Barras')

    graph_html = fig.to_html(full_html=False)


    return render(request, 'data_academy/pages/grafh.html', {'grafh': graph_html})

def slide(request):
    return render(request, 'data_academy/pages/slide.html')
