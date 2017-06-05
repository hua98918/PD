# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:56:36 2016

@author: zhang
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import butter, lfilter

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

# Sample rate and desired cutoff frequencies (in Hz).
fs = 100
lowcut = 3.0
highcut = 8.0

varianceWindows = 15
windowSize = 60
timeInterval = 0.01   #comes from 100HZ in one second; unit:second
#input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509m01feature.csv"
input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02feature.csv"

df = pd.read_csv(input_file, sep=",")
print df.head()
df.fillna(0)
mad = lambda x: np.fabs(x - x.mean()).mean()

df['defLX'] = df['spToeLX'].rolling(windowSize).apply(mad)
df['defLY'] = df['spToeLY'].rolling(windowSize).apply(mad)
df['defLZ'] = df['spToeLZ'].rolling(windowSize).apply(mad)

df['defRX'] = df['spToeRX'].rolling(windowSize).apply(mad)
df['defRY'] = df['spToeRY'].rolling(windowSize).apply(mad)
df['defRZ'] = df['spToeRZ'].rolling(windowSize).apply(mad)


df['stepLX'] = np.where(df['spToeLX'].rolling(windowSize).apply(mad)>50,200,0)
df['stepLY'] = np.where(df['spToeLY'].rolling(windowSize).apply(mad)>50,200,0)
df['stepLZ'] = np.where(df['spToeLZ'].rolling(windowSize).apply(mad)>50,200,0)



df['filterToeLX']= butter_bandpass_filter(df['spToeLX'], lowcut, highcut, fs, order=5)
df['filterToeRX']= butter_bandpass_filter(df['spToeRX'], lowcut, highcut, fs, order=5)


fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(df[['serial']],df[['spToeLX']],label="left side")
ax1.plot(df[['serial']],df[['spToeRX']],c='r',label="right side")
#ax1.plot(df[['serial']],df[['stepLX']],c='g',label="left step")
ax1.plot(df[['serial']],df[['filterToeLX']],c='g',label="left Toe")
ax1.plot(df[['serial']],df[['filterToeRX']],c='y',label="filter right")
ax1.set_title('spToeX position  according to time domain')
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(df[['serial']],df[['spToeLY']],label="left side")
ax2.plot(df[['serial']],df[['spToeRY']],c='r',label="right side")
#ax2.set_title('spToeLY position according to time domain')
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(df[['serial']],df[['spToeLZ']],label="left side")
ax3.plot(df[['serial']],df[['spToeRZ']],c='r',label="right side")
#ax3.plot(df[['serial']],df[['stepLZ']],c='g',label="left step")
ax3.set_title('spToeLZ position according to time domain')
ax3.legend()

#df['stepLZ'] = np.where(df['spHeelLZ'].rolling(windowSize).apply(mad)>100,10,0)
#df['stepRZ'] = np.where(df['spHeelRZ'].rolling(windowSize).apply(mad)>100,10,0)
   
turnStartDF1 = df.loc[(df['defLX'].abs()>700) & (df['defLY'].abs()>700)].head(1)
turnStartDF2 = df.loc[(df['defRX'].abs()>700) & (df['defRY'].abs()>700)].head(1)
startIndex = min(int(turnStartDF1.index.get_values()),int(turnStartDF2.index.get_values()))
print startIndex

turnEndDF1 = df.loc[(df['defLX'].abs()>700) & (df['defLY'].abs()>700)].tail(1)
turnEndDF2 = df.loc[(df['defRX'].abs()>700) & (df['defRY'].abs()>700)].tail(1)
endIndex = max(int(turnEndDF1.index.get_values()),int(turnEndDF2.index.get_values()))
print endIndex
