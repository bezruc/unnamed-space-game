class Group:
    def __init__(self, name) -> None:
        self._name = name
        self._players = None # player reference?
        self._resources = None # as acumulated resources per round