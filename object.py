import pygame as pg
from matrix_functions import *
import numpy as np


class Object3D():
    def __init__(self, render) -> None:
        self.render = render
    
        self.vertices = np.array([(0,0,0,1), (0,1,0,1), (1,1,0,1), (1,0,0,1),
                                  (0,0,1,1), (0,1,1,1), (1,1,1,1), (1,0,1,1)])
        
        self.faces = np.array([(0,1,2,3), (4,5,6,7), (0,4,5,1), (2,3,7,6), (1,2,6,5), (0,3,7,4)])

    def draw(self):
        self.screenProjection()

    def screenProjection(self):
        vertices = self.vertices @ self.render.camera.cameraMatrix()
        vertices = vertices @ self.render.projection.projectionMatrix
        vertices /= vertices[:,-1].reshape(-1,1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ self.render.projection.toScreenMatrix
        vertices = vertices[:, :2]

        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.render.halfWidth) | (polygon == self.render.halfHeight)):
                pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, 3)

        for vertex in vertices:
            if not np.any((vertex == self.render.halfWidth) | (vertex == self.render.halfHeight)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)

    
    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)
    
    def scale(self, scaleTo):
        self.vertices = self.vertices @ scale(scaleTo)

    def rotateX(self, angle):
        self.vertices = self.vertices @ rotateX(angle)
    
    def rotateY(self, angle):
        self.vertices = self.vertices @ rotateY(angle)
    
    def rotateZ(self, angle):
        self.vertices = self.vertices @ rotateZ(angle)
    