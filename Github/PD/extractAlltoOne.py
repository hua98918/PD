# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:29:29 2016

@author: zhang
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

varianceWindows = 15
windowSize = 10
timeInterval = 0.01   #comes from 100HZ in one second; unit:second
directory = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\Turn"

def extract(input_file,output_file):
    df = pd.read_csv(input_file, sep=",")
    #print df.head()
    df.interpolate(method='linear', axis=0)   #axis =0 fill in by column
    dn = os.path.dirname(input_file)
    fn, fnExtent = os.path.splitext(os.path.basename(input_file))
    df.apply(pd.Series.interpolate)
    print dn,fn
    
    count = len(df.index)
    walking_time = len(df.index)*timeInterval
    #stride_speed = df.at[count,'ToeLX']  - df.at[0,'ToeLX']
    x_walking_distance = df['ToeLX'].iloc[-1]  - df['ToeLX'].iloc[0]   #the last - first
    y_walking_distance = df['ToeLY'].iloc[-1]  - df['ToeLY'].iloc[0]   #the last - first
    walking_speed = abs(x_walking_distance)+abs(y_walking_distance)/walking_time
    print walking_time
    print x_walking_distance
    print y_walking_distance
    print walking_speed
    print df['ToeLZ'].max()
    print df['ToeLZ'].quantile(q=0.9, interpolation='linear')
    
    
    '''
    
    df['stepLZ'] = np.where((df['defToeLX']+df['defToeLY'])>200,300,0)
    df['stepRZ'] = np.where((df['defToeRX']+df['defToeRY'])>200,300,0)
   
    fig4 = plt.figure(figsize=(20, 10))
    ax1 = fig4.add_subplot(211)
    ax1.plot(df[['serial']],df[['spToeLX']].abs(),c='b',label="speed")
    ax1.plot(df[['serial']],df[['defToeLX']],c='r',label="def1")
    ax1.plot(df[['serial']],df[['stepLZ']],c='g',label="step")
    ax1.set_title('step detecttion(left Toe) according to time domain')
    ax1.legend()
    ax2 = fig4.add_subplot(212)
    ax2.plot(df[['serial']],df[['spToeRX']].abs(),c='b',label="speed")
    ax2.plot(df[['serial']],df[['defToeRX']],c='r',label="def1")
    ax2.plot(df[['serial']],df[['stepRZ']],c='g',label="step")
    ax2.set_title('step detecttion(right Toe) according to time domain')
    ax2.legend()
    plt.show()
    plt.savefig( str(dn) + str(fn) +'_stepDetect.png',dpi=72)

    turnStartDF1 = df.loc[(df['spToeLX'].abs()>800) & (df['spToeLY'].abs()>800)].head(1)
    turnStartDF2 = df.loc[(df['spToeRX'].abs()>800) & (df['spToeRY'].abs()>800)].head(1)
    startIndex = min(int(turnStartDF1.index.get_values()),int(turnStartDF2.index.get_values()))
    print startIndex
    
    turnEndDF1 = df.loc[(df['spToeLX'].abs()>800) & (df['spToeLY'].abs()>800)].tail(1)
    turnEndDF2 = df.loc[(df['spToeRX'].abs()>800) & (df['spToeRY'].abs()>800)].tail(1)
    endIndex = max(int(turnEndDF1.index.get_values()),int(turnEndDF2.index.get_values()))
    print endIndex

    '''
for filename in os.listdir(directory):
    if filename.endswith(".csv") : 
        input_file = os.path.join(directory, filename)
        filename, file_extension = os.path.splitext(filename)
        output_name = os.path.join(directory,filename+'All.csv')
        print output_name
        extract(input_file,output_name)
    else:
        continue