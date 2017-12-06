from OpenGL.GL import *
from OpenGL.GL import shaders


def shader_t(i):
    return {
        'standard': 1,
        'compute': 2
    }.get(i, 1)


class Shader(object):
    def __init__(self, fileName, t_idx):
        if shader_t(t_idx) == 1:
            with open(fileName + '.vert', 'r') as content_vert, open(fileName + '.frag', 'r') as context_frag:
                vert = shaders.compileShader(content_vert.read(), GL_VERTEX_SHADER)
                frag = shaders.compileShader(context_frag.read(), GL_FRAGMENT_SHADER)

            self.program = shaders.compileProgram(vert, frag)
        if shader_t(t_idx) == 2:
            with open(fileName + '.comp', 'r') as content_comp:
                comp = shaders.compileShader(content_comp.read(), GL_COMPUTE_SHADER)
            self.program = shaders.compileProgram(comp)

    def bind(self):
        glUseProgram(0)
        glUseProgram(self.program)

    def __del__(self):
        glDeleteProgram(self.program)
