# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:48:32 2016

@author: zhang
"""

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
plt.style.use('ggplot')
from mpl_toolkits.mplot3d import Axes3D
import argparse
import numpy as np
import pandas as pd
from os import walk

windowSize = 15


dn= 'C:\\pakinsen\\Vicon\\WALKER2016\\PDkal160525\\feature\\'
f1 = 'PDkal160525c02Feature.csv'
f2 = 'PDkal160525c03Feature.csv'
f3 = 'PDkal160525c04Feature.csv'
f4 = 'PDkal160525m02Feature.csv'
f5 = 'PDkal160525m03Feature.csv'
f6 = 'PDkal160525m04Feature.csv'
f7 = 'PDkal160525m06Feature.csv'
f8 = 'PDkal160525m07Feature.csv'
f9 = 'PDkal160525m08Feature.csv'
f10 = 'PDkal160525m09Feature.csv'
f11 = 'PDkal160525m10Feature.csv'
f12 = 'PDkal160525m11Feature.csv'
f13 = 'PDkal160525m12Feature.csv'
f14 = 'PDkal160525w01Feature.csv'
f15 = 'PDkal160525w02Feature.csv'
f16 = 'PDkal160525w03Feature.csv'


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

#3D plot for all position 
fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspHeelL']]/100,label='PDkal160525c02',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspHeelL']]/100,label='PDkal160525c03',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['meanspHeelL']]/100,label='PDkal160525c04',linewidth=1.5)
#ax1.set_xlabel('Time interval 0.01s')
ax1.set_ylabel('speed(cm per second)')
ax1.set_title('Mean value of Left Heel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['meanspHeelL']]/100,label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['meanspHeelL']]/100,label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['meanspHeelL']]/100,label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['meanspHeelL']]/100,label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['meanspHeelL']]/100,label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['meanspHeelL']]/100,label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['meanspHeelL']]/100,label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['meanspHeelL']]/100,label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['meanspHeelL']]/100,label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['meanspHeelL']]/100,label='PDkal160525m12')
#ax2.set_xlabel('Time interval 0.01s')
ax2.set_ylabel('speed (cm per second)')
ax2.set_title('Mean value of Left Heel speed(Moterlized Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['meanspHeelL']]/100,label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['meanspHeelL']]/100,label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['meanspHeelL']]/100,label='PDkal160525w03',linewidth=1.5)
#ax3.set_xlabel('Time interval 0.01s')
ax3.set_ylabel('speed(cm per second)')
ax3.set_title('Mean value of Left Heel speed(normal Walker)')  
ax3.legend()
plt.savefig(  str(dn) + 'MeanLeftHeel.png',dpi=72)


fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspHeelL']],label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdspHeelL']],label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['stdspHeelL']],label='PDkal160525c04',linewidth=1)
ax1.set_title('Std value of Left Heel speed(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['stdspHeelL']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['stdspHeelL']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['stdspHeelL']],label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['stdspHeelL']],label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['stdspHeelL']],label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['stdspHeelL']],label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['stdspHeelL']],label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['stdspHeelL']],label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['stdspHeelL']],label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['stdspHeelL']],label='PDkal160525m12')
ax2.legend()
ax2.set_title('Std value of Left Heel speed(Moterlized Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['stdspHeelL']],label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['stdspHeelL']],label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['stdspHeelL']],label='PDkal160525w03',linewidth=1.5)
ax3.set_title('Std value of Left Heel speed(Normal Walker)') 
ax3.legend()
plt.savefig(  str(dn) + 'StdLeftHeel.png',dpi=72)


# mean value for left kneel   meanspKneeL
fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanspKneeL']],label='PDkal160525c02',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanspKneeL']],label='PDkal160525c03',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['meanspKneeL']],label='PDkal160525c04',linewidth=1.5)
ax1.legend()
ax1.set_title('Mean value of Left Kneel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['meanspKneeL']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['meanspKneeL']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['meanspKneeL']],label='PDkal160525m05')
ax2.plot(list(range(len(df7.index))),df7[['meanspKneeL']],label='PDkal160525m07')
ax2.plot(list(range(len(df8.index))),df8[['meanspKneeL']],label='PDkal160525m08')
ax2.plot(list(range(len(df9.index))),df9[['meanspKneeL']],label='PDkal160525m09')
ax2.plot(list(range(len(df10.index))),df10[['meanspKneeL']],label='PDkal160525m10')
ax2.plot(list(range(len(df11.index))),df11[['meanspKneeL']],label='PDkal160525m11')
ax2.plot(list(range(len(df12.index))),df12[['meanspKneeL']],label='PDkal160525m12')
ax2.plot(list(range(len(df13.index))),df13[['meanspKneeL']],label='PDkal160525m13')
ax2.legend()
ax2.set_title('Mean value of Left Kneel speed(Moterlized  Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['meanspKneeL']],label='PDkal160525w01')
ax3.plot(list(range(len(df15.index))),df15[['meanspKneeL']],label='PDkal160525w02')
ax3.plot(list(range(len(df16.index))),df16[['meanspKneeL']],label='PDkal160525w03')
ax3.set_title('Mean value of Left Kneel speed(Normal Walker)')  
ax3.legend()
plt.savefig(str(dn)+'MeanLeftKneel.png',dpi=72)

# std value for left kneel
fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdspKneeL']] ,label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdspKneeL']] ,label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['stdspKneeL']] ,label='PDkal160525c04',linewidth=1)
ax1.legend()
ax1.set_title('Std value of Left Kneel speed(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['stdspKneeL']] ,label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['stdspKneeL']] ,label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['stdspKneeL']] ,label='PDkal160525m05')
ax2.plot(list(range(len(df7.index))),df7[['stdspKneeL']] ,label='PDkal160525m07')
ax2.plot(list(range(len(df8.index))),df8[['stdspKneeL']] ,label='PDkal160525m08')
ax2.plot(list(range(len(df9.index))),df9[['stdspKneeL']] ,label='PDkal160525m09')
ax2.plot(list(range(len(df10.index))),df10[['stdspKneeL']] ,label='PDkal160525m10')
ax2.plot(list(range(len(df11.index))),df11[['stdspKneeL']] ,label='PDkal160525m11')
ax2.plot(list(range(len(df12.index))),df12[['stdspKneeL']] ,label='PDkal160525m12')
ax2.plot(list(range(len(df13.index))),df13[['stdspKneeL']] ,label='PDkal160525m13')
ax2.legend()
ax2.set_title('Std value of Left Kneel speed(Moterlized Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['stdspKneeL']] ,label='PDkal160525w01')
ax3.plot(list(range(len(df15.index))),df15[['stdspKneeL']] ,label='PDkal160525w02')
ax3.plot(list(range(len(df16.index))),df16[['stdspKneeL']] ,label='PDkal160525w03')
ax3.set_title('Std value of Left Kneel speed(Normal Walker)') 
ax3.legend()
plt.savefig( str(dn)+ 'StdLeftKneel.png',dpi=72)



# mean value for left kneel   meanspKneeL
fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['meanacKneeL']],label='PDkal160525c02',linewidth=1.5)
ax1.plot(list(range(len(df2.index))),df2[['meanacKneeL']],label='PDkal160525c03',linewidth=1.5)
ax1.plot(list(range(len(df3.index))),df3[['meanacKneeL']],label='PDkal160525c04',linewidth=1.5)
ax1.legend()
ax1.set_title('Mean value of Left Kneel acceleration(walking without help)')  
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['meanacKneeL']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['meanacKneeL']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['meanacKneeL']],label='PDkal160525m05')
ax2.plot(list(range(len(df7.index))),df7[['meanacKneeL']],label='PDkal160525m07')
ax2.plot(list(range(len(df8.index))),df8[['meanacKneeL']],label='PDkal160525m08')
ax2.plot(list(range(len(df9.index))),df9[['meanacKneeL']],label='PDkal160525m09')
ax2.plot(list(range(len(df10.index))),df10[['meanacKneeL']],label='PDkal160525m10')
ax2.plot(list(range(len(df11.index))),df11[['meanacKneeL']],label='PDkal160525m11')
ax2.plot(list(range(len(df12.index))),df12[['meanacKneeL']],label='PDkal160525m12')
ax2.plot(list(range(len(df13.index))),df13[['meanacKneeL']],label='PDkal160525m13')
ax2.legend()
ax2.set_title('Mean value of Left Kneel acceleration L(normal Walker)')  
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['meanacKneeL']],label='PDkal160525w01')
ax3.plot(list(range(len(df15.index))),df15[['meanacKneeL']],label='PDkal160525w02')
ax3.plot(list(range(len(df16.index))),df16[['meanacKneeL']],label='PDkal160525w03')
ax3.set_title('Mean value of Left Kneel acceleration(Moterlized Walker)')  
ax3.legend()
plt.savefig( str(dn)+ 'MeanAccelerationLeftKneel.png')


# std accelerate value for left kneel
fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['stdacKneeL']] ,label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['stdacKneeL']] ,label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['stdacKneeL']] ,label='PDkal160525c04',linewidth=1)
ax1.set_title('Std value of Left Kneel acceleration(walking without help)')  
ax1.legend()
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['stdacKneeL']] ,label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['stdacKneeL']] ,label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['stdacKneeL']] ,label='PDkal160525m05')
ax2.plot(list(range(len(df7.index))),df7[['stdacKneeL']] ,label='PDkal160525m07')
ax2.plot(list(range(len(df8.index))),df8[['stdacKneeL']] ,label='PDkal160525m08')
ax2.plot(list(range(len(df9.index))),df9[['stdacKneeL']] ,label='PDkal160525m09')
ax2.plot(list(range(len(df10.index))),df10[['stdacKneeL']] ,label='PDkal160525m10')
ax2.plot(list(range(len(df11.index))),df11[['stdacKneeL']] ,label='PDkal160525m11')
ax2.plot(list(range(len(df12.index))),df12[['stdacKneeL']] ,label='PDkal160525m12')
ax2.plot(list(range(len(df13.index))),df13[['stdacKneeL']] ,label='PDkal160525m13')
ax2.set_title('Std value of Left Kneel acceleration(normal Walker)')  
ax2.legend()
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['stdacKneeL']] ,label='PDkal160525w01')
ax3.plot(list(range(len(df15.index))),df15[['stdacKneeL']] ,label='PDkal160525w02')
ax3.plot(list(range(len(df16.index))),df16[['stdacKneeL']] ,label='PDkal160525w03')
ax3.set_title('Std value of Left Kneel acceleration(Moterlized Walker)') 
ax3.legend()
plt.savefig(str(dn)+ 'StdAccelerationLeftKneel.png')


 
plt.legend()
plt.show()




'''
fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['varspHeelL']],label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['varspToeR']],label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['varspToeR']],label='PDkal160525c04',linewidth=1)
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['varspToeR']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['varspToeR']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['varspToeR']],label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['varspToeR']],label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['varspToeR']],label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['varspToeR']],label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['varspToeR']],label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['varspToeR']],label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['varspToeR']],label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['varspToeR']],label='PDkal160525m12')
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['varspToeR']],label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['varspToeR']],label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['varspToeR']],label='PDkal160525w03',linewidth=1.5)
plt.legend()
plt.show()

fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['kurspHeelL']],label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['kurspHeelL']],label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['kurspHeelL']],label='PDkal160525c04',linewidth=1)
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['kurspHeelL']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['kurspHeelL']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['kurspHeelL']],label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['kurspHeelL']],label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['kurspHeelL']],label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['kurspHeelL']],label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['kurspHeelL']],label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['kurspHeelL']],label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['kurspHeelL']],label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['kurspHeelL']],label='PDkal160525m12')
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['kurspHeelL']],label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['kurspHeelL']],label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['kurspHeelL']],label='PDkal160525w03',linewidth=1.5)
plt.legend()
plt.show()



fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['skewspHeelL']],label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['skewspHeelL']],label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['skewspHeelL']],label='PDkal160525c04',linewidth=1)
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['skewspHeelL']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['skewspHeelL']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['skewspHeelL']],label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['skewspHeelL']],label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['skewspHeelL']],label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['skewspHeelL']],label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['skewspHeelL']],label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['skewspHeelL']],label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['skewspHeelL']],label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['skewspHeelL']],label='PDkal160525m12')
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['skewspHeelL']],label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['skewspHeelL']],label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['skewspHeelL']],label='PDkal160525w03',linewidth=1.5)
plt.legend()
plt.show()


fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['spkneeLZ']],label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['spkneeLZ']],label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['spkneeLZ']],label='PDkal160525c04',linewidth=1)
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['spkneeLZ']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['spkneeLZ']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['spkneeLZ']],label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['spkneeLZ']],label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['spkneeLZ']],label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['spkneeLZ']],label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['spkneeLZ']],label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['spkneeLZ']],label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['spkneeLZ']],label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['spkneeLZ']],label='PDkal160525m12')
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['spkneeLZ']],label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['spkneeLZ']],label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['spkneeLZ']],label='PDkal160525w03',linewidth=1.5)
plt.legend()
plt.show()


fig1 = plt.figure()
ax1 = fig1.add_subplot(311)
ax1.plot(list(range(len(df1.index))),df1[['spkneeLZ']],label='PDkal160525c02',linewidth=1)
ax1.plot(list(range(len(df2.index))),df2[['spkneeLZ']],label='PDkal160525c03',linewidth=1)
ax1.plot(list(range(len(df3.index))),df3[['spkneeLZ']],label='PDkal160525c04',linewidth=1)
ax2 = fig1.add_subplot(312)
ax2.plot(list(range(len(df4.index))),df4[['spkneeLZ']],label='PDkal160525m02')
ax2.plot(list(range(len(df5.index))),df5[['spkneeLZ']],label='PDkal160525m03')
ax2.plot(list(range(len(df6.index))),df6[['spkneeLZ']],label='PDkal160525m04')
ax2.plot(list(range(len(df7.index))),df7[['spkneeLZ']],label='PDkal160525m06')
ax2.plot(list(range(len(df8.index))),df8[['spkneeLZ']],label='PDkal160525m07')
ax2.plot(list(range(len(df9.index))),df9[['spkneeLZ']],label='PDkal160525m08')
ax2.plot(list(range(len(df10.index))),df10[['spkneeLZ']],label='PDkal160525m09')
ax2.plot(list(range(len(df11.index))),df11[['spkneeLZ']],label='PDkal160525m10')
ax2.plot(list(range(len(df12.index))),df12[['spkneeLZ']],label='PDkal160525m11')
ax2.plot(list(range(len(df13.index))),df13[['spkneeLZ']],label='PDkal160525m12')
ax3 = fig1.add_subplot(313)
ax3.plot(list(range(len(df14.index))),df14[['spkneeLZ']],label='PDkal160525w01',linewidth=1.5)
ax3.plot(list(range(len(df15.index))),df15[['spkneeLZ']],label='PDkal160525w02',linewidth=1.5)
ax3.plot(list(range(len(df16.index))),df16[['spkneeLZ']],label='PDkal160525w03',linewidth=1.5)
plt.legend()
plt.show()
'''