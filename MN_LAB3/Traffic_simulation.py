import numpy as np
import matplotlib.pyplot as plt

nx = 100  # Number of road segments
nt = 20  # Number of time steps
L = 100.0  # Length of the road network
dx = L / nx  # Length of each road segment
dt = 0.001  # Time step
Vmax = 90.0  # Maximum velocity
rho_max = 15.0  # Maximum traffic density

# Initialize traffic density and velocity arrays
rho = np.ones(nx) * rho_max / 2
v = np.zeros(nx)

# Iterate over time steps
for n in range(nt):
    q = rho * v                                      # Calculate traffic flow at each point
    q[0] = q[nx - 1]                                 # Apply periodic boundary conditions
    rho_gradient = np.diff(rho) / dx                 # Calculate traffic density gradient
    v = Vmax * (1 - rho / rho_max)                   # Update traffic velocity using Lighthill-Whitham-Richards (LWR) equation
    delta_rho = -dt * np.diff(q) / dx                # Calculate change in traffic density over time
    delta_rho = np.append(delta_rho, delta_rho[0])   # Apply periodic boundary conditions
    rho += delta_rho                                 # Update traffic density using conservation law equation
    rho = np.maximum(0, np.minimum(rho, rho_max))    # Apply upper and lower bounds to traffic density

    # Plot traffic density and velocity
    if n % 10 == 0:
        plt.clf()
        plt.plot(np.linspace(0, L, nx), rho)
        plt.plot(np.linspace(0, L, nx), v)
        plt.xlabel('Position')
        plt.ylabel('Density / Velocity')  # Upper plot shows traffic density, lower plot shows velocity
        plt.ylim([0, Vmax * 1.2])
        plt.pause(0.001)

plt.show()
