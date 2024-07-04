from player import Player
from unnamed_game.galaxy import Galaxy


class instance:
    def __init__(self, num_of_players: int) -> None:
        self._players = []
        self._galaxy = Galaxy()

        self._players.append(Player())
