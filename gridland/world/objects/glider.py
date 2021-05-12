from gridland.world.entity import Entity

import numpy as np

class Glider(Entity):

    def __init__(self, params, world_hw):
        super().__init__(params, world_hw)

        # glider will only move in the period specified by delay
        self.delay = 0
        self.delay_timer = 0
        if 'delay' in params:
            self.delay = params['delay']

        # glider wont be updated once it reaches the edge of the world
        self.is_dead = False

        origin_x = self.origin[0]
        origin_y = self.origin[1]

        # glider moves from top left to bottom right in a predictable motion
        # initial pattern 
        #
        #   010
        #   001
        #   111
        self.checkAndAdd(self.origin[0] + 1, self.origin[1])
        self.checkAndAdd(self.origin[0] + 2, self.origin[1] + 1)
        for i in range(3):
            self.checkAndAdd(self.origin[0] + i, self.origin[1] + 2)

     
    def checkAndAdd(self, x, y):
        if self._inWorld(x, y):
            self.world_pose[y][x] = 1 # flipped because array indexing...

    def updateThisTick(self):
        if self.delay_timer == self.delay:
            self.delay_timer = 0
            return True
        else:
             self.delay_timer += 1
             return False

    def update(self):

        # if a delay has been added then check if we should update this tick
        if not self.updateThisTick():
            return

        # if the end of the world has been reached, stop updating
        if self.is_dead:
            return

        # remove if reached the edge of the world
        for i in range(self.world_hw):
            if self.world_pose[i][self.world_hw-1] == 1 or self.world_pose[self.world_hw-1][i] == 1:
                self.world_pose = np.zeros((self.world_hw, self.world_hw))
                self.is_dead = True
        
        # game of life rules
        # calculate which neighbours to check (shortcut due to single object of interest)
        check_neighbours = []
        for row in range(self.world_hw):
            for column in range(self.world_hw):
                if self.world_pose[row][column] == 1:

                    # add this point and its neighbours to be checked 
                    for i in range(3):
                        for j in range(3):

                            # only add in world points (this may lead to weirdness at the edge)
                            x = row+i-1
                            y = column+j-1
                            if self._inWorld(x, y):
                                check_neighbours.append((x, y)) 

        # only check each point once
        check_neighbours = set(check_neighbours)

        # count the number of alive
        neighbour_counts = []
        for x, y in check_neighbours:

            count = 0
            
            for i in range(3):
                for j in range(3):

                    if i == 1 and j == 1:
                        # its me
                        continue

                    # get neighbours coordinates
                    neighbour_x = x + i - 1
                    neighbour_y = y + j - 1

                    # is this in the grid
                    if self._inWorld(neighbour_x, neighbour_y):

                        # is the cell alive, if so count
                        if self.world_pose[neighbour_x][neighbour_y] == 1:
                            count += 1
                
            neighbour_counts.append(count)

        # apply rules
        for i, (x, y) in enumerate(check_neighbours):

            count = neighbour_counts[i]

            if self.world_pose[x][y] == 1: # alive

                if count < 2: #exposure
                    self.world_pose[x][y] = 0
                elif count > 3: #overpopulation
                    self.world_pose[x][y] = 0
            else:

                if count == 3: # come alive
                    self.world_pose[x][y] = 1

        return