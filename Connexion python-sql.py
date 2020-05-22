from secret import bdd_login, bdd_password

#PRE REQUIS
#Avoir installer my sql connector
#Pour faire ca, allez dans cmd et tapez "pip install mysql-connector-python"
#Et ensuite on l'importe dans la ligne d'en dessous
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import random
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from datetime import datetime,timedelta,date

def ConnexionSQLSelect(requete):
    madb = mysql.connector.connect(
        host = "localhost",
        user = bdd_login,
        passwd = bdd_password,
        database = "projetpython"
        
        )
    
    #madb = ma database
    moncurseur = madb.cursor()
    moncurseur.execute(requete)
    infos = []
    for ligne in moncurseur :
        infos.append(ligne)
    
    return infos

def ConnexionSQL(requete):
    try:
        madb = mysql.connector.connect(
            host = "localhost",
            user = bdd_login,
            passwd = bdd_password,
            database = "projetpython"
        
        )
    
        moncurseur = madb.cursor()
        moncurseur.execute(requete)
        madb.commit()
        #print(moncurseur.rowcount, "tuple à bien été pris en compte")
        moncurseur.close()
    
    except mysql.connector.Error as error:
        print("La requete a echoue {}".format(error))

    finally:
        if (madb.is_connected()):
            madb.close()
            #print("La connexion MYSQL est fermé")





#TEST POUR LE INSERT/DELETE/UPDATE
requeteInsert = "INSERT INTO `projetpython`.`Admin` (`nom`,`email`,`mdp`) VALUES ('yass','yass@gmail.com','monmdp')"
requeteDelete = "DELETE from Admin where id = 3"
requeteUpdate = "UPDATE Admin SET nom = 'Equipe 4' where id=1"
#ConnexionSQL(requeteUpdate)


#TEST POUR LE SELECT
#requeteSelect = "select nom,id from Admin"
#infos = ConnexionSQLSelect(requeteSelect)
#for ligne in infos:
#    print(ligne)

#TEST AVEC VARIABLES
nouveaunom = "Equipe 4"
requeteSelect = "Select nom,id,email from Admin where nom = '"+nouveaunom+"'"
infos = ConnexionSQLSelect(requeteSelect)

#for ligne in infos:
#    print(ligne)
    
#GENERER PANIER ALEATOIRE

def GenererPanierAleatoire(ID_DEMANDEUR,NB_PRODUITS):

    aujourdhui = datetime.now()
    aujourdhuiString = aujourdhui.strftime('%m/%d/%y')
    requete1 = "INSERT INTO `projetpython`.`Commande` (`idDemandeur`,`dateCommande`) VALUES ("+str(ID_DEMANDEUR)+" , '"+aujourdhuiString+"');"
    ConnexionSQL(requete1)
    requeteId = "select max(id) from Commande"
    idTab = ConnexionSQLSelect(requeteId)
    idCommande = idTab[0][0]

    for panier in range(NB_PRODUITS):    

        idProduit = random.randint(1,20)        
        quantite = random.randint(1,5)    
        requete3 = "INSERT INTO `projetpython`.`SousCommande` (`idCommande`,`idProduit`,`quantiteDemandee`) VALUES ("+str(idCommande)+" , "+str(idProduit)+" , "+str(quantite)+");"    
        ConnexionSQL(requete3)


def GenererDesPaniersAleatoire(NB_PANIERS):
    for i in range(NB_PANIERS):
        GenererPanierAleatoire(1, 6)

#GenererDesPaniersAleatoire(5)


def Apriori():
    
    listeCommandes =[]
    
    #Pour chaque commande
    requete = "select id from Commande "
    tabIdCommandes = ConnexionSQLSelect(requete)
    
    #On recupere la liste des produits (=le panier)
    for idCom in tabIdCommandes:
        idCom = idCom[0]
        
        #On recupere le panier pour chaque commande
        requete2 = "select P.nom from Produit P JOIN SousCommande S ON P.id = S.idProduit where S.idCommande = "+str(idCom)+" ;" #retourne un panier
        panierTab = ConnexionSQLSelect(requete2)
    
        panierListe = []
        #On remet la liste des produits dans une liste
        for i in range (len(panierTab)):
            panierListe.append(panierTab[i][0])
    
        #On ajoute le panier dans la liste des commandes
        listeCommandes.append(panierListe)
        #On obtient une liste de liste, ou chaque ligne represente un panier

    #APRIORI

    te = TransactionEncoder()
    te_ary = te.fit(listeCommandes).transform(listeCommandes)
    tab = pd.DataFrame(te_ary, columns=te.columns_)
    #print(tab)
    frequent_itemsets = apriori(tab, min_support=0.6, use_colnames=True)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    
    #Condition
    x =frequent_itemsets[ (frequent_itemsets['length'] == 2) &(frequent_itemsets['support'] >= 0.6) ]
    val = float(x['support'])
    #return val
    
#GENERER PANIER ALEATOIRE
#Apriori()

#Indique si une commande est en cours(false) de livraion ou si elle est arrivée(true)
def EtatCommande(idCommande):
    arrive=True
    
    requeteSelect="select dateCommande from Commande where id = "+str(idCommande)+" ;"
    tab = ConnexionSQLSelect(requeteSelect)
    dateString = tab[0][0]

    dateCommande = datetime.strptime(dateString,'%m/%d/%y')    
    aujourdhui= datetime.now()
    
    annee = aujourdhui.year-dateCommande.year
    if(annee == 0):
        mois = aujourdhui.month-dateCommande.month
        if(mois == 0):
            jours = aujourdhui.day-dateCommande.day
            if(jours<3):
                arrive=False
    
    return arrive

