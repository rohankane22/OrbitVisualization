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
    def __init__(self,star_dict,planet_dict):
        self.M = star_dict['M']
        self.Teff = star_dict['Teff']
        self.planets = planet_dict
        pass

    def run_timestep(self,dt=0.1):
        
        for pl_name, planet in self.planets.items():
            P = planet.period
            theta = 2*np.pi*dt/P
            planet.theta += theta
            planet.x = planet.a * np.cos(planet.theta)
            planet.y = planet.a * np.sin(planet.theta)

        return
    
    def plot_system(self):
        plt.figure()
        plt.scatter(0,0)
        plt.xlim(-10, 10)
        plt.ylim(-10,10)
        for pl_name, planet in self.planets.items():
            print(planet.x, planet.y)
            plt.scatter(planet.x, planet.y)
        plt.show()


def animate_orbit(system, num_steps):

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
        system.run_timestep()
        planet_names = list(system.planets.keys())
        for n in range(len(marker_plots)):
            b = marker_plots[n]
            pl_name = planet_names[n]
            planet = system.planets[pl_name]
            b.set_offsets(np.array([planet.x , planet.y]))
        return marker_plots
    ax.legend()
    ani = anim.FuncAnimation(fig, update, frames=num_steps, blit=True, interval=100, repeat=True)

    plt.show()

Mercury = Planet(0.24,0.387,0.383/11.209)
Venus = Planet(0.616,0.723,0.949/11.209)
Earth = Planet(1,1,1/11.209)
Mars = Planet(1.88,1.524,0.532/11.209)
Jupiter = Planet(12,5,1) 
Saturn = Planet(29,10,9.449/11.209)
SolarSystem = System(star_dict={'M': 1, 'Teff': 5700},\
                     planet_dict={'Mercury': Mercury, \
                                  'Venus': Venus, \
                                  'Earth': Earth, \
                                  'Mars': Mars, \
                                  'Jupiter': Jupiter, \
                                  'Saturn': Saturn})

Trappist_b = Planet(1.511,0.0115,1.116)
Trappist_c = Planet(2.422,0.0158,1.097)
Trappist_d = Planet(4.049,0.0223,0.788)
Trappist_e = Planet(6.101,0.0293,0.920)
Trappist_f = Planet(9.208,0.0385,1.045)
Trappist_g = Planet(12.352,0.0468,1.129)
Trappist_h = Planet(18.773,0.0619,0.755)


Trappist1 = System(star_dict={'M': 0.09, 'Teff': 2566},
                   planet_dict={'b': Trappist_b,
                                'c': Trappist_c,
                                'd': Trappist_d,
                                'e': Trappist_e,
                                'f': Trappist_f,
                                'g': Trappist_g,
                                'h': Trappist_h,})

# animate_orbit(SolarSystem, 1000)

animate_orbit(Trappist1, 1000)
