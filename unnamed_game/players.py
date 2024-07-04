class Player:
    def __init__(self) -> None:
        self.finances = 0
        self.planets = []
        self.fleets = []

    def get_info(self) -> dict:
        return self.__dict__


class Players:
    def __init__(self, num_of_players) -> None:
        self.num_of_players = num_of_players
        self.players = [self.num_of_players]

    def get_player(self, player_number: int) -> Player:
        return self.players[player_number]

    def get_player_state(self, player_number: int):
        return self.players[player_number]
