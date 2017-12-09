from OpenGL.GL import *
from OpenGL.GL import shaders


class Shader(object):
    # FIXME: create proper constructor for every shader type.
    def __init__(self, file, name):
        self._program = glCreateProgram()
        self._uniforms = []
        self._shaders = []
        if self.shaders(name) == 1:
            with open(file + '.vert') as content_vert, open(file + '.frag') as context_frag:
                self._shaders.append(shaders.compileShader(content_vert.read(), GL_VERTEX_SHADER))
                self._shaders.append(shaders.compileShader(context_frag.read(), GL_FRAGMENT_SHADER))
        elif self.shaders(name) == 2:
            with open(file + '.comp') as content_comp:
                self._shaders.append(shaders.compileShader(content_comp.read(), GL_COMPUTE_SHADER))

        for shader in self._shaders:
            glAttachShader(self._program, shader)

        # if shader type is 'standard', bind pos and texCoord attribs. this is bare minimum for now.
        if self.shaders(name) == 1:
            glBindAttribLocation(self._program, 0, "position")
            glBindAttribLocation(self._program, 1, "texCoord")
        glLinkProgram(self._program)

    def __del__(self):
        for shader in self._shaders:
            glDetachShader(self._program, shader)
            glDeleteShader(shader)
        glDeleteProgram(self._program)

    def bind(self):
        glUseProgram(0)
        glUseProgram(self._program)

    def addUniform(self, name):
        self._uniforms.append(glGetUniformLocation(self._program, name))

    def updateUniform1i(self, id, v0):
        glUniform1i(self._uniforms[id], v0)

    # Shader types dictionary, specifies name of various shader presets and things :)
    @classmethod
    def shaders(cls, name):
        return {
            'surface': 1,
            'compute': 2,
            'image': 3
        }.get(name, 1)
