import os
import sqlite3
from Puissance4.app import main


def checkIfDataExist():
    """create dataBase if not exist"""
    # Obtenir le chemin du dossier contenant le script actuel
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Chemin complet de la base de données
    db_path = os.path.join(current_directory, "dataGame.db")

    if not os.path.exists(db_path):
        print("no existing database")
        """ajout d'un écran de chargement pour la création de la base de données"""""
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE T_Player (
                            id_Player INTEGER PRIMARY KEY AUTOINCREMENT,
                            name_player TEXT NOT NULL,
                            color_player TEXT NOT NULL
                            )""")
        db.commit()
        db.close()


if __name__ == "__main__":
    checkIfDataExist()
    main().main_loop()
