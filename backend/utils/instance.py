from backend.src.map import Map
from backend.src.players import Player


class Instance:
    def __init__(self, q, r, number_of_players) -> None:
        self._number_of_players = number_of_players
        self._map = Map(q, r, number_of_players)
        self._starting_positions = self._map.get_random_starting_positions()
        self._players = [Player(i) for i in range(number_of_players)]
        self._turn_counter = 0
        
        self._set_starting_positions()
        
    def _set_starting_positions(self) -> None:
        starting_positions = self._map.get_random_starting_positions()
        for player in self._players:
            hex = self._map.get_hex(*starting_positions.pop())
            player.add_planet(hex)
            player.add_ship(hex)
        
    def get_map(self) -> list[dict]:
        return self._map.get_map()
    
    def get_player(self, id: int) -> Player:
        return self._players[id]
    
    def get_turn_counter(self) -> int:
        return self._turn_counter
    
    def player_end_turn(self, id) -> None:
        self._players[id].end_turn()
        for player in self._players:
            if not player.ended_turn:
                return
            else:
                self.advance_turn()
    
    def advance_turn(self) -> None:
        self._turn_counter += 1
        for player in self._players:
            player.advance_turn()