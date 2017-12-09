from tempfile import template
import numpy as np
from PIL import Image
from OpenGL.GL import *


class Texture(object):
    def __init__(self, file):
        # PIL can open BMP, EPS, FIG, IM, JPEG, MSP, PCX, PNG, PPM
        # and other file types.  We convert into a texture using GL.
        print('trying to open', file)
        try:
            image = Image.open(file)
        except IOError as ex:
            print('IOError: failed to open texture file')
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            exit(-1)
        print('opened file: size=', image.size, 'format=', image.format)
        imageData = np.array(list(image.getdata()), np.uint8)
        self._width, self._height = image.size[0], image.size[1]

        self._texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
        glBindTexture(GL_TEXTURE_2D, self._texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self._width, self._height,
                     0, GL_RGB, GL_UNSIGNED_BYTE, imageData)
        glBindTexture(GL_TEXTURE_2D, 0)
        image.close()

    def __del__(self):
        glDeleteTextures(self._texture, 1)

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self._texture)

    @classmethod
    def unbind(cls):
        glBindTexture(GL_TEXTURE_2D, 0)


class RenderTexture(object):
    def __init__(self, width, height):
        self._width, self._height = width, height

        self._frameBuffer = glGenFramebuffers(1)
        glBindFramebuffer(GL_FRAMEBUFFER, self._frameBuffer)

        self._textures = glGenTextures(2)

        glBindTexture(GL_TEXTURE_2D, self._textures[0])
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self._width, self._height, 0, GL_RGB, GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glBindTexture(GL_TEXTURE_2D, self._textures[1])
        glTexImage2D(GL_TEXTURE_2D, 0, GL_DEPTH_COMPONENT24, self._width, self._height, 0, GL_DEPTH_COMPONENT, GL_FLOAT, ctypes.c_void_p(0))
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        self._depthRenderBuffer = glGenRenderbuffers(1)
        glBindRenderbuffer(GL_RENDERBUFFER, self._depthRenderBuffer)
        glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH_COMPONENT, self._width, self._height)
        glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_RENDERBUFFER, self._depthRenderBuffer)

        glFramebufferTexture(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, self._textures[0], 0)
        glFramebufferTexture(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, self._textures[1], 0)

        drawBuffers = np.array([GL_COLOR_ATTACHMENT0, GL_DEPTH_ATTACHMENT], dtype=np.int)
        glDrawBuffers(1, GL_COLOR_ATTACHMENT0)

        if glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE:
            exit(-1)

        glBindFramebuffer(GL_FRAMEBUFFER, 0)

    def __del__(self):
        glDeleteRenderbuffers(1, self._depthRenderBuffer)
        glDeleteTextures(2, self._textures)
        glDeleteFramebuffers(1, self._frameBuffer)

    def bind(self):
        glBindFramebuffer(GL_FRAMEBUFFER, self._frameBuffer)

    def unbind(self):
        glBindFramebuffer(GL_FRAMEBUFFER, 0)

    def getTexture(self, name):
        return self._textures[self.textures(name)]

    @classmethod
    def textures(cls, name):
        return {
            'color': 0,
            'depth': 1
        }.get(name, 1)
