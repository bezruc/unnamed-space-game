from unnamed_game.entities.planet import Planet


def test_planet_creation():
    planet = Planet(x_coordinate=0, y_coordinate=0, resources=1)
    assert planet._speed == 0
    assert planet._resources == 1
    assert planet._coordinates == (0, 0)
