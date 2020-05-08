from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import sys
sys.path.append('../')
from DB import *

# Create your views here.

def habitantConnexion (request):
		return HttpResponse("Page de connexion pour les habitants")

def habitantInscription (request):
	if request.method == 'GET':
		return render(request, 'habitant/inscription.html')
	elif request.method == 'POST':
		nom = request.POST["nom"]
		prenom = request.POST["prenom"]
		password = request.POST["password"]
		email = request.POST["email"]
		tel = request.POST["tel"]
		n_rue = request.POST["n-rue"]
		rue = request.POST["rue"]
		code_postal = request.POST["code-postal"]
		foyer_n_habitant = request.POST["foyer-n-habitant"]
		nomsproches = ''

		print(nom,prenom,password,email, tel, n_rue, rue, code_postal, foyer_n_habitant)
		Nom = nom + " " + prenom
		adresse = n_rue + " "+ rue + " " + code_postal
		request = "Insert into `projetpython`.`Demandeur` (`nom`, `email`, `mdp`, `telephone`, `adresse`, `nbprochesfoyer`, `nomsproches`) Values ('"+Nom+"','"+email+"' , '"+password+"','"+tel+"', '"+adresse+"', '"+foyer_n_habitant+"', '"+nomsproches+"');"
		DB.RequestSQL(request)
		return HttpResponseRedirect('/habitant/espace-personnel/')
		# renvoyer vers EspacePerso (code 302)


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

