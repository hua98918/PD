# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:00:48 2016

@author: zhang
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
import numpy as np
import pandas as pd
import os


windowSize = 10
directory = "C:\pakinsen\Vicon\WALKER2016\PDtob160517\\"
#C:\pakinsen\Vicon\WALKER2016\PDmil160429
#C:\pakinsen\Vicon\WALKER2016\PDkal160525
#C:\pakinsen\Vicon\WALKER2016\PDLip160509
#C:\pakinsen\Vicon\WALKER2016\PDmil160429 
#C:\pakinsen\Vicon\WALKER2016\PDtob160517
#C:\pakinsen\Vicon\WALKER2016\PDpra160407

def plotAll(input_file):
    df = pd.read_csv(input_file, sep=",")
    print df
    #fill all theNA as 0
    df.fillna(0)
    
    dn = os.path.dirname(input_file)
    fn, fnExtent = os.path.splitext(os.path.basename(input_file))
    print dn,fn
    
    
    #3D plot for all position 
    fig1 = plt.figure(figsize=(20, 10))
    ax1 = fig1.add_subplot(311, projection='3d')
    ax1.scatter(df[['ToeLX']],df[['ToeLY']],df[['ToeLZ']],label='left side')
    ax1.scatter(df[['ToeRX']],df[['ToeRY']],df[['ToeRZ']],c='r',label='right side')
    ax1.set_xlabel('Toe X axis(cm)')
    ax1.set_ylabel('Toe Y axis(cm)')
    ax1.set_zlabel('Toe Z axis(cm)')
    ax1.legend()
    ax1.set_title('Toe 3D Plot')
    ax2 = fig1.add_subplot(312, projection='3d')
    ax2.scatter(df[['HeelLX']],df[['HeelLY']],df[['HeelLZ']],label='left side')
    ax2.scatter(df[['HeelRX']],df[['HeelRY']],df[['HeelRZ']],c='r',label='right side')
    ax1.set_xlabel('Heel X axis(cm)')
    ax1.set_ylabel('Heel Y axis(cm)')
    ax1.set_zlabel('Heel Z axis(cm)')
    ax2.legend()
    ax2.set_title('Heel 3D Plot')
    ax3 = fig1.add_subplot(313, projection='3d')
    ax3.scatter(df[['shLX']],df[['shLY']],df[['shLZ']],label='left side')
    ax3.scatter(df[['shRX']],df[['shRY']],df[['shRZ']],c='r',label='right side')
    ax3.set_xlabel('shoulder X axis(cm)')
    ax3.set_ylabel('shoulder Y axis(cm)')
    ax3.set_zlabel('shoulder Z axis(cm)')
    ax3.set_title('shoulder 3D Plot')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_3D.png',dpi=72)
    
    
    # 2D Plot for position ToeXYZ
    fig5 = plt.figure(figsize=(20, 10))
    ax1 = fig5.add_subplot(311)
    ax1.scatter(df[['serial']],df[['ToeLX']],label="left side")
    ax1.scatter(df[['serial']],df[['ToeRX']],c='r',label="right side")
    ax1.set_xlabel('Serial')
    ax1.set_ylabel('Toe X axis(cm)')
    ax1.set_title('ToeX position according to time domain')
    ax1.legend()
    ax2 = fig5.add_subplot(312)
    ax2.scatter(df[['serial']],df[['ToeLY']],label="left side")
    ax2.scatter(df[['serial']],df[['ToeRY']],c='r',label="right side")
    ax2.set_title('ToeY position according to time domain')
    ax2.legend()
    ax3 = fig5.add_subplot(313)
    ax3.scatter(df[['serial']],df[['ToeLZ']],label="left side")
    ax3.scatter(df[['serial']],df[['ToeRZ']],c='r',label="right side")
    ax3.set_title('ToeZ position according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_ToeXYZposition.png',dpi=72)
    
    #2D plot for position HeelXYZ 
    fig6 = plt.figure(figsize=(20, 10))
    ax1 = fig6.add_subplot(311)
    ax1.scatter(df[['serial']],df[['HeelLX']],label="left side")
    ax1.scatter(df[['serial']],df[['HeelRX']],c='r',label="right side")
    ax1.set_title('HeelX position  according to time domain')
    ax1.legend()
    ax2 = fig6.add_subplot(312)
    ax2.scatter(df[['serial']],df[['HeelLY']],label="left side")
    ax2.scatter(df[['serial']],df[['HeelRY']],c='r',label="right side")
    ax2.set_title('HeelY position according to time domain')
    ax2.legend()
    ax3 = fig6.add_subplot(313)
    ax3.scatter(df[['serial']],df[['HeelLZ']],label="left side")
    ax3.scatter(df[['serial']],df[['HeelRZ']],c='r',label="right side")
    ax3.set_title('HeelZ position according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_HeelXYZposition.png',dpi=72)
    
    #2D plot for speed ToeXYZ 
    fig2 = plt.figure(figsize=(20, 10))
    ax1 = fig2.add_subplot(311)
    ax1.plot(df[['serial']],df[['spToeLX']],c='b',label="left")
    ax1.plot(df[['serial']],df[['spToeRX']],c='r',label="right")
    ax1.set_title('ToeX speed  according to time domain')
    ax1.legend()
    ax2 = fig2.add_subplot(312)
    ax2.plot(df[['serial']],df[['spToeLY']],c='b',label="left side")
    ax2.plot(df[['serial']],df[['spToeRY']],c='r',label="right side")
    ax2.set_title('ToeY speed according to time domain')
    ax2.legend()
    ax3 = fig2.add_subplot(313)
    ax3.plot(df[['serial']],df[['spToeLZ']],c='b',label="left side")
    ax3.plot(df[['serial']],df[['spToeRZ']],c='r',label="right side")
    ax3.set_title('ToeZ speed according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_ToeXYZspeed.png',dpi=72)
    
    # 2D Plot for speed HeelXYZ
    fig3 = plt.figure(figsize=(20, 10))
    ax1 = fig3.add_subplot(311)
    ax1.plot(df[['serial']],df[['spHeelLX']],c='b',label="left")
    ax1.plot(df[['serial']],df[['spHeelRX']],c='r',label="right")
    ax1.set_title('HeelX speed according to time domain')
    ax1.legend()
    ax2 = fig3.add_subplot(312)
    ax2.plot(df[['serial']],df[['spHeelLY']],c='b',label="left")
    ax2.plot(df[['serial']],df[['spHeelRY']],c='r',label="right")
    ax2.set_title('HeelY speed according to time domain')
    ax2.legend()
    ax3 = fig3.add_subplot(313)
    ax3.plot(df[['serial']],df[['spHeelLZ']],c='b',label="left")
    ax3.plot(df[['serial']],df[['spHeelRZ']],c='r',label="right")
    ax3.set_title('HeelZ speed according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_HeelXYZspeed.png',dpi=72)
    
    
    # 2D Plot for speed KneelXYZ
    fig4 = plt.figure(figsize=(20, 10))
    ax1 = fig4.add_subplot(311)
    ax1.plot(df[['serial']],df[['spkneeLX']],c='b',label="left")
    ax1.plot(df[['serial']],df[['spkneeRX']],c='r',label="right")
    ax1.set_title('KneeLX speed according to time domain')
    ax1.legend()
    ax2 = fig4.add_subplot(312)
    ax2.plot(df[['serial']],df[['spkneeLY']],c='b',label="left")
    ax2.plot(df[['serial']],df[['spkneeRY']],c='r',label="right")
    ax2.set_title('KneelY speed according to time domain')
    ax2.legend()
    ax3 = fig4.add_subplot(313)
    ax3.plot(df[['serial']],df[['spkneeLZ']],c='b',label="left")
    ax3.plot(df[['serial']],df[['spkneeRZ']],c='r',label="right")
    ax3.set_title('KneelZ speed according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_KneelXYZspeed.png',dpi=72)
    
    # 2D Plot for speed HipXYZ
    fig4 = plt.figure(figsize=(20, 10))
    ax1 = fig4.add_subplot(311)
    ax1.plot(df[['serial']],df[['sphipLX']],c='b',label="left")
    ax1.plot(df[['serial']],df[['sphipRX']],c='r',label="right")
    ax1.set_title('HipX speed cm per sec according to time domain')
    ax1.legend()
    ax2 = fig4.add_subplot(312)
    ax2.plot(df[['serial']],df[['sphipLY']],c='b',label="left")
    ax2.plot(df[['serial']],df[['sphipRY']],c='r',label="right")
    ax2.set_title('HipY speed cm per sec according to time domain')
    ax2.legend()
    ax3 = fig4.add_subplot(313)
    ax3.plot(df[['serial']],df[['sphipLZ']],c='b',label="left")
    ax3.plot(df[['serial']],df[['sphipRZ']],c='r',label="right")
    ax3.set_title('HipZ speed cm per sec according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_HipXYZspeed.png',dpi=72)
 
    #shoulder speed plot
    fig4 = plt.figure(figsize=(20, 10))
    ax1 = fig4.add_subplot(311)
    ax1.plot(df[['serial']],df[['spshLX']],c='b',label="left")
    ax1.plot(df[['serial']],df[['spshRX']],c='r',label="right")
    ax1.set_title('ShoulderX speed according to time domain')
    ax1.legend()
    ax2 = fig4.add_subplot(312)
    ax2.plot(df[['serial']],df[['spshLY']],c='b',label="left")
    ax2.plot(df[['serial']],df[['spshRY']],c='r',label="right")
    ax2.set_title('ShoulderY speed according to time domain')
    ax2.legend()
    ax3 = fig4.add_subplot(313)
    ax3.plot(df[['serial']],df[['spshLZ']],c='b',label="left")
    ax3.plot(df[['serial']],df[['spshRZ']],c='r',label="right")
    ax3.set_title('ShoulderZ speed according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_ShouldXYZspeed.png',dpi=72)

     #shoulder speed plot
    fig4 = plt.figure(figsize=(20, 10))
    ax1 = fig4.add_subplot(311)
    ax1.plot(df[['serial']],df[['defToeLX']],c='b',label="left")
    ax1.plot(df[['serial']],df[['defToeRX']],c='r',label="right")
    ax1.set_title('Toe X speed according to time domain')
    ax1.legend()
    ax2 = fig4.add_subplot(312)
    ax2.plot(df[['serial']],df[['defToeLY']],c='b',label="left")
    ax2.plot(df[['serial']],df[['defToeRY']],c='r',label="right")
    ax2.set_title('Toe Y speed according to time domain')
    ax2.legend()
    ax3 = fig4.add_subplot(313)
    ax3.plot(df[['serial']],df[['defToeLZ']],c='b',label="left")
    ax3.plot(df[['serial']],df[['defToeRZ']],c='r',label="right")
    ax3.set_title('Toe Z speed according to time domain')
    ax3.legend()
    plt.savefig( str(dn) + str(fn) +'_DefToeXYZspeed.png',dpi=72)
  
    #plt.legend()
    #plt.show()
   

for filename in os.listdir(directory):
    if filename.endswith(".csv") : 
        input_file = os.path.join(directory, filename)
        filename, file_extension = os.path.splitext(filename)
        #straight_file = os.path.join(directory,filename+'Straight.csv')
        #turn_file = os.path.join(directory,filename+'Turn.csv')
        #afterturn_file = os.path.join(directory,filename+'After.csv')
        #print input_file
        #print straight_file
        #print turn_file
        #print afterturn_file
        plotAll(input_file)
    else:
        continue




