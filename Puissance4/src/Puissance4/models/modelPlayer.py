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

    def modifDataPlayer(self,id_player,name_player,color_player):
        sql = """ UPDATE T_Player SET name_player = ?, color_player = ? WHERE id_player = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql,
                           [name_player,color_player,id_player],
                           )
            self.commit()


    def giveAllDataPlayer(self,id_player):
        sql = """SELECT * FROM T_Player WHERE id_Player = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql,[id_player])
            result = cursor.fetchall()
            return result