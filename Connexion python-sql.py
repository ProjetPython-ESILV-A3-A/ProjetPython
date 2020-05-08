from secret import bdd_login, bdd_password

#PRE REQUIS
#Avoir installer my sql connector
#Pour faire ca, allez dans cmd et tapez "pip install mysql-connector-python"
#Et ensuite on l'importe dans la ligne d'en dessous
import mysql.connector

def ConnexionSQL(requete):
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

infos = ConnexionSQL("select email from Demandeur")
for ligne in infos:
    print(ligne)



