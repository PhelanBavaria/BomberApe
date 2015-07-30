

import os
import yaml


class Entity:
    def __init__(self, id, game, pos, item=None):
        self.id = id
        self.game = game
        self.pos = pos
        id = open(os.path.join(os.getcwd(), 'entities', id))
        self.stats = yaml.load(id)
        self.item = item

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
        if self.item:
            self.item.use(self)
