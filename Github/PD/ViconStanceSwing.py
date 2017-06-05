# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 23:26:16 2017

@author: zhang
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from scipy.signal import argrelextrema
import scipy.fftpack
import peakutils
#from oct2py import octave



windowSize = 256
halfWindow = 128
timeInterval = 0.01   #comes from 100HZ in one second; unit:second
dn = "C:\pakinsen\Vicon\WALKER2016\PDLip160509"
#dn = PDkal160525  PDLip160509   PDmil160429 PDpra160407  PDsey160502 PDtob160517

#input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c04feature.csv"
#output_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c04StanceSwing.csv"
#fn = "PDkal160525c04"
#print df.head()


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
  
    
	
def fftfilter(x,y):
    N = 5
    
    w = scipy.fftpack.rfft(y)
    f = scipy.fftpack.rfftfreq(N, x[1]-x[0])
    spectrum = w**2
    
    cutoff_idx = spectrum < (spectrum.max()/15)   
    w2 = w.copy()
    w2[cutoff_idx] = 0
    
    y2 = scipy.fftpack.irfft(w2)
    plt.plot(x,y)
    plt.plot(x,y2, color='red')
    plt.show()
    return y2


#octave.eval("pkg load signal")
#(peaks, indexes) = octave.findpeaks(df['HeelLZ'], 'DoubleSided', 'MinPeakHeight', 0.04, 'MinPeakDistance', 100, 'MinPeakWidth', 0)

'''
from peakdetect import peakdetect
cb = df['HeelLZ'].as_matrix()
peaks = peakdetect(cb, lookahead=100)
'''

def helperValley(a,b):
    ''' help eliminate the one valleys/peaks between two peaks/valleys
    Only one valley between one peaks.  eg: helperValler(peak,Valley)
    Only one peak between one Valley.  eg: helperValler(Valley,peak)
    '''
    for i in range(len(a)-1):
        h1=a[i]
        h2=a[i+1] 
        for j in range(len(b)-1):
            if b[j]>h1 and b[j]<h2 and b[j+1]<h2:
                #print 10000 + b[j]
                del b[j+1]
                break
    return b
                
def stepBegin(a,b):
    '''we definethe beginner should be one of the peak,not valley.
        so compare the beginning of th peak list and valley list then eliminate all the valleys before the peak
        a is peak; b is valley eg: helperValler(peak，Valleyy)
    '''
    for i in range(len(b)-1):
        if b[i]<=a[0]:
            del b[i]
            break
    return b
        

