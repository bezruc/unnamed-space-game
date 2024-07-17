from unnamed_game.src.entities.entity import Entity
from unnamed_game.src.utilities.logger import logger

class Star(Entity):
    def __init__(self, x_coordinate: float, y_coordinate: float, owner=None) -> None:
        super().__init__(x_coordinate, y_coordinate, owner)
        logger.info("Star %s created at %.2f, %.2f.",  self._id, self._coordinates[0], self._coordinates[1])
        # TODO eco/inf levels?
        # TODO rare resouces as list? (weak link?)
        # TODO Politics (best if its a separate class party.py and just hold references)
