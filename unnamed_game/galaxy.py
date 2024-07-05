class Galaxy:
    def __init__(self) -> None:
        self._entities = []
    
    def simulate(self):
        for entity in self._entities:
            entity.simulate()
