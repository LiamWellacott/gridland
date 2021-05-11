import argparse
import json
import jsonmerge

from gridland.world.display import Display
from gridland.world.loader import load

def main():
    # parser definition
    parser = argparse.ArgumentParser(description='Welcome to Gridland!')

    parser.add_argument('--ui-off', dest='ui_off', action='store_true', default=False)
    parser.add_argument('rest', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    # interpret args
    params = None
    for f in args.rest: # Load one to many files containing the scenario description 
        with open(f, 'r') as infile:
            j = json.loads(infile.read())
            params = jsonmerge.merge(params, j)

    # initialise system
    world = load(params)
    ui = Display()

    # main loop
    while True:
        world.update()
        if not args.ui_off:
            ui.draw(world)
    
if __name__ == "__main__":
    main()