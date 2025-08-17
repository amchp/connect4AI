from enum import Enum

class ScreensEnum(Enum):
    Menu = 0
    Game = 1
    Victory = 2

class Player(Enum):
    Player1 = 1
    Empty = 0
    Player2 = -1
