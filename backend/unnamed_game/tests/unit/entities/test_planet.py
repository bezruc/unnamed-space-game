from unnamed_game.src.entities.star import Star


def test_planet_creation():
    planet = Star(x_coordinate=0, y_coordinate=0)
    assert planet._resources == 1
    assert planet._coordinates == (0, 0)
