class Vector(object):

    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __eq__(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z
        return self


a = Vector(0, 0, 0)
b = Vector(1, 3, 5)

for i in range(0,10):
    a += b
    print("x: ", a.x, "y: ", a.y, "z: ", a.z, "\n")
