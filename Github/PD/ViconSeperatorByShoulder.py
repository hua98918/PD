# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:42:57 2017

@author: Ariel
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 12:01:46 2016

@author: zhang
"""

import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
import os











varianceWindows = 15
windowSize = 10
timeInterval = 0.01   #comes from 100HZ in one second; unit:second
directory = "C:\pakinsen\Vicon\WALKER2016\PDkal160525"
#directory = "C:\pakinsen\Vicon\WALKER2016\PDtob160517"
#C:\pakinsen\Vicon\WALKER2016\PDmil160429
#C:\pakinsen\Vicon\WALKER2016\PDkal160525
#C:\pakinsen\Vicon\WALKER2016\PDLip160509
#C:\pakinsen\Vicon\WALKER2016\PDmil160429 
#C:\pakinsen\Vicon\WALKER2016\PDtob160517
#C:\pakinsen\Vicon\WALKER2016\PDpra160407

'''
input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02feature.csv"
df = pd.read_csv(input_file, sep=",")
print df.head()
df.fillna(0)
mad = lambda x: np.fabs(x - x.mean()).mean()

df['    '].rolling(windowSize).apply(mad).plot(style='k')
df['spToeLY'].rolling(windowSize).apply(mad).plot(style='k')
df['spToeLZ'].rolling(windowSize).apply(mad).plot(style='k)
'''

def extract(input_file,straight_file,turn_file,afterturn_file):
    df = pd.read_csv(input_file, sep=",")
    #print df.head()
    df.fillna(0)
    dn = os.path.dirname(input_file)
    fn, fnExtent = os.path.splitext(os.path.basename(input_file))
    print dn,fn
    
  
    df['stepLZ'] = np.where((df['defToeLX']+df['defToeLY'])>200,300,0)
    df['stepRZ'] = np.where((df['defToeRX']+df['defToeRY'])>200,300,0)
   
    fig4 = plt.figure(figsize=(20, 10))
    ax1 = fig4.add_subplot(211)
    ax1.plot(df[['serial']],df[['spToeLX']].abs(),c='b',label="Left")
    ax1.plot(df[['serial']],df[['spToeRX']].abs(),c='b',label="Right")
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

    turnStartDF1 = df.loc[(df['spToeLX'].abs()>500) & (df['spToeLY'].abs()>500)].head(1)
    turnStartDF2 = df.loc[(df['spToeRX'].abs()>500) & (df['spToeRY'].abs()>500)].head(1)
    startIndex = min(int(turnStartDF1.index.get_values()),int(turnStartDF2.index.get_values()))
    print startIndex
    
    turnEndDF1 = df.loc[(df['spToeLX'].abs()>500) & (df['spToeLY'].abs()>500)].tail(1)
    turnEndDF2 = df.loc[(df['spToeRX'].abs()>500) & (df['spToeRY'].abs()>500)].tail(1)
    endIndex = max(int(turnEndDF1.index.get_values()),int(turnEndDF2.index.get_values()))
    print endIndex
    '''
    turnStartDF1 = df.loc[(df['defToeLX'].abs()>400) & (df['defToeLY'].abs()>400)].head(1)
    turnStartDF2 = df.loc[(df['defToeRX'].abs()>400) & (df['defToeRY'].abs()>400)].head(1)
    startIndex = min(int(turnStartDF1.index.get_values()),int(turnStartDF2.index.get_values()))
    print startIndex
    
    turnEndDF1 = df.loc[(df['defToeLX'].abs()>400) & (df['defToeLY'].abs()>400)].tail(1)
    turnEndDF2 = df.loc[(df['defToeRX'].abs()>400) & (df['defToeRY'].abs()>400)].tail(1)
    endIndex = max(int(turnEndDF1.index.get_values()),int(turnEndDF2.index.get_values()))
    print endIndex
    '''

    with open(straight_file, 'a') as f:
        df[:startIndex].to_csv(f,sep=',',header=True)
        #print df[:startIndex]
        
    with open(turn_file, 'a') as f:
        df[startIndex:endIndex].to_csv(f,sep=',',header=True)
        
    with open(afterturn_file, 'a') as f:
        df[endIndex:].to_csv(f,sep=',',header=True)
    
    #del df   ##need to delete the dataframe from memory then can reuse it next time.
    print 'extrace and devided file done'
  
     
for filename in os.listdir(directory):
    if filename.endswith(".csv") : 
        input_file = os.path.join(directory, filename)
        filename, file_extension = os.path.splitext(filename)
        straight_file = os.path.join(directory,filename+'Straight2.csv')
        turn_file = os.path.join(directory,filename+'Turn2.csv')
        afterturn_file = os.path.join(directory,filename+'After2.csv')
        print input_file
        print straight_file
        print turn_file
        print afterturn_file
        extract(input_file,straight_file,turn_file,afterturn_file)
    else:
        continue
     
