from secret import bdd_login, bdd_password

#PRE REQUIS
#Avoir installer my sql connector
#Pour faire ca, allez dans cmd et tapez "pip install mysql-connector-python"
#Et ensuite on l'importe dans la ligne d'en dessous
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

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
        print(moncurseur.rowcount, "tuple à bien été pris en compte")
        moncurseur.close()
    
    except mysql.connector.Error as error:
        print("La requete a echoue {}".format(error))

    finally:
        if (madb.is_connected()):
            madb.close()
            print("La connexion MYSQL est fermé")





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

for ligne in infos:
    print(ligne)
    




