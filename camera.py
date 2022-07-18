import pygame as pg
from matrix_functions import *

class Camera():
    def __init__(self, render, position) -> None:
        position.append(1.0)
        self.position = np.array([*position])
        self.forward = np.array([0,0,1,1])
        self.up = np.array([0,1,0,1])
        self.right = np.array([1,0,0,1])
        self.hFOV = math.pi / 3
        self.vFOV = self.hFOV * (render.halfHeight / render.halfWidth)
        self.nearPlane = 0.1
        self.farPlane = 100

    def translateMatrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotateMatrix(self):
        rx, ry, rz, w  = self.right
        fx, fy, fz, w  = self.forward
        ux, uy, uz, w  = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
    
    def cameraMatrix(self):
        return self.translateMatrix() @ self.rotateMatrix()
