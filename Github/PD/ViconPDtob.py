# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 09:48:43 2016

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


dn= 'C:\\pakinsen\\Vicon\\WALKER2016\\PDtob160517\\feature\\'
f1 = 'PTtob160517c01Feature.csv'
f2 = 'PTtob160517c02Feature.csv'
f3 = 'PTtob160517m01Feature.csv'
f4 = 'PTtob160517m02Feature.csv'
f5 = 'PTtob160517m03Feature.csv'
f6 = 'PTtob160517m04Feature.csv'
f7 = 'PTtob160517m07Feature.csv'
f8 = 'PTtob160517m08Feature.csv'
f9 = 'PTtob160517m09Feature.csv'
f10 = 'PTtob160517m10Feature.csv'
f11 = 'PTtob160517m11Feature.csv'
f12 = 'PTtob160517m12Feature.csv'
f13 = 'PTtob160517m13Feature.csv'
f14 = 'PTtob160517w01Feature.csv'
f15 = 'PTtob160517w02Feature.csv'
f16 = 'PTtob160517w03Feature.csv'

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
df12 = pd.read_csv(str(dn)+str(f12), sep=",", header = 0)
df13 = pd.read_csv(str(dn)+str(f13), sep=",", header = 0)
df14 = pd.read_csv(str(dn)+str(f14), sep=",", header = 0)
df15 = pd.read_csv(str(dn)+str(f15), sep=",", header = 0)
df16 = pd.read_csv(str(dn)+str(f16), sep=",", header = 0)

