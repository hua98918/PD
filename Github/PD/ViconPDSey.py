# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 09:25:43 2016

@author: zhang
"""


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


dn= 'C:\\pakinsen\\Vicon\\WALKER2016\\PDsey160502\\feature\\'
f1 = 'PDsey160502c01Feature.csv'
f2 = 'PDsey160502c02Feature.csv'
f3 = 'PDsey160502m01Feature.csv'
f4 = 'PDsey160502m02Feature.csv'
f5 = 'PDsey160502m03Feature.csv'
f6 = 'PDsey160502m04Feature.csv'
f7 = 'PDsey160502m05Feature.csv'
f8 = 'PDsey160502m06Feature.csv'
f9 = 'PDsey160502w01Feature.csv'
f10 = 'PDsey160502w01Feature.csv'
f11 = 'PDsey160502w03Feature.csv'


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
ax1.plot(list(range(len(df1.index))),df1[['meanspHeelL']],label='PDsey160502c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspHeelL']],label='PDsey160502c02',linewidth=1.5)
ax1.legend()
ax1.set_title('Mean value of Left Heel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['meanspHeelL']],label='PDsey160502m01')
ax2.plot(list(range(len(df4.index))),df4[['meanspHeelL']],label='PDsey160502m02')
ax2.plot(list(range(len(df5.index))),df5[['meanspHeelL']],label='PDsey160502m03')
ax2.plot(list(range(len(df6.index))),df6[['meanspHeelL']],label='PDsey160502m04')
ax2.plot(list(range(len(df7.index))),df7[['meanspHeelL']],label='PDsey160502m05')
ax2.plot(list(range(len(df8.index))),df8[['meanspHeelL']],label='PDsey160502m06')
ax2.plot(list(range(len(df9.index))),df9[['meanspHeelL']],label='PDsey160502m07')
ax2.set_title('Mean value of Left Heel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df9.index))),df9[['meanspHeelL']],label='PDsey160502w01')
ax3.plot(list(range(len(df10.index))),df10[['meanspHeelL']],label='PDsey160502w02')
ax3.plot(list(range(len(df11.index))),df11[['meanspHeelL']],label='PDsey160502w03')
ax3.set_title('Mean value of Left Heel speed(Moterlized Walker)')  
ax3.legend()
plt.savefig( str(dn) + 'MeanLeftHeel.png',dpi=72)

# std value for left heel   
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspHeelL']],label='PDsey160502c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['stdspHeelL']],label='PDsey160502c05',linewidth=1.5)
ax1.set_title( 'Std value of Left Heel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['stdspHeelL']],label='PDsey160502m01')
ax2.plot(list(range(len(df4.index))),df4[['stdspHeelL']],label='PDsey160502m02')
ax2.plot(list(range(len(df5.index))),df5[['stdspHeelL']],label='PDsey160502m03')
ax2.plot(list(range(len(df6.index))),df6[['stdspHeelL']],label='PDsey160502m04')
ax2.plot(list(range(len(df7.index))),df7[['stdspHeelL']],label='PDsey160502m05')
ax2.plot(list(range(len(df8.index))),df8[['stdspHeelL']],label='PDsey160502m06')
ax2.set_title('Std value of Left Heel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df9.index))),df9[['stdspHeelL']],label='PDsey160502w01')
ax3.plot(list(range(len(df10.index))),df10[['stdspHeelL']],label='PDsey160502w02')
ax3.plot(list(range(len(df11.index))),df11[['stdspHeelL']],label='PDsey160502w03')
ax3.set_title('Std value of Left Heel speed(Moterlized Walker)') 
ax3.legend()
plt.savefig( str(dn)+'StdLeftHeel.png',dpi=72)


# mean value for left kneel   meanspKneeL
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspKneeL']],label='PDsey160502c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspKneeL']],label='PDsey160502c02',linewidth=1.5)
ax1.set_title('Mean value of Left Kneel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['meanspKneeL']],label='PDsey160502m01')
ax2.plot(list(range(len(df4.index))),df4[['meanspKneeL']],label='PDsey160502m02')
ax2.plot(list(range(len(df5.index))),df5[['meanspKneeL']],label='PDsey160502m03')
ax2.plot(list(range(len(df6.index))),df6[['meanspKneeL']],label='PDsey160502m04')
ax2.plot(list(range(len(df7.index))),df7[['meanspKneeL']],label='PDsey160502m05')
ax2.plot(list(range(len(df8.index))),df8[['meanspKneeL']],label='PDsey160502m06')
ax2.set_title('Mean value of Left Kneel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df9.index))),df9[['meanspKneeL']],label='PDsey160502w01')
ax3.plot(list(range(len(df10.index))),df10[['meanspKneeL']],label='PDsey160502w02')
ax3.plot(list(range(len(df11.index))),df11[['meanspKneeL']],label='PDsey160502w03')
ax3.set_title('Mean value of Left Kneel speed(Moterlized Walker)')  
ax3.legend()
plt.savefig(str(dn)+'MeanLeftKneel.png',dpi=72)

# std value for left kneel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspKneeL']] ,label='PDsey160502c01',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdspKneeL']] ,label='PDsey160502c04',linewidth=1)
ax1.set_title('Std value of Left Kneel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax1.plot(list(range(len(df3.index))),df3[['stdspKneeL']],label='PDsey160502m01')
ax2.plot(list(range(len(df4.index))),df4[['stdspKneeL']] ,label='PDsey160502m02')
ax2.plot(list(range(len(df5.index))),df5[['stdspKneeL']] ,label='PDsey160502m03')
ax2.plot(list(range(len(df6.index))),df6[['stdspKneeL']] ,label='PDsey160502m04')
ax2.plot(list(range(len(df7.index))),df7[['stdspKneeL']] ,label='PDsey160502m05')
ax2.plot(list(range(len(df8.index))),df8[['stdspKneeL']] ,label='PDsey160502m06')
ax2.set_title('Std value of Left Kneel speed(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df9.index))),df9[['stdspKneeL']] ,label='PDsey160502w01')
ax3.plot(list(range(len(df10.index))),df10[['stdspKneeL']] ,label='PDsey160502w02')
ax3.plot(list(range(len(df11.index))),df11[['stdspKneeL']] ,label='PDsey160502w03')
ax3.set_title('Std value of Left Kneel speed(Moterlized Walker)')
ax3.legend() 
plt.savefig( str(dn)+ 'StdLeftKneel.png',dpi=72)



# mean value for left kneel   meanspKneeL
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanacKneeL']],label='PDsey160502c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanacKneeL']],label='PDsey160502c04',linewidth=1.5)
ax1.set_title('Mean value of Left Kneel acceleration(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['meanacKneeL']],label='PDsey160502m01')
ax2.plot(list(range(len(df4.index))),df4[['meanacKneeL']],label='PDsey160502m02')
ax2.plot(list(range(len(df5.index))),df5[['meanacKneeL']],label='PDsey160502m03')
ax2.plot(list(range(len(df6.index))),df6[['meanacKneeL']],label='PDsey160502m04')
ax2.plot(list(range(len(df7.index))),df7[['meanacKneeL']],label='PDsey160502m05')
ax2.plot(list(range(len(df8.index))),df8[['meanacKneeL']],label='PDsey160502m06')
ax2.set_title('Mean value of Left Kneel acceleration L(normal Walker)') 
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df9.index))),df9[['meanacKneeL']],label='PDsey160502w01')
ax3.plot(list(range(len(df10.index))),df10[['meanacKneeL']],label='PDsey160502w02')
ax3.plot(list(range(len(df11.index))),df11[['meanacKneeL']],label='PDsey160502w03')
ax3.set_title('Mean value of Left Kneel acceleration(Moterlized Walker)')  
ax3.legend()
plt.savefig( str(dn)+ 'MeanAccelerationLeftKneel.png',dpi=72)

# std accelerate value for left kneel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdacKneeL']] ,label='PDsey160502c01',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdacKneeL']] ,label='PDsey160502c04',linewidth=1)
ax1.set_title('Std value of Left Kneel acceleration(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['stdacKneeL']],label='PDsey160502m01')
ax2.plot(list(range(len(df4.index))),df4[['stdacKneeL']] ,label='PDsey160502m02')
ax2.plot(list(range(len(df5.index))),df5[['stdacKneeL']] ,label='PDsey160502m03')
ax2.plot(list(range(len(df6.index))),df6[['stdacKneeL']] ,label='PDsey160502m04')
ax2.plot(list(range(len(df7.index))),df7[['stdacKneeL']] ,label='PDsey160502m05')
ax2.plot(list(range(len(df8.index))),df8[['stdacKneeL']] ,label='PDsey160502m06')
ax2.set_title('Std value of Left Kneel acceleration(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df9.index))),df9[['stdacKneeL']] ,label='PDsey160502w01')
ax3.plot(list(range(len(df10.index))),df10[['stdacKneeL']] ,label='PDsey160502w02')
ax3.plot(list(range(len(df11.index))),df11[['stdacKneeL']] ,label='PDsey160502w03')
ax3.set_title('Std value of Left Kneel acceleration(Moterlized Walker)') 
ax3.legend()
plt.savefig(str(dn)+ 'StdAccelerationLeftKneel.png',dpi=72)


 
plt.legend()
plt.show()



