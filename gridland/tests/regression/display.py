# manual test to check the display is working correctly (inspection)
from gridland.world.display import Display
from gridland.world.loader import load
from gridland.world.entity import Colour

import numpy as np

def manyBox(): # test colour gradient on distance
    world_size = 10
    objects = []
    for i in range(world_size):
        objects.append({
            'box' : {
                'position' : [i, i, i],
                'colour' : Colour.RED.value,
                'size' : 2
            }
        })
    params = {
        'world_size' : 10,
        'objects' : objects
    }
    run(params)

def oneBox(): # test object spawn
    world_size = 10
    objects = []
    objects.append({
        'box' : {
            'position' : [0, 0, 0],
            'colour' : Colour.RED.value,
            'size' : 2
        }
    })
    params = {
        'world_size' : 10,
        'objects' : objects
    }
    run(params)

def run(params):
    d = Display()
    w = load(params)

    while True:
        
        d.draw(w)

if __name__ == '__main__':
    # change this to change test case
    #oneBox()
    manyBox()