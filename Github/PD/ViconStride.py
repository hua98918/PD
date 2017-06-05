# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:18:09 2016

@author: zhang
"""



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
import numpy as np
import pandas as pd


windowSize = 10
highSpeed =  0.3
lowSpeed =  0.15
highGyroscope = 16
lowGyroscope =  9
highMagnetometer = 0.015
lowMagnetometer = 0.008

i = 0
step =1

#input_file = "C:\pakinsen\Vicon\WALKER2016\PDmil160429\PDmil160429c01.txt"
input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525c03Feature.csv"


linedf = pd.DataFrame()
newdf = pd.DataFrame()
#read csv into dataframe 

df = pd.read_csv(input_file, sep=",", header = 0)
#print df
#fill all theNA as 0
df.fillna(0)
'''
df.columns = ['serial','origSerial','na','ToeLX','ToeLY', 'ToeLZ','HeelLX', 'HeelLY','HeelLZ','HeelRX','HeelRY','HeelRZ', \
'ToeRX','ToeRY','ToeRZ','kneeLX','kneeLY','kneeLZ','knee1X','knee1Y','knee1Z','hipLX','hipLY','hipLZ', \
'hipRX','hipRY','hipRZ','shRX','shRY','shRZ','shLX','shLY','shLZ','elbowRX','elbowRY','elbowRZ', \
'wristRX','wristRY','wristRZ','walkerLX','walkerLY','walkerLZ','walkerRX','walkerRY','walkerRZ',\
'spToeLX','spToeLY','spToeLZ','varspToeLX','varspToeLY','varspToeLZ','spHeelLX','spHeelLY','spHeelLZ','spHeelRX','spHeelRY','spHeelRZ',\
'spToeRX','spToeRY','spToeRZ','spkneeLX','spkneeLY','spkneeLZ','spkneeRX','spkneeRY','spkneeRZ',\
'spshRX','spshRY','spshRZ','spshLX','spshLY','spshLZ','acToeLX','acToeLY','acToeLZ','acHeelLX',\
'acHeelLY','acHeelLZ','acHeelRX','acHeelRY','acHeelRZ','acToeRX','acToeRY','acToeRZ','ackneeLX',\
'ackneeLY','ackneeLZ','ackneeRX','ackneeRY','ackneeRZ','acshRX','acshRY','acshRZ','acshLX','acshLY','acshLZ',\
'ToeL','spToeL','meanspToeL','stdspToeL','varspToeL','kurspToeL','skewspToeL','acToeL','meanacToeL','stdacToeL','varacToeL','kuracToeL',\
'skewacToeL','HeelL','spHeelL','meanspHeelL','stdspHeelL','varspHeelL','kurspHeelL','skewspHeelL','acHeelL','meanacHeelL',\
'stdacHeelL','varacHeelL','kuracHeelL','skewacHeelL','HeelR','spHeelR','meanspHeelR','stdspHeelR','varspHeelR','kurspHeelR','skewspHeelR',\
'acHeelR','meanacHeelR','stdacHeelR','varacHeelR','kuracHeelR','skewacHeelR','ToeR','spToeR','meanspToeR','stdspToeR','varspToeR','kurspToeR',\
'skewspToeR','acToeR','meanacToeR','stdacToeR','varacToeR','kuracToeR','skewacToeR','KneeL','spKneeL','meanspKneeL','stdspKneeL','varspKneeL',\
'kurspKneeL','skewspKneeL','acKneeL','meanacKneeL','stdacKneeL','varacKneeL','kuracKneeL','skewacKneeL','kneeR','spKneeR',\
'meanspKneeR','stdspKneeR','varspKneeR','kurspKneeR','skewspKneeR','acKneeR','meanacKneeR','stdacKneeR','varacKneeR','kuracKneeR','skewacKneeR',\
'shR','spshR','meanspshR','stdspshR','varspshR','kurspshR','skewspshR','acshR','meanacshR','stdacshR','varacshR','kuracshR','skewacshR','shL',\
'spshL','meanspshL','stdspshL','varspshL','kurspshL','skewspshL','acshL','meanacshL','stdacshL','varacshL','kuracshL','skewacshL']
'''
print df
     

'''
fig3 = plt.figure()
ax1 = fig3.add_subplot(311)
#ax1.plot(df[['serial']],df[['spHeelLX']],c='b')
#ax1.plot(df[['serial']],df[['meanacHeelRX']],c='r')
ax1.plot(df[['serial']],df[['varacHeelRX']],c='g')
ax1.set_title('HeellX speed according to time domain')

ax2 = fig3.add_subplot(312)
#ax2.plot(df[['serial']],df[['spHeelLY']],c='b')
#ax2.plot(df[['serial']],df[['meanacHeelRY']],c='r')
ax2.plot(df[['serial']],df[['varacHeelRY']],c='g')
ax2.set_title('HeelY speed according to time domain')

ax3 = fig3.add_subplot(313)
ax3.plot(df[['serial']],df[['spHeelLZ']],c='b')
ax3.plot(df[['serial']],df[['meanacHeelRZ']],c='r')
ax3.plot(df[['serial']],df[['varacHeelRZ']],c='g')
ax3.set_title('HeelZ speed according to time domain')

plt.legend()
plt.show()
'''

#df['spHeelLX']
#df['spHeelRX']

