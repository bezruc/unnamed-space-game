from player import Player


def dummy_generate():
    pass


class Instance:
    def __init__(self, num_of_players: int) -> None:
        self._players = []
        self._galaxy, self._fleets = dummy_generate()

        for i in range(num_of_players):
            self._players.append(Player(i, self._galaxy, self._fleets))

        # at the end schedule lib -> schedule.every(24).do(self.advance_time)

    def advance_time(self):
        for fleet in self._fleets():
            fleet.simulate()
