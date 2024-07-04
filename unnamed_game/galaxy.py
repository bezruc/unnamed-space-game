from unnamed_game.entities.planet import Planet


class Galaxy:
    def __init__(self, num_of_players: int, generation_settings={}) -> None:
        self._planets = []
        # (player: int, list(Planets))
        self._starting_planets = {}

        # placeholder
        for player in num_of_players:
            self._planets.append(Planet(1, 1, 1))

    def get_planet(self, id):
        return self._planets[0]

    def get_starting_planets(self):
        return self._starting_planets
