

import os
import yaml


class Entity:
    def __init__(self, id, game, pos, item=None):
        self.alive = True
        self.id = id
        self.game = game
        self.pos = pos
        id = open(os.path.join(os.getcwd(), 'entities', id))
        self.stats = yaml.load(id)
        self.item = item
        self.appendages = []
        self.on_death = {
            'detonate': self._detonate
        }

    def _move(self, x=0, y=0):
        self.pos[0] += x
        self.pos[1] += y

    def _detonate(self):
        print('DEBUG: Detonated')

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
            max_uses = min(self.stats['max_uses'],
                           self.item.stats['max_uses'])
            if max_uses > len(self.appendages):
                self.item.use(self)

    def die(self):
        for appendage in self.appendages:
            appendage.die()
        self.alive = False
        if self.stats['on_death']:
            self.on_death[self.stats['on_death']]()
