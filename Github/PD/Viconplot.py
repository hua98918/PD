# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 23:03:51 2016

@author: zhang
"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
import numpy as np
import pandas as pd


windowSize = 10
highAccelerometer =  0.3
lowAccelerometer =  0.15
highGyroscope = 16
lowGyroscope =  9
highMagnetometer = 0.015
lowMagnetometer = 0.008

i = 0

input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c01.txt"
output_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c01Feature.csv"


linedf = pd.DataFrame()
newdf = pd.DataFrame()
#read csv into dataframe 
df=pd.read_csv(input_file)
df = pd.read_csv(input_file, sep=",", header = None)
#print df
#fill all theNA as 0
df.fillna(0)

df.columns = ['serial','na','ToeLX','ToeLY', 'ToeLZ','HeelLX', 'HeelLY','HeelLZ','HeelRX','HeelRY','HeelRZ', \
'ToeRX','ToeRY','ToeRZ','kneeLX','kneeLY','kneeLZ','knee1X','knee1Y','knee1Z','hipLX','hipLY','hipLZ', \
'hipRX','hipRY','hipRZ','shRX','shRY','shRZ','shLX','shLY','shLZ','elbowRX','elbowRY','elbowRZ', \
'wristRX','wristRY','wristRZ','walkerLX','walkerLY','walkerLZ','walkerRX','walkerRY','walkerRZ']


fig = plt.figure()

ax1 = fig.add_subplot(311, projection='3d')
ax1.scatter(df[['ToeLX']],df[['ToeLY']],df[['ToeLZ']],label='left side')
ax1.scatter(df[['ToeRX']],df[['ToeRY']],df[['ToeRZ']],c='r',label='left side')
ax1.set_title('Toe Curve')


ax2 = fig.add_subplot(312, projection='3d')
ax2.scatter(df[['HeelLX']],df[['HeelLY']],df[['HeelLZ']])
ax2.scatter(df[['HeelRX']],df[['HeelRY']],df[['HeelRZ']],c='r')
ax2.set_title('Heelcurve')

ax3 = fig.add_subplot(313, projection='3d')
ax3.scatter(df[['shLX']],df[['shLY']],df[['shLZ']])
ax3.scatter(df[['shRX']],df[['shRY']],df[['shRZ']],c='r')
ax3.set_title('shin curve')

'''
ax4 = fig.add_subplot(234, projection='3d')
ax4.scatter(df[['hipLX']],df[['hipLX']],df[['hipLX']])
ax4.scatter(df[['hipRX']],df[['hipRX']],df[['hipRX']],c='r')
ax4.set_title('hip curve')

ax5 = fig.add_subplot(235, projection='3d')
ax5.scatter(df[['elbowRX']],df[['elbowRX']],df[['elbowRX']])
ax5.scatter(df[['wristRX']],df[['wristRX']],df[['wristRX']],c='r')
ax5.set_title('elbow(blue) wrist(red) curve')

ax6 = fig.add_subplot(236, projection='3d')
ax6.scatter(df[['walkerLX']],df[['walkerLX']],df[['walkerLX']])
ax6.scatter(df[['walkerRX']],df[['walkerRX']],df[['walkerRX']],c='r')
ax6.set_title('walker curve')
'''
#ax4 = fig.add_subplot(334, projection='3d')
#ax4.scatter(df[['ToeRX']],df[['ToeRY']],df[['ToeRZ']],label='Toe Right curve')
plt.legend()
plt.show()
