from django.shortcuts import render
from django.http import HttpResponse
from DB import *

# Create your views here.

def communeBase(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/"
            },
            {
                "nom": "action",
                "link": "/commune/action"
            }
        ],
        "titre":"Imaginer ici un ecran d'identification"
        }
    return render(request, "commune/communeBase.html", data)

def communeaction(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/"
            },
            {
                "nom": "produits",
                "link": "/commune/produits/"
            },
            {
                "nom":"Visualisation",
                "link":"/commune/Visualisation/"
            }
        ],
        "titre":"Selection action à faire"
        }
    return render(request, "commune/communeBase.html", data)

def communeproduitChoix(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/action/"
            },
            {
                "nom": "ajout",
                "link": "/commune/produits/add/"
            },
            {
                "nom":"retirer",
                "link": "/commune/produits/sub/"
            }
        ],
        "titre":"Selection du destin de produits"
        }
    return render(request, "commune/communeBase.html", data)

def communeproduitSub(request):
    if request.method=='GET':
        if str(request.GET)=="<QueryDict: {}>":
            listedataproduits=[]

            listeproduitsbrute=DB.ConnexionSQLSelect("SELECT id,nom,categorie, unite FROM produit")
            for produit in listeproduitsbrute:
                listedataproduits.append({
                "produitId":produit[0],
                "NomProduit":produit[1],
                "CategorieProduit":produit[2],
                "uniteProduit":produit[3]})
            data={"data": [
                    {
                        "nom":"retour arriere",
                        "link":"/commune/produits/"
                    }
                ],
                "produits":listedataproduits,
                "titre":"Selection du/des produit/s à supprimer"
                }
            return render(request, "commune/choixSuppression.html", data)
        else:
            for element in request.GET:
                print(element)
                requete="DELETE FROM produit WHERE id="+element+";"
                DB.RequestSQL(requete)
            listedataproduits=[]

            listeproduitsbrute=DB.ConnexionSQLSelect("SELECT id,nom,categorie, prix FROM produit")
            for produit in listeproduitsbrute:
                listedataproduits.append({
                "produitId":produit[0],
                "NomProduit":produit[1],
                "CategorieProduit":produit[2],
                "PrixProduit":produit[3]})
            data={"data": [
                    {
                        "nom":"retour arriere",
                        "link":"/commune/produits/"
                    }
                ],
                "produits":listedataproduits,
                "titre":"Selection du/des produit/s à supprimer"
                }
            return render(request, "commune/choixSuppression.html", data)

def communeproduitAdd(request):
    if request.method=='GET':
        if str(request.GET)=="<QueryDict: {}>":
            data={"data": [
                    {
                        "nom":"retour arriere",
                        "link":"/commune/produits/"
                    }
                ],
                "titre":"Selection du/des produit/s à ajouter"
                }
            return render(request, "commune/ChoixAjoutProd.html", data)
        else:
            nom=request.GET['nomProduit']
            categorie=request.GET['categorieProduit']
            unite=request.GET['uniteProduit']
            prix=request.GET['prixProduit']
            print(nom+":"+str(type(nom))+"\n"+categorie+":"+str(type(categorie))+"\n"+unite+":"+str(type(unite))+"\n"+str(prix)+":"+str(type(prix))+"\n")
            requete="INSERT INTO produit(`nom`,`categorie`,`unite`,`prix`) VALUES ('"+nom+"','"+categorie+"','"+unite+"',"+prix+");"
            print(requete)
            reussite=True
            try:
                DB.RequestSQL(requete)
                reussite=True
            except:
                reussite=False
            data={"data": [
                    {
                        "nom":"retour arriere",
                        "link":"/commune/produits/"
                    }
                ],
                "titre":"Selection du/des produit/s à ajouter",
                "soustitre":"Produit rajouter avec succes"*reussite+"Echec de l'ajout"*(not(reussite))
                }
            return render(request, "commune/ChoixAjoutProd.html", data)


def communevisuchoix(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/action/"
            },
            {
                "nom": "Visualisation 1",
                "link": "/commune/Visualisation/1/"
            },
            {
                "nom": "Visualisation 2",
                "link": "/commune/Visualisation/2/"
            }
        ],
        "titre":"Selection de la visualisation"
        }
    return render(request, "commune/communeBase.html", data)

def communeVisualisation(request,numeroVu):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/Visualisation/"
            }
        ],
        "titre":"Option de Visualisation n°"+str(numeroVu)
        }
    return render(request, "commune/communeBase.html", data)

def communevalidsuppr(request,Produitasupprimer):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/action/"
            }
        ],
        "titre":"Etes-vous sûr de vouloir supprimer le produit "+Produitasupprimer+"?"
        }
    return render(request, "commune/communeBase.html", data)
