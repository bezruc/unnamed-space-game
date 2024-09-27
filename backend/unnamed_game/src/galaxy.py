import random
import schedule
from unnamed_game.src.entities.star import Star
from unnamed_game.src.entities.fleet import Fleet
           

class Galaxy:
    def __init__(self, players: list) -> None:
        self._players = players
        self._stars = {}
        self._fleets = {}

        # --------------------------------------------------------------------------
        # placeholder galaxy generation, TODO: Create separate method for generation
        # RN each player stars with one planet and 1 fleet with no power at the time
        num_of_stars = 32
        for i in range(num_of_stars):
            star = Star(random.uniform(0,1000), random.uniform(0,1000))
            self._stars[star.get_id()] = star
        
        homestars = random.sample(sorted(self._stars), len(players))
        for star, player in zip(homestars, players):
            self._stars[star].set_owner(player)
            coords = self._stars[star].get_coordinates()
            fleet = Fleet(coords[0], coords[1])
            self._fleets[fleet.get_id()] = fleet
            
        # --------------------------------------------------------------------------

    def advance_time(self):
        for id, star in self._stars.items():
            star.simulate()
        
        for id, fleet in self._fleets.items():
            fleet.simulate()
          
    def get_galaxy_state(self):
        return {
            "stars": self._stars,
            "fleets": self._fleets
        }