def findpeaks(df):
    '''return 4 list of peaks
        first smooth the data
        then find extrema
        last elminator some of the repeated lower point
    '''
    highL= list()
    lowerL=list()
    highR= list()
    lowerR=list()
    fig1 = plt.figure(figsize=(20,10))
    ax1 = fig1.add_subplot(311)
    ax1.plot(df['serial'],df['HeelLZ'].as_matrix())
    ax1.plot(df['serial'],df['HeelRZ'].as_matrix())
    xL = smooth(df['HeelLZ'].as_matrix(),window_len=20,window='hanning')   # smooth the data
    xR = smooth(df['HeelRZ'].as_matrix(),window_len=20,window='hanning')   # smooth the data
    #x = savitzky_golay(df['HeelLZ'].as_matrix(),window_size=61,order=1)
    ax1.plot(df['serial'],xL, color='red')
    ax1.plot(df['serial'],xR, color='red')
    ax1.set_title('Smoothed Vertical Heel spacial')
    #ax1.set_xlabel('Time(10ms)')
    #ax1.set_ylabel('cm')
    plt.show()
    
    ax2 = fig1.add_subplot(312)
    #indices = peakutils.indexes(xL, thres=0.02/max(cb), min_dist=0.1)    #return out time indices, way 1: pind the peak(peakutils) 
    higherPeakL = argrelextrema(xL, np.greater)    # way2: find the peak(scipy.signal )
    lowerVallyL = argrelextrema(xL, np.less)
    #filter the higherPeakL
    for j in higherPeakL[0]:    #select the Peak bigger than 0.75 quantile
        #print j, df['HeelLZ'].iloc[j],df['HeelLZ'].quantile(.75)
        if df['HeelLZ'].iloc[j] > df['HeelLZ'].quantile(.75):
            highL.append(j) 
    #filter the lowerVally
    temp = lowerVallyL[0][0]
    lowerL.append(temp) 
    for i in lowerVallyL[0]:    
        if (i-temp) > 80 :
            lowerL.append(i) 
            temp =i
    lowerL = helperValley(highL,lowerL)
    lowerL= stepBegin(highL,lowerL)
    highL = helperValley(lowerL,highL)  
    higherPeakR = argrelextrema(xR, np.greater)    # way2: find the peak(scipy.signal )
    lowerVallyR = argrelextrema(xR, np.less)
    for j in higherPeakR[0]:
        #print j, df['HeelRZ'].iloc[j],df['HeelRZ'].quantile(.75)
        if df['HeelRZ'].iloc[j] > df['HeelRZ'].quantile(.75):
            highR.append(j) 
    #filter the lowerVally  
    temp = lowerVallyR[0][0]
    lowerR.append(temp) 
    for i in lowerVallyR[0]:    #select the Peak bigger than 0.75 quantile
        if (i-temp) > 80 :
            lowerR.append(i) 
            temp =i
    lowerR = helperValley(highR,lowerR)
    lowerR= stepBegin(highR,lowerR)
    highR = helperValley(lowerR,highR)  
    #markers_on = list(set(markers_high + markers_low))
    ax2.plot(df['serial'], xL, '-bD', markevery=lowerL, label='Left Heel' )
    ax2.plot(df['serial'], xL, '-bD', markevery=highL )
    ax2.plot(df['serial'], xR, '-rD', markevery=lowerR, label='Right Heel' )
    ax2.plot(df['serial'], xR, '-rD', markevery=highR )
    ax2.set_title('Vertical Heel Peaks and Valleys')
    #ax2.set_xlabel('Time(10ms)')
    #ax2.set_ylabel('cm')
    ax2.legend()
    plt.show()
    
    ax3 = fig1.add_subplot(313)
    ax3.plot(df['serial'], df['spHeelLX'], '-bD', markevery=lowerL, label='Left Heel' )
    ax3.plot(df['serial'], df['spHeelLX'], '-bD', markevery=highL )
    ax3.plot(df['serial'], df['spHeelRX'], '-rD', markevery=lowerR, label='Right Heel' )
    ax3.plot(df['serial'], df['spHeelRX'], '-rD', markevery=highR )
    ax2.set_title('Heel X axis speed')
    #ax2.set_xlabel('Time(10ms)')
    #ax2.set_ylabel('cm/ms')
    ax3.legend()
    plt.show()
    plt.savefig( str(dn) + str(fn) +'_SwingStance.png',dpi=144)
    return highL,lowerL,highR,lowerR



#print LeftHigh, LeftLower,RightHigh,RightLower

def getGCT(a):
    gct = list()
    for i in range(len(a)):
        if i<len(a)-1:
            gct.append(0.01*(a[i+1]-a[i]))
    return gct

def getStance(a,b):
    stance = list()
    for i in range(min(len(a),len(b))):
        stance.append(a[i]-b[i])
    return stance

def getSwing(a,b):       
    swing = list()
    start_position = 0
    if abs(a[0]-b[0])>100 or (a[0]<b[0]):
        start_position = 1
    for i in range(min(len(a),len(b)) - start_position):
        swing.append(abs(0.01*(a[start_position+i]-b[i])))
    return swing

def getIDS(a,b):     
    '''There should have another side lower before the peak.
    For example, find right feet IDS. there should have one left valley before right peak 
    if there is no left valley before right peak, left valley and right peak move forwad 1 position
    '''
    ids = list()
    if abs(a[0]-b[0])>100 or (a[0]<b[0]):
        del a[0]
        #start_position = 1
    for i in range(min(len(a),len(b))):
        ids.append(abs(0.01*(a[i]-b[i])))
        #print ids
    return ids
    
