from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def acceuil(request):
    output=", ".join(["Page d'acceuil","acces Commune","acces Habitant"])
    return HttpResponse(output)
