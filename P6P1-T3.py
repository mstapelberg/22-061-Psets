#Matplotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

#Science Library
import numpy as np
from scipy.optimize import curve_fit

#with open('REBCOExperiment_IVData.dat', 'r') as input_file:
I = np.loadtxt('REBCOExperiment_IVData.dat', delimiter = ',', usecols = 0)
V = np.loadtxt('REBCOExperiment_IVData.dat', delimiter = ',', usecols = 1)

coef = np.polyfit(I, np.log(V), 1, w = np.sqrt(V))

plt.plot(I, V, label = 'REBCO-Experimental')
plt.plot(coef, label = 'FIT-DATA')

plt.title("REBCO Experimental IV Data")

plt.legend()
plt.show()
