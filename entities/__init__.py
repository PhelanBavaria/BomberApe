

import os
import yaml
from items import Item


class Entity:
    def __init__(self, id, game, pos, item=None):
        self.id = id
        self.game = game
        self.pos = pos
        id = open(os.path.join(os.getcwd(), 'entities', id))
        self.stats = yaml.load(id)
        if not item:
            self.item = Item('bomb', game)

    def _move(self, x=0, y=0):
        self.pos[0] += x
        self.pos[1] += y

    def move_left(self):
        self._move(x=1)

    def move_right(self):
        self._move(x=-1)

    def move_up(self):
        self._move(y=-1)

    def move_down(self):
        self._move(y=1)

    def use(self):
        self.item.use(self)
