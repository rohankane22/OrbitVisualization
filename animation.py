import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

def animate_orbit(system, num_steps):

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_xlabel("AU")
    ax.set_ylabel("AU")

    def update(frame):
        system.run_timestep()

        for i in system.planet_list.shape[0]:
            ax.plot(system.planet_list[i].x, system.planet_list[i].y, markersize=10, color='b')
    
    ani = anim.FuncAnimation(fig, update, frames=num_steps, blit=True, interval=100, repeat=True)