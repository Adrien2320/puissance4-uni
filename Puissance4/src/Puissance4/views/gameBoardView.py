import toga
from toga.style import Pack
from toga.style.pack import COLUMN,ROW,CENTER,RIGHT,LEFT
from controllers.controllerPlayer import ControllerPlayer

class GameBoardView(toga.Box):
    def __init__(self):
        super().__init__(style=(Pack(direction=COLUMN, background_color="#34495e", padding=30, alignment=CENTER,flex=1)))
        self.columns = 7
        self.rows = 6
        self.grid = []

        button_row = toga.Box(style=Pack(direction=ROW, alignment=CENTER, background_color="#424949"))
        footerButtonRow = toga.Box(style=Pack(direction=ROW,alignment=CENTER, background_color="#34495e",height=15))
        for col in range(self.columns):
            button = toga.Button(icon=toga.Icon("pictures/fleche.png"),style=Pack(flex=1, padding=5,background_color="#424949"))
            button_row.add(button)
        self.add(button_row,footerButtonRow)

        for row in range(self.rows):
            line = toga.Box(style=Pack(direction=ROW, background_color="#424949", flex=1))
            for col in range(self.columns):
                cell = toga.Box(
                    style=Pack(flex=1, background_color='#616a6b', padding=5))
                line.add(cell)
                self.grid.append(cell)
            self.add(line)