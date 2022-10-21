
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiares

def familiares(request,nombre, edad, fechaDeNac):
    familiares = Familiares(nombre=nombre, edad=edad, fechaDeNac=fechaDeNac)
    familiares.save()

    return HttpResponse(f"""
        <p>Nombre: {familiares.nombre} - Edad: {familiares.edad} - fechaDeNac: {familiares.fechaDeNac} - Toda la familia reunida <p/>
    """)
def lista_familiares(request):

    lista = Familiares.objects.all()

    return render(request, "Lista_familiares.html", {"lista_familiares": lista})