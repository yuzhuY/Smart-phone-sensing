#import numpy as np
#from scipy.optimize import curve_fit
from constants import *

def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def gaussFit(rawList):
	for i in range(0, len(rawList)):
		x = []
		y = []
		for j in range(0, len(rawList[i])):
			if rawList[i][j] != 0:
				x.append(j)
				y.append(rawList[i][j])
		print y
		print x
		xFake = range(0, len(x))
		popt, pcov = curve_fit(gauss_function, xFake, y)

		for j in range(0, len(rawList[i])):
			rawList[i][j] = round(gauss_function(j - x[0], *popt))
