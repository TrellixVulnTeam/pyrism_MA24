from xml.etree import ElementTree


# TODO: properly log and error handle the file loading procedure.
class Scene(object):
    def __init__(self, file):
        data = ElementTree.parse(file)
        cameras = data.findall('objects/cameras/camera')
        shapes = data.findall('objects/shapes/shape')
        lights = data.findall('objects/lights/light')
        for camera in cameras:
            print(camera.find('name').text)
        for shape in shapes:
            print(shape.find('name').text)
        for light in lights:
            print(light.find('name').text)
