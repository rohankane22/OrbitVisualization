import OrbitVisualization as ov
import pytest

def test_xy():
    planet = ov.Planet(1,1,1)
    system = ov.System(star_dict={'M': 1, 'Teff': 5700},planet_dict={'1': planet})

    assert planet.x == pytest.approx(-1, 1e-5) "initial position not as expected"
    assert planet.y == pytest.approx(0, 1e-5) "initial position not as expected"