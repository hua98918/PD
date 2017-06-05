# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:51:16 2017

@author: Ariel
#function： read in the 

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import MDFA as mdfa

#input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c02feature.csv"
input_file = "C:\pakinsen\Vicon\AllSwing.csv"
output_file = "C:\pakinsen\Vicon\PDlip160509StraightSum.csv"

df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')
df.head()

name = df['name'].map(lambda x: x.startswith('PDlip160509'))
#indenpentend walking by themselves       
'''
c_straight_df = df[(df['position'] == 0) & (df['type'] == 'c') & name]
c_turn_df = df[(df['position'] == 1) & (df['type'] == 'c') & name]
m_straight_df = df[(df['position'] == 0) & (df['type'] == 'm') & name]
m_turn_df = df[(df['position'] == 1) & (df['type'] == 'm') & name]
w_straight_df = df[(df['position'] == 0) & (df['type'] == 'w') & name]
w_turn_df = df[(df['position'] == 1) & (df['type'] == 'w') & name]
'''

straight_df = df[(df['position'] ==0)]

#straight_df = df[(df['position'] ==1)]
straight_grouped = straight_df.groupby(['type'])


#fig, ax = plt.subplots(figsize=(12,  8))
#straight_grouped.boxplot(column=['LeftGCT','RightGCT','LeftStance','RightStance',\
#             'LeftSwing','RightSwing'], by='name')


'''
bp = df_time.boxplot(by='type')
df_time[df_time.type =='c'].type.hist()
df_time[df_time.type =='m'].type.hist()
df_time[df_time.type =='w'].type.hist()

breaks = np.asarray(np.percentile(df_time.LeftGCT, [25,50,75,100]))
df_time['Class'] = (df_time.LeftGCT.values > breaks[..., np.newaxis]).sum(0)
ax = df.boxplot(column='type', by='Class')
ax.xaxis.set_ticklabels(['%s'%val for val in breaks])
'''
'''
fig, ax = plt.subplots(figsize=(12,  8))
df.boxplot(['LeftGCT','RightGCT','LeftStance','RightStance',\
             'LeftSwing','RightSwing'], 'type', ax)

'''''
'''
print c_straight_df.describe()
c_straight_df.boxplot(['ZStideHeightL','ZStideHeightR'], 'name', ax)
'''

with open(output_file, 'a') as f:
    #df.to_csv(f,sep=',',header=True)
    straight_grouped.describe().to_csv(f,sep=',',header=True)  
    '''
    m_straight_df.describe().to_csv(f,sep=',',header=True)  
    w_straight_df.describe().to_csv(f,sep=',',header=True)  
    c_turn_df.describe().to_csv(f,sep=',',header=True)  
    m_turn_df.describe().to_csv(f,sep=',',header=True) 
    w_turn_df.describe().to_csv(f,sep=',',header=True) 
    '''
print 'extrace Feature done'

