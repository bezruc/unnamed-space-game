from unnamed_game.fleets import Fleets
from unnamed_game.galaxy import Galaxy


class Player:
    def __init__(self, galaxy: Galaxy, fleets: Fleets) -> None:

        self._finances = 0
        self._planets = []
        self._fleets = []
