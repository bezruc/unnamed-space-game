class Player:
    def __init__(self) -> None:
        self._turn_ended = False

    def end_turn(self):
        self._turn_ended = True

    def __dict__(self):
        return {
            "turn_ended": self._turn_ended
        }
