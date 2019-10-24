import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, 0.1)
plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(t, t, 'r.-')
plt.subplot(3, 1, 2)
plt.plot(t, t ** 2, 'g*-')
plt.subplot(313)
plt.plot(t,t**3, 'b^--')
plt.show()
