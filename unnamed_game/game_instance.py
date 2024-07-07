from unnamed_game.src.player import Player
from unnamed_game.src.galaxy import Galaxy

class Instance:
    def __init__(self, num_of_players: int) -> None:
        self._players = []
        self._galaxy = None

        for i in range(num_of_players):
            self._players.append(Player)

        self._galaxy = Galaxy(self._players)


instance = None

def init():
    instance = Instance(4)
