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
		request.session.set_expiry(300)#5 minutes avant que la session n'expire
		return HttpResponse("Page d'accueil de l'espace personnel des habitants")

def habitantDemande (request):
	request.session.set_expiry(300)
	listedataproduits=[]

	listeproduitsbrute=DB.ConnexionSQLSelect("SELECT id,nom,categorie, prix FROM produit")
	for produit in listeproduitsbrute:
		listedataproduits.append({
		"produitId":produit[0],
		"NomProduit":produit[1],
		"CatégorieProduit":produit[2],
		"PrixProduit":produit[3]})
	data={"produits": listedataproduits}
	if request.method=='GET':
		if str(request.GET)=="<QueryDict: {}>":
			data["Title"]="Produits proposés"
			return render(request, "habitant/demande.html", data)
	elif request.method=='POST':
		idClient = 1
		requete = "INSERT INTO commande (idDemandeur) VALUES ("+str(idClient)+");"
		DB.RequestSQL(requete)
		requeteId = "SELECT MAX(id) FROM commande WHERE idDemandeur="+str(idClient)+";";
		idcommande = DB.ConnexionSQLSelect(requeteId)
		for element in request.POST:
			if(request.POST[element]!='0'):
				DB.RequestSQL("INSERT INTO souscommande(`idCommande`,`idProduit`,`quantiteDemandee`) VALUES ("+str(idcommande[0][0])+",'"+str(element)+"',"+str(request.POST[element])+");")
		request.session['username']=idcommande[0][0]
		return HttpResponseRedirect("/habitant/paiement/")


def habitantSpecial (request):
		return HttpResponse("Page pour les demandes spéciales des habitants")

def habitantPanier (request):
		return HttpResponse("Page pour visualiser le panier des habitants + debug"+str(request.session['username']))

def habitantPaiement (request):
		return HttpResponse("Page attribué au paiement des commandes + (pr le debug) : "+str(request.session['username']))

