from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alfajor
from .forms import AlfajorForm



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
    return render(request, 'alfajores/crear.html', {'formulario' : formulario} )

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
