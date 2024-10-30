import toga
from toga.style import Pack
from toga.style.pack import COLUMN,ROW,CENTER,RIGHT,LEFT
from controllers.controllerPlayer import ControllerPlayer

class HeadGameBoard(toga.Box):
    def __init__(self):
        super().__init__(style=(Pack(direction=ROW, background_color="#34495e", padding=5, alignment=CENTER)))
        """récupèration des données des joueurs"""
        """joueur1"""
        result = ControllerPlayer().giveAllDataPlayer(1)
        result = result[0]
        namePlayer1 = result[1]
        colorPlayer1 = result[2]

        """joueur2"""
        result = ControllerPlayer().giveAllDataPlayer(2)
        result = result[0]
        namePlayer2 = result[1]
        colorPlayer2 = result[2]

        """box pour afficher les données du joueur 1 """
        labelInfoColorPlayer1 = toga.Label(text="",style=Pack(padding=3,width=30,height=30,background_color=colorPlayer1, alignment=CENTER,flex=1))
        labelNamePlayer1 = toga.Label(text=namePlayer1,style=(Pack(padding=3,font_size=15,text_align=CENTER,font_weight="bold", alignment=CENTER,flex=1,background_color='#b2babb')))
        self.labelScorePlayer1 = toga.Label(text="0",style=(Pack(padding=3,font_size=15,text_align=CENTER,font_weight="bold", alignment=CENTER,flex=1,width=50,background_color='#b2babb')))
        boxPlayer1 = toga.Box(style=(Pack(direction=ROW,background_color="#34495e",alignment=CENTER,padding=10,flex=1)))
        boxLeftPlayer1 = toga.Box(style=(Pack(direction=ROW,background_color="#abb2b9",alignment=LEFT,padding=10,flex=1)))
        boxRightPlayer1 = toga.Box(style=(Pack(direction=ROW, background_color="#34495e", alignment=RIGHT, padding=10, flex=1)))
        boxPlayer1.add(boxLeftPlayer1,labelInfoColorPlayer1,labelNamePlayer1,self.labelScorePlayer1,boxRightPlayer1)

        """box pour afficher les données du joueur 2 """
        labelInfoColorPlayer2 = toga.Label(text="",style=Pack(padding=3, width=30, height=30, background_color=colorPlayer2,alignment=CENTER, flex=1))
        labelNamePlayer2 = toga.Label(text=namePlayer2, style=(Pack(padding=3, font_size=15, text_align=CENTER, font_weight="bold", alignment=CENTER, flex=1,background_color='#b2babb')))
        self.labelScorePlayer2 = toga.Label(text="0", style=(Pack(padding=3, font_size=15, text_align=CENTER, font_weight="bold", alignment=CENTER, flex=1, width=50,background_color='#b2babb')))
        boxPlayer2 = toga.Box(style=(Pack(direction=ROW, background_color="#34495e", alignment=CENTER, padding=10, flex=1)))
        boxLeftPlayer2 = toga.Box(style=(Pack(direction=ROW, background_color="#abb2b9", alignment=LEFT, padding=10, flex=1)))
        boxRightPlayer2 = toga.Box(style=(Pack(direction=ROW, background_color="#34495e", alignment=RIGHT, padding=10, flex=1)))
        boxPlayer2.add(boxLeftPlayer2, labelInfoColorPlayer2,labelNamePlayer2,self.labelScorePlayer2, boxRightPlayer2)

        """ajout de toutes les box sur la box qui est la classe elle même"""
        self.add(boxPlayer1,boxPlayer2)

