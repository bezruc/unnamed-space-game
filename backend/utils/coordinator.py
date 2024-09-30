from itertools import count

from backend.src.map import Map
from backend.src.players import Player


class Instance:
    def __init__(self, q, r, number_of_players) -> None:
        self._number_of_players = number_of_players
        self._map = Map(q, r, number_of_players)
        self._starting_positions = self._map.get_random_starting_positions()
        self._players = [Player(i) for i in range(number_of_players)]
        self._set_starting_positions()
        
    def _set_starting_positions(self) -> None:
        starting_positions = self._map.get_random_starting_positions()
        for player in self._players:
            hex = self._map.get_hex(*starting_positions.pop())
            player.add_planet(hex)
            player.add_ship(hex)
        
    def get_map(self) -> list[dict]:
        return self._map.get_map()


class Coordinator:
    _ids = count(0)
    
    def __init__(self) -> None:
        self._instances: dict[int, Instance] = {}
    
    def start_instance(self, number_of_players: int) -> int:
        id = next(self._ids)
        self._instances[id] = Instance(10, 10, number_of_players)
        return id
        
    def get_instance(self, id: int) -> Instance:
        return self._instances[id]