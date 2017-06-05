# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 14:53:54 2017

@author: Ariel
"""


import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
import os 
import scipy.stats as sp
import MDFA as dfa

#input_file = input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Stairs\Trial01\LoggedData_CalInertialAndMag.csv"

input_file = input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Stairs\Trial01\Filterdata.csv"


df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')
'''
x=df['Accelerometer X (g)']
y=df['Accelerometer Y (g)']
z=df['Accelerometer Z (g)']
'''
x=df['AccelerometerX']
y=df['AccelerometerY']
z=df['AccelerometerZ']


def plot_trends(X,scale,m=1,label='',title=''):   #find the trend  m=1 linear  m=2 为 quadratic
    t = np.arange(X.shape[0])  # t is the range of all number the signal X
    plt.plot(t,X,lw=2.0)   #plotting the original signal line width =2
    for i0 in xrange(0,X.shape[0]-scale+1,(scale-1)/2):  # start from 0 to last whole scale, steps is (windows-1)/2, overlapping half windows
        i1 = i0+scale  #forwarding scale dots
        t0 = t[i0:i1]  #intersect t0 array from steps
        C = np.polyfit(t0,X[i0:i1],m)  # fit for the polynomial order M   C is the coefficent of the polynomio
        fit = np.polyval(C,t0);  #get all the fitted data
        RMS = np.sqrt(((X[i0:i1]-fit)**2).mean()) #the RMS root mean square.
        #print RMS
        plt.plot(t0,fit,'r--')
        plt.plot(t0,fit-RMS,'r')
        plt.plot(t0,fit+RMS,'r')
    plt.ylabel(label,ha='center')
    if title: plt.text(100,500,title,fontsize=12) 

n = 15
scale=2*n+1
#scale = np.floor(2.0**np.arange(4,8,0.25)).astype('i4')

#RW = np.cumsum(df['acToeRX']-df['acToeRX'].mean())
#RW = np.cumsum(df['spToeLX']-df['spToeLX'].mean())
RW= np.cumsum(x-x.mean())


#plt.subplot(311)
#plot_rms(RW,label='acToeRX signal')
plt.subplot(211)
plot_trends(RW,scale,1,label='signal\namplitude',
            title='A Linear detrending')
plt.legend(['Noise like time-series','Local trend','+/- 1 local RMS'])
plt.subplot(212)
plot_trends(RW,scale,2,label='signal\namplitude',
            title='B Quadratic detrending')

plt.savefig('HC_IMU.png')



########################################################
scales = np.floor(2.0**np.arange(4,10,0.25)).astype('i4')
#F_si = trends(RW,16,1)
#F_xf = comp_Fs(df['spHeelR'],scales,1)
F_si = dfa.compRMS(RW,scales,1).ravel() 
L = 70

import numpy.ma as ma

scales = (2**np.arange(4,12)).astype('i4')
RMS = dfa.compRMS(RW,scales)
plt.subplot(311)
plt.plot(np.arange(0,RW.shape[0],scales[0]),RMS.T/scales + 0.01*np.arange(len(scales)))
plt.subplot(312)
mRMS = ma.array(RMS,mask=np.isnan(RMS))
plt.loglog(scales,mRMS.mean(1),'o-',ms=5.0,lw=0.5)
plt.subplot(313)
for q in [-3,-1,1,3]:
	plt.loglog(scales,((mRMS**q).mean(1))**(1.0/q),'o-',ms=5.0,lw=0.5) 

'''
fig2 = plt.figure()

ax1= fig2.add_subplot(121)
#ax1.plot(np.gradient(np.angle(X)),np.angle(X),c='r',label='HS')   
ax1.plot(np.arange(F_si.shape[0]),F_si,c='b',label='PD')    
ax1.grid()
#ax1.set_title('Residual data')
ax1.set_xlabel('Index')
ax1.set_ylabel('Residual data')
ax1.legend()
plt.show()
    
ax1= fig2.add_subplot(122)
#ax1.plot(np.gradient(np.angle(X)),np.angle(X),c='r',label='HS')   
ax1.plot(F_si[:(F_si.shape[0]-L)],F_si[L:],c='b',label='PD')    
ax1.grid()
ax1.set_title('phase diageam ')
ax1.set_xlabel('residual X[i]')
ax1.set_ylabel('X[i+L]')
ax1.legend()
plt.show()  
'''