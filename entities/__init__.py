

import os
import yaml


class Entity:
    def __init__(self, kind, game, pos):
        self.game = game
        self.pos = pos
        kind = open(os.path.join(os.getcwd(), 'entities', kind))
        self.stats = yaml.load(kind)

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
