from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameterization of the curve (e.g., a circle in 3D space)
t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = t  # Just for illustration, let's say the curve rises as it goes around

# Plot the curve in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')

# Now let's do a line integral along this curve
# We need a function to integrate
# For simplicity, let's integrate the x-component along the curve

# The integrand function receives the parameter t, not the x, y, z directly
def integrand(t):
    x = np.cos(t)
    # y = np.sin(t)  # y is not used in this example, but this is how you would get it
    return x

# Perform the line integral along the curve
result, error = quad(integrand, 0, 2*np.pi)

print(f"The line integral result is {result} with an error of {error}")

# Show the plot with the curve
ax.legend()
plt.show()



