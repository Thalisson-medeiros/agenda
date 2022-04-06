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

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id') #pegando o id
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento) 
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('criacao')
        usuario = request.user
        local = request.POST.get('local')
        id_evento = request.GET.get('evento/id')
        print(id_evento)
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.local = local
                evento.save()
                
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
            #                                            data_evento=data_evento,
            #                                            descricao = descricao,
            #                                            local=local)
        else:
            Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao =descricao,
                              local=local,
                              usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')