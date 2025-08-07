import OrbitVisualization.OrbitVisualization as ov
from OrbitVisualization.OrbitVisualization import *
import matplotlib.animation as anim
import os
import pytest

def test_animate_orbit():

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlabel("AU")
    ax.set_ylabel("AU")

    ax.scatter([0],[0],marker='*',s=100)

    planet = ov.Planet(1,1,1)
    dt=planet.period/5
    system = ov.System(star_dict={'M': 1, 'Teff': 5700},planet_dict={'1': planet})
    num_steps = 5

    semimajor_axis = 0
    marker_plots = []
    for pl_name, planet in system.planets.items():
        if planet.a > semimajor_axis:
            semimajor_axis = planet.a
        marker = ax.scatter(planet.x, planet.y, label=pl_name, s=300*planet.radius, alpha=0.9)
        marker_plots.append(marker)
        circle = Circle((0, 0), planet.a, color='white', fill=False, alpha=0.7,zorder=0)
        ax.add_patch(circle)

    ax.set_xlim(-1.2*semimajor_axis,1.2*semimajor_axis)
    ax.set_ylim(-1.2*semimajor_axis,1.2*semimajor_axis)

    def update(frame):
        system.run_timestep(dt)
        planet_names = list(system.planets.keys())
        for n in range(len(marker_plots)):
            b = marker_plots[n]
            pl_name = planet_names[n]
            planet = system.planets[pl_name]
            b.set_offsets(np.array([planet.x , planet.y]))
        return marker_plots
    ax.legend()
    ani = anim.FuncAnimation(fig, update, frames=num_steps, blit=True, interval=1000, repeat=True)

    writervideo = anim.FFMpegWriter(fps=30)
    ani.save('test_orbit.gif', writer=writervideo) #, writer=writervideo

    assert os.path.exists(os.path.join(os.getcwd(),'test_orbit.gif')), "Animation not created"


test_animate_orbit()