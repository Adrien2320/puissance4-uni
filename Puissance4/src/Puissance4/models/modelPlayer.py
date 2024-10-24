from config import Config
import sqlite3
from dataclasses import dataclass,field
from contextlib import closing

@dataclass
class Player:
    id_player: int
    name_player: str
    color_player: str

class DataPlayer:
    def __init__(self):
        self.database = sqlite3.connect(Config().givePathDb())

    @property
    def cursor(self):
        """créer le paramètre"""
        return self.database.cursor()

    def commit(self):
        """sauvegarde les modifications appliqué à la table"""
        self.database.commit()

    def setDataPlayer(self,id_player,name_player,color_player):
        sql = """ INSERT INTO T_Player (id_player,name_player,color_player) VALUES (?,?,?)"""

        with closing(self.cursor) as cursor:
            cursor.execute(sql,
                           [id_player,name_player,color_player],
                           )
            self.commit()

    def clearDataPlayer(self):
        """supprime tout le contenu de la table T_Player"""
        sql = """DELETE FROM T_Player"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql)
            self.commit()