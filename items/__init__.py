

import os
import yaml


class Item:
    def __init__(self, id, game):
        self.actions = {
            'place_bomb': self._place_bomb
        }
        self.id = id
        self.game = game
        id = open(os.path.join(os.getcwd(), 'items', id))
        self.stats = yaml.load(id)

    def use(self, entity):
        self.actions[self.stats['on_use']](entity)

    def _place_bomb(self, entity):
        print('DEBUG: Placed bomb')
