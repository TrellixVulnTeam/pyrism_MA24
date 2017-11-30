import math
from PIL import Image
from maths.vector import Vec2


class ImageRGB(object):
    def __init__(self, size):
        self.size = size
        self.texelSize = Vec2(1.0/self.size.x, 1.0/self.size.y)
        self.image = Image.new('RGB', (size.x, size.y), 0)
        self.pixels = self.image.load()

    def getPixel(self, uv):
        uv = uv%Vec2(1.0, 1.0)

        pixelPos = Vec2(int(uv.x / self.texelSize.x), int(uv.y / self.texelSize.y))
        return self.pixels[pixelPos.x, pixelPos.y]

    def show(self):
        self.image.show()


img = ImageRGB(Vec2(800, 600))

# Image population loop
for x in range(img.size.x):
    for y in range(img.size.y):
        uv = Vec2(x*img.texelSize.x, y*img.texelSize.y)
        offset = Vec2(0, math.sin(uv.x * uv.y *100000000000
                                  ) * 0.5)
        uv0 = uv + offset
        if (0.3 < uv0.x < 0.5) and (0.4<uv0.y-0.5 <0.5):
            img.pixels[x, y] = (0,0,0)
        else:
            cr = int(uv0.y * 255)
            cb = int(uv0.x * 255)
            cg = int(((uv0.x + uv0.y)/2)*255)
            col = (cr, cg, cb)
            img.pixels[x, y] = col

img.show()
