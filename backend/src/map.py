import json
import random

class Hex:
    def __init__(self, q, r) -> None:
        self._q = q
        self._r = r
        self._ships = []
        self._planets = []
        
    def to_json(self) -> str:
        return json.dumps({
            'q': self._q,
            'r': self._r,
            'ships': [json.loads(ship.to_json()) for ship in self._ships],
            'planets': [json.loads(planet.to_json()) for planet in self._planets]
        })
        
    def add_ship(self, ship) -> None:
        self._ships.append(ship)
    
    def remove_ship(self, ship) -> None:
        self._ships.remove(ship)
    
    def add_planet(self, planet) -> None:
        self._planets.append(planet)
        
    def remove_planet(self, planet) -> None:
        self._planets.remove(planet)
        

class Map:
    def __init__(self, q: int , r: int, number_of_players: int) -> None:
        self._hexes: list[list[Hex]] = []
        for i in range(q):
            self._hexes.append([])
            for j in range(r):
                self._hexes[i].append(Hex(i, j))
        
        self._number_of_players = number_of_players
              
    def get_random_starting_positions(self) -> list[tuple[int, int]]:
        positions = []
        while len(positions) < self._number_of_players:
            q = random.randint(0, len(self._hexes) - 1)
            r = random.randint(0, len(self._hexes[0]) - 1)
            pos = (q, r)
            if pos not in positions:
                positions.append(pos)
        return positions

    def get_hex(self, q: int, r: int) -> Hex:
        return self._hexes[q][r]
    
    def get_map(self) -> list[Hex]:
        hexes = []
        for i in range(len(self._hexes)):
            for j in range(len(self._hexes[i])):
                hexes.append(self._hexes[i][j].to_json())
        return hexes
                
        
    def get_hexes_in_range(self, q: int, r: int, range: int) -> list[Hex]:
        pass
    
    def get_hexes_in_view(self, hexes: list[Hex]) -> list[Hex]:
        pass
