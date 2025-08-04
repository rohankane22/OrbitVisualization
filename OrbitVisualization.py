import numpy as np
import matplotlib.pyplot as plt

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

    def run_timestep(self,dt=0.1)
        
        planets = self.planets.keys()
        for planet in planets:
            P = self.planets[planet].period
            dtheta = 2*np.pi*dt/P
            self.planets[planet].theta += theta

        return
    
    def plot_system(self):
        plt.figure()
        plt.plot(0,0)
        planets = self.planets.keys()
        for planet in planets:
            plt.plot(self.planets[planet].x,self.planets[planet].y)
        
Jupiter = Planet(12,5,1)
Saturn = Planet(29,10,.8)
SolarSystem = System(star_dict={'M': 1, 'Teff': 5700},planet_dict={'Jupiter': Jupiter, 'Saturn': Saturn})
