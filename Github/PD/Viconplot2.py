# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 13:21:02 2016

@author: zhang
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 23:03:51 2016

@author: zhang
"""


import matplotlib.pyplot as plt
#plt.style.use('ggplot')
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

dn= 'C:\pakinsen\Vicon\WALKER2016\PDtob160517\\'
fn = 'PTtob160517m06feature'

input_file = str(dn) + str(fn) + ".csv"
df = pd.read_csv(input_file, sep=",", header = 0)
#print df
#fill all theNA as 0
df.fillna(0)


#3D plot for all position 
fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311, projection='3d')
ax1.scatter(df[['ToeLX']],df[['ToeLY']],df[['ToeLZ']],label='left side')
ax1.scatter(df[['ToeRX']],df[['ToeRY']],df[['ToeRZ']],c='r',label='right side')
#
ax1.legend()
ax1.set_title('Toe 3D Plot')
ax2 = fig1.add_subplot(312, projection='3d')
ax2.scatter(df[['HeelLX']],df[['HeelLY']],df[['HeelLZ']],label='left side')
ax2.scatter(df[['HeelRX']],df[['HeelRY']],df[['HeelRZ']],c='r',label='right side')
ax2.legend()
ax2.set_title('Heel 3D Plot')
ax3 = fig1.add_subplot(313, projection='3d')
ax3.scatter(df[['shLX']],df[['shLY']],df[['shLZ']],label='left side')
ax3.scatter(df[['shRX']],df[['shRY']],df[['shRZ']],c='r',label='right side')
ax3.set_title('shoulder 3D Plot')
ax3.legend()
plt.savefig( str(dn) + str(fn) +'_3D.png',dpi=72)

# 2D Plot for position ToeXYZ
fig5 = plt.figure(figsize=(20, 10))
ax1 = fig5.add_subplot(311)
ax1.plot(df[['serial']],df[['ToeLX']],c='b',label="left side")
ax1.plot(df[['serial']],df[['ToeRX']],c='r',label="right side")
ax1.set_title('ToeX position according to time domain')
ax1.legend()
ax2 = fig5.add_subplot(312)
ax2.plot(df[['serial']],df[['ToeLY']],c='b',label="left side")
ax2.plot(df[['serial']],df[['ToeRY']],c='r',label="right side")
ax2.set_title('ToeY position according to time domain')
ax2.legend()
ax3 = fig5.add_subplot(313)
ax3.plot(df[['serial']],df[['ToeLZ']],c='b',label="left side")
ax3.plot(df[['serial']],df[['ToeRZ']],c='r',label="right side")
ax3.set_title('ToeZ position according to time domain')
ax3.legend()
plt.savefig( str(dn) + str(fn) +'_ToeXYZposition.png',dpi=72)

#2D plot for position HeelXYZ 
fig6 = plt.figure(figsize=(20, 10))
ax1 = fig6.add_subplot(311)
ax1.plot(df[['serial']],df[['HeelLX']],c='b',label="left side")
ax1.plot(df[['serial']],df[['HeelRX']],c='r',label="right side")
ax1.set_title('HeelX position  according to time domain')
ax1.legend()
ax2 = fig6.add_subplot(312)
ax2.plot(df[['serial']],df[['HeelLY']],c='b',label="left side")
ax2.plot(df[['serial']],df[['HeelRY']],c='r',label="right side")
ax2.set_title('HeelY position according to time domain')
ax2.legend()
ax3 = fig6.add_subplot(313)
ax3.plot(df[['serial']],df[['HeelLZ']],c='b',label="left side")
ax3.plot(df[['serial']],df[['HeelRZ']],c='r',label="right side")
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

'''
#shoulder speed plot
fig4 = plt.figure()
ax1 = fig4.add_subplot(311)
ax1.plot(df[['serial']],df[['spshLX']])
ax1.plot(df[['serial']],df[['spshRX']],c='r')
ax1.set_title('shoulderX speed according to time domain')
ax4 = fig4.add_subplot(312)
ax2.plot(df[['serial']],df[['spshLY']])
ax2.plot(df[['serial']],df[['spshRY']],c='r')
ax2.set_title('shoulderY speed according to time domain')
ax4 = fig4.add_subplot(313)
ax3.plot(df[['serial']],df[['spshLZ']])
ax3.plot(df[['serial']],df[['spshRZ']],c='r')
ax3.set_title('shoulderXYZ speed according to time domain')
#plt.savefig( str(dn) + str(fn) +'_shoulderXYZspeed.png',dpi=72)
'''


plt.legend()
plt.show()






