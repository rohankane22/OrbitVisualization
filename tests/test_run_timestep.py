import OrbitVisualization.OrbitVisualization as ov
import numpy as np
import pytest

def test_run_timestep():
    """
    Unit test of the run_timestep function in OrbitVisualization.py
    """

    planet = ov.Planet(1,1,1,np.pi) 

    system = ov.System(star_dict={'M': 1, 'Teff': 5700},\
                        planet_dict={'test planet': planet})

    system.run_timestep()

    exp_theta = 1.2*np.pi
    exp_x = -0.809017
    exp_y = -0.587785

    assert planet.theta == pytest.approx(exp_theta, abs=0.001)
    assert planet.x == pytest.approx(exp_x, abs=0.001)
    assert planet.y == pytest.approx(exp_y, abs=0.001)

if __name__ == "__main__":
    test_run_timestep()
