# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:18:14 2016

@author: zhang
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import MDFA as mdfa

#input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c02feature.csv"
input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Filterdata.csv"
output_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Freqdata.csv"
df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')

df2 = pd.DataFrame(columns=['AccelerometerX_Amp','AcceX_Amp_derivative','AccelerometerX_Phase','AcceX_Phase_derivative'\
                            'AccelerometerY_Amp','AcceY_Amp_derivative','AccelerometerY_Phase','AcceX_Phase_derivative'\
                            'AccelerometerZ_Amp','AcceZ_Amp_derivative','AccelerometerZ_Phase','AcceX_Phase_derivative'])


Fs = 100.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector
x=df['AccelerometerX'].fillna(method='ffill')
y=df['AccelerometerY'].fillna(method='ffill')
z=df['AccelerometerZ'].fillna(method='ffill')


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

df2['AccelerometerX_Amp'] = abs(X)
df2['AcceX_Amp_derivative'] = np.gradient(abs(X))
df2['AccelerometerX_Phase'] = np.angle(X)
df2['AcceX_Phase_derivative'] = np.gradient(np.angle(X))
df2['AccelerometerY_Amp'] = abs(Y)
df2['AcceY_Amp_derivative'] = np.gradient(abs(Y))
df2['AccelerometerY_Phase'] = np.angle(Y)
df2['AcceY_Phase_derivative'] = np.gradient(np.angle(Y))
df2['AccelerometerZ_Amp'] = abs(Z)
df2['AcceZ_Amp_derivative'] = np.gradient(abs(Z))
df2['AccelerometerZ_Phase'] = np.angle(Z)
df2['AcceZ_Phase_derivative'] = np.gradient(np.angle(Z))
df2.to_csv(output_file,sep=',',header=True)  #save the data frequency


fig1 = plt.figure(figsize=(20,10))
ax1 = fig1.add_subplot(211)
ax1.plot(df[['Serial']],x,c='r',label='AccelerometerX')
#ax1.plot(df[['Serial']],y,c='b',label='AccelerometerY')
#ax1.plot(df[['Serial']],z,c='g',label='AccelerometerZ')
ax1.grid()
ax1.set_title('Accelerometer on x-y axises')
ax1.set_xlabel('sample number')
ax1.set_ylabel('Left Toe speed')
ax1.legend()
ax2 = fig1.add_subplot(212)
ax2.plot(frq,abs(X),c='r',label='AccelerometerX')     #the absolute value of the complex number (sqrt(x.real**2 + x.imag**2), or numpy.abs()) is the amplitude
#ax2.plot(frq,abs(Y),c='b',label='AccelerometerY')
#ax2.plot(frq,abs(Z),c='g',label='AccelerometerZ')
ax2.grid()
ax2.set_title('Accelerometer on x-y axises on frequncy ')
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Left Toe Accelerometer Magitude =|')
ax2.legend()
plt.show()


fig2 = plt.figure()
ax1= fig2.add_subplot(111)
#ax1.plot(np.gradient(np.angle(X)),np.angle(X),c='r',label='HS')   
ax1.plot(np.angle(X),np.gradient(np.angle(X)),c='r',label='HS')    
ax1.grid()
ax1.set_title('AccelerometerX phase diageam ')
ax1.set_xlabel('Amp X')
ax1.set_ylabel('first derivative of X')
ax1.legend()
plt.show()
 
print max(abs(Y))


scales = np.floor(2.0**np.arange(4,10,0.25)).astype('i4')
RMS = mdfa.compRMS(df2['AcceZ_Phase_derivative'] ,scales,1).ravel() 
L = 30
fig3 = plt.figure()
ax1= fig3.add_subplot(111)
#ax1.plot(np.gradient(np.angle(X)),np.angle(X),c='r',label='HS')   
ax1.plot(RMS[:(RMS.shape[0]-L)],RMS[L:],c='b',label='Control')    
ax1.grid()
ax1.set_title('phase diageam ')
ax1.set_xlabel('residual X[i]')
ax1.set_ylabel('X[i+L]')
ax1.legend()
plt.show()    
