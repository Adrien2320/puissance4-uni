from models.modelPlayer import DataPlayer

class ControllerPlayer:

    def modifConfigPlayer(self,namePlayer:str,colorPlayer:str, playerNumber:int):
        DataPlayer().modifDataPlayer(id_player=playerNumber,name_player=namePlayer,color_player=colorPlayer)

    def giveAllDataPlayer(self,playerNumber:int):
        result = DataPlayer().giveAllDataPlayer(id_player=playerNumber)
        return result