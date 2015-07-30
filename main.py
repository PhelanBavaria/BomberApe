

import random


class Game:
    def create_match(self):
        width = random.randint(25, 50)
        height = random.randint(25, 50)
        tiles = {}
        for y in range(height):
            for x in range(width):
                tiles[(x, y)] = 'grass'


if __name__ == '__main__':
    random.seed(555)
    game = Game()
    game.create_match()