def getStideLength(a,df):       
    StideLength = list()
    for i in range(len(a)):
        if i<len(a)-1:
            StideLength.append(0.1*(abs(df.iloc[a[i+1]] - df.iloc[a[i]])))
    return StideLength

def getStideVelocity(a,b):       
    velocity = list()
    for i in range(min(len(a),len(b))):
        velocity.append(a[i]/b[i])
    return velocity


def getStideHeight(a,b,df):       
    StideHeight = list()
    for i in range(min(len(a),len(b))):
        StideHeight.append(0.1*(abs(df.iloc[a[i]] - df.iloc[b[i]])))
        #print StideHeight
    return StideHeight



'''
(LeftHigh,LeftLower,RightHigh,RightLower)=findpeaks(df)
df2 = pd.DataFrame(columns=['LeftGCT'])
df3 = pd.DataFrame(columns=['RightGCT'])
df4 = pd.DataFrame(columns=['LeftStance'])
df5 = pd.DataFrame(columns=['RightStance'])
df6 = pd.DataFrame(columns=['LeftSwing'])
df7 = pd.DataFrame(columns=['RightSwing'])
df8 = pd.DataFrame(columns=['LeftIDS'])
df9 = pd.DataFrame(columns=['RightIDS'])   
df10 = pd.DataFrame(columns=['XStideLengthL']) 
df11 = pd.DataFrame(columns=['XStideLengthR']) 
df12 = pd.DataFrame(columns=['YStideLengthL']) 
df13 = pd.DataFrame(columns=['YStideLengthR']) 
df14 = pd.DataFrame(columns=['XStideVelocityL']) 
df15 = pd.DataFrame(columns=['XStideVelocityR']) 
df16 = pd.DataFrame(columns=['YStideVelocityL']) 
df17 = pd.DataFrame(columns=['YStideVelocityR']) 
df18 = pd.DataFrame(columns=['ZStideHeightL']) 
df19 = pd.DataFrame(columns=['ZStideHeightR']) 

df2['LeftGCT'] = getGCT(LeftHigh)
df3['RightGCT'] = getGCT(RightHigh)
df4['LeftStance'] = getStance(getGCT(LeftHigh),getSwing(LeftLower,LeftHigh))
df5['RightStance'] = getStance(getGCT(RightHigh),getSwing(RightLower,RightHigh))
df6['LeftSwing'] = getSwing(LeftLower,LeftHigh)
df7['RightSwing'] = getSwing(RightLower,RightHigh)
df8['LeftIDS'] = getIDS(LeftHigh,RightLower)
df9['RightIDS'] = getIDS(RightHigh,LeftLower)
df10['XStideLengthL'] = getStideLength(LeftHigh,df['HeelLX'])
df11['XStideLengthR'] = getStideLength(RightHigh,df['HeelLX'])
df12['YStideLengthL'] = getStideLength(LeftHigh,df['HeelLY'])
df13['YStideLengthR'] = getStideLength(RightHigh,df['HeelLY'])
df14['XStideVelocityL'] = getStideVelocity(df10['XStideLengthL'],df2['LeftGCT'])
df15['XStideVelocityR'] = getStideVelocity(df11['XStideLengthR'],df3['RightGCT'])
df16['YStideVelocityL'] = getStideVelocity(df12['YStideLengthL'],df2['LeftGCT'])
df17['YStideVelocityR'] = getStideVelocity(df13['YStideLengthR'],df3['RightGCT'])
df18['ZStideHeightL'] = getStideHeight(LeftHigh,LeftLower,df['HeelLZ'])
df19['ZStideHeightR'] = getStideHeight(LeftHigh,LeftLower,df['HeelRZ'])

new_df = pd.concat([df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19], axis=1)

with open(output_file, 'a') as f:
    #df.to_csv(f,sep=',',header=True)
    new_df.to_csv(f,sep=',',header=True)  
print 'extrace Feature done'

'''