# mean value for left heel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspHeelL']],label='PTtob160517c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspHeelL']],label='PTtob160517c02',linewidth=1.5)
ax1.set_title('Mean value of Left Heel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['meanspHeelL']],label='PTtob160517m01')
ax2.plot(list(range(len(df4.index))),df4[['meanspHeelL']],label='PTtob160517m02')
ax2.plot(list(range(len(df5.index))),df5[['meanspHeelL']],label='PTtob160517m03')
ax2.plot(list(range(len(df6.index))),df6[['meanspHeelL']],label='PTtob160517m04')
ax2.plot(list(range(len(df7.index))),df7[['meanspHeelL']],label='PTtob160517m07')
ax2.plot(list(range(len(df8.index))),df8[['meanspHeelL']],label='PTtob160517m08')
ax2.plot(list(range(len(df9.index))),df9[['meanspHeelL']],label='PTtob160517m09')
ax2.plot(list(range(len(df10.index))),df10[['meanspHeelL']],label='PTtob160517m10')
ax2.plot(list(range(len(df11.index))),df11[['meanspHeelL']],label='PTtob160517m11')
ax2.plot(list(range(len(df12.index))),df12[['meanspHeelL']],label='PTtob160517m12')
ax2.plot(list(range(len(df13.index))),df13[['meanspHeelL']],label='PTtob160517m13')
ax2.set_title('Mean value of Left Heel speed(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['meanspHeelL']],label='PTtob160517w01')
ax3.plot(list(range(len(df15.index))),df15[['meanspHeelL']],label='PTtob160517w02')
ax3.plot(list(range(len(df16.index))),df16[['meanspHeelL']],label='PTtob160517w03')
ax3.set_title('Mean value of Left Heel speed(Moterlized Walker)')  
plt.savefig( str(dn) + 'MeanLeftHeel.png',dpi=72)

# std value for left heel   
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspHeelL']],label='PTtob160517c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['stdspHeelL']],label='PTtob160517c02',linewidth=1.5)
ax1.set_title( 'Std value of Left Heel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax1.plot(list(range(len(df3.index))),df3[['stdspHeelL']],label='PTtob160517m01')
ax2.plot(list(range(len(df4.index))),df4[['stdspHeelL']],label='PTtob160517m02')
ax2.plot(list(range(len(df5.index))),df5[['stdspHeelL']],label='PTtob160517m03')
ax2.plot(list(range(len(df6.index))),df6[['stdspHeelL']],label='PTtob160517m05')
ax2.plot(list(range(len(df7.index))),df7[['stdspHeelL']],label='PTtob160517m07')
ax2.plot(list(range(len(df8.index))),df8[['stdspHeelL']],label='PTtob160517m08')
ax2.plot(list(range(len(df9.index))),df9[['stdspHeelL']],label='PTtob160517m09')
ax2.plot(list(range(len(df10.index))),df10[['stdspHeelL']],label='PTtob160517m10')
ax2.plot(list(range(len(df11.index))),df11[['stdspHeelL']],label='PTtob160517m11')
ax2.plot(list(range(len(df12.index))),df12[['stdspHeelL']],label='PTtob160517m12')
ax2.plot(list(range(len(df13.index))),df13[['stdspHeelL']],label='PTtob160517m13')
ax2.set_title('Std value of Left Heel speed(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['stdspHeelL']],label='PTtob160517w01')
ax3.plot(list(range(len(df15.index))),df15[['stdspHeelL']],label='PTtob160517w02')
ax3.plot(list(range(len(df16.index))),df16[['stdspHeelL']],label='PTtob160517w03')
ax3.set_title('Std value of Left Heel speed(Moterlized Walker)') 
plt.savefig( str(dn)+'StdLeftHeel.png',dpi=72)


# mean value for left kneel   meanspKneeL
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspKneeL']],label='PTtob160517c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspKneeL']],label='PTtob160517c02',linewidth=1.5)
ax1.set_title('Mean value of Left Kneel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['meanspKneeL']],label='PTtob160517m01')
ax2.plot(list(range(len(df4.index))),df4[['meanspKneeL']],label='PTtob160517m02')
ax2.plot(list(range(len(df5.index))),df5[['meanspKneeL']],label='PTtob160517m03')
ax2.plot(list(range(len(df6.index))),df6[['meanspKneeL']],label='PTtob160517m05')
ax2.plot(list(range(len(df7.index))),df7[['meanspKneeL']],label='PTtob160517m07')
ax2.plot(list(range(len(df8.index))),df8[['meanspKneeL']],label='PTtob160517m08')
ax2.plot(list(range(len(df9.index))),df9[['meanspKneeL']],label='PTtob160517m09')
ax2.plot(list(range(len(df10.index))),df10[['meanspKneeL']],label='PTtob160517m10')
ax2.plot(list(range(len(df11.index))),df11[['meanspKneeL']],label='PTtob160517m11')
ax2.plot(list(range(len(df12.index))),df12[['meanspKneeL']],label='PTtob160517m12')
ax2.plot(list(range(len(df13.index))),df13[['meanspKneeL']],label='PTtob160517m13')
ax2.set_title('Mean value of Left Kneel speed(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['meanspKneeL']],label='PTtob160517w01')
ax3.plot(list(range(len(df15.index))),df15[['meanspKneeL']],label='PTtob160517m02')
ax3.plot(list(range(len(df16.index))),df16[['meanspKneeL']],label='PTtob160517m03')
ax3.set_title('Mean value of Left Kneel speed(Moterlized Walker)')  
plt.savefig(str(dn)+'MeanLeftKneel.png',dpi=72)

# std value for left kneel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspKneeL']] ,label='PTtob160517c01',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdspKneeL']] ,label='PTtob160517c02',linewidth=1)
ax1.set_title('Std value of Left Kneel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax1.plot(list(range(len(df3.index))),df3[['stdspKneeL']] ,label='PTtob160517m01')
ax2.plot(list(range(len(df4.index))),df4[['stdspKneeL']] ,label='PTtob160517m02')
ax2.plot(list(range(len(df5.index))),df5[['stdspKneeL']] ,label='PTtob160517m03')
ax2.plot(list(range(len(df6.index))),df6[['stdspKneeL']] ,label='PTtob160517m05')
ax2.plot(list(range(len(df7.index))),df7[['stdspKneeL']] ,label='PTtob160517m07')
ax2.plot(list(range(len(df8.index))),df8[['stdspKneeL']] ,label='PTtob160517m08')
ax2.plot(list(range(len(df9.index))),df9[['stdspKneeL']] ,label='PTtob160517m09')
ax2.plot(list(range(len(df10.index))),df10[['stdspKneeL']] ,label='PTtob160517m10')
ax2.plot(list(range(len(df11.index))),df11[['stdspKneeL']] ,label='PTtob160517m11')
ax2.plot(list(range(len(df12.index))),df12[['stdspKneeL']] ,label='PTtob160517m12')
ax2.plot(list(range(len(df13.index))),df13[['stdspKneeL']] ,label='PTtob160517m13')
ax2.set_title('Std value of Left Kneel speed(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['stdspKneeL']] ,label='PTtob160517w01')
ax3.plot(list(range(len(df15.index))),df15[['stdspKneeL']] ,label='PTtob160517w02')
ax3.plot(list(range(len(df16.index))),df16[['stdspKneeL']] ,label='PTtob160517w03')
ax3.set_title('Std value of Left Kneel speed(Moterlized Walker)') 
plt.savefig( str(dn)+ 'StdLeftKneel.png',dpi=72)



# mean value for left kneel   meanspKneeL
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanacKneeL']],label='PTtob160517c01',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanacKneeL']],label='PTtob160517c02',linewidth=1.5)
ax1.set_title('Mean value of Left Kneel acceleration(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df3.index))),df3[['meanacKneeL']],label='PTtob160517m01')
ax2.plot(list(range(len(df4.index))),df4[['meanacKneeL']],label='PTtob160517m02')
ax2.plot(list(range(len(df5.index))),df5[['meanacKneeL']],label='PTtob160517m03')
ax2.plot(list(range(len(df6.index))),df6[['meanacKneeL']],label='PTtob160517m05')
ax2.plot(list(range(len(df7.index))),df7[['meanacKneeL']],label='PTtob160517m07')
ax2.plot(list(range(len(df8.index))),df8[['meanacKneeL']],label='PTtob160517m08')
ax2.plot(list(range(len(df9.index))),df9[['meanacKneeL']],label='PTtob160517m09')
ax2.plot(list(range(len(df10.index))),df10[['meanacKneeL']],label='PTtob160517m10')
ax2.plot(list(range(len(df11.index))),df11[['meanacKneeL']],label='PTtob160517m11')
ax2.plot(list(range(len(df12.index))),df12[['meanacKneeL']],label='PTtob160517m12')
ax2.plot(list(range(len(df13.index))),df13[['meanacKneeL']],label='PTtob160517m13')
ax2.set_title('Mean value of Left Kneel acceleration L(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['meanacKneeL']],label='PTtob160517w01')
ax3.plot(list(range(len(df15.index))),df15[['meanacKneeL']],label='PTtob160517w02')
ax3.plot(list(range(len(df16.index))),df16[['meanacKneeL']],label='PTtob160517w03')
ax3.set_title('Mean value of Left Kneel acceleration(Moterlized Walker)')  
plt.savefig( str(dn)+ 'MeanAccelerationLeftKneel.png',dpi=72)

# std accelerate value for left kneel
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdacKneeL']] ,label='PTtob160517c01',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdacKneeL']] ,label='PTtob160517c02',linewidth=1)
ax1.set_title('Std value of Left Kneel acceleration(walking without help)')  
ax2 = fig1.add_subplot(312)
ax1.plot(list(range(len(df3.index))),df3[['stdacKneeL']] ,label='PTtob160517m01')
ax2.plot(list(range(len(df4.index))),df4[['stdacKneeL']] ,label='PTtob160517m02')
ax2.plot(list(range(len(df5.index))),df5[['stdacKneeL']] ,label='PTtob160517m03')
ax2.plot(list(range(len(df6.index))),df6[['stdacKneeL']] ,label='PTtob160517m05')
ax2.plot(list(range(len(df7.index))),df7[['stdacKneeL']] ,label='PTtob160517m07')
ax2.plot(list(range(len(df8.index))),df8[['stdacKneeL']] ,label='PTtob160517m08')
ax2.plot(list(range(len(df9.index))),df9[['stdacKneeL']] ,label='PTtob160517m09')
ax2.plot(list(range(len(df10.index))),df10[['stdacKneeL']] ,label='PTtob160517m10')
ax2.plot(list(range(len(df11.index))),df11[['stdacKneeL']] ,label='PTtob160517m11')
ax2.plot(list(range(len(df12.index))),df12[['stdacKneeL']] ,label='PTtob160517m12')
ax2.plot(list(range(len(df13.index))),df13[['stdacKneeL']] ,label='PTtob160517m13')
ax2.set_title('Std value of Left Kneel acceleration(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['stdacKneeL']] ,label='PTtob160517w01')
ax3.plot(list(range(len(df15.index))),df15[['stdacKneeL']] ,label='PTtob160517w02')
ax3.plot(list(range(len(df16.index))),df16[['stdacKneeL']] ,label='PTtob160517w03')
ax3.set_title('Std value of Left Kneel acceleration(Moterlized Walker)') 
plt.savefig(str(dn)+ 'StdAccelerationLeftKneel.png',dpi=72)


 
plt.legend()
plt.show()



