import sys, os, sdl2, sdl2.ext
from OpenGL.GL import *

import numpy as np

from pyrism.shader import Shader
from pyrism.texture import Texture, RenderTexture
from pyrism.window import Window
from pyrism.model import Model

here = os.path.dirname(__file__)


def run():
    width, height = 800, 600
    window = Window(width, height, "filters")

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    model = Model(os.path.join(here, '..\\..\\quad.obj'))

    texture = None
    effshader = None

    shader = Shader('shaders\\default', 'surface')

    with open(os.path.join(here, 'config.txt')) as f:
        lines = f.readlines()
        found_shader = False
        found_texture = False
        for line in lines:
            if line.startswith('#'): continue
            values = line.split()
            if not values or len(values) is not 2: continue

            elif values[0] == 'sh' and not found_shader:
                effshader = Shader(os.path.join(here, str('shaders\\')+values[1]), 'surface')
                found_shader = True
            elif values[0] == 'in' and not found_texture:
                texture = Texture(os.path.join(here, values[1]))
                found_texture = True

    renderTexture = RenderTexture(texture.getWidth(), texture.getHeight())
    texelSize = np.array([1.0/texture.getWidth(), 1.0/texture.getHeight()], dtype=np.float32)

    effshader.addUniform("ColorTexture")
    effshader.addUniform("DepthTexture")
    effshader.addUniform("texelSize")
    effshader.bindFragDataLocation(0, "color")

    running = True
    while running:
        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        renderTexture.bind()
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glViewport(0,0,texture.getWidth(), texture.getHeight())
        shader.bind()
        texture.bind()
        model.draw()
        texture.unbind()
        renderTexture.unbind()

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glViewport(0,0,width,height)
        effshader.bind()
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, renderTexture.getTexture('color'))
        effshader.updateUniform1i(0, 0)
        effshader.updateUniform2fv(2, texelSize)

        model.draw()
        window.refresh()

    del texture
    del effshader
    del shader
    del renderTexture
    del model
    del window

    return 0


if __name__ == "__main__":
    sys.exit(run())
