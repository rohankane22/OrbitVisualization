import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.patches import Circle

plt.style.use('dark_background')

class Planet(object):
    def __init__(self,period,a,radius,theta=np.pi,e=0):
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

#SolarSystem.plot_system()

animate_orbit(SolarSystem, 1000)