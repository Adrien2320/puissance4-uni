import toga
from toga.style import Pack
from toga.style.pack import COLUMN,ROW,CENTER
from controllers.controllerPlayer import ControllerPlayer

class ConfigPlayerView(toga.Box):
    def __init__(self,playerNumber:int,mainBox,mainWindow,api):
        super().__init__(style=(Pack(direction=COLUMN,background_color="#34495e",padding=5,alignment=CENTER)))
        self.mainBox = mainBox
        self.playerNumber = playerNumber
        self.mainWindow = mainWindow
        self.api = api

        """box pour enregistré nom du joueur"""
        nameBox = toga.Box(style=(Pack(direction=ROW,background_color="#abb2b9",alignment=CENTER,padding=10)))
        labelName = toga.Label(text=f"NOM DU JOUEUR {playerNumber}",style=(Pack(padding=3,font_size=15,text_align=CENTER,font_weight="bold")))
        self.inputName = toga.TextInput(style=(Pack(flex=1,width=225,text_align=CENTER,padding=3,font_size=12)))
        nameBox.add(labelName,self.inputName)

        """box pour choisir la couleur du joueur"""
        colorBox = toga.Box(style=Pack(direction=ROW, background_color="#abb2b9", alignment=CENTER, padding=10))
        labelColor = toga.Label(text=f"COULEUR DU JOUEUR {playerNumber}", style=Pack(padding=3, font_size=15, text_align=CENTER, font_weight="bold"))
        self.colorSelection = self.createListColor(self.playerNumber)
        self.colorSelection.on_select = self.changeColor
        self.labelInfoColor = toga.Label(text="",style=Pack(padding=3,width=30,height=30,background_color="gray"))
        colorBox.add(labelColor,self.labelInfoColor,self.colorSelection)

        """box pour le bouton annulé et enregistré"""
        actionBox = toga.Box(style=Pack(direction=ROW, background_color="#abb2b9", alignment=CENTER, padding=10))
        buttonCancel = toga.Button(text="ANNULER",on_press=self.cancel,style=(Pack(padding=5,font_size=15,width=180,background_color="#c0392b")))
        buttonRegister = toga.Button(text="ENREGISTRER", on_press=self.register,style=(Pack(padding=5, font_size=15,width=180, background_color="#27ae60")))
        actionBox.add(buttonCancel,buttonRegister)

        self.add(nameBox,colorBox,actionBox)

    def cancel(self,widget):
        self.api.modifEnabledCmdPlayer(True)
        self.mainBox.clear()

    def register(self,widget):
        color_map = {
            "ROUGE": "red",
            "VERT": "green",
            "BLEU": "blue",
            "JAUNE": "yellow",
            "ORANGE": "orange",
            "ROSE": "pink"
        }
        selected_color = self.colorSelection.value
        if selected_color in color_map:
            colorPlayer = color_map[selected_color]
        ControllerPlayer().modifConfigPlayer(namePlayer=self.inputName.value,colorPlayer=colorPlayer,playerNumber=self.playerNumber)
        self.mainWindow.info_dialog("Succès", f"Les données ont été bien enregistrées, le joueur {self.playerNumber} a comme nom: {self.inputName.value} et comme couleur: {selected_color}")
        self.api.modifEnabledCmdPlayer(True)
        self.mainBox.clear()


    def changeColor(self, widget):
        color_map = {
            "ROUGE": "red",
            "VERT": "green",
            "BLEU": "blue",
            "JAUNE": "yellow",
            "ORANGE": "orange",
            "ROSE": "pink"
        }
        selected_color = widget.value
        if selected_color in color_map:
           self.labelInfoColor.style.background_color = color_map[selected_color]

    def createListColor(self,playerNumber:int):
        if playerNumber == 1:
            result = ControllerPlayer().giveAllDataPlayer(2)
        else:
            result = ControllerPlayer().giveAllDataPlayer(1)
        result = result[0]
        colorOtherPlayer = result[2]

        match colorOtherPlayer:
            case "red":
                colorOptions = ["VERT", "BLEU", "JAUNE", "ORANGE", "ROSE"]
            case "green":
                colorOptions = ["ROUGE", "BLEU", "JAUNE", "ORANGE", "ROSE"]
            case "blue":
                colorOptions = ["ROUGE", "VERT", "JAUNE", "ORANGE", "ROSE"]
            case "yellow":
                colorOptions = ["ROUGE", "VERT", "BLEU", "ORANGE", "ROSE"]
            case "orange":
                colorOptions = ["ROUGE", "VERT", "BLEU", "JAUNE", "ROSE"]
            case "pink":
                colorOptions = ["ROUGE", "VERT", "BLEU", "JAUNE", "ORANGE"]
            case _:
                colorOptions = ["ROUGE", "VERT", "BLEU", "JAUNE", "ORANGE", "ROSE"]
        listColor = toga.Selection(items=colorOptions, value=colorOptions[0],
                                       style=Pack(flex=1, padding=3, width=150, font_size=15, text_align=CENTER))
        return listColor
