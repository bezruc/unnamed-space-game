from unnamed_game.entities.entity import Entity


class Planet(Entity):
    def __init__(self, x_coordinate, y_coordinate, resources) -> None:
        super().__init__(x_coordinate, y_coordinate)
        self._resources = resources
        self._owner = None
