import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.patches import Circle

plt.style.use('dark_background')

class Planet(object):
    """
    Planet class.
    
    This class defines a planet and its properties.

    Attributes:
        period (float): Period of the planet's orbit
        a (float): Semi-major axis of the planet's orbit
        theta (float): angle of the orbit
        radius (float): radius of the planet
        x (float): x-coordinate of the location of the planet
        y (float): y-coordinate of the location of the planet
    
    """
    def __init__(self,period,a,radius,theta=np.pi):
        """
        Initialize the planet class.
        
        Args:
            period (float): Period of the planet's orbit, in years.
            a (float): Semi-major axis of the planet's orbit, in AU.
            radius (float): Radius of the planet. No specific units required, user's choice.
            theta (float, optional): Angle of the planet's orbit. Default value is pi radians.
        """
        self.period = period  # years
        self.a = a            # AU
        self.theta = theta    # radians
        self.radius = radius  # TBD

        self.x = a*np.cos(theta)
        self.y = a*np.sin(theta)
        pass


class System(Planet):
    """
    System class.
    
    This class defines a planetary system, including a star and its planets.

    Attributes:
        M (float): Mass of the star in solar masses.
        Teff (float): Effective temperature of the star in Kelvin.
        planets (dict): Dictionary containing the planets in the system, with planet names as keys.

    Args:
        star_dict (dict): Dictionary containing the star's properties, including 'M' and 'Teff'.
        planet_dict (dict): Dictionary containing the planets in the system, with planet names as keys and Planet objects as values.
    
    """
    def __init__(self,star_dict,planet_dict):
        self.M = star_dict['M']
        self.Teff = star_dict['Teff']
        self.planets = planet_dict
        pass

    def run_timestep(self,dt=0.1):
        """
        Advances the system by a timestep, updating the positions of the planets.

        Args:
            dt (float, optional): Time step in years. Default is 0.1 years.
        
        """
        
        for pl_name, planet in self.planets.items():
            P = planet.period
            theta = 2*np.pi*dt/P
            planet.theta += theta
            planet.x = planet.a * np.cos(planet.theta)
            planet.y = planet.a * np.sin(planet.theta)

        return
    
    def plot_system(self):
        """
        Plots the current positions of the planets in the system.
        """
        plt.figure()
        plt.scatter(0,0)
        plt.xlim(-10, 10)
        plt.ylim(-10,10)
        for pl_name, planet in self.planets.items():
            print(planet.x, planet.y)
            plt.scatter(planet.x, planet.y)
        plt.show()


def animate_orbit(system, num_steps, dt=0.1, save_anim=False, show_anim=True, savefile=None):
    """
    Animates the orbits of the planets in the system.

    Plots the system at a given timestep, runs a timestep, plots the new configuration, repeats N=num_steps times and creates a gif.

    Args:
        system (System): The planetary system to animate.
        num_steps (int): Number of time steps to loop over.
    """

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlabel("AU")
    ax.set_ylabel("AU")

    ax.scatter([0],[0],marker='*',s=100)

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
        system.run_timestep(dt=dt)
        planet_names = list(system.planets.keys())
        for n in range(len(marker_plots)):
            b = marker_plots[n]
            pl_name = planet_names[n]
            planet = system.planets[pl_name]
            b.set_offsets(np.array([planet.x , planet.y]))
        return marker_plots
    ax.legend()
    ani = anim.FuncAnimation(fig, update, frames=num_steps, blit=True, interval=100, repeat=True)

    if save_anim:
        writervideo = anim.FFMpegWriter(fps=30)
        ani.save(savefile, writer=writervideo)

    if show_anim:
        plt.show()
