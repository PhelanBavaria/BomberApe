

import random
from entities import Entity


class Game:
    def create_match(self):
        self.width = random.randint(25, 50)
        self.height = random.randint(25, 50)
        self.tiles = {}
        for y in range(height):
            for x in range(width):
                tiles[(x, y)] = 'grass'
        test_entity = Entity('test_ape')


if __name__ == '__main__':
    random.seed(555)
    game = Game()
    game.create_match()
