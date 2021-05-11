from gridland.world.objects.box import Box

from gridland.world.entity import Colour

_OBJECTS = {
    "box" : Box
}

_COLOURS = {
    "RED" : Colour.RED.value,
    "YELLOW" : Colour.YELLOW.value,
    "GREEN" : Colour.GREEN.value,
    "CYAN" : Colour.CYAN.value,
    "BLUE" : Colour.BLUE.value,
    "PURPLE" : Colour.PURPLE.value
}

class World:

    def __init__(self, objects, size=10):
        self.size = size
        self.objects = objects

    def update(self):
        for obj in self.objects:
            obj.update()

def load(params):

    size = params['world_size']
    objects = []
    for obj in params['objects']:
        # key name in json is used to look up the type of object
        obj_id = list(obj.keys())[0] 

        # if text key used for colour, swap it for floating point value
        if obj[obj_id]['colour'] in _COLOURS:
            obj[obj_id]['colour'] = _COLOURS[obj[obj_id]['colour']]

        # create the object and add it to the list
        objects.append(_OBJECTS[obj_id](obj[obj_id], size))

    return World(objects, size)