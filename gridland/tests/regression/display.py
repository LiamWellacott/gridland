# manual test to check the display is working correctly (inspection)
from gridland.world.display import Display

import numpy as np

def manyBox(): # test colour gradient on distance
    world_size = 10
    objects = [ Box([i, i, i], world_size, Colour.RED, 2) for i in range(world_size) ]
    d = Display()

    while True:
        d.draw(objects, world_size)

def oneBox(): # test object spawn
    world_size = 10
    b = Box([0, 0, 0], world_size, Colour.RED, 2)
    d = Display()

    while True:
        d.draw([b], world_size)

def basic():
    # for testing the display only
    # Test grid
    cellMAP = np.random.randint(2, size=(10, 10))
    d = Display()
    while True:
        d.draw(cellMAP)

if __name__ == '__main__':
    # change this to change test case
    basic()