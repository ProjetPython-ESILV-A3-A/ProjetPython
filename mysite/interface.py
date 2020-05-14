# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:08:51 2020

@author: bapti
"""

import matplotlib.pyplot as plt
import sys
sys.path.append('../')
from DB import *


#barplot des moyennes de chaque produit
def moyenne_tous_produits():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit ORDER BY P.nom;"
    liste = DB.ConnexionSQLSelect(requete)
    n = len(liste)
    liste_nom = []
    liste_moy=[]
    requete2 = "SELECT count(*) FROM commande;"
    nb_commande = DB.ConnexionSQLSelect(requete2)[0][0]
    for i in range(0,n):
        liste_nom.append(liste[i][0])
        liste_moy.append(liste[i][1]/nb_commande)
    plt.bar(liste_nom,liste_moy)
    plt.xlabel('Produits')
    plt.ylabel('Moyenne')
    plt.show()
    

#barplot de tous les produits avec quantités commandées 
def quantite_total_produit():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit ORDER BY P.nom;"
    liste = DB.ConnexionSQLSelect(requete)
    n = len(liste)
    liste_nom = []
    liste_quant=[]
    for i in range(0,n):
        liste_nom.append(liste[i][0])
        liste_quant.append(liste[i][1])
    plt.bar(liste_nom,liste_quant)
    plt.xlabel('Produits')
    plt.ylabel('Quantités commandées')
    plt.show()
    
    
#barplot de tous les produits d'une catégorie avec quantités commandées 
def quantite_produit_par_categ(categorie):
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit AND P.categorie ='"+categorie+"' ORDER BY P.nom;"
    liste = DB.ConnexionSQLSelect(requete)
    n = len(liste)
    liste_nom = []
    liste_quant=[]
    for i in range(0,n):
        liste_nom.append(liste[i][0])
        liste_quant.append(liste[i][1])
    plt.bar(liste_nom,liste_quant)
    plt.xlabel('Produits de la catégorie : '+categorie)
    plt.ylabel('Quantités commandées')
    plt.show()
    
    
#barplot du top 5 des produits les plus commandés
def top5_produit():
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit ORDER BY sum(SC.quantiteDemandee) DESC;"
    reponse = DB.ConnexionSQLSelect(requete)
    liste_produit = []
    liste_quantite = []
    for i in range(0,5):
        liste_produit.append(reponse[i][0])
        liste_quantite.append(reponse[i][1])
    plt.bar(liste_produit, liste_quantite)
    plt.xlabel('Produits')
    plt.ylabel('Quantités commandées')
    plt.show()
    

#renvoie les produits qui constituent une commande avec les quantités
def detail_commande(id_comm):
    requete = "SELECT P.nom, SC.quantiteDemandee FROM sous-commande SC, produit P, commande C WHERE C.id="+id_comm+" AND SC.id_commande = C.id AND P.id = SC.idProduit; "
    return DB.ConnexionSQLSelect(requete)


#renvoi la liste des produits d'une catégorie
def produit_par_categorie(categorie):
    requete = "SELECT nom FROM produit WHERE categorie='"+categorie+"' ORDER BY nom;"
    return DB.ConnexionSQLSelect(requete)


#Combien de fois un produit est acheté en moyenne, lorsqu'il est acheté
def moyenne_par_commande(produit):
    requete = "SELECT sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit and P.nom='"+produit+"';"
    a = DB.ConnexionSQLSelect(requete)
    quantite=a[0][0]
    requete = "SELECT count(*) FROM souscommande SC WHERE SC.idProduit = P.id AND P.nom='"+produit+"';"
    b = DB.ConnexionSQLSelect(requete)
    nb_comm = b[0][0]
    return quantite/nb_comm


#combien de fois un produit est acheté en moyenne
def moyenne(produit):
    requete = "SELECT sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit and P.nom='"+produit+"';"
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
    requete = "SELECT P.nom, sum(SC.quantiteDemandee) FROM produit P, souscommande SC WHERE P.id = SC.idProduit ORDER BY sum(SC.quantiteDemandee) DESC;"
    nom_produit = DB.ConnexionSQLSelect(requete)[0][0]
    quant_produit = DB.ConnexionSQLSelect(requete)[0][1]
    return nom_produit , quant_produit


def nombre_inscription():
    requete = "SELECT count(*) FROM demandeur;"
    nb = DB.ConnexionSQLSelect(requete)[0][0]
    return nb
