from django.shortcuts import render, HttpResponse
from .forms import ScriptForm
# Create your views here.


def home (request):
    return render(request, 'data_academy/pages/home.html')

def content (request):
    return render(request, 'data_academy/pages/content.html')

def login (request):
    return render(request, 'data_academy/pages/login.html')

def interpretador(request):
    if request.method == 'POST':
        form = ScriptForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['codigo']
            try:
                output = {}
                exec(code, {}, output)
                return render(request, 'data_academy/pages/resultado.html', {'output': output})
            except Exception as e:
                return render(request, 'data_academy/pages/erro.html', {'erro': str(e)})
    else:
        form = ScriptForm()
    return render(request, 'data_academy/pages/interpretador.html', {'form': form})
