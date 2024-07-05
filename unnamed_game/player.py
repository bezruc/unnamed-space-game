from unnamed_game.galaxy import Stars, Fleets


class Player:
    def __init__(self, id: int, galaxy: Stars, fleets: Fleets) -> None:

        self._id = id
        self._finances = 0
        self._planets = []
        self._fleets = []
        self._passed = False

    def has_passed(self):
        return self._passed
