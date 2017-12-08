import numpy as np
from OpenGL.GL import *


class Model(object):
    def __init__(self, file):
        self.positions = np.ndarray
        self.texCoords = np.ndarray
        self.normals = np.ndarray
        self.indices = np.ndarray
        if file.endswith('.obj'):
            self.load_obj(self, file)
            self.drawCount = self.indices.size

        self.vertexArrayObject = glGenVertexArrays(1)
        glBindVertexArray(self.vertexArrayObject)

        self.vertexArrayBuffers = glGenBuffers(3)

        glBindBuffer(GL_ARRAY_BUFFER, self.vertexArrayBuffers[0])
        glBufferData(GL_ARRAY_BUFFER, self.positions.nbytes, self.positions, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ARRAY_BUFFER, self.vertexArrayBuffers[1])
        glBufferData(GL_ARRAY_BUFFER, self.texCoords.nbytes, self.texCoords, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vertexArrayBuffers[2])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glBindVertexArray(0)

    def __del__(self):
        glDeleteBuffers(3, self.vertexArrayBuffers)
        glDeleteVertexArrays(self.vertexArrayObject, 1)

    def draw(self):
        glBindVertexArray(self.vertexArrayObject)
        glDrawElementsBaseVertex(GL_TRIANGLES, self.drawCount, GL_UNSIGNED_INT, ctypes.c_void_p(0), 0)
        glBindVertexArray(0)

    @classmethod
    def load_obj(cls, model, file):
        positions = []
        texCoords = []
        normals = []
        indices = []
        if file.endswith('.obj'):
            for line in open(file):
                if line.startswith('#'): continue
                values = line.split()
                if not values: continue
                # Check first string with each data type marker string
                fstr = values.pop(0)
                if fstr == 'v':
                    positions.append(values)
                if fstr == 'vt':
                    texCoords.append(values)
                if fstr == 'vn':
                    normals.append(values)

                if fstr == 'f':
                    face_i = []
                    tex_i = []
                    norm_i = []
                    for v in values[0:3]:
                        w = v.split('/')
                        indices.append(int(w[0])-1)
                        #face_i.append(int(w[0])-1)
                        #tex_i.append(int(w[1])-1)
                        #norm_i.append(int(w[2])-1)

            model.positions = np.array(positions, dtype=np.float32)
            model.texCoords = np.array(texCoords, dtype=np.float32)
            model.normals = np.array(normals, dtype=np.float32)
            model.indices = np.array(np.array(indices), dtype=np.uint)
