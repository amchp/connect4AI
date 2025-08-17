from pygame import display, init
from choices import ScreensEnum
from screens.menu import Menu 
from screens.game_screen import GameScreen
from screens.victory_screen import VictoryScreen
from constant import WINDOW_WIDTH, WINDOW_HEIGHT

init()
class ScreenControler:
    def __init__(self):
        self.size = self.width, self.height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.screen = display.set_mode(self.size)
        self.current_screen = GameScreen(self.width, self.height, self.screen)
        # Map to constructors so GameScreen receives window args on transitions
        self.screen_map = {
            ScreensEnum.Menu: lambda: Menu(),
            ScreensEnum.Game: lambda: GameScreen(self.width, self.height, self.screen),
            ScreensEnum.Victory: lambda: VictoryScreen(),
        }

    def controls(self) -> None:
        next_screen = self.current_screen.controls()
        if next_screen:
            self.current_screen = self.screen_map[next_screen]()

    def draw(self) -> None:
        self.current_screen.draw()

game = ScreenControler()

while True:
    game.controls()
    game.draw()
