import colorwall
reload(colorwall)
import random

class Wall(colorwall.ColorWall):
    def update(self):
        for row in self.tiles:
            for tile in row:
                color = random.choice([(1, 1, 1), (0, 0, 0)])
                tile.color = color

wall = Wall()
colorwall.animate(wall, frame_interval=60)
