from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def communeBase(request):
    return render(request, "commune/index.html")

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

def communeproduitAdd(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/produits/"
            }
        ],
        "titre":"Selection du/des produit/s à ajouter"
        }
    return render(request, "commune/communeBase.html", data)

def communeproduitSub(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/produits/"
            },
            {
                "nom":"Produit 1",
                "link":"/commune/produits/sub/validation/1/"
            },
            {
                "nom":"Produit 2",
                "link":"/commune/produits/sub/validation/2/"
            }
        ],
        "titre":"Selection du/des produit/s à supprimer"
        }
    return render(request, "commune/communeBase.html", data)

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
