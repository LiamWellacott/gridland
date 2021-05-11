# gridland

Toy environment for testing object understanding inspired by the [Abstraction and Reasoning Corpus (ARC)](https://github.com/fchollet/ARC). a 3D cube shaped grid world contains objects which may move around. An agent will be tasked with tracking/predicting the location of a given object.

## Project structure

- agent: everything to do with sensing and tracking the objects.
- world: display, object spawning/moving logic.
- scenarios: configurations of gridland to test different aspects of the agents understanding.
- tests: testing for the project.

## Notes

- Objects are somewhat arbritrarily fixed to one depth level, would be fairly easy to make them fully 3d... will think about it. 
    - Constraining objects to one depth plain should make avoiding collisions easier.
    - also can precompute colours, may not be that significant...

## running tests

just tests:

```
python -m pytest gridland/tests/unit
```

tests with coverage 
```
coverage run -m pytest
# to view in nice format
covrage html
```