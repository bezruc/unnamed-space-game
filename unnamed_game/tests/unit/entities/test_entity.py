from unnamed_game.entities.entity import Entity


def test_entity_creation():
    planet = Entity(x_coordinate=0, y_coordinate=0, speed=45)
    assert planet._speed == 45
    assert planet._coordinates == (0, 0)