#Indique la commande en cours de l'utilisateur et -1 si aucune commande n'est en cours,-2 si il n'a aucune commande tout cours
def CommandeEnCours(ID_DEMANDEUR):
    requete = "select id from Commande where idDemandeur = "+str(ID_DEMANDEUR)+" ;"
    idCommandes = ConnexionSQLSelect(requete)
    if(len(idCommandes)==0):
        return -2
    else:
        for commande in idCommandes:
            commande = commande[0]
            if(EtatCommande(commande) == False):
                return commande
        return -1

def GenererPanierAleatoire(ID_DEMANDEUR,NB_PRODUITS):

    requete1 = "INSERT INTO `projetpython`.`Commande` (`idDemandeur`) VALUES ("+str(ID_DEMANDEUR)+");"
    ConnexionSQL(requete1)
    requeteId = "select max(id) from Commande"
    idTab = ConnexionSQLSelect(requeteId)
    idCommande = idTab[0][0]
    print(idCommande)
    for panier in range(NB_PRODUITS):    

        idProduit = random.randint(1,20)        
        quantite = random.randint(1,5)    
        requete3 = "INSERT INTO `projetpython`.`SousCommande` (`idCommande`,`idProduit`,`quantiteDemandee`) VALUES ("+str(idCommande)+" , "+str(idProduit)+" , "+str(quantite)+");"    
        ConnexionSQL(requete3)


def GenererDesPaniersAleatoire(NB_PANIERS):
    for i in range(NB_PANIERS):
        GenererPanierAleatoire(1, 5)

GenererDesPaniersAleatoire(6)

def Commandes(ID_DEMANDEUR):
    commande = CommandeEnCours(ID_DEMANDEUR)
    if(commande==-2):
        print("Ce client n'a effectue aucune commande")
    elif(commande==-1):
        print("Ce client n'a pas de commande en cours")
    else :
        print("La commande en cours de ce client est "+str(commande))


#Indique le prix totale d'une commande ainsi que le nombre de produits dans la commande
def PrixTotaleEtQteCommande(ID_COMMANDE):
    requete = "select P.prix,S.quantiteDemandee from SousCommande S JOIN Produit P ON S.idProduit=P.id where S.idCommande= " +str(ID_COMMANDE)+ " ;"
    produitsTab = ConnexionSQLSelect(requete)
    prixTot=0
    
    for produit in produitsTab:
        prixProd=produit[0]
        qte=produit[1]
        prixTot+=prixProd*qte
    
    
    nbproduits = len(produitsTab)
    return prixTot,nbproduits

def CommandeLaPlusRecente(ID_DEMANDEUR):
    requete = "select max(dateCommande) from Commande where idDemandeur= "+str(ID_DEMANDEUR)+" ;"
    dateMaxTab = ConnexionSQLSelect(requete)
    dateMax = dateMaxTab[0][0]
    
    requete = "select id from Commande where dateCommande = '"+dateMax+"' ;"
    idDateMaxTab = ConnexionSQLSelect(requete)
    idDateMax = idDateMaxTab[0][0]
    
    return idDateMax     
        
def LstProduitsDeCommande(ID_COMMANDE):
    requete = "select S.quantiteDemandee,P.unite,P.nom from Produit P JOIN SousCommande S ON P.id = S.idProduit where S.idCommande = "+str(ID_COMMANDE)+" ;"
    produitsTab = ConnexionSQLSelect(requete)
    return produitsTab

def HistoriqueCommande(ID_DEMANDEUR):
    requete ="select id from Commande where idDemandeur = "+str(ID_DEMANDEUR)+" ;"
    idCommandesTab = ConnexionSQLSelect(requete)
    historique=[]
    
    for commande in idCommandesTab:
        idcommande = commande[0]
        lstProd = LstProduitsDeCommande(idcommande)
        prix,nbproduits = PrixTotaleEtQteCommande(idcommande)
        
        historique.append([idcommande,lstProd,prix,nbproduits])
        #EXEMPLE : [[1 , [(2,"g","banane"),(4,"kg","legumes secs")], 15.4euros , 2], [...], ]
    return historique

def AffichageHistorique(ID_DEMANDEUR):
    historique = HistoriqueCommande(ID_DEMANDEUR)
    nbcommandes = len(historique)
    print("Cet utilisateur a fait "+str(nbcommandes)+" commandes !")
    print()
    
    for commande in historique:
        print("Commande numéro : "+ str(commande[0]))
        print("LISTE PRODUITS DU PANIER : ")
        print(AffichageListe(commande[1]))
        print()
        print("Pour un prix de "+str(commande[2])+" euros.")
        print("Total des articles : "+str(commande[3]))
        print("---------------------------------------------")

def AffichageListe(liste):
    listeStr=""
    for produit in liste:
        listeStr+="-"+str(produit[0])+" "+str(produit[1])+" de "+str(produit[2])+"\n"
    return listeStr
        
#Commandes(1)
#prixTotale,nbproduits = PrixTotaleEtQteCommande(1)
#print("le prix est de "+str(prixTotale)+" euros pour "+str(nbproduits)+" produits achetés.")
#idDateMax = CommandeLaPlusRecente(1)
#print(idDateMax)
#HistoriqueCommande(1)
AffichageHistorique(1)

