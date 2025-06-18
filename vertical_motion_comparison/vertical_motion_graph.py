# Vertical motion under gravity. For understanding the importance of dt to be infinitesimaly small when integrating by using graphs. 
import matplotlib.pyplot as plt
import numpy as np

a = -10
s_f = 0
s_i = 0
dt = 1 # Change this value (time interval)
v = 30 # Change this value (initial velocity)
t = 15 # Change this value (time period)


tVal = 0
v_i = v
tList = []
sList = []

# Make a list of time at each instance. and also to make a list of dispacement.
# To make graph of integration
while tVal <= t:
    tList.append(tVal)

    if tVal != 0:
        v_i += a * dt
        s_i += v_i * dt
        sList.append(s_i)
    else:
        sList.append(s_i)
        
    tVal += dt

plt.plot(tList, sList, 'red')

# To make graph of correct displacemet values at each instance
tList = np.array(tList)
s_f = v * tList + 0.5 * a * tList ** 2

plt.plot(tList, s_f, 'blue')

# Set up the Graph
plt.title("Vertical motion under gravity")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.legend("∫")
plt.grid(True)

plt.show()