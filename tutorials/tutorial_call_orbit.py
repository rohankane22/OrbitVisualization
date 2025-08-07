"""
Tutorial Script to Plot the Orbits of the Solar System and the TRAPPIST-1 system
"""

from OrbitVisualization.OrbitVisualization import Planet, System, animate_orbit

if __name__ == "__main__":
    """
    Define planets with a period (years), separation (AU), and radius (R_Jup).
    """
    Mercury = Planet(0.24,0.387,0.383/11.209)
    Venus = Planet(0.616,0.723,0.949/11.209)
    Earth = Planet(1,1,1/11.209)
    Mars = Planet(1.88,1.524,0.532/11.209)
    Jupiter = Planet(12,5,1) 
    Saturn = Planet(29,10,9.449/11.209)

    """
    Define your stellar system with stellar properties and a list of Planet objects.
    """
    SolarSystem = System(star_dict={'M': 1, 'Teff': 5700},\
                        planet_dict={'Mercury': Mercury, \
                                    'Venus': Venus, \
                                    'Earth': Earth, \
                                    'Mars': Mars, \
                                    'Jupiter': Jupiter, \
                                    'Saturn': Saturn})

    """
    Repeat with the Trappist1 system.
    """
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

    """
    Create animation.
    """
    animate_orbit(SolarSystem, 1000)

    animate_orbit(Trappist1, 1000)