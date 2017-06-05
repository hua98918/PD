# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:13:29 2017

@author: Ariel
"""

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

def symmetric(L, R):
    print L-R
    return (L-R)/max(L,R)


#input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c02feature.csv"
input_file = "C:\pakinsen\Vicon\AllSwing.csv"
output_file_1 = "C:\pakinsen\Vicon\StraightSum.csv"
output_file_2 = "C:\pakinsen\Vicon\TurnSum.csv"

df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')
df.head()

#name = df['name'].map(lambda x: x.startswith('PDlip160509'))
c_straight_df = df[(df['position'] == 0) & (df['type'] == 'c') ]
c_turn_df = df[(df['position'] == 1) & (df['type'] == 'c') ]
ml_straight_df = df[(df['position'] == 0) & (df['type'] == 'ml') ]
ml_turn_df = df[(df['position'] == 1) & (df['type'] == 'ml') ]
mm_straight_df = df[(df['position'] == 0) & (df['type'] == 'mm') ]
mm_turn_df = df[(df['position'] == 1) & (df['type'] == 'mm') ]
mh_straight_df = df[(df['position'] == 0) & (df['type'] == 'mh') ]
mh_turn_df = df[(df['position'] == 1) & (df['type'] == 'mh') ]
w_straight_df = df[(df['position'] == 0) & (df['type'] == 'w') ]
w_turn_df = df[(df['position'] == 1) & (df['type'] == 'w') ]


c_turn_df['LSL']= np.sqrt(np.square(c_turn_df['XStideLengthL']) + np.square(c_turn_df['YStideLengthL']))
c_turn_df['RSL']= np.sqrt(np.square(c_turn_df['XStideLengthR']) + np.square(c_turn_df['YStideLengthR']))
ml_turn_df['LSL']= np.sqrt(np.square(ml_turn_df['XStideLengthL']) + np.square(ml_turn_df['YStideLengthL']))
ml_turn_df['RSL']= np.sqrt(np.square(ml_turn_df['XStideLengthR']) + np.square(ml_turn_df['YStideLengthR']))
mm_turn_df['LSL']= np.sqrt(np.square(mm_turn_df['XStideLengthL']) + np.square(mm_turn_df['YStideLengthL']))
mm_turn_df['RSL']= np.sqrt(np.square(mm_turn_df['XStideLengthR']) + np.square(mm_turn_df['YStideLengthR']))
mh_turn_df['LSL']= np.sqrt(np.square(mh_turn_df['XStideLengthL']) + np.square(mh_turn_df['YStideLengthL']))
mh_turn_df['RSL']= np.sqrt(np.square(mh_turn_df['XStideLengthR']) + np.square(mh_turn_df['YStideLengthR']))
w_turn_df['LSL']= np.sqrt(np.square(w_turn_df['XStideLengthL']) + np.square(w_turn_df['YStideLengthL']))
w_turn_df['RSL']= np.sqrt(np.square(w_turn_df['XStideLengthR']) + np.square(w_turn_df['YStideLengthR']))

c_turn_df['LVel']= np.sqrt(np.square(c_turn_df['XStideVelocityL']) + np.square(c_turn_df['YStideVelocityL']))
c_turn_df['RVel']= np.sqrt(np.square(c_turn_df['XStideVelocityR']) + np.square(c_turn_df['YStideVelocityR']))
ml_turn_df['LVel']= np.sqrt(np.square(ml_turn_df['XStideVelocityL']) + np.square(ml_turn_df['YStideVelocityL']))
ml_turn_df['RVel']= np.sqrt(np.square(ml_turn_df['XStideVelocityR']) + np.square(ml_turn_df['YStideVelocityR']))
mm_turn_df['LVel']= np.sqrt(np.square(mm_turn_df['XStideVelocityL']) + np.square(mm_turn_df['YStideVelocityL']))
mm_turn_df['RVel']= np.sqrt(np.square(mm_turn_df['XStideVelocityR']) + np.square(mm_turn_df['YStideVelocityR']))
mh_turn_df['LVel']= np.sqrt(np.square(mh_turn_df['XStideVelocityL']) + np.square(mh_turn_df['YStideVelocityL']))
mh_turn_df['RVel']= np.sqrt(np.square(mh_turn_df['XStideVelocityR']) + np.square(mh_turn_df['YStideVelocityR']))
w_turn_df['LVel']= np.sqrt(np.square(w_turn_df['XStideVelocityL']) + np.square(w_turn_df['YStideVelocityL']))
w_turn_df['RVel']= np.sqrt(np.square(w_turn_df['XStideVelocityR']) + np.square(w_turn_df['YStideVelocityR']))

c_turn_df['GCTsymmetric'] =  (c_turn_df['RightGCT']-c_turn_df['LeftGCT'])/c_turn_df[['RightGCT','LeftGCT']].max(axis=1)
c_turn_df['SHsymmetric'] =  (c_turn_df['ZStideHeightR'] - c_turn_df['ZStideHeightL'])/c_turn_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
c_turn_df['SLsymmetric'] =  (c_turn_df['RSL']- c_turn_df['LSL'])/c_turn_df[['RSL','LSL']].max(axis=1)
c_turn_df['Velsymmetric'] =  (c_turn_df['RVel'] - c_turn_df['LVel']) / c_turn_df[['RVel','LVel']].max(axis=1)
ml_turn_df['GCTsymmetric'] =  (ml_turn_df['RightGCT']-ml_turn_df['LeftGCT'])/ml_turn_df[['RightGCT','LeftGCT']].max(axis=1)
ml_turn_df['SHsymmetric'] =  (ml_turn_df['ZStideHeightR'] - ml_turn_df['ZStideHeightL'])/ml_turn_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
ml_turn_df['SLsymmetric'] =  (ml_turn_df['RSL']- ml_turn_df['LSL'])/ml_turn_df[['RSL','LSL']].max(axis=1)
ml_turn_df['Velsymmetric'] =  (ml_turn_df['RVel'] - ml_turn_df['LVel']) / ml_turn_df[['RVel','LVel']].max(axis=1)
mm_turn_df['GCTsymmetric'] =  (mm_turn_df['RightGCT']-mm_turn_df['LeftGCT'])/mm_turn_df[['RightGCT','LeftGCT']].max(axis=1)
mm_turn_df['SHsymmetric'] =  (mm_turn_df['ZStideHeightR'] - mm_turn_df['ZStideHeightL'])/mm_turn_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
mm_turn_df['SLsymmetric'] =  (mm_turn_df['RSL']- mm_turn_df['LSL'])/mm_turn_df[['RSL','LSL']].max(axis=1)
mm_turn_df['Velsymmetric'] =  (mm_turn_df['RVel'] - mm_turn_df['LVel']) / mm_turn_df[['RVel','LVel']].max(axis=1)
mh_turn_df['GCTsymmetric'] =  (mh_turn_df['RightGCT']-mh_turn_df['LeftGCT'])/mh_turn_df[['RightGCT','LeftGCT']].max(axis=1)
mh_turn_df['SHsymmetric'] =  (mh_turn_df['ZStideHeightR'] - mh_turn_df['ZStideHeightL'])/mh_turn_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
mh_turn_df['SLsymmetric'] =  (mh_turn_df['RSL']- mh_turn_df['LSL'])/mh_turn_df[['RSL','LSL']].max(axis=1)
mh_turn_df['Velsymmetric'] =  (mh_turn_df['RVel'] - mh_turn_df['LVel']) / mh_turn_df[['RVel','LVel']].max(axis=1)
w_turn_df['GCTsymmetric'] =  (w_turn_df['RightGCT']-w_turn_df['LeftGCT'])/w_turn_df[['RightGCT','LeftGCT']].max(axis=1)
w_turn_df['SHsymmetric'] =  (w_turn_df['ZStideHeightR'] - w_turn_df['ZStideHeightL'])/w_turn_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
w_turn_df['SLsymmetric'] =  (w_turn_df['RSL']- w_turn_df['LSL'])/w_turn_df[['RSL','LSL']].max(axis=1)
w_turn_df['Velsymmetric'] =  (w_turn_df['RVel'] - w_turn_df['LVel']) / w_turn_df[['RVel','LVel']].max(axis=1)


'''
c_turn_df['GCTsymmetric'] =  c_turn_df['RightGCT']/c_turn_df['LeftGCT'] 
c_turn_df['SHsymmetric'] =  c_turn_df['ZStideHeightR']/ c_turn_df['ZStideHeightL'] 
c_turn_df['SLsymmetric'] =  c_turn_df['RSL']/c_turn_df['LVel'] 
c_turn_df['Velsymmetric'] =  c_turn_df['RVel'] / c_turn_df['LVel'] 
ml_turn_df['GCTsymmetric'] =  ml_turn_df['RightGCT']/ml_turn_df['LeftGCT'] 
ml_turn_df['SHsymmetric'] =  ml_turn_df['ZStideHeightR']/ml_turn_df['ZStideHeightL'] 
ml_turn_df['SLsymmetric'] =  ml_turn_df['RSL'] / ml_turn_df['LSL'] 
ml_turn_df['Velsymmetric'] =  ml_turn_df['RVel'] / ml_turn_df['LVel'] 
mm_turn_df['GCTsymmetric'] =  mm_turn_df['RightGCT'] /mm_turn_df['LeftGCT'] 
mm_turn_df['SHsymmetric'] =  mm_turn_df['ZStideHeightR'] / mm_turn_df['ZStideHeightL'] 
mm_turn_df['SLsymmetric'] =  mm_turn_df['RSL']/ mm_turn_df['LSL'] 
mm_turn_df['Velsymmetric'] =  mm_turn_df['RVel'] / mm_turn_df['LVel'] 
mh_turn_df['GCTsymmetric'] =  mh_turn_df['RightGCT'] / mh_turn_df['LeftGCT'] 
mh_turn_df['SHsymmetric'] =  mh_turn_df['ZStideHeightR']/ mh_turn_df['ZStideHeightL'] 
mh_turn_df['SLsymmetric'] =  mh_turn_df['RSL']/ mh_turn_df['LSL'] 
mh_turn_df['Velsymmetric'] =  mh_turn_df['RVel']/ mh_turn_df['LVel'] 
w_turn_df['GCTsymmetric'] =  w_turn_df['RightGCT'] / w_turn_df['LeftGCT'] 
w_turn_df['SHsymmetric'] =  w_turn_df['ZStideHeightR'] / w_turn_df['ZStideHeightL'] 
w_turn_df['SLsymmetric'] =  w_turn_df['RSL'] / w_turn_df['LSL'] 
w_turn_df['Velsymmetric'] =  w_turn_df['RVel'] / w_turn_df['LVel'] 
'''


c_straight_df['LSL']= np.sqrt(np.square(c_straight_df['XStideLengthL']) + np.square(c_straight_df['YStideLengthL']))
c_straight_df['RSL']= np.sqrt(np.square(c_straight_df['XStideLengthR']) + np.square(c_straight_df['YStideLengthR']))
ml_straight_df['LSL']= np.sqrt(np.square(ml_straight_df['XStideLengthL']) + np.square(ml_straight_df['YStideLengthL']))
ml_straight_df['RSL']= np.sqrt(np.square(ml_straight_df['XStideLengthR']) + np.square(ml_straight_df['YStideLengthR']))
mm_straight_df['LSL']= np.sqrt(np.square(mm_straight_df['XStideLengthL']) + np.square(mm_straight_df['YStideLengthL']))
mm_straight_df['RSL']= np.sqrt(np.square(mm_straight_df['XStideLengthR']) + np.square(mm_straight_df['YStideLengthR']))
mh_straight_df['LSL']= np.sqrt(np.square(mh_straight_df['XStideLengthL']) + np.square(mh_straight_df['YStideLengthL']))
mh_straight_df['RSL']= np.sqrt(np.square(mh_straight_df['XStideLengthR']) + np.square(mh_straight_df['YStideLengthR']))
w_straight_df['LSL']= np.sqrt(np.square(w_straight_df['XStideLengthL']) + np.square(w_straight_df['YStideLengthL']))
w_straight_df['RSL']= np.sqrt(np.square(w_straight_df['XStideLengthR']) + np.square(w_straight_df['YStideLengthR']))

c_straight_df['LVel']= np.sqrt(np.square(c_straight_df['XStideVelocityL']) + np.square(c_straight_df['YStideVelocityL']))
c_straight_df['RVel']= np.sqrt(np.square(c_straight_df['XStideVelocityR']) + np.square(c_straight_df['YStideVelocityR']))
ml_straight_df['LVel']= np.sqrt(np.square(ml_straight_df['XStideVelocityL']) + np.square(ml_straight_df['YStideVelocityL']))
ml_straight_df['RVel']= np.sqrt(np.square(ml_straight_df['XStideVelocityR']) + np.square(ml_straight_df['YStideVelocityR']))
mm_straight_df['LVel']= np.sqrt(np.square(mm_straight_df['XStideVelocityL']) + np.square(mm_straight_df['YStideVelocityL']))
mm_straight_df['RVel']= np.sqrt(np.square(mm_straight_df['XStideVelocityR']) + np.square(mm_straight_df['YStideVelocityR']))
mh_straight_df['LVel']= np.sqrt(np.square(mh_straight_df['XStideVelocityL']) + np.square(mh_straight_df['YStideVelocityL']))
mh_straight_df['RVel']= np.sqrt(np.square(mh_straight_df['XStideVelocityR']) + np.square(mh_straight_df['YStideVelocityR']))
w_straight_df['LVel']= np.sqrt(np.square(w_straight_df['XStideVelocityL']) + np.square(w_straight_df['YStideVelocityL']))
w_straight_df['RVel']= np.sqrt(np.square(w_straight_df['XStideVelocityR']) + np.square(w_straight_df['YStideVelocityR']))


c_straight_df['GCTsymmetric'] =  (c_straight_df['RightGCT']-c_straight_df['LeftGCT'])/c_straight_df[['RightGCT','LeftGCT']].max(axis=1)
c_straight_df['SHsymmetric'] =  (c_straight_df['ZStideHeightR'] - c_straight_df['ZStideHeightL'])/c_straight_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
c_straight_df['SLsymmetric'] =  (c_straight_df['RSL']- c_straight_df['LSL'])/c_straight_df[['RSL','LSL']].max(axis=1)
c_straight_df['Velsymmetric'] =  (c_straight_df['RVel'] - c_straight_df['LVel']) / c_straight_df[['RVel','LVel']].max(axis=1)
ml_straight_df['GCTsymmetric'] =  (ml_straight_df['RightGCT']-ml_straight_df['LeftGCT'])/ml_straight_df[['RightGCT','LeftGCT']].max(axis=1)
ml_straight_df['SHsymmetric'] =  (ml_straight_df['ZStideHeightR'] - ml_straight_df['ZStideHeightL'])/ml_straight_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
ml_straight_df['SLsymmetric'] =  (ml_straight_df['RSL']- ml_straight_df['LSL'])/ml_straight_df[['RSL','LSL']].max(axis=1)
ml_straight_df['Velsymmetric'] =  (ml_straight_df['RVel'] - ml_straight_df['LVel']) / ml_straight_df[['RVel','LVel']].max(axis=1)
mm_straight_df['GCTsymmetric'] =  (mm_straight_df['RightGCT']-mm_straight_df['LeftGCT'])/mm_straight_df[['RightGCT','LeftGCT']].max(axis=1)
mm_straight_df['SHsymmetric'] =  (mm_straight_df['ZStideHeightR'] - mm_straight_df['ZStideHeightL'])/mm_straight_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
mm_straight_df['SLsymmetric'] =  (mm_straight_df['RSL']- mm_straight_df['LSL'])/mm_straight_df[['RSL','LSL']].max(axis=1)
mm_straight_df['Velsymmetric'] =  (mm_straight_df['RVel'] - mm_straight_df['LVel']) / mm_straight_df[['RVel','LVel']].max(axis=1)
mh_straight_df['GCTsymmetric'] =  (mh_straight_df['RightGCT']-mh_straight_df['LeftGCT'])/mh_straight_df[['RightGCT','LeftGCT']].max(axis=1)
mh_straight_df['SHsymmetric'] =  (mh_straight_df['ZStideHeightR'] - mh_straight_df['ZStideHeightL'])/mh_straight_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
mh_straight_df['SLsymmetric'] =  (mh_straight_df['RSL']- mh_straight_df['LSL'])/mh_straight_df[['RSL','LSL']].max(axis=1)
mh_straight_df['Velsymmetric'] =  (mh_straight_df['RVel'] - mh_straight_df['LVel']) / mh_straight_df[['RVel','LVel']].max(axis=1)
w_straight_df['GCTsymmetric'] =  (w_straight_df['RightGCT']-w_straight_df['LeftGCT'])/w_straight_df[['RightGCT','LeftGCT']].max(axis=1)
w_straight_df['SHsymmetric'] =  (w_straight_df['ZStideHeightR'] - w_straight_df['ZStideHeightL'])/w_straight_df[['ZStideHeightR','ZStideHeightL']].max(axis=1)
w_straight_df['SLsymmetric'] =  (w_straight_df['RSL']- w_straight_df['LSL'])/w_straight_df[['RSL','LSL']].max(axis=1)
w_straight_df['Velsymmetric'] =  (w_straight_df['RVel'] - w_straight_df['LVel']) / w_straight_df[['RVel','LVel']].max(axis=1)





'''
c_straight_df['GCTsymmetric'] =  c_straight_df['RightGCT']/c_straight_df['LeftGCT'] 
c_straight_df['SHsymmetric'] =  c_straight_df['ZStideHeightR']/ c_straight_df['ZStideHeightL'] 
c_straight_df['SLsymmetric'] =  c_straight_df['RSL']/c_straight_df['LVel'] 
c_straight_df['Velsymmetric'] =  c_straight_df['RVel'] / c_straight_df['LVel'] 
ml_straight_df['GCTsymmetric'] =  ml_straight_df['RightGCT']/ml_straight_df['LeftGCT'] 
ml_straight_df['SHsymmetric'] =  ml_straight_df['ZStideHeightR']/ml_straight_df['ZStideHeightL'] 
ml_straight_df['SLsymmetric'] =  ml_straight_df['RSL'] / ml_straight_df['LSL'] 
ml_straight_df['Velsymmetric'] =  ml_straight_df['RVel'] / ml_straight_df['LVel'] 
mm_straight_df['GCTsymmetric'] =  mm_straight_df['RightGCT'] /mm_straight_df['LeftGCT'] 
mm_straight_df['SHsymmetric'] =  mm_straight_df['ZStideHeightR'] / mm_straight_df['ZStideHeightL'] 
mm_straight_df['SLsymmetric'] =  mm_straight_df['RSL']/ mm_straight_df['LSL'] 
mm_straight_df['Velsymmetric'] =  mm_straight_df['RVel'] / mm_straight_df['LVel'] 
mh_straight_df['GCTsymmetric'] =  mh_straight_df['RightGCT'] / mh_straight_df['LeftGCT'] 
mh_straight_df['SHsymmetric'] =  mh_straight_df['ZStideHeightR']/ mh_straight_df['ZStideHeightL'] 
mh_straight_df['SLsymmetric'] =  mh_straight_df['RSL']/ mh_straight_df['LSL'] 
mh_straight_df['Velsymmetric'] =  mh_straight_df['RVel']/ mh_straight_df['LVel'] 
w_straight_df['GCTsymmetric'] =  w_straight_df['RightGCT'] / w_straight_df['LeftGCT'] 
w_straight_df['SHsymmetric'] =  w_straight_df['ZStideHeightR'] / w_straight_df['ZStideHeightL'] 
w_straight_df['SLsymmetric'] =  w_straight_df['RSL'] / w_straight_df['LSL'] 
w_straight_df['Velsymmetric'] =  w_straight_df['RVel'] / w_straight_df['LVel'] 
'''


'''
c_straight_df['GCTsymmetric'] =  c_straight_df['RightGCT'] / c_straight_df['LeftGCT'] 
c_straight_df['SHsymmetric'] =  c_straight_df['ZStideHeightR'] / c_straight_df['ZStideHeightL'] 
c_straight_df['SLsymmetric'] =  c_straight_df['XStideLengthR'] / c_straight_df['XStideLengthL'] 
c_straight_df['Velsymmetric'] =  c_straight_df['XStideVelocityR'] / c_straight_df['XStideVelocityL'] 
ml_straight_df['GCTsymmetric'] =  ml_straight_df['RightGCT'] / ml_straight_df['LeftGCT'] 
ml_straight_df['SHsymmetric'] =  ml_straight_df['ZStideHeightR'] / ml_straight_df['ZStideHeightL'] 
ml_straight_df['SLsymmetric'] =  ml_straight_df['XStideLengthR'] / ml_straight_df['XStideLengthL'] 
ml_straight_df['Velsymmetric'] =  ml_straight_df['XStideVelocityR'] / ml_straight_df['XStideVelocityL'] 
mm_straight_df['GCTsymmetric'] =  mm_straight_df['RightGCT'] / mm_straight_df['LeftGCT'] 
mm_straight_df['SHsymmetric'] =  mm_straight_df['ZStideHeightR'] / mm_straight_df['ZStideHeightL'] 
mm_straight_df['SLsymmetric'] =  mm_straight_df['XStideLengthR'] / mm_straight_df['XStideLengthL'] 
mm_straight_df['Velsymmetric'] =  mm_straight_df['XStideVelocityR'] / mm_straight_df['XStideVelocityL'] 
mh_straight_df['GCTsymmetric'] =  mh_straight_df['RightGCT']/ mh_straight_df['LeftGCT'] 
mh_straight_df['SHsymmetric'] =  mh_straight_df['ZStideHeightR'] / mh_straight_df['ZStideHeightL'] 
mh_straight_df['SLsymmetric'] =  mh_straight_df['XStideLengthR'] / mh_straight_df['XStideLengthL'] 
mh_straight_df['Velsymmetric'] =  mh_straight_df['XStideVelocityR'] / mh_straight_df['XStideVelocityL'] 
w_straight_df['GCTsymmetric'] =  w_straight_df['RightGCT'] / w_straight_df['LeftGCT'] 
w_straight_df['SHsymmetric'] =  w_straight_df['ZStideHeightR'] / w_straight_df['ZStideHeightL'] 
w_straight_df['SLsymmetric'] =  w_straight_df['XStideLengthR'] / w_straight_df['XStideLengthL'] 
w_straight_df['Velsymmetric'] =  w_straight_df['XStideVelocityR'] / w_straight_df['XStideVelocityL'] 
'''
#straight_df = df[(df['position'] ==0)]

#straight_df = df[(df['position'] ==1)]
#straight_grouped = straight_df.groupby(['type'])


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

with open(output_file_1, 'a') as f1:
    #df.to_csv(f,sep=',',header=True)
    #straight_grouped.describe().to_csv(f,sep=',',header=True)  
    c_straight_df.describe().to_csv(f1,sep=',',header=True)
    ml_straight_df.describe().to_csv(f1,sep=',',header=True)  
    mm_straight_df.describe().to_csv(f1,sep=',',header=True)  
    mh_straight_df.describe().to_csv(f1,sep=',',header=True)  
    w_straight_df.describe().to_csv(f1,sep=',',header=True)  
    
with open(output_file_2, 'a') as f2:    
    c_turn_df.describe().to_csv(f2,sep=',',header=True)
    ml_turn_df.describe().to_csv(f2,sep=',',header=True)  
    mm_turn_df.describe().to_csv(f2,sep=',',header=True)  
    mh_turn_df.describe().to_csv(f2,sep=',',header=True)  
    w_turn_df.describe().to_csv(f2,sep=',',header=True)  
    #c_turn_df.describe().to_csv(f,sep=',',header=True)  
    #m_turn_df.describe().to_csv(f,sep=',',header=True) 
    #w_turn_df.describe().to_csv(f,sep=',',header=True) 

print 'extrace Feature done'

