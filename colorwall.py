import scene

class Tile(object):
    def __init__(self, wall, pos, size, color):
        pos = scene.Point(*pos)
        size = scene.Size(*size)
        self.wall = wall
        self.bounds = scene.Rect(pos.x, pos.y, *size)
        self.color = color
    
    def draw(self):
        x, y, sx, sy = self.bounds
        x += self.wall.bounds.x
        y += self.wall.bounds.y
        scene.fill(*self.color)
        scene.rect(x, y, sx, sy)

class ColorWall(object):
    def __init__(self, size=(8, 8), tsize=(64, 64)):
        self.tiles = self.gentiles(size, tsize, (0, 0, 0))
        self.size  = scene.Size(*size)
        self.bounds = self.calcbounds()
    
    def calcbounds(self):
        tile = self.tiles[0][0]
        sx = tile.bounds.w * self.size.w
        sy = tile.bounds.h * self.size.h
        return scene.Rect(0, 0, sx, sy)
    
    def gentiles(self, (sx, sy), (tsx, tsy), color):
        tiles = []
        for x in range(sx):
            row = []
            for y in range(sy):
                tile = Tile(self,
                            (x * tsx, y * tsy),
                            (tsx, tsy),
                            color)
                row.append(tile)
            tiles.append(row)
        return tiles
    
    def update(self):
        pass
    
    def move(self, addx, addy):
        self.bounds.x = addx
        self.bounds.y = addy

class Scene(scene.Scene):
    def should_rotate(self, orientation):
        return True 
    
    def do_setup(self, wall):
        self.wall = wall
        
    def draw(self):
        scene.background(0.9, 0.9, 0.9)
        sx, sy = self.size
        mx = 0.5 * (sx - self.wall.bounds.w)
        my = 0.5 * (sy - self.wall.bounds.h)
        self.wall.move(mx, my)
        self.draw_tiles(self.wall.tiles)
        self.wall.update()
    
    def draw_tiles(self, tiles):
        for row in tiles:
            for tile in row:
                tile.draw()

def animate(wall, *args, **kwargs):
    anim = Scene()
    anim.do_setup(wall)
    scene.run(anim, *args, **kwargs)
