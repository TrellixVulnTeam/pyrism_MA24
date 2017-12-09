import numpy as np
from OpenGL.GL import *


class frameBufferObject(object):
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.frameBuffers = glGenFramebuffers(1)

    def bind(self):
        pass
