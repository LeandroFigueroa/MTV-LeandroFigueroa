from django.shortcuts import render
from .models import ModeloFamilia

def inicio(request):
   familiares = ModeloFamilia.objects.all()
   contexto = {'familiares': familiares}
   return render(request, 'FamilyProject/inicio.html', contexto)

def family_members(request, pk):
    pariente = ModeloFamilia.objects.get(id=int(pk))
    contexto = {'pariente': pariente} 
    return render(request, 'FamilyProject/familiar.html', contexto)
 
