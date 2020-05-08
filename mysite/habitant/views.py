from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def habitantConnexion (request):
    return HttpResponse("Page de connexion pour les habitants")

def habitantInscription (request): 
    return HttpResponse("Page d'inscription pour les habitants")

def habitantEspacePerso (request):
    return HttpResponse("Page d'accueil de l'espace personnel des habitants")

def habitantDemande (request): 
    return HttpResponse("Page de demande pour les habitants")

def habitantSpecial (request):
    return HttpResponse("Page pour les demandes spéciales des habitants")

def habitantPanier (request):
    return HttpResponse("Page pour visualiser le panier des habitants")

def habitantPaiement (request):
    return HttpResponse("Page attribué au paiement des commandes")

