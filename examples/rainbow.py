import colorwall
reload(colorwall)
import random
from colorsys import hsv_to_rgb as cv

class Wall(colorwall.ColorWall):
    def __init__(self, *args, **kwargs):
        colorwall.ColorWall.__init__(self, *args, **kwargs)
        self.pad = 0
        self.rainbow()
    
    def rainbow(self, pad=0):
        pad = pad % self.size.w
        colors = self.gencolors(self.size.w)
        for row in self.tiles:
            for index, tile in enumerate(row):
                ind = (index + pad) % self.size.w
                tile.color = colors[ind]
    
    def gencolors(self, size):
        step = 1./size
        colors = [cv(step * i, 1, 1) for i in range(size + 1)]
        return colors
    
    def update(self):
        self.rainbow(self.pad)
        self.pad += 1

wall = Wall((128, 8), (4, 64))
colorwall.animate(wall, frame_interval=1)
