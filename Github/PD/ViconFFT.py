# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:18:14 2016

@author: zhang
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy.signal import butter, lfilter

input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525w02feature.csv"
dn = os.path.dirname(input_file)
print dn
#input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Filterdata.csv"
df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')


# Sample rate and desired cutoff frequencies (in Hz).
fs = 64
lowcut = 0.0
highcut = 8.0

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y



Fs = 200.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector
x = butter_bandpass_filter(df['acToeLX'].fillna(method='ffill'),lowcut, highcut, fs, order=5)
y = butter_bandpass_filter(df['acToeLY'].fillna(method='ffill'),lowcut, highcut, fs, order=5)
z = butter_bandpass_filter(df['acToeLZ'].fillna(method='ffill'),lowcut, highcut, fs, order=5)
#print x,y,z

n = len(x) # length of the signal ,fft size
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

#Y = np.fft(y)/n # fft computing and normalization
X = np.fft.fft(x)/n 
Y = np.fft.fft(y)/n # fft computing and normalization
Z = np.fft.fft(z)/n
#print Y
X = X[range(n/2)]
Y = Y[range(n/2)]
Z = z[range(n/2)]


#power, freqs = matplotlib.mlab.psd(x, NFFT, Fs,detrend, window, noverlap=0, pad_to, sides=,scale_by_freq)



fig1 = plt.figure(figsize=(20,10))
ax1 = fig1.add_subplot(211)
ax1.plot(df[['serial']],x,c='r',label='Left accel Toe x')
ax1.plot(df[['serial']],y,c='b',label='Left accel Toe y')
#ax1.plot(df[['serial']],z,c='g',label='Left accel Toe z')
ax1.grid()
ax1.set_title('acceleration of left Toe')
ax1.set_xlabel('sample number')
ax1.set_ylabel('acceleration')
ax1.legend()
ax2 = fig1.add_subplot(212)
ax2.plot(frq,abs(X),c='r',label='Left accel Toe x')
ax2.plot(frq,abs(Y),c='b',label='Left accel Toe y')
#ax2.plot(frq,abs(Z),c='g',label='Left accel Toe z')
ax2.grid()
ax2.set_title('accelerator of left Toe FFT')
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|(Amplitude)|')
ax2.legend()
plt.show()
plt.savefig(str(dn) + 'PDkal160525w03featureacToeL_FFT.png')
 
#print max(abs(Y)),frq 
