import math

from maths.vector import *
from rendering import Ray


class Transform(object):
    def __init__(self, position=Vec3(0, 0, 0), scale=Vec3(1, 1, 1), rotation=Vec3(0, 0, 0)):
        self.position = position
        self.scale = scale
        self.rotation = rotation

    def translate(self, translation):
        self.position += translation


class Intersection(object):
    def __init__(self, arg):
        if type(arg) == Ray:
            self.ray = arg
            self.t = self.ray.tMax
            self.shape = None
        elif type(arg) == Intersection:
            intersection = arg
            self.ray = intersection.ray
            self.t = intersection.t
            self.shape = intersection.shape

    def __eq__(self, other):
        self.ray = other.ray
        self.t = other.t
        self.shape = other.shape
    def intersected(self):
        return self.shape is not None
    def position(self):
        return self.ray.calculate(self.t)


# Template classes for every Shape
class Shape(object):
    def intersect(self, intersection):
        raise NotImplementedError()

    def doesIntersect(self, ray):
        raise NotImplementedError()

class ShapeSet(Shape):
    def __init__(self):
        self.shapes = []
    def addShapes(self, *args):
        for arg in args:
            self.shapes.append(arg)
    def intersect(self, intersection):
        doesIntersect = False
        for shape in self.shapes:
            if shape.intersect(intersection):
                doesIntersect = True
        return doesIntersect
    def doesIntersect(self, ray):
        for shape in self.shapes:
            if shape.doesIntersect(ray):
                return True
        return False


# TODO: reorganise shape classes in different files.
class Plane(Shape):
    def __init__(self, position, normal):
        self.position = position
        self.normal = normal

    def intersect(self, intersection):
        dDotN = dot(intersection.ray.direction, self.normal)
        if dDotN == 0:
            return False
        t = dot(self.position - intersection.ray.origin, self.normal)/dDotN
        if(t <= intersection.ray.tMax) or (t <= intersection.t):
            return False
        intersection.t = t
        intersection.shape = self
        return True

    def doesIntersect(self, ray):
        dDotN = dot(ray.direction, self.normal)
        if dDotN == 0:
            return False
        t = dot(self.position - ray.origin, self.normal) / dDotN
        if (t <= ray.tMin) or (t >= ray.tMax):
            return False
        return True


class Sphere(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def intersect(self, intersection):
        localRay = Ray(intersection.ray)
        localRay.origin -= self.center
        # Calculate the quadratic coefficients
        a = localRay.direction.len2()
        b = 2 * dot(localRay.direction, localRay.origin)
        c = localRay.origin.len2() - sqr(self.radius)
        # Check whether we intersect
        discriminant = math.pow(b,2)-(4*a*c)
        if discriminant < 0:
            return False
        # Find two points of intersection, t1 close and t2 far
        t1 = (-b - math.sqrt(discriminant)/(2*a))
        t2 = (-b + math.sqrt(discriminant)/(2*a))
        if intersection.ray.tMin < t1 < intersection.t:
            intersection.t = t1
        elif intersection.ray.tMin < t2 < intersection.t:
            intersection.t = t2
        else:
            return False
        intersection.shape = self
        return True

    def doesIntersect(self, ray):
        localRay = Ray(ray)
        localRay.origin -= self.center
        # Calculate the quadratic coefficients
        a = localRay.direction.len2()
        b = 2 * dot(localRay.direction, localRay.origin)
        c = localRay.origin.len2() - sqr(self.radius)
        # Check wether we intersect
        discriminant = math.pow(b, 2) - (4 * a * c)
        if discriminant < 0:
            return False
        # Find two points of intersection, t1 close and t2 far
        t1 = (-b - math.sqrt(discriminant) / (2 * a))
        if ray.tMin < t1 < ray.tMax:
            return True
        t2 = (-b + math.sqrt(discriminant) / (2 * a))
        if ray.tMin < t2 < ray.tMax:
            return True
        return False

    def normal(self, position):
        return (position-self.center).normalize()
