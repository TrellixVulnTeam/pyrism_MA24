import numpy as np
from OpenGL.GL import *
from tempfile import template


class Model(object):
    def __init__(self, file):
        self.positions = np.ndarray
        self.texCoords = np.ndarray
        self.normals = np.ndarray

        self.indices = np.ndarray

        if file.endswith('.obj'):
            print('trying to open', file)
            try:
                self.load_obj(self, file)
            except IOError as ex:
                print('IOError: failed to open obj file')
                message = template.format(type(ex).__name__, ex.args)
                print(message)
                exit(-1)
            self.drawCount = self.indices.size

        print(self.texCoords)

        self._vertexArrayObject = glGenVertexArrays(1)
        glBindVertexArray(self._vertexArrayObject)

        self._vertexArrayBuffers = glGenBuffers(3)

        glBindBuffer(GL_ARRAY_BUFFER, self._vertexArrayBuffers[0])
        glBufferData(GL_ARRAY_BUFFER, self.positions.nbytes, self.positions, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ARRAY_BUFFER, self._vertexArrayBuffers[1])
        glBufferData(GL_ARRAY_BUFFER, self.texCoords.nbytes, self.texCoords, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self._vertexArrayBuffers[2])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glBindVertexArray(0)

    def __del__(self):
        glDeleteBuffers(3, self._vertexArrayBuffers)
        glDeleteVertexArrays(self._vertexArrayObject, 1)

    def draw(self):
        glBindVertexArray(self._vertexArrayObject)
        glDrawElementsBaseVertex(GL_TRIANGLES, self.drawCount, GL_UNSIGNED_INT, ctypes.c_void_p(0), 0)
        glBindVertexArray(0)

    @classmethod
    def load_obj(cls, model, file):
        positions = []
        texCoords = []
        normals = []

        position_index = []
        texture_index = []
        normal_index = []

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
                    for v in values[0:3]:
                        w = v.split('/')
                        position_index.append(int(w[0])-1)
                        texture_index.append(int(w[1])-1)
                        normal_index.append(int(w[2])-1)

            newTexCoords = np.ndarray((len(texCoords), 2), dtype=np.float32)
            for i in range(len(texture_index)):
                newTexCoords[position_index[i]] = texCoords[texture_index[i]]
            texCoords = newTexCoords

            model.positions = np.array(positions, dtype=np.float32)
            model.texCoords = np.array(texCoords, dtype=np.float32)
            model.normals = np.array(normals, dtype=np.float32)

            model.indices = np.array(position_index, dtype=np.uint)
