import numpy as np
import matplotlib.pyplot as plt

def initial(N = 1500):
    y = np.zeros(11)
    y[0] = N -1 #number of not infected
    y[1] = 1.0  #number of infected
    return y

def system_derivatives(t, y, beta, gamma=1.0):
    I = np.sum(y[1:10]) #exclude healthy&immune people
    n_I = beta * y[0] * I #new infected

    dydt = np.zeros(11)
    dydt[0] = -n_I
    dydt[1] = n_I -gamma * y[1]
    dydt[2:10] = y[1:9] * gamma - gamma * y[2:10]   #progressed infected from previous day minus progressed infected from this day
    dydt[10] = gamma * y[9]

    return dydt

#y0 = initial()
#print(np.sum(system_derivatives(0, y0, beta=0.0003)))

