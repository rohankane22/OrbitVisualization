# OrbitVisualization
Code/Astro Project

Animates planetary orbits around a star. Reads in stellar and planetary properties.

## Installation Instructions

To install, run
```
pip install OrbitVisualization
```

## Generating an animation

To create an animation, first import the Planet and System classes, and the animate_orbit function
```
from OrbitVisualization.OrbitVisualization import Planet, System, animate_orbit
```
Define planets using the Planet class. Inputs are period, semi-major axis, and radius.
```
Jupiter = Planet(12,5,1) 
Saturn = Planet(29,10,9.449/11.209)
```
Define the system object, passing a dictionary for the star containing the mass and effective temperature, and a dictionary for the planet containing the planet name and the Planet object.
```
SolarSystem = System(star_dict={'M': 1, 'Teff': 5700}, planet_dict={'Jupiter': Jupiter, 'Saturn': Saturn})
```
Finally, animate the orbit by passing in the System object and the number of frames you want in your animation.
```
animate_orbit(SolarSystem, 1000)
```

![A rectangular badge, half black half purple containing the text made at Code Astro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)
[![DOI](https://zenodo.org/badge/1032071309.svg)](https://doi.org/10.5281/zenodo.16764013)

