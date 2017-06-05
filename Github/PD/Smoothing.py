# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 21:03:12 2017

@author: Zhang
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
import scipy.fftpack
import peakutils


def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    from math import factorial
         
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
         raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
         raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
     # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')

def smooth(x,window_len=11,window='hanning'):
    if x.ndim != 1:
            raise ValueError, "smooth only accepts 1 dimension arrays."
    if x.size < window_len:
            raise ValueError, "Input vector needs to be bigger than window size."
    if window_len<3:
            return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
            raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
    s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
    if window == 'flat': #moving average
            w=np.ones(window_len,'d')
    else:  
            w=eval('np.'+window+'(window_len)')
    y=np.convolve(w/w.sum(),s,mode='same')
    return y[window_len:-window_len+1]
  
    
input_file = "C:\pakinsen\Vicon\WALKER2016\PDpra160407\PDpra160407m01feature.csv"

df = pd.read_csv(input_file, sep=",")

fig1 = plt.figure(figsize=(20,10))
ax1 = fig1.add_subplot(311)
ax1.plot(df['serial'],df['HeelLZ'].as_matrix(),label='original data')
#ax1.plot(df['serial'],df['HeelRZ'].as_matrix())
xL = smooth(df['HeelLZ'].as_matrix(),window_len=20,window='hanning')   # smooth the data
#xR = smooth(df['HeelRZ'].as_matrix(),window_len=20,window='hanning')   # smooth the data
#xL = savitzky_golay(df['HeelLZ'].as_matrix(),window_size=61,order=1)
ax1.plot(df['serial'],xL, color='red',label='smoothed data')
#ax1.plot(df['serial'],xR, color='red')
ax1.set_title('Smoothed Vertical Heel spacial')

higherPeakL = argrelextrema(xL, np.greater)    # way2: find the peak(scipy.signal )
lowerVallyL = argrelextrema(xL, np.less)
ax2 = fig1.add_subplot(312)
ax2.plot(df['serial'], xL, '-bD', markevery=list(higherPeakL), label='Left Heel' )
ax2.plot(df['serial'], xL, '-rD', markevery=list(lowerVallyL) )





#elminate peaks and valleys


plt.show()
