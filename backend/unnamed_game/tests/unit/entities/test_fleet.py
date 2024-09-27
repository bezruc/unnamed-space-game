from unnamed_game.src.entities.fleet import Fleet


# test if math of simulation is correct
def test_fleet_simulation():
    entity = Fleet(x_coordinate=0, y_coordinate=0, speed=1)
    entity.set_target(1, 1)
    assert entity._coordinates == (0, 0)
    entity.simulate()
    assert entity._coordinates != (0, 0)
    assert entity._coordinates != (1, 1)
    entity.simulate()
    assert entity._coordinates == (1, 1)

    entity = Fleet(x_coordinate=3, y_coordinate=4, speed=1)
    entity.simulate()
    entity.simulate()
    assert entity._coordinates == (3, 4)
    entity.set_target(0, 0)
    entity.simulate()
    entity.simulate()
    entity.simulate()
    entity.simulate()
    assert entity._coordinates > (0, 0)
    entity.simulate()
    assert entity._coordinates == (0, 0)
