from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def communeBase(request):
    return HttpResponse("Page de base d'une commune")

def communeaction(request):
    return HttpResponse("Page de choix d'action d'une commune")

def communeproduitChoix(request):
    return HttpResponse("Page de choix d'action sur les produits d'une commune")

def communeproduitAdd(request):
    return HttpResponse("Page pour ajouter un produit dans une commune")

def communeproduitSub(request):
    return HttpResponse("Page pour enlever un produit dans une commune")

def communevisuchoix(request):
    return HttpResponse("Page de choix de visualisation d'une commune")

def communevisualisation(request,numeroVu):
    return HttpResponse("Page de visualisation n°%s d'une commune" % numeroVu)
