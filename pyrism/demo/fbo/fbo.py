import sys, os, sdl2, sdl2.ext
from OpenGL.GL import *

from pyrism.window import Window
from pyrism.shader import Shader
from pyrism.model import Model
from pyrism.texture import Texture, RenderTexture

here = os.path.dirname(__file__)


def run():
    width, height = 800, 600
    window = Window(width, height, "fbo")

    model = Model(os.path.join(here, '..\\..\\quad.obj'))
    shader = Shader(os.path.join(here, '..\\..\\shaders\\default'), 'surface')
    texture = Texture(os.path.join(here, 'pink.jpg'))
    renderTexture = RenderTexture(window.width, window.height)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        shader.bind()
        texture.bind()
        model.draw()
        window.refresh()

    del texture
    del renderTexture
    del shader
    del model
    del window

    return 0


if __name__ == "__main__":
    sys.exit(run())