import logging
import itertools


# Defines basic entity object
class Entity():
    _id_iter = itertools.count()

    def __init__(self, x_coordinate: float, y_coordinate: float, owner=None) -> None:
        self._coordinates = (x_coordinate, y_coordinate)
        self._owner = None
        self._id = next(Entity._id_iter)
        logging.info("Entity %s created at %.2f, %.2f.",  self._id, self._coordinates[0], self._coordinates[1])

    def get_owner(self):
        return self._owner
    
    def set_owner(self, owner):
        return self._owner
    
    def get_id(self):
        return self._id
    
    def get_coordinates(self):
        return self._coordinates

    def simulate(self) -> None:
        return
