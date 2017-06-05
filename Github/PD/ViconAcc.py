# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 09:02:05 2017

@author: zhang
"""


import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
import os 
import scipy.stats as sp
import MDFA as dfa


windowSize =60
RMS_X = []
RMS_Y = []
RMS_Z = []

input_file = "C:\pakinsen\Vicon\WALKER2016\PDsey160502\PDsey160502m01feature.csv"
#input_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Filterdata.csv"

df = pd.read_csv(input_file, sep=",")
#df.interpolate(method='linear', axis=1)



df2 = pd.DataFrame(columns=['AcToeX_rs','AcToeX_rs','AcToeY_rs','AcToe_rs'\
                            'AcHeelX_rs','AcHeelY_rs','AcHeelZ_rs','AcHeel_rs'\
                            'AcHipX_rs','AcHipX_rs','AcHipX_rs','AcHip_rs'\
                            'AcKneelX_rs','AcKneelX_rs','AcKneelX_rs','AcKneel_rs'])




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
scale = 2*n+1

#RW = np.cumsum(df['acToeRX']-df['acToeRX'].mean())
#RW = np.cumsum(df['spToeLX']-df['spToeLX'].mean())
RW= np.cumsum(df['spHeelRX']-df['spHeelRX'].mean())

#plt.subplot(311)
#plot_rms(RW,label='acToeRX signal')
plt.subplot(211)
plot_trends(RW,scale,1,label='signal\namplitude',
            title='A Linear detrending')
plt.legend(['Noise like time-series','Local trend','+/- 1 local RMS'])
plt.subplot(212)
plot_trends(RW,scale,2,label='signal\namplitude',
            title='B Quadratic detrending')

plt.savefig('PDkal160525c02_trends.png')

################


def Residualtrends(X,scale,m=1):
    t = np.arange(X.shape[0])
    segments = np.arange(0,X.shape[0]-scale+1,(scale-1)/2)  # start with 0, step wide is (scale-1)/2， end number is X.shape[0]-scale+1   
    Residual = []
    #RMS =[]
    for i0 in segments:
        i1 = i0+scale
        i2 = i0+(scale-1)/2
        t0 = t[i0:i1]   #full scale
        t2 = t[i0:i2]   #half scale
        C = np.polyfit(t0,X[i0:i1],m)
        fit = np.polyval(C,t2)
        #RMS.append( np.sqrt(((X[i0:i1]-fit)**2).mean()) )
        Residual.append (X[i0:i2] - fit)
    return np.array(Residual).ravel()    #flatten 2D array into 1D array

def trends(X,scale,m=1):
    t = np.arange(X.shape[0])
    segments = np.arange(0,X.shape[0]-scale+1,(scale-1)/2)  # start with 0, step wide is (scale-1)/2， end number is X.shape[0]-scale+1   
    trend = []
    #RMS =[]
    for i0 in segments:
        i1 = i0+scale
        i2 = i0+(scale-1)/2
        t0 = t[i0:i1]   #full scale
        t2 = t[i0:i2]   #half scale
        C = np.polyfit(t0,X[i0:i1],m)
        fit = np.polyval(C,t2)
        #RMS.append( np.sqrt(((X[i0:i1]-fit)**2).mean()) )
        trend.append (fit)
        #print trend
    return np.array(trend).ravel()    #flatten 2D array into 1D array


def comp_Fs(X,scales,m=1):
    RW = np.cumsum(X-X.mean())
    return np.array([ np.sqrt((trends(RW,scale,m)**2).mean()) for scale in scales ])
    
def save(X,Scales,m=1):
    return 0
    
'''
X = np.cumsum(df['acHeelRX']-df['acHeelRX'].mean())
scales = (2**np.arange(4,10)).astype('i4')
RMS2 = dfa.fastRMS(X,scales)
qs = np.arange(-5,5.1,1.0)
np.loglog(scales,dfa.compFq(RMS2,qs),'.-')
'''

scales = np.floor(2.0**np.arange(4,10,0.25)).astype('i4')
#F_si = trends(RW,16,1)
F_xf = comp_Fs(df['spHeelR'],scales,1)
F_si = dfa.compRMS(RW,scales,1).ravel() 
L = 30
 
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
    
    
for filename in os.listdir(directory):
    if filename.endswith(".txt") : 
        input_file = os.path.join(directory, filename)
        filename, file_extension = os.path.splitext(filename)
        output_file = os.path.join(directory,filename+'feature.csv')
        print output_file
        #straight_file = os.path.join(directory,filename+'Straight.csv')
        #turn_file = os.path.join(directory,filename+'Turn.csv')
        #afterturn_file = os.path.join(directory,filename+'After.csv')
        #print input_file
        #print straight_file
        #print turn_file
        #print afterturn_file
        extract(input_file,output_file)
    else:
        continue    
    
    
    

#def stitch_Fs(x,scales,m=1):
#    return np.array([Residualtrends(x,scale,m) for scale in scales])
'''
def trends(X,scale,m=1):
    X = X[:X.shape[0]-X.shape[0]%scale].reshape(-1,scale)    #reshape 成两维数组，每个数组scale个
    i = np.arange(scale,dtype='f8')
    RMS = np.zeros(X.shape[0],'f8')
    for j in xrange(X.shape[0]):
        C = np.polyfit(i,X[j],m)
        fit = np.polyval(C,i)
        RMS[j] = np.sqrt(((X[j]-fit)**2).mean())        
        print RMS
    return RMS

def comp_Fs(X,scales,m=1):
    RW = np.cumsum(X-X.mean())
    return np.array([ np.sqrt((trends(RW,scale,m)**2).mean()) for scale in scales ])
    
scales = np.floor(2.0**np.arange(4,9,0.25)).astype('i4')
F_xf = comp_Fs(df['acHeelRX'],scales,1)

   
def trends(X,scale,m=1):
    t = np.arange(X.shape[0])
    segments = np.arange(0,X.shape[0]-scale+1,(scale-1)/2)  # start with 0, step wide is (scale-1)/2， end number is X.shape[0]-scale+1
    print segments     
    RMS =[]
    for i0 in segments:
        i1 = i0+scale
        i2 = i0+(scale-1)/2
        t0 = t[i0:i1]   #full scale
        t2 = t[i0:i2]   #half scale
        C = np.polyfit(t0,X[i0:i1],m)
        fit = np.polyval(C,t0)
        #print fit
        RMS.append( np.sqrt(((X[i0:i1]-fit)**2).mean()) )
    return np.array(RMS)  
    
def comp_Fs(X,scales,m=1):          #composite all the TRENDS 
    RW2 = np.cumsum(X-X.mean())      ## 偏离mean值
    return np.array([np.sqrt((trends(RW2,scale,m)**2).mean()) for scale in scales ])   #把偏离值的trends，在windows里取几何平均值

#
#RW2 =  np.cumsum(df['acHeelRX']-df['acHeelRX'].mean())
#F_xf = comp_Fs(df['acHeelRX'],scale,1)

def comp_Fs(X,scales,m=1):          #composite all the TRENDS 
    RW2 = np.cumsum(X-X.mean())      ## 偏离mean值
    return np.array([np.sqrt((Residualtrends(RW2,scale,m)**2).mean()) for scale in scales ])   #把偏离值的trends，在windows里取几何平均值

#scales = np.arange(1,1000,4)  
scales = np.floor(2.0**np.arange(4,10,0.25)).astype('i4')
F_xf = stitch_Fs(df['spToeLX'],scales,1)
#F_xf = comp_Fs(df['spToeLX'],scales,1)
F_yf = comp_Fs(df['spToeLY'],scales,1)
F_zf = comp_Fs(df['spToeLZ'],scales,1)


plt.figure(figsize=(10,6))
plt.loglog(scales,F_xf,'ro',label='spToeLX X')
plt.loglog(scales,F_yf,'go',label='spToeLY Y')
plt.loglog(scales,F_zf,'bo',label='spToeLZ Z')
#plt.axis([16,1024,1000,32])
plt.xticks(2**np.arange(4,9),2**np.arange(4,9))
#plt.yticks(2**np.arange(0,6),2**np.arange(0,6))
'''


'''
def plot_logfit(x,y,lc):
    C = np.polyfit(np.log2(x),np.log2(y),1)
    plt.plot(x,2**np.polyval(C,np.log2(x)),lc,label='Slope H = %0.2f'%C[0])

plot_logfit(scales,F_xf,'r')
plot_logfit(scales,F_yf,'g')
plot_logfit(scales,F_zf,'b')
plt.legend(loc='upper left')

plt.savefig('figure5.png')

'''


#plt.axis([16,1024,1000,32])



#print sp.entropy()