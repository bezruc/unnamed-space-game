from backend.src.map import Hex
from backend.src.entities import Ship
from backend.src.entities import Planet

class Player:
    def __init__(self, id) -> None:
        self._id = id
        self._ships = []
        self._planets = []
        self._ended_turn = False   
    
    def end_turn(self) -> None:
        self._ended_turn = True
    
    def add_ship(self, hex: Hex) -> None:
        ship = Ship(hex._q, hex._r, self, 1, 1, 1)	
        hex.add_ship(ship)
        
    def add_planet(self, hex: Hex) -> None:
        planet = Planet(hex._q, hex._r, self, 1)
        hex.add_planet(planet)
        
    def get_id(self) -> int:
        return self._id
    
    def advance_turn(self) -> None:
        self._ended_turn = False
        
    def ended_turn(self) -> bool:
        return self._ended_turn
