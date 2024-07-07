from unnamed_game.src.entities.entity import Entity
import math
import logging


class Fleet(Entity):
    def __init__(self, x_coordinate: float, y_coordinate: float, speed=10, owner=None) -> None:
        super().__init__(x_coordinate, y_coordinate, owner)
        self._speed = speed
        self._target = None

    def set_target(self, x_coordinate, y_coordinate):
        self._target = (x_coordinate, y_coordinate)
        return

    def simulate(self) -> None:
        """Simulates single tick behavior"""
        if self._speed == 0 or self._target is None:
            return

        # calculate change of position, you can probably do it simpler but
        # fuck it
        direction_vector_x = self._target[0] - self._coordinates[0]
        direction_vector_y = self._target[1] - self._coordinates[1]

        # Calculate the magnitude of the direction vector
        magnitude = math.sqrt(direction_vector_x**2 + direction_vector_y**2)

        if magnitude < self._speed:
            self._coordinates = self._target
            self._target = None
            return

        # Normalize the direction vector to get the unit direction vector
        unit_direction_vector_x = direction_vector_x / magnitude
        unit_direction_vector_y = direction_vector_y / magnitude

        # Calculate the change in position
        change_in_position_x = unit_direction_vector_x * self._speed
        change_in_position_y = unit_direction_vector_y * self._speed

        # Calculate the new position
        x_new = self._coordinates[0] + change_in_position_x
        y_new = self._coordinates[1] + change_in_position_y

        self._coordinates = (x_new, y_new)
        logging.info('Fleet %s at: %.2f, %.2f', self._id, self._coordinates[0], self._coordinates[1])
        return
