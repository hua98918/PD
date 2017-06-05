# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:51:16 2017

@author: Ariel
#function： read in the 

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


#input_file = "C:\pakinsen\Vicon\WALKER2016\PDLip160509\PDlip160509c02feature.csv"
input_file = "C:\pakinsen\Vicon\AllSwing.csv"
output_file = "C:\pakinsen\Vicon\PDmil160429Turn.csv"
dn = "C:\pakinsen\Vicon\\"
fn = "PDmil160429"

#PDkal160525   PDlip160509  PTtob160517  PDsey160502 PDpra160407 PDmil160429

df = pd.read_csv(input_file, sep=",")
df.fillna(method='ffill')
df.head()

name = df['name'].map(lambda x: x.startswith(fn))
straight_df = df[(df['position'] == 1) & name]
straight_grouped = straight_df.groupby(['name'])

#name_ticks = straight_df['name'].tolist()
#name_ticks = name_ticks.split(fn)
'''
pd.options.display.mpl_style = 'default'
straight_df.boxplot(['C','RightGCT','LeftStance','RightStance',\
             'LeftSwing','RightSwing'],by='name')
savefig('C:\pakinsen\Vicon\PDkal160525Box1.png')
straight_df.boxplot(['ZStideHeightL','ZStideHeightR'],by='name')
savefig('C:\pakinsen\Vicon\PDkal160525Box2.png')
'''

####using plotly online visualize data#####
mins = straight_grouped.min()
maxes = straight_grouped.max()
means = straight_grouped.mean()
std = straight_grouped.std()


trace1 = []
trace2 = []
trace1 = go.Bar(x=means.index, y=means.LeftGCT, error_y=dict(type='trace1',array=std.LeftGCT,visible=True), name='Left')
trace2 = go.Bar(x=means.index, y=means.RightGCT, error_y=dict(type='trace2',array=std.RightGCT,visible=True), name='Right')

data = [trace1, trace2]

layout = go.Layout(barmode='group', xaxis=go.XAxis(type='names') ,title= fn+" Turn phase Left Right Gait Cycle Time(GCT) Bar Chart")
fig = go.Figure(data=data, layout=layout)
# IPython notebook
#py.iplot(fig, filename='GCT_Left_Right_errorbar')
url = py.plot(fig, filename=fn+' Turn phase GCT_Left_Right_errorbar')
#py.image.save_as(fig, filename=fn+' Turn phase GCT_Left_Right_errorbar')


trace3 = []
trace4 = []
trace5 = []
trace6 = []
trace7 = []
trace8 = []
trace3 = go.Bar(x=means.index, y=means.LeftStance, error_y=dict(type='trace3',array=std.LeftStance,visible=True), name='Left Stance')
trace4 = go.Bar(x=means.index, y=means.LeftSwing, error_y=dict(type='trace4',array=std.LeftSwing,visible=True), name='Left Swing')
trace5 = go.Bar(x=means.index, y=means.RightStance, error_y=dict(type='trace5',array=std.RightStance,visible=True), name='Right Stance')
trace6 = go.Bar(x=means.index, y=means.RightSwing, error_y=dict(type='trace6',array=std.RightSwing,visible=True), name='Right Swing')
trace7 = go.Bar(x=means.index, y=means.LeftIDS, error_y=dict(type='trace7',array=std.LeftIDS,visible=True), name='Left IDS')
trace8 =go.Bar(x=means.index, y=means.RightIDS, error_y=dict(type='trace8',array=std.RightIDS,visible=True), name='Right IDS')

data = [trace3, trace4, trace5, trace6, trace7, trace8]

layout = go.Layout(barmode='group', xaxis=go.XAxis(type='names'),title= fn+" Turn phase Swing Stance IDS Bar Chart" )
fig = go.Figure(data=data, layout=layout)
# IPython notebook
#py.iplot(fig, filename='Swing Stance IDS Bar Chart')
url = py.plot(fig, filename=fn+' Turn phase Swing Stance IDS Bar Chart')
#py.image.save_as(fig, filename=fn+' Turn phase Swing Stance IDS Bar Chart')

trace1 = []
trace2 = []
trace3 = []
trace4 = []
trace1 = go.Bar(x=means.index, y=means.ZStideHeightL, error_y=dict(type='trace1',array=std.ZStideHeightL,visible=True), name='Left Stride Height')
trace2 = go.Bar(x=means.index, y=means.ZStideHeightR, error_y=dict(type='trace2',array=std.ZStideHeightR,visible=True), name='Right Stride Height')
trace3 = go.Bar(x=means.index, y=means.XStideLengthL, error_y=dict(type='trace3',array=std.XStideLengthL,visible=True), name='Left Stride Length')
trace4 = go.Bar(x=means.index, y=means.XStideLengthR, error_y=dict(type='trace4',array=std.XStideLengthR,visible=True), name='Right Stride Length')
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(barmode='group', xaxis=go.XAxis(type='names'),title= fn+ " Turn phase Stride Height and Length Bar Chart" )
fig = go.Figure(data=data, layout=layout)
# IPython notebook
#py.iplot(fig, filename='Stride Height and Length Bar Chart')
url = py.plot(fig, filename=fn+' Turn phase Stride Height and Length Bar Chart')
#py.image.save_as(fig, filename=fn+' Turn phase Stride Height and Length Bar Chart')


trace1 = []
trace2 = []
trace1 = go.Bar(x=means.index, y=means.XStideVelocityL, error_y=dict(type='trace1',array=std.XStideVelocityL,visible=True), name='Left Velocity')
trace2 = go.Bar(x=means.index, y=means.XStideVelocityR, error_y=dict(type='trace2',array=std.XStideVelocityR,visible=True), name='Right Velocity')
data = [trace1, trace2]
layout = go.Layout(barmode='group', xaxis=go.XAxis(type='names'),title= fn+ " Turn phase Stride Velocity Bar Chart" )
fig = go.Figure(data=data, layout=layout)
# IPython notebook
#py.iplot(fig, filename='Stride Height and Length Bar Chart')
url = py.plot(fig, filename=fn+' Turn phase Stride Velocity Bar Chart')
#py.image.save_as(fig, filename=fn+' Turn phase Stride Velocity Bar Chart')



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