def extract(input_file, output_file):
    
    df = pd.read_csv(input_file, sep=",")
    
    (LeftHigh,LeftLower,RightHigh,RightLower)=findpeaks(df)
    
    df2 = pd.DataFrame(columns=['LeftGCT'])
    df3 = pd.DataFrame(columns=['RightGCT'])
    df4 = pd.DataFrame(columns=['LeftStance'])
    df5 = pd.DataFrame(columns=['RightStance'])
    df6 = pd.DataFrame(columns=['LeftSwing'])
    df7 = pd.DataFrame(columns=['RightSwing'])
    df8 = pd.DataFrame(columns=['LeftIDS'])
    df9 = pd.DataFrame(columns=['RightIDS'])   
    df10 = pd.DataFrame(columns=['XStideLengthL']) 
    df11 = pd.DataFrame(columns=['XStideLengthR']) 
    df12 = pd.DataFrame(columns=['YStideLengthL']) 
    df13 = pd.DataFrame(columns=['YStideLengthR']) 
    df14 = pd.DataFrame(columns=['XStideVelocityL']) 
    df15 = pd.DataFrame(columns=['XStideVelocityR']) 
    df16 = pd.DataFrame(columns=['YStideVelocityL']) 
    df17 = pd.DataFrame(columns=['YStideVelocityR']) 
    df18 = pd.DataFrame(columns=['ZStideHeightL']) 
    df19 = pd.DataFrame(columns=['ZStideHeightR']) 
    
    df2['LeftGCT'] = getGCT(LeftHigh)
    df3['RightGCT'] = getGCT(RightHigh)
    df4['LeftStance'] = getStance(getGCT(LeftHigh),getSwing(LeftLower,LeftHigh))
    df5['RightStance'] = getStance(getGCT(RightHigh),getSwing(RightLower,RightHigh))
    df6['LeftSwing'] = getSwing(LeftLower,LeftHigh)
    df7['RightSwing'] = getSwing(RightLower,RightHigh)
    df8['LeftIDS'] = getIDS(LeftHigh,RightLower)
    df9['RightIDS'] = getIDS(RightHigh,LeftLower)
    df10['XStideLengthL'] = getStideLength(LeftHigh,df['HeelLX'])
    df11['XStideLengthR'] = getStideLength(RightHigh,df['HeelLX'])
    df12['YStideLengthL'] = getStideLength(LeftHigh,df['HeelLY'])
    df13['YStideLengthR'] = getStideLength(RightHigh,df['HeelLY'])
    df14['XStideVelocityL'] = getStideVelocity(df10['XStideLengthL'],df2['LeftGCT'])
    df15['XStideVelocityR'] = getStideVelocity(df11['XStideLengthR'],df3['RightGCT'])
    df16['YStideVelocityL'] = getStideVelocity(df12['YStideLengthL'],df2['LeftGCT'])
    df17['YStideVelocityR'] = getStideVelocity(df13['YStideLengthR'],df3['RightGCT'])
    df18['ZStideHeightL'] = getStideHeight(LeftHigh,LeftLower,df['HeelLZ'])
    df19['ZStideHeightR'] = getStideHeight(RightHigh,RightLower,df['HeelRZ'])
    
    new_df = pd.concat([df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19], axis=1)

    with open(output_file, 'a') as f:
        #df.to_csv(f,sep=',',header=True)
        new_df.to_csv(f,sep=',',header=True)  
    print 'extrace Feature done'



for filename in os.listdir(dn):
    if filename.endswith("feature.csv") : 
        input_file = os.path.join(dn, filename)
        fn, file_extension = os.path.splitext(filename)
        output_file = os.path.join(dn,fn+'SwingStance.csv')
        print output_file
        extract(input_file,output_file)
    else:
        continue

#x = fftfilter(df['serial'],df['HeelLZ'].as_matrix())
#x = savitzky_golay(df['HeelLZ'].as_matrix(), 51, 3)
#x= df['HeelLZ'].as_matrix()
#for local maxima
#print argrelextrema(x, np.greater)
# for local minima
#print argrelextrema(x, np.less)

