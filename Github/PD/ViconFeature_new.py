# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:32:44 2016

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

i = 0


directory = "C:\pakinsen\Vicon\WALKER2016\PDtob160517"
'''
input_file = "C:\pakinsen\Vicon\WALKER2016\PDsey160502\PDsey160502w03.txt"
output_file = "C:\pakinsen\Vicon\WALKER2016\PDsey160502\PDsey160502w03Feature.csv"
straight_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02Before.csv"
turn_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02turn.csv"
afterturn_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c02after.csv"
'''
    
for filename in os.listdir(directory):
    if filename.endswith(".txt") : 
        input_file = os.path.join(directory, filename)
        filename, file_extension = os.path.splitext(filename)
        straight_file = os.path.join(directory,filename+'Straight.csv')
        turn_file = os.path.join(directory,filename+'Turn.csv')
        afterturn_file = os.path.join(directory,filename+'After.csv')
        print input_file
        print straight_file
        print turn_file
        print afterturn_file
        extract(input_file,straight_file,turn_file,afterturn_file)
    else:
        continue


 
def extract(input_file,straight_file,turn_file,afterturn_file):
    df=pd.read_csv(input_file)
    df = pd.read_csv(input_file, sep=",", header = None)
    #print df
    #fill all theNA as 0
    df.fillna(0)
    
    df.columns = ['serial','na','ToeLX','ToeLY', 'ToeLZ','HeelLX', 'HeelLY','HeelLZ','HeelRX','HeelRY','HeelRZ', \
    'ToeRX','ToeRY','ToeRZ','kneeLX','kneeLY','kneeLZ','kneeRX','kneeRY','kneeRZ','hipLX','hipLY','hipLZ', \
    'hipRX','hipRY','hipRZ','shRX','shRY','shRZ','shLX','shLY','shLZ','elbowRX','elbowRY','elbowRZ', \
    'wristRX','wristRY','wristRZ','walkerLX','walkerLY','walkerLZ','walkerRX','walkerRY','walkerRZ']
    
    #caculate the 3 axis speed
    df['spToeLX'] = df['ToeLX'].diff(-1)/timeInterval    #-1 means the period=-1, the latter-former
    df['spToeLY'] = df['ToeLY'].diff(-1)/timeInterval
    df['spToeLZ'] = df['ToeLZ'].diff(-1)/timeInterval
    df['varspToeLX'] = df['spToeLX'].rolling(varianceWindows).var()
    df['varspToeLY'] = df['spToeLY'].rolling(varianceWindows).var()
    df['varspToeLZ'] = df['spToeLZ'].rolling(varianceWindows).var()
    df['spHeelLX'] = df['HeelLX'].diff(-1)/timeInterval
    df['spHeelLY'] = df['HeelLY'].diff(-1)/timeInterval
    df['spHeelLZ'] = df['HeelLZ'].diff(-1)/timeInterval
    df['spHeelRX'] = df['HeelRX'].diff(-1)/timeInterval
    df['spHeelRY']  = df['HeelRY'].diff(-1)/timeInterval
    df['spHeelRZ'] = df['HeelRZ'].diff(-1)/timeInterval
    df['sphipLX'] = df['hipLX'].diff(-1)/timeInterval
    df['sphipLY'] = df['hipLY'].diff(-1)/timeInterval
    df['sphipLZ'] = df['hipLZ'].diff(-1)/timeInterval
    df['sphipRX'] = df['hipRX'].diff(-1)/timeInterval
    df['sphipRY'] = df['hipRY'].diff(-1)/timeInterval
    df['sphipRZ'] = df['hipRZ'].diff(-1)/timeInterval
    df['meanacHeelRX'] = df['spHeelRX'].rolling(windowSize).mean()
    df['varacHeelRX'] = df['spHeelRX'].rolling(windowSize).var()
    df['meanacHeelRY']  = df['spHeelRY'].rolling(windowSize).mean()
    df['varacHeelRY'] = df['spHeelRY'].rolling(windowSize).var()
    df['meancHeelRZ'] = df['spHeelRZ'].rolling(windowSize).mean()
    df['varacHeelRZ'] = df['spHeelRZ'].rolling(windowSize).var()   
    df['spToeRX'] = df['ToeRX'].diff(-1)/timeInterval
    df['spToeRY'] = df['ToeRY'].diff(-1)/timeInterval
    df['spToeRZ'] = df['ToeRZ'].diff(-1)/timeInterval
    df['spkneeLX'] = df['kneeLX'].diff(-1)/timeInterval
    df['spkneeLY'] = df['kneeLY'].diff(-1)/timeInterval
    df['spkneeLZ'] = df['kneeLZ'].diff(-1)/timeInterval
    df['spkneeRX'] = df['kneeRX'].diff(-1)/timeInterval
    df['spkneeRY']= df['kneeRY'].diff(-1)/timeInterval
    df['spkneeRZ'] = df['kneeRZ'].diff(-1)/timeInterval
    df['spshRX'] =  df['shRX'].diff(-1)/timeInterval
    df['spshRY']= df['shRY'].diff()/timeInterval
    df['spshRZ'] = df['shRZ'].diff()/timeInterval
    df['spshLX'] = df['shLX'].diff()/timeInterval
    df['spshLY'] = df['shLY'].diff()/timeInterval
    df['spshLZ'] = df['shLZ'].diff()/timeInterval
    
    #caculate the 3 axis accecelerate
    df['acToeLX'] = df['spToeLX'].diff(-1)/timeInterval    #-1 means the period=-1, the latter-former
    df['acToeLY'] = df['spToeLY'].diff(-1)/timeInterval
    df['acToeLZ'] = df['spToeLZ'].diff(-1)/timeInterval
    df['acHeelLX'] = df['spHeelLX'].diff(-1)/timeInterval
    df['acHeelLY'] = df['spHeelLY'].diff(-1)/timeInterval
    df['acHeelLZ'] = df['spHeelLZ'].diff(-1)/timeInterval
    df['acHeelRX'] = df['spHeelRX'].diff(-1)/timeInterval
    df['acHeelRY']  = df['spHeelRY'].diff(-1)/timeInterval
    df['acHeelRZ'] = df['spHeelRZ'].diff(-1)/timeInterval
    df['acToeRX'] = df['spToeRX'].diff(-1)/timeInterval
    df['acToeRY'] = df['spToeRY'].diff(-1)/timeInterval
    df['acToeRZ'] = df['spToeRZ'].diff(-1)/timeInterval
    df['ackneeLX'] = df['spkneeLX'].diff(-1)/timeInterval
    df['ackneeLY'] = df['spkneeLY'].diff(-1)/timeInterval
    df['ackneeLZ'] = df['spkneeLZ'].diff(-1)/timeInterval
    df['ackneeRX'] = df['spkneeRX'].diff(-1)/timeInterval
    df['ackneeRY']= df['spkneeRY'].diff(-1)/timeInterval
    df['ackneeRZ'] = df['spkneeRZ'].diff(-1)/timeInterval
    df['acshRX'] =  df['spshRX'].diff(-1)/timeInterval
    df['acshRY']= df['spshRY'].diff()/timeInterval
    df['acshRZ'] = df['spshRZ'].diff()/timeInterval
    df['acshLX'] = df['spshLX'].diff()/timeInterval
    df['acshLY'] = df['spshLY'].diff()/timeInterval
    df['acshLZ'] = df['spshLZ'].diff()/timeInterval
    
    
    #caculate the Euclidean distance,speed,accelerate feature 
    df['ToeL'] = np.sqrt(df['ToeLX']**2+df['ToeLY']**2+df['ToeLZ']**2)   
    df['spToeL'] = df['ToeL'].diff(-1)/timeInterval
    df['meanspToeL'] = df['spToeL'].rolling(windowSize).mean() 
    df['stdspToeL'] = df['spToeL'].rolling(windowSize).std() 
    df['varspToeL'] = df['spToeL'].rolling(windowSize).var()
    df['kurspToeL'] = df['spToeL'].rolling(windowSize).kurt() 
    df['skewspToeL'] = df['spToeL'].rolling(windowSize).skew() 
    df['acToeL'] = df['spToeL'].diff(-2)/timeInterval*2
    df['meanacToeL'] = df['acToeL'].rolling(windowSize).mean() 
    df['stdacToeL'] = df['acToeL'].rolling(windowSize).std() 
    df['varacToeL'] = df['acToeL'].rolling(windowSize).var()
    df['kuracToeL'] = df['acToeL'].rolling(windowSize).kurt() 
    df['skewacToeL'] = df['acToeL'].rolling(windowSize).skew() 
    
    df['HeelL'] = np.sqrt(df['HeelLX']**2+df['HeelLY']**2+df['HeelLX']**2)
    df['spHeelL'] = df['HeelL'].diff(-1)/timeInterval
    df['meanspHeelL'] = df['spHeelL'].rolling(windowSize).mean() 
    df['stdspHeelL'] = df['spHeelL'].rolling(windowSize).std() 
    df['varspHeelL'] = df['spHeelL'].rolling(windowSize).var()
    df['kurspHeelL'] = df['spHeelL'].rolling(windowSize).kurt() 
    df['skewspHeelL'] = df['spHeelL'].rolling(windowSize).skew() 
    df['acHeelL'] = df['spHeelL'].diff(-2)/timeInterval*2
    df['meanacHeelL'] = df['acHeelL'].rolling(windowSize).mean() 
    df['stdacHeelL'] = df['acHeelL'].rolling(windowSize).std() 
    df['varacHeelL'] = df['acHeelL'].rolling(windowSize).var()
    df['kuracHeelL'] = df['acHeelL'].rolling(windowSize).kurt() 
    df['skewacHeelL'] = df['acHeelL'].rolling(windowSize).skew() 
    
    df['HeelR'] = np.sqrt(df['HeelRX']**2+df['HeelRY']**2+df['HeelRZ']**2)   
    df['spHeelR'] = df['HeelR'].diff(-1)/timeInterval
    df['meanspHeelR'] = df['spHeelR'].rolling(windowSize).mean() 
    df['stdspHeelR'] = df['spHeelR'].rolling(windowSize).std() 
    df['varspHeelR'] = df['spHeelR'].rolling(windowSize).var()
    df['kurspHeelR'] = df['spHeelR'].rolling(windowSize).kurt() 
    df['skewspHeelR'] = df['spHeelR'].rolling(windowSize).skew() 
    df['acHeelR'] = df['spHeelR'].diff(-2)/timeInterval*2
    df['meanacHeelR'] = df['acHeelR'].rolling(windowSize).mean() 
    df['stdacHeelR'] = df['acHeelR'].rolling(windowSize).std() 
    df['varacHeelR'] = df['acHeelR'].rolling(windowSize).var()
    df['kuracHeelR'] = df['acHeelR'].rolling(windowSize).kurt() 
    df['skewacHeelR'] = df['acHeelR'].rolling(windowSize).skew() 
    
    df['ToeR'] = np.sqrt(df['ToeRX']**2+df['ToeRY']**2+df['ToeRZ']**2)   
    df['spToeR'] = df['ToeR'].diff(-1)/timeInterval
    df['meanspToeR'] = df['spToeR'].rolling(windowSize).mean() 
    df['stdspToeR'] = df['spToeR'].rolling(windowSize).std() 
    df['varspToeR'] = df['spToeR'].rolling(windowSize).var()
    df['kurspToeR'] = df['spToeR'].rolling(windowSize).kurt() 
    df['skewspToeR'] = df['spToeR'].rolling(windowSize).skew() 
    df['acToeR'] = df['spToeR'].diff(-2)/timeInterval*2
    df['meanacToeR'] = df['acToeR'].rolling(windowSize).mean() 
    df['stdacToeR'] = df['acToeR'].rolling(windowSize).std() 
    df['varacToeR'] = df['acToeR'].rolling(windowSize).var()
    df['kuracToeR'] = df['acToeR'].rolling(windowSize).kurt() 
    df['skewacToeR'] = df['acToeR'].rolling(windowSize).skew() 
    
    df['KneeL'] = np.sqrt(df['kneeLX']**2+df['kneeLY']**2+df['kneeLZ']**2) 
    df['spKneeL'] = df['KneeL'].diff(-1)/timeInterval
    df['meanspKneeL'] = df['spKneeL'].rolling(windowSize).mean() 
    df['stdspKneeL'] = df['spKneeL'].rolling(windowSize).std() 
    df['varspKneeL'] = df['spKneeL'].rolling(windowSize).var()
    df['kurspKneeL'] = df['spKneeL'].rolling(windowSize).kurt() 
    df['skewspKneeL'] = df['spKneeL'].rolling(windowSize).skew() 
    df['acKneeL'] = df['spKneeL'].diff(-2)/timeInterval*2
    df['meanacKneeL'] = df['acKneeL'].rolling(windowSize).mean() 
    df['stdacKneeL'] = df['acKneeL'].rolling(windowSize).std() 
    df['varacKneeL'] = df['acKneeL'].rolling(windowSize).var()
    df['kuracKneeL'] = df['acKneeL'].rolling(windowSize).kurt() 
    df['skewacKneeL'] = df['acKneeL'].rolling(windowSize).skew() 
    
    df['kneeR'] = np.sqrt(df['kneeRX']**2+df['kneeRY']**2+df['kneeRZ']**2)  
    df['spKneeR'] = df['kneeR'].diff(-1)/timeInterval
    df['meanspKneeR'] = df['spKneeR'].rolling(windowSize).mean() 
    df['stdspKneeR'] = df['spKneeR'].rolling(windowSize).std() 
    df['varspKneeR'] = df['spKneeR'].rolling(windowSize).var()
    df['kurspKneeR'] = df['spKneeR'].rolling(windowSize).kurt() 
    df['skewspKneeR'] = df['spKneeR'].rolling(windowSize).skew() 
    df['acKneeR'] = df['spKneeR'].diff(-2)/timeInterval*2
    df['meanacKneeR'] = df['acKneeR'].rolling(windowSize).mean() 
    df['stdacKneeR'] = df['acKneeR'].rolling(windowSize).std() 
    df['varacKneeR'] = df['acKneeR'].rolling(windowSize).var()
    df['kuracKneeR'] = df['acKneeR'].rolling(windowSize).kurt() 
    df['skewacKneeR'] = df['acKneeR'].rolling(windowSize).skew() 
    
    
    df['shR'] = np.sqrt(df['ToeRX']**2+df['ToeRY']**2+df['ToeRZ']**2)   
    df['spshR'] = df['shR'].diff(-1)/timeInterval
    df['meanspshR'] = df['spshR'].rolling(windowSize).mean() 
    df['stdspshR'] = df['spshR'].rolling(windowSize).std() 
    df['varspshR'] = df['spshR'].rolling(windowSize).var()
    df['kurspshR'] = df['spshR'].rolling(windowSize).kurt() 
    df['skewspshR'] = df['spshR'].rolling(windowSize).skew() 
    df['acshR'] = df['spshR'].diff(-2)/timeInterval*2
    df['meanacshR'] = df['acshR'].rolling(windowSize).mean() 
    df['stdacshR'] = df['acshR'].rolling(windowSize).std() 
    df['varacshR'] = df['acshR'].rolling(windowSize).var()
    df['kuracshR'] = df['acshR'].rolling(windowSize).kurt() 
    df['skewacshR'] = df['acshR'].rolling(windowSize).skew() 
    
    df['shL'] = np.sqrt(df['ToeRX']**2+df['ToeRY']**2+df['ToeRZ']**2)   
    df['spshL'] = df['shL'].diff(-1)/timeInterval
    df['meanspshL'] = df['spshL'].rolling(windowSize).mean() 
    df['stdspshL'] = df['spshL'].rolling(windowSize).std() 
    df['varspshL'] = df['spshL'].rolling(windowSize).var()
    df['kurspshL'] = df['spshL'].rolling(windowSize).kurt() 
    df['skewspshL'] = df['spshL'].rolling(windowSize).skew() 
    df['acshL'] = df['spshL'].diff(-2)/timeInterval*2
    df['meanacshL'] = df['acshL'].rolling(windowSize).mean() 
    df['stdacshL'] = df['acshL'].rolling(windowSize).std() 
    df['varacshL'] = df['acshL'].rolling(windowSize).var()
    df['kuracshL'] = df['acshL'].rolling(windowSize).kurt() 
    df['skewacshL'] = df['acshL'].rolling(windowSize).skew() 
      
    
    with open(straight_file, 'a') as f:
        df.to_csv(f,sep=',',header=True)

    
    print 'extrace and devided file done'