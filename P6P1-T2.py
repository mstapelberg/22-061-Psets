import plotly.plotly as py
import plotly.graph_objs as go

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

popt, pcov = curve_fit(exponential_func, I, V, p0=(1, 1e-6, 1))

II = np.linspace(1, 1.659587E+2, 1000)
VV = exponential_func(II, *popt)

plt.plot(I,V, 'o', II, VV)
pylab.title("REBCO Experimental Data + Fit")
ax = plt.gca()
ax.set_axis_bgcolor((0.898, 0.898, 0.898))
fig = plt.gcf()
py.plot_mpl(fig, filename="REBCO-Experimental-Fit")
