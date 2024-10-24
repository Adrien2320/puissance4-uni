import os

class Config:
    def __init__(self):
        # Obtenir le chemin du dossier contenant le script actuel
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Chemin global de la base de données
        self.db_path = os.path.join(current_directory, "dataGame.db")

    def givePathDb(self):
        return self.db_path
