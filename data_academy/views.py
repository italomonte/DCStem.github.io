from django.shortcuts import render
from django.http import JsonResponse
import io
import sys

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

        try:
            exec(code)
        except Exception as e:
            output.write(f'Erro: {str(e)}')

        # Restaure a saída padrão original
        sys.stdout = sys.__stdout__
        responseData = {'code': code, 'output': output.getvalue()}
        return JsonResponse(responseData)
    return render(request, 'data_academy/pages/content.html')

