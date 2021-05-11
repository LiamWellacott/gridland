import pytest

from gridland.world.entity import Colour, Box

def test_Box():

    world_hw = 10 # world size
    box_size = 2
    b = Box([0, 0, 0], world_hw, Colour.RED, box_size)

    for row in range(world_hw):
        for colomn in range(world_hw):
            if row < box_size and colomn < box_size:
                assert b.world_pose[row][colomn] == 1
            else:
                assert b.world_pose[row][colomn] == 0

