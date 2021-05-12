import numpy as np
import colorsys
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
- Objects have a colour which is passed as a Hue value 0..1, s = 1 and v is determined based on the depth of the object (closer objects are brighter) 
- Objects have a depth part of the world origin, this will be used to determine what is visible, and the value (HSV) of the colour (constrained to range 0.5..1 to display better) 

'''

    def __init__(self, params, world_hw):

        self.origin = params['position']
        colour = params['colour']
        
        # occupancy grid for the world size, must be filled by specific object
        self.world_pose = np.zeros((world_hw, world_hw) )
        self.world_hw = world_hw

        # convert colour to RGB   
        v = 1.0 - ((self.getDepth() / world_hw))# between 1.0 and 0.5 depending on depth, closer things are brighter
        r, g, b = colorsys.hsv_to_rgb(colour, 1.0, v)
        r = self._rebaseColour(r)
        g = self._rebaseColour(g)
        b = self._rebaseColour(b)

        self.colour = (r, g, b)

    def getDepth(self):
        return self.origin[2]

    def update(self):
        NotImplementedError()

    # check if object position falls inside the range of the cube world
    def _inWorld(self, x, y):
        return x >= 0 and x < self.world_hw and y >= 0 and y < self.world_hw

    # bring colour from 0..1 range into int range 0..255 
    def _rebaseColour(self, c):
        return int(c * 255)

