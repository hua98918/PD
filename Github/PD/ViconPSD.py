# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 21:48:04 2017

@author: zhang
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from matplotlib import mlab
import pandas as pd
import os
import pylab

input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02feature.csv"
ouput_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02PSD.csv"
#input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Stairs\Trial01\Filterdata.csv"
dn = os.path.dirname(input_file)
print dn
#input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Filterdata.csv"
df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')

# Sampling information
Fs = 200.
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector


# y is spHeelLX
f0 = 27.
y =df['acKneeR'].fillna(method='ffill')
#y=df['AccelerometerX'].fillna(method='ffill')



# Add in some white noise
#A_noise = 1e-3
#y += (A_noise * np.random.randn(len(y)))

nperseg = 256    # even
#nperseg = 256 # odd

if nperseg > len(y):
    raise ValueError('nperseg > len(y); preventing unintentional zero padding')

# Compute PSD with `scipy.signal.welch`
f_welch, S_welch = welch(
    y, fs=Fs, nperseg=nperseg, noverlap=(nperseg // 2),
    detrend=pylab.detrend_linear, scaling='density', window='hanning')

# Compute PSD with `matplotlib.mlab.psd`, using parameters that are
# *equivalent* to those used in `scipy.signal.welch` above
S_mlab, f_mlab = mlab.psd(
    y, Fs=Fs, NFFT=nperseg, noverlap=(nperseg // 2),
    detrend= pylab.detrend_linear, scale_by_freq=True, window=mlab.window_hanning, sides='twosided')

#pylab.detrend_linear

#fig, axes = plt.subplots(2, 1, sharex=True)
fig1 = plt.figure(figsize=(20,10))
ax1 = fig1.add_subplot(211)
ax1.plot(f_mlab, S_mlab, '-^')
ax1.set_xlabel('frequency')
ax1.set_ylabel('PSD')
ax1.legend(['PSD'],loc='upper left')
ax2 = fig1.add_subplot(212)
ax2.loglog(f_mlab, S_mlab, '-^')
ax2.set_xlabel('logrithm of frequency')
ax2.set_ylabel('logrithm of PSD')
ax2.legend(['PSD loglog'],loc='upper left')
plt.show()
plt.savefig(str(dn) + 'PDkal160525c02_PSD.png')


#fig, axes = plt.subplots(2, 1)
# Plot PSD computed via both methods
#axes[0].loglog(f_welch, S_welch, '-s')
'''
axes[0].loglog(f_mlab, S_mlab, '-^')
axes[0].set_xlabel('frequency')
axes[0].set_ylabel('PSD')
axes[0].legend(['psd'], loc='upper left')
'''
#axes[0].legend(['scipy.signal.welch', 'mlab.psd'], loc='upper left')

# Plot relative error
#delta = np.abs(S_welch - S_mlab)
#avg = 0.5 * np.abs(S_welch + S_mlab)
#relative_error = delta / avg
#axes[1].loglog(f_welch, relative_error, 'k')
#axes[1].set_xlabel('f')
#axes[1].set_ylabel('relative error')

plt.suptitle('nperseg = %i' % nperseg)
plt.show()
