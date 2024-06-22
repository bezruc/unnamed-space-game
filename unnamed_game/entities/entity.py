import math

# Defines basic entity object
class Entity():
    def __init__(self,  x_coordinate, y_coordinate, speed=0) -> None:
        self._target = None
        self._coordinates = (x_coordinate, y_coordinate)
        self._speed = speed

    def simulate(self) -> None:
        return
