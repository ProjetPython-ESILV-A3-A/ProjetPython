# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import sys
sys.path.append('../')
from DB import *

def transfoDate(date):
	return "'"+str(date.year)+"/"+str(date.month)+"/"+str(date.day)+"'"

#Fonction de test de connexion :
def TestConnexion(request):
	if request.session.has_key('username'):
		if request.session.has_key('motDePasse'):
			requete="SELECT id FROM Demandeur WHERE id=" + str(request.session['username']) + " AND mdp='" + str(request.session['motDePasse']) + "';"
			resultat=DB.ConnexionSQLSelect(requete)
			if resultat!=[[]]:
				return True
	return False
# Create your views here.

def habitantConnexion (request):
	if request.method == 'GET':
		request.session.flush()
		return render(request,'habitant/connexion.html')
	elif request.method == 'POST':
		email = request.POST["email"]
		password = request.POST["password"]
		requete = "Select id,mdp from Demandeur where email = '"+email+"' and mdp ='"+password+ "';"
		print("email:"+email)
		IdDemandeur = DB.ConnexionSQLSelect(requete)
		if IdDemandeur!=[]:
			print(IdDemandeur)
			request.session.set_expiry(600)
			request.session['username']=IdDemandeur[0][0]
			request.session['motDePasse']=IdDemandeur[0][1]
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
		#On selectione l'ID du nouvel
		requete = "Select id,mdp from Demandeur where email = '"+email+"' and mdp ='"+password+ "';"
		print("email:"+email)
		IdDemandeur = DB.ConnexionSQLSelect(requete)
		request.session['username']=IdDemandeur[0][0]
		request.session['motDePasse']=IdDemandeur[0][1]
		return HttpResponseRedirect('/habitant/espace-personnel/')
		# renvoyer vers EspacePerso (code 302)


