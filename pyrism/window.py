from sdl2.video import *
import sdl2


class Window(object):
    def __init__(self, width, height, title):
        self.width, self.height = width, height
        self.title = title

        if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
            print(sdl2.SDL_GetError())
            exit(-1)

        self.window = sdl2.SDL_CreateWindow(str.encode(self.title),
                                            sdl2.SDL_WINDOWPOS_CENTERED,
                                            sdl2.SDL_WINDOWPOS_CENTERED, self.width, self.height,
                                            sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
        if not self.window:
            print(sdl2.SDL_GetError())
            exit(-1)

        # Force OpenGL 4.3 'core' context. This is needed for compute shader support.
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 3)
        SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK,
                                  SDL_GL_CONTEXT_PROFILE_CORE)

        SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 8)
        SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 8)
        SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 8)
        SDL_GL_SetAttribute(SDL_GL_ALPHA_SIZE, 8)
        SDL_GL_SetAttribute(SDL_GL_BUFFER_SIZE, 32)
        SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)
        SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
        self._context = sdl2.SDL_GL_CreateContext(self.window)

    def __del__(self):
        sdl2.SDL_GL_DeleteContext(self._context)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()

    def refresh(self):
        sdl2.SDL_GL_SwapWindow(self.window)
