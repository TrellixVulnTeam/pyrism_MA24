import sys, os, sdl2, sdl2.ext
from OpenGL import GL

from pyrism.window import Window
from pyrism.shader import Shader

here = os.path.dirname(__file__)

def run():
    width, height = 640, 480
    window = Window(width, height, "demo")
    shader = Shader(os.path.join(here, '..\\shaders\\standard'), 'standard')
    GL.glClearColor(0.0, 0.0, 0.0, 1.0)
    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        window.refresh()

    del shader
    del window
    return 0


if __name__ == "__main__":
    sys.exit(run())
