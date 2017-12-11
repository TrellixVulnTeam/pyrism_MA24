from OpenGL.GL import *
from OpenGL.GL import shaders


class Shader(object):
    # FIXME: create proper constructor for every shader type.
    def __init__(self, file, name):
        self._program = None
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
        glUseProgram(self._program)

    def bindFragDataLocation(self, texture, name):
        glBindFragDataLocation(self._program, texture, name)

    def addUniform(self, name):
        self._uniforms.append(glGetUniformLocation(self._program, name))

    def updateUniform1i(self, i, v0):
        glUniform1i(self._uniforms[i], v0)

    def updateUniform2fv(self, i, v):
        glUniform2fv(self._uniforms[i], 1, v)

    def updateUniform2f(self, i, v0, v1):
        glUniform2f(self._uniforms[i], v0, v1)

    def getUniformLocation(self, name):
        return glGetUniformLocation(self._program, name)

    # Shader types dictionary, specifies name of various shader presets and things :)
    @classmethod
    def shaders(cls, name):
        return {
            'surface': 1,
            'compute': 2,
            'image': 3
        }.get(name, 1)
