import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Planet(object):
    def __init__(self,period,a,radius,theta=np.pi,e=0):
        self.period = period
        self.a = a
        self.theta = theta
        self.radius = radius

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
        
        planets = self.planets.keys()
        for planet in planets:
            P = self.planets[planet].period
            theta = 2*np.pi*dt/P
            self.planets[planet].theta += theta

        return
    
    def plot_system(self):
        plt.figure()
        plt.scatter(0,0)
        plt.xlim(-10, 10)
        plt.ylim(-10,10)
        planets = self.planets.keys()
        for planet in planets:
            print(self.planets[planet].x, self.planets[planet].y)
            plt.scatter(self.planets[planet].x, self.planets[planet].y)
        plt.show()


def animate_orbit(system, num_steps):

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-15,15)
    ax.set_ylim(-15,15)
    ax.set_xlabel("AU")
    ax.set_ylabel("AU")

    planets = system.planets.keys()
    marker_plots = []
    for planet in planets:
        marker = ax.scatter(system.planets[planet].x, system.planets[planet].y)
        marker_plots.append(marker)

    def update(frame):
        system.run_timestep()

        for n in range(len(marker_plots)):
            b = marker_plots[n]
            b.set_offsets(np.array([system.planets[planet].x , system.planets[planet].y]))
        return marker_plots
    
    ani = anim.FuncAnimation(fig, update, frames=num_steps, blit=True, interval=100, repeat=True)

    ani.save("animation.gif", writer=anim.PillowWriter(fps=100))

Jupiter = Planet(12,5,1)
Saturn = Planet(29,10,.8)
SolarSystem = System(star_dict={'M': 1, 'Teff': 5700},planet_dict={'Jupiter': Jupiter, 'Saturn': Saturn})

#SolarSystem.plot_system()

animate_orbit(SolarSystem, 5000)