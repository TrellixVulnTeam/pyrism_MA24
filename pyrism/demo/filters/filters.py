import sys, os, sdl2, sdl2.ext
from OpenGL.GL import *

from pyrism.shader import Shader
from pyrism.texture import Texture, RenderTexture
from pyrism.window import Window
from pyrism.model import Model

here = os.path.dirname(__file__)


def run():
    width, height = 640, 480
    window = Window(width, height, "filters")

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    model = Model(os.path.join(here, '..\\..\\quad.obj'))
    renderTexture = RenderTexture(window.width, window.height)

    textures = []
    effshader = None

    shader = Shader('shaders\\default', 'surface')

    with open(os.path.join(here, 'config.txt')) as f:
        lines = f.readlines()
        found_shader = False
        for line in lines:
            if line.startswith('#'): continue
            values = line.split()
            if not values or len(values) is not 2: continue

            elif values[0] == 'sh' and not found_shader:
                effshader = Shader(os.path.join(here, str('shaders\\')+values[1]), 'surface')
                found_shader = True
            elif values[0] == 'in':
                textures.append(Texture(os.path.join(here, values[1])))

    effshader.addUniform("ColorTexture")
    effshader.addUniform("DepthTexture")

    if effshader and textures:
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        for texture in textures:
            renderTexture.bind()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            shader.bind()
            texture.bind()
            model.draw()
            texture.unbind()

            renderTexture.unbind()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            effshader.bind()
            glActiveTexture(GL_TEXTURE0 + 1)
            glBindTexture(GL_TEXTURE_2D, renderTexture.getTexture('color'))
            effshader.updateUniform1i(0, 1)


            glActiveTexture(GL_TEXTURE0 + 2)
            glBindTexture(GL_TEXTURE_2D, renderTexture.getTexture('depth'))
            effshader.updateUniform1i(1, 2)

            model.draw()
            window.refresh()

        sdl2.SDL_Delay(10000)
        del textures
        del effshader
        del shader
        del renderTexture
        del model
        del window

    return 0


if __name__ == "__main__":
    sys.exit(run())
