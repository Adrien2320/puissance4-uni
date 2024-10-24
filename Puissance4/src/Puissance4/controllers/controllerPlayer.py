from models.modelPlayer import DataPlayer

class ControllerPlayer:

    def setConfigPlayer(self,namePlayer:str,colorPlayer:str, playerNumber:int):
        print(namePlayer,colorPlayer,playerNumber)
        DataPlayer().setDataPlayer(id_player=playerNumber,name_player=namePlayer,color_player=colorPlayer)

    def clearConfigPlayer(self):
        DataPlayer().clearDataPlayer()
