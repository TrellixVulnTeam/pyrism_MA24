import numpy as np


class ObjModel(object):
    def __init__(self):
        self.positions, self.texCoords, self.normals, self.indices = [], [], [], []


def load_obj(file):
    model = ObjModel()
    positions = []
    texCoords = []
    normals = []
    indices = []
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

    model.positions = np.array(positions, dtype=np.float32)
    model.texCoords = np.array(texCoords, dtype=np.float32)
    model.normals = np.array(normals, dtype=np.float32)
    model.indices = np.array(np.array(indices), dtype=np.uint)
    return model


class Model(object):
    def __init__(self, file):
        if file.endswith('.obj'):
            model = load_obj(file)
            print(model.texCoords)