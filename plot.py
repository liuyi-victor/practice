import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0, 3*math.pi,1001)
x = np.multiply(t,np.cos(t))
y = np.multiply(t,np.sin(t))
#plt.xlim([-100, 10])
#plt.ylim([-100,-100])
plt.plot(x,y)
plt.axis()
plt.title("plot of parametric function")
plt.show()
