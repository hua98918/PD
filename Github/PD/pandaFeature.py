# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 21:01:38 2016

@author: zhang
"""
import matplotlib.pyplot as plt
import os
import datetime
import numpy as np
import pandas as pd
import scipy.stats as st 
import scipy.signal as sig

ver=pd.read_csv("C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Filterdata.csv")
pd.set_option('display.max_columns', 164) 
#output_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\Featuredata.csv"


print len(ver)
#print ver.shape
#print ver.columns
#print ver.describe()


window_number = len(ver)/82
print window_number 
i=0
while(i <= window_number):
    window_begin = i*82
    window_end = window_begin+164
    #print window_begin,window_end
    window = ver[window_begin:window_end]
    #print window.describe()
    print st.entropy(window)    
    i += 1


    '''
    with open(output_file, 'a') as f:
       #window.describe().to_csv(f, sep='\t',header=True)
        print st.entropy(window)
    i += 1
    '''  


    

#print st.entropy(ver)   #entropy what is mean???

#print pd.crosstab(ver['GyroscopeX'],ver['GyroscopeY'])

'''
window = sig.get_window('boxcar',164)
print window
plt.plot(window)

number = sig.resample(ver,164,t='Serial',axis=10,)
print number
plt.plot(number)
'''
