from unnamed_game.src.player import Player
from unnamed_game.src.galaxy import Galaxy


class Instance:    
    
    def __init__(self, num_of_players: int) -> None:
        self._players = []
        self._galaxy = None

        for i in range(num_of_players):
            self._players.append(Player)

        self._galaxy = Galaxy(self._players)
    
    def _advance_time(self):
        self._galaxy.advance_time()

    def end_turn(self, player):
        if player > len(self._players):
            raise ValueError
        
        self._players[player].end_turn()

        for player in self._players:
            if not player.end_turn():
                return
        
        self._advance_time()
    
    def get_state(self, player):
        return {
            f"player{1}".format(player): self._players[player].__dict__(),
            "galaxy": self._galaxy.__dict__()
        }
