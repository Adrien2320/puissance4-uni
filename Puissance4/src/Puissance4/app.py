import platform
import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class puissance4(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.mainBox = toga.Box(style=Pack(direction=COLUMN, background_color="#007ab7"))


        """création des commandes pour les boutons"""
        cmdPlayer1 = toga.Command(self.player1, text="Joueur 1", icon=toga.Icon("pictures/player.png"))
        cmdPlayer2 = toga.Command(self.player2, text="Joueur 2", icon=toga.Icon("pictures/player.png"))
        cmdSetting = toga.Command(self.settingApp, text="Options", icon=toga.Icon("pictures/setting.png"))
        cmdPlay = toga.Command(self.play, text="Jouer", icon=toga.Icon("pictures/play.png"))

        self.main_window.toolbar.add(cmdPlayer1, cmdPlayer2, cmdSetting, cmdPlay)
        """création du bouton quitter, uniquement pour windows"""
        if platform.system() == 'Windows':
            cmdQuit = toga.Command(self.closeApp, text="Quitter", icon=toga.Icon("pictures/close.png"))
            self.main_window.toolbar.add(cmdQuit)

        self.main_window.content = self.mainBox
        self.commands.clear()
        self.main_window.show()

    def player1(self, widget):
        print("Player 1")

    def player2(self, widget):
        print("Player 2")

    def settingApp(self, widget):
        print("Options")

    def play(self, widget):
        print("Play")

    def closeApp(self, widget):
        self.main_window.close()


def main():
    return puissance4()

