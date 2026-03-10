import pyxel
from core import settings
from entities.player import Player


class Game:
    def __init__(self):
        pyxel.init(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, title=settings.TITLE)
        pyxel.load("assets/sprites.pyxres")  # apenas essa linha
        self.player = Player()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
