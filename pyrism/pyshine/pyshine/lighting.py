RAY_T_MAX = 1.0e30
RAY_T_MIN = 0.1


class Ray(object):
    def __init__(self, tMax=RAY_T_MAX, tMin=RAY_T_MIN, *args):
        if len(args)==2:
            self.origin = args[0]
            self.direction = args[1].normalize()
        elif len(args)==1 and type(args[0])==Ray:
            ray = args[0]
            self.origin = ray.origin
            self.direction = ray.direction.normalize()
        self.tMax = tMax
        self.tMin = tMin

    def __eq__(self, other):
        self.origin = other.origin
        self.direction = other.direction

    def calculate(self, t):
        return (self.origin+self.direction)*t


class Light(object):
    def __init__(self, position):
        self.position = position