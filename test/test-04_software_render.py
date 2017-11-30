from maths.vector import *
from camera import Camera

from shape import ShapeSet, Sphere

shapeSet = ShapeSet()
sphere1 = Sphere(Vec3(0.0, 0.0, 5.0), 1.0)
sphere2 = Sphere(Vec3(2.0, 0.0, 7.0), 2.0)

shapeSet.addShapes(sphere1, sphere2)

camera = Camera(Vec3(0.0), Vec3(0.0, 0.0, 1.0), 75)
camera.render(800, 600, shapeSet, mode='software')
