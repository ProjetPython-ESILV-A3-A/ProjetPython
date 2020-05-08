from django.shortcuts import render
from django.http import HttpResponse

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
        ]}
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
                "nom":"visualisation",
                "link": "/commune/visualisation/"
            }
        ]}
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
                "link": "/commune/produits/add/"
            }
        ]}
    return render(request, "commune/communeBase.html", data)

def communeproduitAdd(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/produits/"
            }
        ]
        }
    return render(request, "commune/communeBase.html", data)

def communeproduitSub(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/produits/"
            },
            {
                "nom":"Produit 1"
                "link":"/commune/produits/sub/validation/"
            },
            {
                "nom":"Produit 2"
                "link":"/commune/produits/sub/validation/"
            }
        ]}
    return render(request, "commune/communeBase.html", data)

def communevisuchoix(request):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/action/"
            },
            {
                "nom": "visualisation 1",
                "link": "/commune/visualisation/1/"
            },
            {
                "nom": "visualisation 2",
                "link": "/commune/visualisation/2/"
            }
        ]}
    return render(request, "commune/communeBase.html", data)

def communevisualisation(request,numeroVu):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/"
            }
        ]}
    return render(request, "commune/communeBase.html", data)

def communevalidsuppr(request,Produitasupprimer):
    data={"data": [
            {
                "nom":"retour arriere",
                "link":"/commune/action/"
            }
        ]}
    return render(request, "commune/communeBase.html", data)
