

import os
import yaml


class Tile:
    def __init__(self, id, game, pos):
        self.id = id
        self.game = game
        self.pos = pos
        id = open(os.path.join(os.getcwd(), 'entities', id))
        self.stats = yaml.load(id)
