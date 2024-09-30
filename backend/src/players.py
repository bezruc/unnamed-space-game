from backend.src.map import Hex
from backend.src.entities import Ship
from backend.src.entities import Planet

class Player:
    def __init__(self, id) -> None:
        self._id = id
        self._ships = []
        self._planets = []   
    
    def end_turn(self) -> None:
        pass
    
    def add_ship(self, hex: Hex) -> None:
        ship = Ship(hex._q, hex._r, self, 1, 1, 1)	
        hex.add_ship(ship)
        
    def add_planet(self, hex: Hex) -> None:
        planet = Planet(hex._q, hex._r, self, 1)
        hex.add_planet(planet)
        
    def get_id(self) -> int:
        return self._id