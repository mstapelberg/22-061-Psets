#Matplotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

#Science Library
import numpy as np
from scipy.optimize import curve_fit

#with open('REBCOExperiment_IVData.dat', 'r') as input_file:
I = np.loadtxt('REBCOExperiment_IVData.dat', delimiter = ',', usecols = 0)
V = np.loadtxt('REBCOExperiment_IVData.dat', delimiter = ',', usecols = 1)

def exponential_func(x, a, b , c):
    return a*np.exp(b*x)+c

popt, pcov = curve_fit(exponential_func, I, V, p0= [1, 1, 1])

plt.plot(I,V, label = 'REBCO-Experimental Data')
plt.plot(I, exponential_func(I, popt[0], popt[1], popt[2]), label = 'Fitted-Data')

plt.legend(loc = 'best')
plt.show()
