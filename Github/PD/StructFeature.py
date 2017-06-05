# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 22:07:04 2016

@author: zhang
"""

import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
import scipy.stats as st 
import scipy.signal as sig

windowSize = 10
highAccelerometer =  0.4
lowAccelerometer =  0.15
highGyroscope = 15
lowGyroscope =  8
highMagnetometer = 0.015
lowMagnetometer = 0.008
i = 0


#output_file = "C:\pakinsen\IMU\DataWithTrials\SubjectData\User01\Foot\Straight\Trial01\StructureFeature.csv"


def extract(input_file,output_file):
    linedf = pd.DataFrame()
    newdf = pd.DataFrame()
    #read csv into dataframe 
    df=pd.read_csv(input_file)
    
    for i in df.ix[:,'Serial']:
        s1 = pd.Series([df.ix[i,'Serial']])
        s2 = pd.Series([np.sqrt(df.ix[i,'AccelerometerX']**2+df.ix[i,'AccelerometerY']**2+df.ix[i,'AccelerometerZ']**2)])
        s3 = pd.Series([np.sqrt(df.ix[i,'GyroscopeX']**2+df.ix[i,'GyroscopeY']**2+df.ix[i,'GyroscopeZ']**2)])     
        s4 = pd.Series([np.sqrt(df.ix[i,'MagnetometerX']**2+df.ix[i,'MagnetometerY']**2+df.ix[i,'MagnetometerZ']**2)])      
        #d = {'serial' : pd.Series([df.ix[i,'Serial']]) ,'two' : pd.Series([np.sqrt(df.ix[i,'AccelerometerX']**2+df.ix[i,'AccelerometerY']**2+df.ix[i,'AccelerometerZ']**2)])}        
        #newdf = pd.DataFrame(d)
        linedf = pd.concat([s1,s2,s3,s4],axis=1)  #axis=1 means concat to colume, axis =0 means contact to lines; concat 2 series to a 1 dataFrame
        newdf = newdf.append(linedf)    
        i += 1
    #reset index from 0 to sequential number
    newdf = newdf.reset_index(drop=True)    
    #print newdf
    
    #using pd rolling windows to calculate the mean and local variance
    meanAccelerometer = newdf[newdf.columns[1:2]].rolling(windowSize).mean() 
    varAccelerometer = np.sqrt(newdf[newdf.columns[1:2]].rolling(windowSize).var())
    kurtAccelerometer = newdf[newdf.columns[1:2]].rolling(windowSize).kurt() 
    skewAccelerometer = newdf[newdf.columns[1:2]].rolling(windowSize).skew() 
    stdAccelerometer = newdf[newdf.columns[1:2]].rolling(windowSize).std() 
    #covAccelerometer = newdf[newdf.columns[1:2]].rolling(windowSize).cov() 
    #corrAccelerometer = newdf[newdf.columns[1:2]].rolling(windowSize).corr() 
    
    meanGyroscope =  newdf[newdf.columns[2:3]].rolling(windowSize).mean() 
    varGyroscope = np.sqrt(newdf[newdf.columns[2:3]].rolling(windowSize).var()) 
    kurtGyroscope =  newdf[newdf.columns[2:3]].rolling(windowSize).kurt() 
    skewGyroscope =  newdf[newdf.columns[2:3]].rolling(windowSize).skew() 
    stdGyroscope = newdf[newdf.columns[2:3]].rolling(windowSize).std() 
    
    meanMagnetometer =  newdf[newdf.columns[3:4]].rolling(windowSize).mean() 
    varMagnetometer = np.sqrt(newdf[newdf.columns[3:4]].rolling(windowSize).var()) 
    kurtMagnetometer =  newdf[newdf.columns[3:4]].rolling(windowSize).kurt() 
    skewMagnetometer =  newdf[newdf.columns[3:4]].rolling(windowSize).skew() 
    stdMagnetometer = newdf[newdf.columns[3:4]].rolling(windowSize).std() 
    
    meandf = pd.concat([meanAccelerometer,meanGyroscope,meanMagnetometer],axis=1)
    variancedf = pd.concat([varAccelerometer,varGyroscope,varMagnetometer],axis=1)
    kurtdf = pd.concat([kurtAccelerometer,kurtGyroscope,kurtMagnetometer],axis=1)
    skewdf = pd.concat([skewAccelerometer,skewGyroscope,skewMagnetometer],axis=1)
    stddf = pd.concat([stdAccelerometer,stdGyroscope,stdMagnetometer],axis=1)
    
    finaldf = pd.concat([newdf,meandf,variancedf,kurtdf,skewdf,stddf],axis=1)
    #set column name for plot to handle them
    finaldf.columns = ['serial', 'Accelerometer', 'Gyroscope', 'Magnetometer','meanAccelerometer','meanGyroscope','meanMagnetometer','varAccelerometer','varGyroscope','varMagnetometer','kurtAccelerometer','kurtGyroscope','kurtMagnetometer','skewAccelerometer','skewGyroscope','skewMagnetometer','stdAccelerometer','stdGyroscope','stdMagnetometer']
    #print finaldf
    with open(output_file, 'a') as f:
        finaldf.to_csv(f,sep=',',header=True)
    
    
    fig = plt.figure() 
    
    ax1 = fig.add_subplot(311) 
    #ax1 = plt.subplot2grid((3,3), (0, 0), rowspan=1, colspan=4)
    ax1.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[1:2]], label='Accelerometer')
    ax1.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[4:5]], label='Mean Accelerometer')
    ax1.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[7:8]], label='Local Variance Accelerometer')
    #detect the swing phase with high acceleration
    swingdf = finaldf.copy()
    #swingdf['varAccelerometer'].clip_upper(highAccelerometer)
    swingdf['varAccelerometer'] = np.where(swingdf['varAccelerometer'] > highAccelerometer, 0.1,0)
    #swingdf[swingdf['varAccelerometer'] > highAccelerometer] = 0.4
    #swingdf[swingdf['varAccelerometer'] <= highAccelerometer] = 0
    ax1.plot(swingdf[swingdf.columns[0:1]], swingdf[swingdf.columns[7:8]], label='Swing')
    #detect the stance phase with lower acceleration
    stancedf = finaldf.copy()
    #stancedf['varAccelerometer'].clip_upper(lowAccelerometer)
    stancedf['varAccelerometer'] = np.where(stancedf['varAccelerometer'] <= lowAccelerometer,0.04,0)
    #stancedf[stancedf['varAccelerometer'] < lowAccelerometer] = 0.1
    #stancedf[stancedf['varAccelerometer'] >= lowAccelerometer] = 0
    ax1.plot(stancedf[stancedf.columns[0:1]], stancedf[stancedf.columns[7:8]], label='Stance')
    
    #main.axes.xaxis.set_ticklabels([])[]
    plt.title('Step detaection with Acceleration reading')
    plt.legend() 
    
    
    ####### Gyroscope#####
    ax2 = fig.add_subplot(312) 
    #ax2 = plt.subplot2grid((3,3), (0, 0), rowspan=2, colspan=4)
    ax2.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[2:3]], label='Gyroscope')
    ax2.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[5:6]], label='Mean Gyroscope')
    ax2.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[8:9]], label='Local Variance Gyroscope')
    #detect the swing phase with high acceleration
    swingdf = finaldf.copy()
    #swingdf['varAccelerometer'].clip_upper(highAccelerometer)
    swingdf['varGyroscope'] = np.where(swingdf['varGyroscope'] > highGyroscope, 10,0)
    #swingdf[swingdf['varAccelerometer'] > highAccelerometer] = 0.4
    #swingdf[swingdf['varAccelerometer'] <= highAccelerometer] = 0
    ax2.plot(swingdf[swingdf.columns[0:1]], swingdf[swingdf.columns[8:9]], label='Swing')
    
    #detect the stance phase with lower acceleration
    stancedf = finaldf.copy()
    #stancedf['varAccelerometer'].clip_upper(lowAccelerometer)
    stancedf['varGyroscope'] = np.where(stancedf['varGyroscope'] <= lowGyroscope,5,0)
    #stancedf[stancedf['varAccelerometer'] < lowAccelerometer] = 0.1
    #stancedf[stancedf['varAccelerometer'] >= lowAccelerometer] = 0
    ax2.plot(stancedf[stancedf.columns[0:1]], stancedf[stancedf.columns[8:9]], label='Stance')
    
    #main.axes.xaxis.set_ticklabels([])[]
    plt.title('Step detaection with Gyroscope reading')
    plt.legend()
    
    ####### Magnetometer#####
    ax3 = fig.add_subplot(313) 
    #ax2 = plt.subplot2grid((3,3), (0, 0), rowspan=2, colspan=4)
    ax3.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[3:4]], label='Magnetometer')
    ax3.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[6:7]], label='Mean Magnetometer')
    ax3.plot(finaldf[finaldf.columns[0:1]], finaldf[finaldf.columns[9:10]], label='Local Variance Magnetometer')
    #detect the swing phase with high Magnetometer
    swingdf = finaldf.copy()
    #swingdf['varAccelerometer'].clip_upper(highAccelerometer)
    swingdf['varMagnetometer'] = np.where(swingdf['varMagnetometer'] > highMagnetometer, 0.01,0)
    #swingdf[swingdf['varAccelerometer'] > highAccelerometer] = 0.4
    #swingdf[swingdf['varAccelerometer'] <= highAccelerometer] = 0
    ax3.plot(swingdf[swingdf.columns[0:1]], swingdf[swingdf.columns[9:10]], label='Swing')
    
    #detect the stance phase with lower Magnetometer
    stancedf = finaldf.copy()
    stancedf['varMagnetometer'] = np.where(stancedf['varMagnetometer'] <= lowMagnetometer,0.005,0)
    ax3.plot(stancedf[stancedf.columns[0:1]], stancedf[stancedf.columns[9:10]], label='Stance')
    
    plt.title('Step detaection with Magnetometer reading')
    plt.legend()
    
    plt.tight_layout()
    plt.show()



   
def getParser():
    usage="""
    {program} input_file output_file"""   
    parser =argparse.ArgumentParser(description="extract Struct Feature from filtered data", usage=usage)
    parser.add_argument("input_file",help="input file name")
    parser.add_argument("output_file",help="output file name")
    args= parser.parse_args()
    #print args
    return args


def main():
    args = getParser()
    print(args.input_file)
    extract(args.input_file,args.output_file)

if __name__ == "__main__":
    main()


  