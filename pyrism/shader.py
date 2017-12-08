from OpenGL.GL import *
from OpenGL.GL import shaders

import OpenGL.error


# Shader types dictionary, specifies name of various shader presets and things :)
def shader_t(i):
    return {
        'surface': 1,
        'compute': 2
    }.get(i, 1)


class Shader(object):
    def __init__(self, file, t_idx):

        self.program = glCreateProgram()

        self.shaders = []
        if shader_t(t_idx) == 1:
            with open(file + '.vert') as content_vert, open(file + '.frag') as context_frag:
                self.shaders.append(shaders.compileShader(content_vert.read(), GL_VERTEX_SHADER))
                self.shaders.append(shaders.compileShader(context_frag.read(), GL_FRAGMENT_SHADER))
        if shader_t(t_idx) == 2:
            with open(file + '.comp') as content_comp:
                self.shaders.append(shaders.compileShader(content_comp.read(), GL_COMPUTE_SHADER))

        try:
            for shader in self.shaders:
                glAttachShader(self.program, shader)
            glBindAttribLocation(self.program, 0, "position")
            glLinkProgram(self.program)
        except OpenGL.error.NullFunctionError as error:
            pass

    def bind(self):
        glUseProgram(0)
        glUseProgram(self.program)

    def __del__(self):
        try:
            for shader in self.shaders:
                glDetachShader(self.program, shader)
                glDeleteShader(shader)
            glDeleteProgram(self.program)
        except OpenGL.error.NullFunctionError as error:
            pass
