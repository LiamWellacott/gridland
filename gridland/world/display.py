# adapted from https://betterprogramming.pub/making-grids-in-python-7cf62c95f413

import sys
import pygame
import colorsys
#from pygame.locals import KEYDOWN, K_q
import numpy as np

### CONSTANTS:
# Display
SCREENSIZE = WIDTH, HEIGHT = 1600, 600
GRID_WH = 400
LINE_WIDTH = 2

BORDER_X = 30
BORDER_Y = 100
WORLD_GRID_ORIGIN = (BORDER_X, BORDER_Y)
CANN_GRID_ORIGIN = (WORLD_GRID_ORIGIN[0] + GRID_WH + BORDER_X, BORDER_Y)

# Colours
BLACK = (0, 0, 0)
GREY = (160, 160, 160)

class Display:

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode(SCREENSIZE)

    def draw(self, world):
        # Background colour
        self.surface.fill(GREY)

        # World object grid
        self._drawSquareGrid(WORLD_GRID_ORIGIN, world.size)
        self._drawObjects(WORLD_GRID_ORIGIN, world.objects, world.size) # TODO will call this for each object, need to test replacement based on "depth" of the passed object

        # CANN visualisation
        self._drawSquareGrid(CANN_GRID_ORIGIN, world.size) 
        # TODO need an input for the CANN data

        pygame.display.update()

    def _drawObjects(self, grid_origin, objects, world_size):
        
        cellBorder = 0
        celldimX = celldimY = (GRID_WH / world_size) - (cellBorder*2)

        for row in range(world_size):
            for column in range(world_size):

                # find the foremost object in this cell
                is_occupied = False
                min_depth = world_size
                min_depth_obj_colour = None

                for obj in objects:
                    if obj.world_pose[row][column] == 1: # object occupies this space

                        if obj.getDepth() < min_depth: # if this is closer than previously found objects
                            
                            # there is at least one object
                            is_occupied = True

                            # set new min depth object
                            min_depth = obj.getDepth()
                            min_depth_obj_colour = obj.colour
          
                # Is the grid cell tiled ?
                if is_occupied: # TODO update

                    self._drawSquareCell(
                        grid_origin[0] + (celldimY*row)
                        + cellBorder + (2*row*cellBorder) + LINE_WIDTH/2,
                        grid_origin[1] + (celldimX*column)
                        + cellBorder + (2*column*cellBorder) + LINE_WIDTH/2,
                        celldimX, celldimY, min_depth_obj_colour)

    # Draw filled rectangle at coordinates
    def _drawSquareCell(self, x, y, dimX, dimY, colour):
        pygame.draw.rect(
        self.surface, colour,
        (x, y, dimX, dimY)
        )

    def _drawSquareGrid(self, origin, grid_width):

        cont_x, cont_y = origin

        # DRAW Grid Border:
        # TOP lEFT TO RIGHT
        pygame.draw.line(
        self.surface, BLACK,
        (cont_x, cont_y),
        (GRID_WH + cont_x, cont_y), LINE_WIDTH)
        # # BOTTOM lEFT TO RIGHT
        pygame.draw.line(
        self.surface, BLACK,
        (cont_x, GRID_WH + cont_y),
        (GRID_WH + cont_x,
        GRID_WH + cont_y), LINE_WIDTH)
        # # LEFT TOP TO BOTTOM
        pygame.draw.line(
        self.surface, BLACK,
        (cont_x, cont_y),
        (cont_x, cont_y + GRID_WH), LINE_WIDTH)
        # # RIGHT TOP TO BOTTOM
        pygame.draw.line(
        self.surface, BLACK,
        (GRID_WH + cont_x, cont_y),
        (GRID_WH + cont_x,
        GRID_WH + cont_y), LINE_WIDTH)

        # Get cell size, just one since its a square grid.
        cellSize = GRID_WH/grid_width

        # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
        for x in range(grid_width):
            pygame.draw.line(
            self.surface, BLACK,
            (cont_x + (cellSize * x), cont_y),
            (cont_x + (cellSize * x), GRID_WH + cont_y), 2)
        # # HORIZONTAl DIVISIONS
            pygame.draw.line(
            self.surface, BLACK,
            (cont_x, cont_y + (cellSize*x)),
            (cont_x + GRID_WH, cont_y + (cellSize*x)), 2)
