import math
from PIL import Image

from shape import Transform, Intersection
from rendering import Ray
from maths.vector import *


class Camera(Transform):
    def __init__(self, transform, forward, fov):
        Transform.__init__(self, transform)
        self.forward = (forward-self.position).normalize()
        self.fov = fov

        self.right = cross(self.forward, Vec3(0.0, 1.0, 0.0)).normalize()
        self.up = cross(self.right, self.forward).normalize()

    # start of renderer functions TODO: create renderer class
    def __render_software(self, width, height, shapeSet):

        img = Image.new('RGB', (width, height))
        pixels = img.load()

        fovRadians = math.pi*((self.fov/2)/180)
        heightWidthRatio = height / width
        halfWidth = math.tan(fovRadians)
        halfHeight = heightWidthRatio * halfWidth
        cameraWidth = halfWidth * 2
        cameraHeight = halfHeight * 2
        pixelWidth = cameraWidth / (width - 1)
        pixelHeight = cameraHeight / (height - 1)

        ray = Ray(self.position, self.forward)

        for y in range(0, height):
            for x in range(0, width):
                xcomp = self.right * ((x * pixelWidth) - halfWidth)
                ycomp = self.up * ((y * pixelHeight) - halfHeight)
                ray.direction = (self.forward + xcomp + ycomp).normalized()
                intersection = Intersection(ray)

                col = (0,0,0)
                if shapeSet.intersect(intersection):
                    oldRange = 25 - ray.tMin
                    newRange = 255 - 0
                    c = int(((intersection.t-ray.tMin)*newRange)/oldRange)
                    col = (c, c, c)
                pixels[x, y] = col
        img.show()

    # this function right now draws the scene to a picture and shows it immediately
    # TODO: create proper renderer setup
    def render(self, *args, **kwargs):
        width=args[0]
        height=args[1]
        shapeSet=args[2]

        mode = kwargs.get('mode')
        if mode == 'software':
            self.__render_software(width, height, shapeSet)
        return
