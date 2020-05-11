from secret import bdd_login, bdd_password
#PRE REQUIS
#Avoir installer my sql connector
#Pour faire ca, allez dans cmd et tapez "pip install mysql-connector-python"
#Et ensuite on l'importe dans la ligne d'en dessous
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
class DB:
    def __init__():
        pass
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

    def RequestSQL(requete):
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

