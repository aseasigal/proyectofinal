from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alfajor
from .forms import AlfajorForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm



def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm (request,data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                login(request,user)
                return render(request,'paginas/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request,'paginas/inicio.html',{'mensaje':'Error, datos incorrectos'})
        else:
            return render(request,'paginas/inicio.html',{'mensaje':'Error, formulario erroneo'})
    form = AuthenticationForm()
    return render(request,'paginas/login.html',{'form':form} )
    
    

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')



def alfajores(request):
    alfajores = Alfajor.objects.all()
    return render(request, 'alfajores/index.html', {'alfajores': alfajores} )


def crear(request):
    formulario = AlfajorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('alfajores')
    return render(request, 'alfajores/crear.html', {'formulario' : formulario})

def editar(request, id):
    alfajor = Alfajor.objects.get(id=id)
    formulario = AlfajorForm(request.POST or None, request.FILES or None, instance = alfajor)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('alfajores')
    return render(request, 'alfajores/editar.html', {'formulario' : formulario} )

def eliminar (request,id):
    alfajor = Alfajor.objects.get (id=id)
    alfajor.delete()
    return redirect('alfajores')

# Create your views here.
