import numpy as np
from enum import Enum

### Colours (Hue from HSV scaled to 0..1)
class Colour(Enum):
    RED = 0.0
    YELLOW = 60.0/360.0
    GREEN = 120.0/360.0
    CYAN = 180.0/360.0
    BLUE = 240.0/360.0
    PURPLE = 300/360.0

class Entity(object):
    '''
Not object to conflict with use of the term in programming, but entitiy is an object for all intents and purposes.

- Objects have some initial postion, the subclass object will decide how it will display based on this origin 
- Objects may move, in which case they must be translated in the update function, objects must implement the update function even if they just return (no movement)
- For simplicity of upstream logic each object maintains its position in the world grid and is responsible for updating it's occupancy map if it comes into or out of view
- Objects have a colour which is a Hue value 0..1 
- Objects have a depth part of the world origin, this will be used to determine what is visible, and the value (HSV) of the colour (constrained to range 0.5..1 to display better) 

'''

    def __init__(self, world_origin, world_hw, colour):

        # occupancy grid for the world size, must be filled by specific object
        self.world_pose = np.zeros((world_hw, world_hw) )
        self.origin = world_origin
        self.world_hw = world_hw
        self.colour = colour

    def update(self):
        NotImplementedError()

    def _inWorld(self, x, y):
        return x >= 0 and x < self.world_hw and y >= 0 and y < self.world_hw

class Box(Entity):

    def __init__(self, world_origin, world_hw, colour, size):
        super().__init__(world_origin, world_hw, colour)

        # TODO update depending on how I send this info
        origin_x = self.origin[0]
        origin_y = self.origin[1]

        # a square of size starting at origin 
        for row in range(size):
            for colomn in range(size):
                x = origin_x + row
                y = origin_y + colomn
                if self._inWorld(x, y):
                    self.world_pose[x][y] = 1
                
    def update(self):
        # static object
        return

def main():
    # for testing
    print(Box([5, 5], 10, Colour.RED, 2).world_pose)

if __name__ == "__main__":
    main()
