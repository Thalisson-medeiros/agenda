from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout #usado no formulario ao clicar e enviar
from django.contrib import messages

# Create your views here.

#def index(request): #primeira forma de redirecionar o usuario para pagina agenda
#     return redirect('/agenda/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username = username, password = password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "usuário ou senha inválido")#ira mandar uma lista para login.html
        return redirect('/')

def login_user(request):
    return render(request, 'login.html') #pagina html

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/') #obriga o usuario a estar logado para poder acessar a pagina / se o usuario não for encontrado será redirecionado para a pagina login
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)