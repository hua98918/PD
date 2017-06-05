# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:49:14 2017

@author: Ariel
"""

import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import os
import rdp

dn = "C:\pakinsen\Vicon\WALKER2016\PDkal160525"
##dn = PDkal160525  PDLip160509   PDmil160429 PDpra160407  PDsey160502 PDtob160517

'''
input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525m02feature.csv"
output_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\TurnAngle.csv"
fn = "PDkal160525m02"
#print df.head()
'''

### truncate the beginning of straight walking part
WindowsSize = 40  
def turndf(df):
    turnStartDF1 = df.loc[(df['HeelLY'].rolling(WindowsSize).max()- df['HeelLY'].rolling(WindowsSize).min())>60].head(1)
    turnStartDF2 = df.loc[(df['HeelRY'].rolling(WindowsSize).max()- df['HeelRY'].rolling(WindowsSize).min())>60].head(1)
    startIndex = min(int(turnStartDF1.index.get_values()),int(turnStartDF2.index.get_values()))
    print startIndex
    turndf= df[startIndex:]
    return turndf

def angle(dir):
    """
    Returns the angles between vectors.

    Parameters:
    dir is a 2D-array of shape (N,M) representing N vectors in M-dimensional space.

    The return value is a 1D-array of values of shape (N-1,), with each value
    between 0 and pi.

    0 implies the vectors point in the same direction
    pi/2 implies the vectors are orthogonal
    pi implies the vectors point in opposite directions
    """
    dir2 = dir[1:]
    dir1 = dir[:-1]
    return np.arccos((dir1*dir2).sum(axis=1)/(
        np.sqrt((dir1**2).sum(axis=1)*(dir2**2).sum(axis=1))))


def extract(input_file, output_file):
    df = pd.read_csv(input_file, sep=",")   
  
    df=turndf(df)
    Lxdata=np.array(df['shLX'])
    Lydata=np.array(df['shLY'])
    Rxdata=np.array(df['shRX'])
    Rydata=np.array(df['shRY'])
        
    tolerance = 70
    min_angle = np.pi*0.11
    max_angle = np.pi*0.99
    Lpoints = zip(Lxdata,Lydata)
    Rpoints = zip(Rxdata,Rydata)
    print(len(Lpoints))
    
    # Use the Ramer-Douglas-Peucker algorithmta to simplify the path
    # http://en.wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm
    # Python implementation: https://github.com/sebleier/RDP/
    Lsimplified = np.array(rdp.rdp(Lpoints, tolerance))
    Rsimplified = np.array(rdp.rdp(Rpoints, tolerance))
    
    
    lsx, lsy = Lsimplified.T
    rsx, rsy = Rsimplified.T   #unzip to array
    
    # compute the direction vectors on the simplified curve
    Ldirections = np.diff(Lsimplified, axis=0)
    Ltheta = angle(Ldirections)
    # Select the index of the points with the greatest theta
    # Large theta is associated with greatest change in direction.
    Lidx = np.where(Ltheta>min_angle)[0]+1
    Lidx = np.where(Ltheta<max_angle)[0]+1               
    
    # compute the direction vectors on the simplified curve
    Rdirections = np.diff(Rsimplified, axis=0)
    Rtheta = angle(Rdirections)
    print Rtheta
    # Select the index of the points with the greatest theta
    # Large theta is associated with greatest change in direction.
    Ridx = np.where(Rtheta>min_angle)[0]+1        
    Ridx = np.where(Rtheta<max_angle)[0]+1

    
    with open(output_file, 'a') as f:
        for x in Ltheta:
            f.write(fn)          
            f.write(",")  
            f.write("Left")          
            f.write(",")  
            f.write(str(x))
            f.write(",")
            f.write("\n")   
        for x in Rtheta:
            f.write(fn)          
            f.write(",")
            f.write("Right")          
            f.write(",")  
            f.write(str(x))
            f.write(",")
            f.write("\n")   
        
    fig = plt.figure()
    ax =fig.add_subplot(111)
    ax.plot(df[['shLX']],df[['shLY']],label='left side')
    ax.plot(df[['shRX']],df[['shRY']],c='r',label='right side')
    ax.plot(lsx, lsy, 'g--', label='simplified path')
    ax.plot(rsx, rsy, 'g--')
    ax.plot(lsx[Lidx], lsy[Lidx], 'ro', markersize = 10, label='turning points')
    ax.plot(rsx[Ridx], rsy[Ridx], 'ro', markersize = 10)
    #ax.invert_yaxis()
    ax.set_title("P1"+ fn[11:14]+"Turn")
    plt.legend(loc='best')
    plt.show()
    plt.savefig(str(dn)+'\\'+str(fn)+ 'Turn.png')
    


for filename in os.listdir(dn):
    if filename.endswith("feature.csv") : 
        input_file = os.path.join(dn, filename)
        fn, file_extension = os.path.splitext(filename)
        print fn
        output_file = os.path.join(dn,'TurnAngle.csv')
        print output_file
        extract(input_file,output_file)
    else:
        continue



#def func(x, p1,p2):
#  return p1*np.cos(p2*x) + p2*np.sin(p1*x)

#def func(x, a, b, c):
#    return a * np.exp(-b * x) + c

#def func(x, a, b, c, d):
#    return a * np.sin(b*x + c) + d
'''
def func(x, a, b, c):
    return a * x*x+ b*x + c

fitParams, fitCovariances = curve_fit(func, xdata, ydata)
x = np.linspace(min(xdata), max(xdata), 1000)


fig1 = plt.figure(figsize=(20, 10))
ax1 = fig1.add_subplot(111)
ax1.scatter(df[['shLX']],df[['shLY']],label='left side')
ax1.scatter(df[['shRX']],df[['shRY']],c='r',label='right side')
ax1.plot(x, func(x, *fitParams), 'g-', label='fit')
ax1.set_title('shoulder Plot')
ax1.legend()
plt.show()

#scipy.optimize.curve_fit(func, df[['shLX']].to, df[['shLY']], p0=None, sigma=None)



#C = np.polyfit(x, y, 3)
#fit = np.polyval(C,x)


'''