def habitantEspacePerso (request):
	if TestConnexion(request):
		request.session.set_expiry(600)#10 minutes avant que la session n'expire
		listelongueur=DB.ConnexionSQLSelect("SELECT dateCommande FROM commande WHERE idDemandeur="+str(request.session['username'])+" AND dateCommande<="+transfoDate(datetime.datetime.now())+" AND dateCommande>"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")
		existenceCommande=(len(listelongueur)!=0)
		data={
			"StatutCommande1":existenceCommande*"En cours"+(not(existenceCommande))*"Aucune commande en cours",
			"PrixTotalCommande1":DB.ConnexionSQLSelect("SELECT sum(prix*quantiteDemandee) FROM produit,sousCommande,commande WHERE idDemandeur="+str(request.session['username'])+" AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<="+transfoDate(datetime.datetime.now())+" AND dateCommande>"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+" GROUP BY commande.id ORDER BY commande.id DESC;")[0][0],
			"NombreProduitCommande1":DB.ConnexionSQLSelect("SELECT Count(*) FROM produit,sousCommande,commande WHERE idDemandeur="+str(request.session['username'])+" AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<="+transfoDate(datetime.datetime.now())+" AND dateCommande>"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+" GROUP BY commande.id ORDER BY commande.id DESC;")[0][0],
			"DateLivraison":DB.ConnexionSQLSelect("SELECT MAX(dateCommande) FROM produit,sousCommande,commande WHERE idDemandeur="+str(request.session['username'])+" AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")[0][0],
			"PrixTotalCommande2":DB.ConnexionSQLSelect("SELECT sum(prix) FROM produit,sousCommande,commande WHERE idDemandeur="+str(request.session['username'])+" AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")[0][0],
			"NombreProduitCommande2":DB.ConnexionSQLSelect("SELECT Count(prix) FROM produit,sousCommande,commande WHERE idDemandeur="+str(request.session['username'])+" AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")[0][0]
			}
		return render(request,"habitant/espace-personnel.html",data)
	else:
		return HttpResponseRedirect("/habitant/connexion/")

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
	if not(TestConnexion(request)):
		return HttpResponseRedirect("/habitant/connexion/")
	elif request.method=='GET':
		if str(request.GET)=="<QueryDict: {}>":
			data["Title"]="Produits proposés"
			return render(request, "habitant/demande.html", data)
	elif request.method=='POST':
		idClient = request.session['username']
		requete = "INSERT INTO commande(idDemandeur,dateCommande) VALUES ("+str(idClient)+","+transfoDate(datetime.datetime.now())+");"
		DB.RequestSQL(requete)
		requeteId = "SELECT MAX(id) FROM commande WHERE idDemandeur="+str(idClient)+";";
		idcommande = DB.ConnexionSQLSelect(requeteId)
		for element in request.POST:
			if(request.POST[element]!='0'):
				DB.RequestSQL("INSERT INTO souscommande(`idCommande`,`idProduit`,`quantiteDemandee`) VALUES ("+str(idcommande[0][0])+",'"+str(element)+"',"+str(request.POST[element])+");")
		return HttpResponseRedirect("/habitant/espace-personnel/")

def habitantDerniereCommande(request):
	if TestConnexion(request):
		listedataproduits=[]
		MaxID=DB.ConnexionSQLSelect("SELECT MAX(id) FROM commande WHERE idDemandeur="+str(request.session['username'])+" AND dateCommande<="+transfoDate(datetime.datetime.now())+" AND dateCommande>"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")[0][0]
		listeproduitsbrute=DB.ConnexionSQLSelect("SELECT commande.id,nom,categorie, prix,quantiteDemandee FROM produit,souscommande,commande WHERE idDemandeur='"+str(request.session['username'])+"' AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")
		for produit in listeproduitsbrute:
			if(produit[0]==MaxID):
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
	else:
		return HttpResponseRedirect("/habitant/connexion/")

def habitantCommandeEnCours (request):
	if TestConnexion(request):
		listedataproduits=[]
		MaxID=DB.ConnexionSQLSelect("SELECT MAX(id) FROM commande WHERE idDemandeur="+str(request.session['username'])+" AND dateCommande<="+transfoDate(datetime.datetime.now())+" AND dateCommande>"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")[0][0]
		listeproduitsbrute=DB.ConnexionSQLSelect("SELECT commande.id,nom,categorie, prix,quantiteDemandee  FROM produit,souscommande,commande WHERE idDemandeur="+str(request.session['username'])+" AND produit.id=idProduit AND idCommande=commande.id AND dateCommande<="+transfoDate(datetime.datetime.now())+" AND dateCommande>"+transfoDate(datetime.datetime.now()+datetime.timedelta(days=-3))+";")
		for produit in listeproduitsbrute:
			if(produit[0]==MaxID):
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
	if TestConnexion(request):
		request.session.set_expiry(600)
		return render(request,"habitant/demande-spéciale.html",{})
	else:
		return HttpResponseRedirect("/habitant/connexion/")

def habitantPaiement (request):
	if TestConnexion(request):
		request.session.set_expiry(600)
		return HttpResponse("Page attribuée au paiement des commandes")
	else:
		return HttpResponseRedirect("/habitant/connexion/")

def habitantHistoriqueCommandes(request):
	if TestConnexion(request):
		request.session.set_expiry(600)
		user=request.session['username']
		listedataproduits=[]
		listeproduitsbrute=DB.ConnexionSQLSelect("SELECT commande.id,dateCommande,categorie, sum(prix),sum(quantiteDemandee) FROM produit,souscommande,commande WHERE idDemandeur="+str(user)+" AND produit.id=idProduit AND idCommande=commande.id GROUP BY id;")
		for produit in listeproduitsbrute:
			listedataproduits.append({
			"IdCommande":produit[0],
			"DateCommande":produit[1],
			"DateLivraison":produit[1] + datetime.timedelta(days=3),
			"PrixTotalCommande":(produit[3]//0.01)*0.01,
			"NombreProduit":produit[4]
			})
		data={"produits": listedataproduits}
		if request.method=='GET':
			data["Title"]="Produits proposés"
			return render(request, "habitant/historique-des-commandes.html", data)
	else:
		return HttpResponseRedirect("/habitant/connexion/")
