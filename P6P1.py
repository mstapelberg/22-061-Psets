import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#with open('REBCOExperiment_IVData.dat', 'r') as input_file:
I = np.loadtxt('REBCOExperiment_IVData.dat', delimiter = ',', usecols = 0)
V = np.loadtxt('REBCOExperiment_IVData.dat', delimiter = ',', usecols = 1)
def func(x,a,b,c):
    return a * np.exp(b*x) + c

popt, pcov  = curve_fit(func, I, V)
#print(I)
#Plotting
plt.plot(I, V, label = 'IV-Graph')

plt.plot(I, func(I, *popt), 'r-', label = 'Curve-Fit: a=%5.3f, b=%5.3f, c=%5.3f % tuple(popt)')

plt.xlabel('Current [A]')
plt.ylabel('Voltage [uV]')

plt.title("REBCO Experimental IV Data")

plt.legend()
plt.show()
