from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import Datos_familiares

# Create your views here.

def tio(self):

    tio = Datos_familiares(nombre="Lucas", apellido="Moura", telefono=1158658545, cumpleaños="1969-5-13")
    tio.save()
    texto = f"Tio cargado: {tio.nombre} {tio.apellido} {tio.telefono} {tio.cumpleaños}"

    return HttpResponse(texto)

def primo(self):

    primo = Datos_familiares(nombre="Eduardo", apellido="Moura", telefono=1158941235, cumpleaños="1989-7-18")
    primo.save()
    texto = f"Primo cargado: {primo.nombre} {primo.apellido} {primo.telefono} {primo.cumpleaños}"

    return HttpResponse(texto)

def hermano(self):
    
    hermano = Datos_familiares(nombre="Jose", apellido="Moura", telefono=1155689814, cumpleaños="1992-2-23")
    hermano.save()
    texto = f"Hermano cargado: {hermano.nombre} {hermano.apellido} {hermano.telefono} {hermano.cumpleaños}"
    
    return HttpResponse(texto)