from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from DB import *
import matplotlib.pyplot as plt
import io

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
    elif request.method=="POST":
        for element in request.POST:
            print(element)
            requete="DELETE FROM produit WHERE id="+element+";"
            DB.RequestSQL(requete)
        listedataproduits=[]
        return HttpResponseRedirect("/commune/produits/sub/")

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
    elif request.method=='POST':
        nom=request.POST['nomProduit']
        categorie=request.GET['categorieProduit']
        unite=request.GET['uniteProduit']
        prix=request.GET['prixProduit']
        requete="INSERT INTO produit(`nom`,`categorie`,`unite`,`prix`) VALUES ('"+nom+"','"+categorie+"','"+unite+"',"+prix+");"
        return HttpResponseRedirect("/commune/produits/add/")


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
            },
            {
                "nom":"Visualisation plot",
                "link":"/commune/Visualisation/plot/"
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

def communeVisualisationplot(request):
    f=plt.figure(figsize=(16,6))
    produits=[]
    nombreProduits=[]
    requete="SELECT SUM(quantiteDemandee),nom FROM souscommande,produit WHERE idProduit=produit.id GROUP BY idProduit;"
    resultat=DB.ConnexionSQLSelect(requete)
    for element in resultat:
        produits.append(str(element[1]))
        nombreProduits.append(int(element[0]))
    produits.append("")
    nombreProduits.append(0)
    plt.hist(produits,bins=len(produits)-1,weights=nombreProduits,align='left')
    buf=io.BytesIO()
    plt.savefig(buf,format='svg',bbox_inches='tight')
    s=buf.getvalue()
    buf.close()
    plt.cla()
    response=HttpResponse(s,content_type='image/svg+xml')
    plt.close(f)
    # data={"data": [
    #         {
    #             "nom":"retour arriere",
    #             "link":"/commune/Visualisation/"
    #         }
    #     ],
    #     "titre":"Option de Visualisation n°"+str(numeroVu)
    #     }
    # return render(request, "commune/communeBase.html", data)
    return response

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
