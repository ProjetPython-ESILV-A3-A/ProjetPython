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

    requete1 = "INSERT INTO `projetpython`.`Commande` (`idDemandeur`) VALUES ("+str(ID_DEMANDEUR)+");"
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
    
Apriori()