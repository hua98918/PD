
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 23:03:51 2016

@author: zhang
"""


import matplotlib.pyplot as plt
plt.style.use('ggplot')
from mpl_toolkits.mplot3d import Axes3D
import argparse
import numpy as np
import pandas as pd
from os import walk

windowSize = 15


dn= 'C:\\pakinsen\\Vicon\\WALKER2016\\PDpra160407\\feature\\'
f1 = 'PDpra160407c01Feature.csv'
f2 = 'PDpra160407c04Feature.csv'
f3 = 'PDpra160407c06Feature.csv'
f4 = 'PDpra160407m01Feature.csv'
f5 = 'PDpra160407m02Feature.csv'
f6 = 'PDpra160407m03Feature.csv'
f7 = 'PDpra160407m05Feature.csv'
f8 = 'PDpra160407m06Feature.csv'
f9 = 'PDpra160407m07Feature.csv'
f10 = 'PDpra160407w01Feature.csv'
f11 = 'PDpra160407w03Feature.csv'


'''
# get all the filenames from the diretory
f = []
for (dirpath, dirnames, filenames) in walk(dn):
    f.extend(filenames)
    break 
'''

df1 = pd.read_csv(str(dn)+str(f1), sep=",", header = 0)
df2 = pd.read_csv(str(dn)+str(f2), sep=",", header = 0)
df3 = pd.read_csv(str(dn)+str(f3), sep=",", header = 0)
df4 = pd.read_csv(str(dn)+str(f4), sep=",", header = 0)
df5 = pd.read_csv(str(dn)+str(f5), sep=",", header = 0)
df6 = pd.read_csv(str(dn)+str(f6), sep=",", header = 0)
df7 = pd.read_csv(str(dn)+str(f7), sep=",", header = 0)
df8 = pd.read_csv(str(dn)+str(f8), sep=",", header = 0)
df9 = pd.read_csv(str(dn)+str(f9), sep=",", header = 0)
df10 = pd.read_csv(str(dn)+str(f10), sep=",", header = 0)
df11 = pd.read_csv(str(dn)+str(f11), sep=",", header = 0)

# mean value for left heel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspHeelL']],label='PDpra160407c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspHeelL']],label='PDpra160407c04',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['meanspHeelL']],label='PDpra160407c06',linewidth=1.5)
ax1.legend()
ax1.set_title('Mean value of Left Heel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['meanspHeelL']],label='PDpra160407m01')
ax2.plot(list(range(len(df5.index))),df5[['meanspHeelL']],label='PDpra160407m02')
ax2.plot(list(range(len(df6.index))),df6[['meanspHeelL']],label='PDpra160407m03')
ax2.plot(list(range(len(df7.index))),df7[['meanspHeelL']],label='PDpra160407m05')
ax2.plot(list(range(len(df8.index))),df8[['meanspHeelL']],label='PDpra160407m06')
ax2.plot(list(range(len(df9.index))),df9[['meanspHeelL']],label='PDpra160407m07')
ax2.set_title('Mean value of Left Heel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df10.index))),df10[['meanspHeelL']],label='PDpra160407w01')
ax3.plot(list(range(len(df11.index))),df11[['meanspHeelL']],label='PDpra160407w03')
ax3.set_title('Mean value of Left Heel speed(Moterlized Walker)')  
ax3.legend()
plt.savefig( str(dn) + 'MeanLeftHeel.png',dpi=72)

# std value for left heel   
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspHeelL']],label='PDpra160407c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['stdspHeelL']],label='PDpra160407c05',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['stdspHeelL']],label='PDpra160407c06',linewidth=1.5)
ax1.set_title( 'Std value of Left Heel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['stdspHeelL']],label='PDpra160407m01')
ax2.plot(list(range(len(df5.index))),df5[['stdspHeelL']],label='PDpra160407m02')
ax2.plot(list(range(len(df6.index))),df6[['stdspHeelL']],label='PDpra160407m03')
ax2.plot(list(range(len(df7.index))),df7[['stdspHeelL']],label='PDpra160407m05')
ax2.plot(list(range(len(df8.index))),df8[['stdspHeelL']],label='PDpra160407m06')
ax2.plot(list(range(len(df9.index))),df9[['stdspHeelL']],label='PDpra160407m07')
ax2.set_title('Std value of Left Heel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df10.index))),df10[['stdspHeelL']],label='PDpra160407w01')
ax3.plot(list(range(len(df11.index))),df11[['stdspHeelL']],label='PDpra160407w03')
ax3.set_title('Std value of Left Heel speed(Moterlized Walker)') 
ax3.legend()
plt.savefig( str(dn)+'StdLeftHeel.png',dpi=72)


# mean value for left kneel   meanspKneeL
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspKneeL']],label='PDpra160407c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspKneeL']],label='PDpra160407c04',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['meanspKneeL']],label='PDpra160407c06',linewidth=1.5)
ax1.set_title('Mean value of Left Kneel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['meanspKneeL']],label='PDpra160407m01')
ax2.plot(list(range(len(df5.index))),df5[['meanspKneeL']],label='PDpra160407m02')
ax2.plot(list(range(len(df6.index))),df6[['meanspKneeL']],label='PDpra160407m03')
ax2.plot(list(range(len(df7.index))),df7[['meanspKneeL']],label='PDpra160407m05')
ax2.plot(list(range(len(df8.index))),df8[['meanspKneeL']],label='PDpra160407m06')
ax2.plot(list(range(len(df9.index))),df9[['meanspKneeL']],label='PDpra160407m07')
ax2.set_title('Mean value of Left Kneel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df10.index))),df10[['meanspKneeL']],label='PDpra160407w01')
ax3.plot(list(range(len(df11.index))),df11[['meanspKneeL']],label='PDpra160407w03')
ax3.set_title('Mean value of Left Kneel speed(Moterlized Walker)')  
ax3.legend()
plt.savefig(str(dn)+'MeanLeftKneel.png',dpi=72)

# std value for left kneel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspKneeL']] ,label='PDpra160407c01',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdspKneeL']] ,label='PDpra160407c04',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['stdspKneeL']],label='PDpra160407c06',linewidth=1.5)
ax1.set_title('Std value of Left Kneel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['stdspKneeL']] ,label='PDpra160407m01')
ax2.plot(list(range(len(df5.index))),df5[['stdspKneeL']] ,label='PDpra160407m02')
ax2.plot(list(range(len(df6.index))),df6[['stdspKneeL']] ,label='PDpra160407m03')
ax2.plot(list(range(len(df7.index))),df7[['stdspKneeL']] ,label='PDpra160407m05')
ax2.plot(list(range(len(df8.index))),df8[['stdspKneeL']] ,label='PDpra160407m06')
ax2.plot(list(range(len(df9.index))),df9[['stdspKneeL']] ,label='PDpra160407m07')
ax2.set_title('Std value of Left Kneel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df10.index))),df10[['stdspKneeL']] ,label='PDpra160407w01')
ax3.plot(list(range(len(df11.index))),df11[['stdspKneeL']] ,label='PDpra160407w03')
ax3.set_title('Std value of Left Kneel speed(Moterlized Walker)')
ax3.legend() 
plt.savefig( str(dn)+ 'StdLeftKneel.png',dpi=72)



# mean value for left kneel   meanspKneeL
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanacKneeL']],label='PDpra160407c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanacKneeL']],label='PDpra160407c04',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['meanacKneeL']],label='PDpra160407c06',linewidth=1.5)
ax1.set_title('Mean value of Left Kneel acceleration(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['meanacKneeL']],label='PDpra160407m01')
ax2.plot(list(range(len(df5.index))),df5[['meanacKneeL']],label='PDpra160407m02')
ax2.plot(list(range(len(df6.index))),df6[['meanacKneeL']],label='PDpra160407m03')
ax2.plot(list(range(len(df7.index))),df7[['meanacKneeL']],label='PDpra160407m05')
ax2.plot(list(range(len(df8.index))),df8[['meanacKneeL']],label='PDpra160407m06')
ax2.plot(list(range(len(df9.index))),df9[['meanacKneeL']],label='PDpra160407m07')
ax2.set_title('Mean value of Left Kneel acceleration L(normal Walker)') 
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df10.index))),df10[['meanacKneeL']],label='PDpra160407w01')
ax3.plot(list(range(len(df11.index))),df11[['meanacKneeL']],label='PDpra160407w03')
ax3.set_title('Mean value of Left Kneel acceleration(Moterlized Walker)')  
ax3.legend()
plt.savefig( str(dn)+ 'MeanAccelerationLeftKneel.png',dpi=72)

# std accelerate value for left kneel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdacKneeL']] ,label='PDpra160407c01',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdacKneeL']] ,label='PDpra160407c04',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['stdacKneeL']],label='PDpra160407c06',linewidth=1.5)
ax1.set_title('Std value of Left Kneel acceleration(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['stdacKneeL']] ,label='PDpra160407m01')
ax2.plot(list(range(len(df5.index))),df5[['stdacKneeL']] ,label='PDpra160407m02')
ax2.plot(list(range(len(df6.index))),df6[['stdacKneeL']] ,label='PDpra160407m03')
ax2.plot(list(range(len(df7.index))),df7[['stdacKneeL']] ,label='PDpra160407m05')
ax2.plot(list(range(len(df8.index))),df8[['stdacKneeL']] ,label='PDpra160407m06')
ax2.plot(list(range(len(df9.index))),df9[['stdacKneeL']] ,label='PDpra160407m07')
ax2.set_title('Std value of Left Kneel acceleration(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df10.index))),df10[['stdacKneeL']] ,label='PDpra160407w01')
ax3.plot(list(range(len(df11.index))),df11[['stdacKneeL']] ,label='PDpra160407w02')
ax3.set_title('Std value of Left Kneel acceleration(Moterlized Walker)') 
ax3.legend()
plt.savefig(str(dn)+ 'StdAccelerationLeftKneel.png',dpi=72)


 
plt.legend()
plt.show()



