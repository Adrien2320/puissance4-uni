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
        """ajout d'un écran de chargement pour la création de la base de données"""""
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE T_Player (
                            id_Player INTEGER PRIMARY KEY AUTOINCREMENT,
                            name_player TEXT NOT NULL,
                            color_player TEXT NOT NULL
                            )""")
        cursor.execute("""INSERT INTO T_Player (id_Player, name_player, color_player) VALUES (1, 'Joueur1', 'red')""")
        cursor.execute("""INSERT INTO T_Player (id_Player, name_player, color_player) VALUES (2, 'joueur2', 'yellow')""")
        db.commit()
        db.close()
    else:
        print("reset db player")
        db = sqlite3.connect(db_path)
        cursor = db.cursor()
        cursor.execute("""UPDATE T_Player SET name_player = '', color_player = '' WHERE id_player = 1""")
        cursor.execute("""UPDATE T_Player SET name_player = '', color_player = '' WHERE id_player = 2""")
        db.commit()
        db.close()



if __name__ == "__main__":
    checkIfDataExist()
    main().main_loop()
