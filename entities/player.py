import pyxel


class Player:
    def __init__(self, x=70, y=50):
        self.x = x
        self.y = y

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)
