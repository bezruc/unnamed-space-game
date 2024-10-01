import json
from itertools import count

class Entity:
    _ids = count(0)
    
    def __init__(self, q, r, owner) -> None:
        self._id = next(self._ids)
        self._q = q
        self._r = r
        self._owner = owner

    def to_json(self) -> str:
        return json.dumps({
            'q': self._q,
            'r': self._r,
            'owner': self._owner.get_id()
        })
        
    def get_position(self) -> tuple[int, int]:
        return (self._q, self._r)
        
    def update_owner(self, owner) -> None:
        self._owner = owner
        
    def simulate(self) -> None:
        pass


class Ship(Entity):
    def __init__(self, q, r, owner, range, hp, power) -> None:
        super().__init__(q, r, owner)
        self._hp = hp
        self._range = range
        self._power = power
        self._target = None
        
    def to_json(self) -> str:
        data = json.loads(super().to_json())
        data['hp'] = self._hp
        data['range'] = self._range
        data['power'] = self._power
        data['target'] = None
        return json.dumps(data)
        
    def set_target(self, q: int, r: int) -> None:
        self._target = (q, r)

    
class Planet(Entity):
    def __init__(self, q, r, owner, production) -> None:
        super().__init__(q, r, owner)
        self._production = production
        
    def to_json(self) -> str:
        data = json.loads(super().to_json())
        data['production'] = self._production
        return json.dumps(data)