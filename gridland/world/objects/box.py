from gridland.world.entity import Entity

class Box(Entity):

    def __init__(self, params, world_hw):
        super().__init__(params, world_hw)

        size = params['size']

        origin_x = self.origin[0]
        origin_y = self.origin[1]

        # a square of size starting at origin 
        for row in range(size):
            for column in range(size):
                x = origin_x + row
                y = origin_y + column
                if self._inWorld(x, y):
                    self.world_pose[x][y] = 1
     
    def update(self):
        # static object
        return