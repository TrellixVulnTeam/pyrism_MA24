import sys, os, sdl2, sdl2.ext
from OpenGL.GL import *

from pyrism.window import Window
from pyrism.shader import Shader
from pyrism.model import Model
from pyrism.texture import Texture

here = os.path.dirname(__file__)

def run():
    width, height = 640, 480
    window = Window(width, height, "demo")

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    model = Model(os.path.join(here, '..\\..\\quad.obj'))
    shader = Shader(os.path.join(here, 'shaders\\sobel'), 'surface')
    texture = Texture(os.path.join(here, 'pink.jpg'))
    texture.bind()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        shader.bind()
        model.draw()

        window.refresh()

    texture.unbind()
    del texture
    del shader
    del model
    del window

    return 0


if __name__ == "__main__":
    sys.exit(run())
