# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:08:51 2020

@author: bapti
"""
import datetime
import time
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from DB import *


#barplot des moyennes de chaque produit
def moyenne_tous_produits():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P WHERE P.id = SC.idProduit GROUP BY P.nom ORDER BY P.categorie;"
    liste = DB.ConnexionSQLSelect(requete)
    n = len(liste)
    liste_nom = []
    liste_moy=[]
    requete2 = "SELECT count(*) FROM commande;"
    nb_commande = DB.ConnexionSQLSelect(requete2)[0][0]
    for i in range(0,n):
        liste_nom.append(liste[i][0])
        liste_moy.append(liste[i][1]/nb_commande)
    plt.figure(figsize=(15,n//2))
    plt.barh(liste_nom,liste_moy,height=0.5,color = 'dodgerblue')
    plt.xlabel('Moyenne')
    plt.ylabel('Produits')
    plt.savefig('moyenne_produit.png')
    #plt.show()

#barplot de tous les produits avec quantités commandées 
def quantite_total_produit():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P  WHERE P.id = SC.idProduit GROUP BY P.nom ORDER BY P.categorie;"
    liste = DB.ConnexionSQLSelect(requete)
    n = len(liste)
    liste_nom = []
    liste_quant=[]
    for i in range(0,n):
        liste_nom.append(liste[i][0])
        liste_quant.append(liste[i][1])
    plt.figure(figsize=(15,n//2))
    plt.barh(liste_nom,liste_quant,height=0.5,color = 'dodgerblue')
    plt.xlabel('Quantités commandées')
    plt.ylabel('Produits')
    plt.savefig('quantite_produit.png')
    #plt.show()


#barplot des produits d'une catégorie choisie
def quantite_produits_categorie(categorie):
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P WHERE P.id = SC.idProduit AND P.categorie='"+categorie+"' GROUP BY P.nom;"
    liste = DB.ConnexionSQLSelect(requete)
    n = len(liste)
    liste_nom = []
    liste_quant=[]
    for i in range(0,n):
        liste_nom.append(liste[i][0])
        liste_quant.append(liste[i][1])
    plt.figure(figsize=(15,n//2+3))
    plt.barh(liste_nom,liste_quant,height=0.5,color = 'dodgerblue')
    plt.title('Produits de la catégorie : '+categorie)
    plt.xlabel('Quantités commandées')
    plt.ylabel('Produits')
    plt.savefig('quantite_produit_catégorie.png')
    #plt.show()
    
    
#barplot du top 5 des produits les plus commandés
def top5_produit():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P WHERE P.id = SC.idProduit GROUP BY P.nom ORDER BY sum(SC.quantiteDemandee) DESC;"
    reponse = DB.ConnexionSQLSelect(requete)
    liste_produit = []
    liste_quantite = []
    for i in range(0,5):
        liste_produit.append(reponse[i][0])
        liste_quantite.append(reponse[i][1])
    plt.figure(figsize=(12,6))
    plt.bar(liste_produit, liste_quantite, width=0.5,color = 'dodgerblue')
    plt.xlabel('Produits')
    plt.ylabel('Quantités commandées')
    plt.savefig('top5.png')
    #plt.show()

     
#renvoie les produits qui constituent une commande avec les quantités
def detail_commande(id_comm):
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM souscommande SC, produit P, commande C WHERE C.id="+str(id_comm)+" AND SC.idCommande = C.id AND P.id = SC.idProduit GROUP BY P.nom; "
    return DB.ConnexionSQLSelect(requete)


#renvoi la liste des produits d'une catégorie
def produit_par_categorie(categorie):
    requete = "SELECT nom FROM produit WHERE categorie='"+categorie+"';"
    return DB.ConnexionSQLSelect(requete)


#Combien de fois un produit est acheté en moyenne, lorsqu'il est acheté
def moyenne_par_commande(produit):
    requete = "SELECT sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P WHERE P.id = SC.idProduit and P.nom='"+produit+"';"
    a = DB.ConnexionSQLSelect(requete)
    quantite=a[0][0]
    requete = "SELECT count(*) FROM souscommande SC JOIN produit P  WHERE SC.idProduit = P.id AND P.nom='"+produit+"';"
    b = DB.ConnexionSQLSelect(requete)
    nb_comm = b[0][0]
    return quantite/nb_comm


#combien de fois un produit est acheté en moyenne
def moyenne(produit):
    requete = "SELECT sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P WHERE P.id = SC.idProduit and P.nom='"+produit+"';"
    a = DB.ConnexionSQLSelect(requete)
    quantite=a[0][0]
    requete = "SELECT count(*) FROM commande;"
    b = DB.ConnexionSQLSelect(requete)
    nb_comm = b[0][0] 
    return quantite/nb_comm


def nombre_commande():
    requete = "SELECT count(*) FROM commande;"
    nb = DB.ConnexionSQLSelect(requete)[0][0]
    return nb


def nombre_produit():
    requete = "SELECT count(*) FROM produit;"
    nb = DB.ConnexionSQLSelect(requete)[0][0]
    return nb


def Produit_plus_demande():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM souscommande SC JOIN produit P WHERE P.id = SC.idProduit ORDER BY sum(SC.quantiteDemandee) DESC;"
    nom_produit = DB.ConnexionSQLSelect(requete)[0][0]
    quant_produit = DB.ConnexionSQLSelect(requete)[0][1]
    return nom_produit , quant_produit


def nombre_inscription():
    requete = "SELECT count(*) FROM demandeur;"
    nb = DB.ConnexionSQLSelect(requete)[0][0]
    return nb


def liste_categorie():
    requete = "SELECT distinct categorie FROM produit;"
    return DB.ConnexionSQLSelect(requete)
    
#renvoie le nombre de commande en cours (pas encore livrées)
def nombre_commande_encours():
    date0 = datetime.date.today()
    date1 = date0 - datetime.timedelta(days=1)
    date2 = date0 - datetime.timedelta(days=2)
    requete = "SELECT count(*) FROM commande WHERE datecommande ='"+date0+"' OR datecommande ='"+date1+"' OR datecommande ='"+date2+"';"
    nb = DB.ConnexionSQLSelect(requete)[0][0]
    return nb

