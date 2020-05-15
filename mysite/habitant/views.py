# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import sys
sys.path.append('../')
from DB import *

# Create your views here.

def habitantConnexion (request):
	if request.method == 'GET':
		request.session.flush()
		return render(request,'habitant/connexion.html')
	elif request.method == 'POST':
		email = request.POST["email"]
		password = request.POST["password"]
		requete = "Select id from Demandeur where email = '"+email+"' and mdp ='"+password+ "';"
		print("email:"+email)
		IdDemandeur = DB.ConnexionSQLSelect(requete)
		if IdDemandeur!=[]:
			print(IdDemandeur)
			request.session.set_expiry(600)
			request.session['username']=IdDemandeur[0][0]
			return HttpResponseRedirect('/habitant/espace-personnel/')
		else:
			#l'identifiant demandé n'existe pas
			return HttpResponseRedirect('/habitant/connexion/')

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
	if request.method=='GET' and str(request.GET)!="<QueryDict: {}>":
		print(request.GET)
	request.session.set_expiry(600)#10 minutes avant que la session n'expire
	return render(request,"habitant/espace-personnel.html",{"data":""})

def habitantDemande (request):
	request.session.set_expiry(600)
	listedataproduits=[]

	listeproduitsbrute=DB.ConnexionSQLSelect("SELECT id,nom,categorie, prix FROM produit")
	for produit in listeproduitsbrute:
		listedataproduits.append({
		"produitId":produit[0],
		"NomProduit":produit[1],
		"CatégorieProduit":produit[2],
		"PrixProduit":produit[3]})
	data={"produits": listedataproduits}
	if not(request.session.has_key('username')):
		return HttpResponseRedirect("/habitant/connexion/")
	elif request.method=='GET':
		if str(request.GET)=="<QueryDict: {}>":
			data["Title"]="Produits proposés"
			return render(request, "habitant/demande.html", data)
	elif request.method=='POST':
		idClient = request.session['username']
		requete = "INSERT INTO commande (idDemandeur) VALUES ("+str(idClient)+");"
		DB.RequestSQL(requete)
		requeteId = "SELECT MAX(id) FROM commande WHERE idDemandeur="+str(idClient)+";";
		idcommande = DB.ConnexionSQLSelect(requeteId)
		for element in request.POST:
			if(request.POST[element]!='0'):
				DB.RequestSQL("INSERT INTO souscommande(`idCommande`,`idProduit`,`quantiteDemandee`) VALUES ("+str(idcommande[0][0])+",'"+str(element)+"',"+str(request.POST[element])+");")
		request.session['username']=idcommande[0][0]
		return HttpResponseRedirect("/habitant/espace-personnel/")

def habitantDerniereCommande(request):
	listedataproduits=[]

	listeproduitsbrute=DB.ConnexionSQLSelect("SELECT produit.id,nom,categorie, prix,quantiteDemandee FROM produit,souscommande,commande")
	for produit in listeproduitsbrute:
		listedataproduits.append({
		"produitId":produit[0],
		"NomProduit":produit[1],
		"CatégorieProduit":produit[2],
		"PrixProduit":produit[3],
		"Nombre":produit[4]
		})
	data={"produits": listedataproduits}
	if request.method=='GET':
		# for element in listeproduitsbrute:
		# 	titre+=str(element[0])+","+request.GET[str(element[0])+',Quantite']+";"
		if str(request.GET)=="<QueryDict: {}>":
			data["Title"]="Produits proposés"
			return render(request, "habitant/commande-en-cours.html", data)
		"""else:
			idClient = request.session["username"]"""

def habitantCommandeEnCours (request):
	if request.session.has_key('username'):
		listedataproduits=[]

		listeproduitsbrute=DB.ConnexionSQLSelect("SELECT commande.id,nom,categorie, prix,quantiteDemandee FROM produit,souscommande,commande WHERE idDemandeur='"+str(request.session['username'])+"' AND produit.id=idProduit AND idCommande=commande.id AND commande.id=(SELECT MAX(id) FROM commande WHERE idDemandeur='"+str(request.session['username'])+"');")
		for produit in listeproduitsbrute:
			listedataproduits.append({
			"produitId":produit[0],
			"NomProduit":produit[1],
			"CatégorieProduit":produit[2],
			"PrixProduit":produit[3],
			"Nombre":produit[4]
			})
		data={"produits": listedataproduits}
		if request.method=='GET':
			# for element in listeproduitsbrute:
			# 	titre+=str(element[0])+","+request.GET[str(element[0])+',Quantite']+";"
			if str(request.GET)=="<QueryDict: {}>":
				data["Title"]="Produits proposés"
				return render(request, "habitant/commande-en-cours.html", data)
	else:
		return HttpResponseRedirect("/habitant/connexion/")

def habitantSpecial (request):
		return HttpResponse("Page pour les demandes spéciales des habitants")

def habitantPaiement (request):
		return HttpResponse("Page attribuée au paiement des commandes")

def habitantHistoriqueCommandes(request):
	user=request.session['username']
	listedataproduits=[]

	listeproduitsbrute=DB.ConnexionSQLSelect("SELECT commande.id,nom,categorie, sum(prix),sum(quantiteDemandee) FROM produit,souscommande,commande WHERE idDemandeur="+str(user)+" AND produit.id=idProduit AND idCommande=commande.id;")
	for produit in listeproduitsbrute:
		listedataproduits.append({
		"IdCommande":produit[0],
		"DateCommande":produit[1],
		"DateLivraison":produit[2],
		"PrixTotalCommande":produit[3],
		"NombreProduit":produit[4]
		})
	data={"produits": listedataproduits}
	if request.method=='GET':
		data["Title"]="Produits proposés"
		return render(request, "habitant/commande-en-cours.html", data)
