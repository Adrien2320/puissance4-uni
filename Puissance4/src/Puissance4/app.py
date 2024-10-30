
import platform
from pickle import FALSE

import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from views.configPlayerView import ConfigPlayerView
from controllers.controllerPlayer import ControllerPlayer
from views.headGameBoardView import HeadGameBoard
from views.gameBoardView import GameBoardView


class puissance4(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        """box principale ou tout va se passer"""
        self.mainBox = toga.Box(style=Pack(direction=COLUMN, background_color="#34495e",flex=1))

        """création des commandes pour les boutons"""
        self.cmdPlay = toga.Command(self.play, text="Jouer", icon=toga.Icon("pictures/play.png"),order=0)
        self.cmdEndGame = toga.Command(self.ExitGame, text="Fin de la partie", icon=toga.Icon("pictures/fin.png"),order=1)
        self.cmdPlayer1 = toga.Command(self.player1, text="Joueur 1", icon=toga.Icon("pictures/player.png"),order=2)
        self.cmdPlayer2 = toga.Command(self.player2, text="Joueur 2", icon=toga.Icon("pictures/player.png"),order=3)
        self.cmdSetting = toga.Command(self.settingApp, text="Options", icon=toga.Icon("pictures/setting.png"),order=4)


        self.main_window.toolbar.add(self.cmdPlay, self.cmdEndGame, self.cmdPlayer1, self.cmdPlayer2, self.cmdSetting)
        """création du bouton quitter, uniquement pour windows"""
        if platform.system() == 'Windows':
            cmdQuit = toga.Command(self.closeApp, text="Quitter", icon=toga.Icon("pictures/close.png"),order=5)
            self.main_window.toolbar.add(cmdQuit)

        self.main_window.content = self.mainBox
        self.commands.clear()
        self.main_window.show()

    def player1(self, widget):
        self.mainBox.add(ConfigPlayerView(playerNumber=1, mainBox=self.mainBox, mainWindow=self.main_window,api=self))
        self.modifEnabledAllCmd(cmdPlay=False,cmdEndGame=False,cmdPlayer1=False,cmdPlayer2=False,cmdSetting=False)

    def player2(self, widget):
        self.mainBox.add(ConfigPlayerView(playerNumber=2, mainBox=self.mainBox, mainWindow=self.main_window,api=self))
        self.modifEnabledAllCmd(cmdPlay=False,cmdEndGame=False,cmdPlayer1=False,cmdPlayer2=False,cmdSetting=False)


    def settingApp(self, widget):
        print("Options")

    def play(self, widget):
        result = ControllerPlayer().giveAllDataPlayer(1)
        result2 = ControllerPlayer().giveAllDataPlayer(2)
        result = result[0]
        result = result[1]
        result2 = result2[0]
        result2 = result2[1]
        if not result and not result2:
            self.main_window.info_dialog("Attention", "Veuillez modifier le joueur 1 et le joueur 2, avant de lancé une partie")
        else:
            self.modifEnabledAllCmd(cmdPlay=False, cmdEndGame=True, cmdPlayer1=False, cmdPlayer2=False,cmdSetting=False)
            self.mainBox.add(HeadGameBoard(),GameBoardView())


    def closeApp(self, widget):
        self.main_window.close()

    def modifEnabledAllCmd(self, cmdPlay:bool,cmdEndGame:bool,cmdPlayer1:bool,cmdPlayer2:bool,cmdSetting:bool):
        self.cmdPlay.enabled= cmdPlay
        self.cmdEndGame.enabled= cmdEndGame
        self.cmdPlayer1.enabled= cmdPlayer1
        self.cmdPlayer2.enabled= cmdPlayer2
        self.cmdSetting.enabled= cmdSetting

    def ExitGame(self, widget):
        pass


def main():
    return puissance4()

