# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 13:26:10 2017

@author: Ariel
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c02feature.csv"
input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\TurnAngle.csv"
output_file = "C:\pakinsen\Vicon\AllTurn.csv"

df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')
df.head()
trail_df = df.groupby(['trails'])

print trail_df.max()
print trail_df.min()
print trail_df.mean()
print trail_df.std()

#df['trails'].unique().tolist()


#df.plot.hexbin(x='a', y='b', gridsize=25)
sct = plt.scatter(trail_df.mean().index, trail_df.mean().angel, s=trail_df.std(), linewidths=2, edgecolor='w')
sct.set_alpha(0.75)

plt.axis([0,11,200,1280])
plt.xlabel('Murders per 100,000 population')
plt.ylabel('Burglaries per 100,000 population')
plt.show()
'''
df['trails'].replace(['PDlip160509c01feature','PDlip160509c02feature','PDlip160509m01feature','PDlip160509m02feature'\
  'PDlip160509m03feature','PDlip160509m05feature','PDlip160509m07feature','PDlip160509m08feature','PDlip160509m09feature','PDlip160509m10feature'\
  'PDlip160509w01feature','PDlip160509w02feature'],(1,2,3,4,5,6,7,8,9,10,11,12))
#xticks=['PDlip160509w02feature','PDlip160509w02feature','PDlip160509w01','PDlip160509w02']

#plt.plot(df.trails, df.angel)
#plt.scatter(x=trails, y=df['angel'],c=df['position'])

plt.xticks(x,xticks)

plt.show()
'''