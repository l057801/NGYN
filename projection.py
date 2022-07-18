import numpy as np
import math
import numpy as np

class Projection():
    def __init__(self, render) -> None:
        NEAR = render.camera.nearPlane
        FAR = render.camera.farPlane
        RIGHT = math.tan(render.camera.hFOV / 2)
        LEFT = -RIGHT
        TOP = math.tan(render.camera.vFOV / 2)
        BOTTOM = -TOP

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP / BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projectionMatrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 0],
            [0, 0, m32, 0]
        ])
