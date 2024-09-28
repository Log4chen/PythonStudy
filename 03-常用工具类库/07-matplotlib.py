import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

x = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, x, z)
plt.show()
