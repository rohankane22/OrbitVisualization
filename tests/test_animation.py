import OrbitVisualization.OrbitVisualization as ov
import os

def test_animate_orbit():
    """
    Tests animate orbit, working if a gif with five frames is created.
    """

    planet = ov.Planet(1,1,1)

    system = ov.System(star_dict={'M': 1, 'Teff': 5700},planet_dict={'1': planet})

    ov.animate_orbit(system, num_steps=5, dt=0.2, save_anim=True, show_anim=False, savefile='test_orbit.gif')

    assert os.path.exists(os.path.join(os.getcwd(),'test_orbit.gif'))  #Animation not created

    os.remove(os.path.join(os.getcwd(),'test_orbit.gif'))


test_animate_orbit()