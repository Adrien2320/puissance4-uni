from models.modelPlayer import DataPlayer

class ControllerPlayer:

    def setConfigPlayer(self,namePlayer:str,colorPlayer:str, playerNumber:int):
        print(namePlayer,colorPlayer,playerNumber)
        DataPlayer().setDataPlayer(id_player=playerNumber,name_player=namePlayer,color_player=colorPlayer)

    def clearConfigPlayer(self):
        DataPlayer().clearDataPlayer()

    def checkIfPlayerExist(self,playerNumber:int):
        result = DataPlayer().chekIfPlayerExist(id_player=playerNumber)
        return result

    def giveAllDataPlayer(self,playerNumber:int):
        result = DataPlayer().giveAllDataPlayer(id_player=playerNumber)
        return result