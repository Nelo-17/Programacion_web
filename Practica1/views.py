from django.shortcuts import render
from django.http import HttpResponse
from .forms import PracticaForm

# Create your views here.
def index(request):
    return render(request,'index.html',{
        
    })
    
def servicios(request):
    return render(request,'servicios.html',{
        
    })
    
    
def Inicio(request):
    return render(request,'Inicio.html',{
        
    })

def contactos(request):
    if request.method == 'POST':
        form = PracticaForm(request.POST)
        if form.is_valid():
            form.save()
            form = PracticaForm()
    else:
        form = PracticaForm()
    return render(request,'contactos.html',{
        'form': form
    })
