import pygame as pg
from object import Object3D
from camera import *
from projection import *


class Render():
    def __init__(self) -> None:
        pg.init()
        self.resolution = self.width, self.height = 1600, 900
        self.halfWidth, self.halfHeight = self.width // 2, self.height // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.resolution)
        self.clock = pg.time.Clock()
        self.createObject()

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()
    
    def createObject(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotateY(math.pi / 6)

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f'fps: {str(int(self.clock.get_fps()))}')
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = Render()
    app.run()

