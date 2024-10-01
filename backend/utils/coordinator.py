from itertools import count

from backend.utils.instance import Instance


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