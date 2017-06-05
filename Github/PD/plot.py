# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:27:43 2016

@author: zhang
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
x = []

def plotdata(originalFile,filterFile):
    with open(originalFile,'r') as csvfile:
        plot1 = csv.reader(csvfile, delimiter=',')
        fileds = plot1.next()  #read the next line
        for row in plot1:
            a.append(int(row[0]))  #package
            b.append(float(row[1]))  #gyroX
            c.append(float(row[2]))  #gyroY
            d.append(float(row[3]))  #gyroZ
            e.append(float(row[4]))  #accelX
            f.append(float(row[5]))  #accelY
            g.append(float(row[6]))  #accelZ
            h.append(float(row[7]))  #magnetX
            i.append(float(row[8]))  #magnetY          
            j.append(float(row[9]))  #magnetZ             
    
    with open(filterFile,'r') as f2:
        plot2 = csv.reader(f2, delimiter=',')
        next(plot2)  #read the next line
        for row in plot2:
            x.append(int(row[1]))  #package
            m.append(float(row[2]))  #gyroX
            n.append(float(row[3]))  #gyroY
            o.append(float(row[4]))  #gyroZ
            p.append(float(row[5]))  #accelX
            q.append(float(row[6]))  #accelY
            r.append(float(row[7]))  #accelZ
            s.append(float(row[8]))  #magnetX
            t.append(float(row[9]))  #magnetY
            u.append(float(row[10]))  #magnetZ      


       
    fig = plt.figure()

    ax1 = fig.add_subplot(331)
    ax1.set_ylabel('Gyroscope deg/s')
    ax1.set_title('Gyroscope X')
    ax1.plot(a,b)
    ax1.plot(x,m,'r')

    ax2 = fig.add_subplot(332)
    ax2.set_title('Gyroscope Y')
    ax2.plot(a,c)
    ax2.plot(x,n,'r')

    ax3 = fig.add_subplot(333)
    ax3.set_title('Gyroscope Z')
    ax3.plot(a,d)
    ax3.plot(x,o,'r')
  
    ax4 = fig.add_subplot(334)
    ax4.set_ylabel('Accelerometer g/s')
    ax4.set_title('Accelerometer X')
    ax4.plot(a,e)
    ax4.plot(x,p,'r')
    
    ax5 = fig.add_subplot(335)
    ax5.set_title('Accelerometer Y')
    ax5.plot(a,f)
    ax5.plot(x,q,'r')

    ax6 = fig.add_subplot(336)
    ax6.set_title('Accelerometer Z')
    ax6.plot(a,g)
    ax6.plot(x,r,'r')

    ax7 = fig.add_subplot(337)
    ax7.set_title('MagnetMeter G')
    ax7.set_title('MagnetMeter X')
    ax7.plot(a,h)
    ax7.plot(x,s,'r')
    
    ax8 = fig.add_subplot(338)
    ax8.set_title('MagnetMeter Y')
    ax8.plot(a,i)
    ax8.plot(x,t,'r')    
    
    ax9 = fig.add_subplot(339)
    ax9.set_title('MagnetMeter Y')
    ax9.plot(a,j)
    ax9.plot(x,u,'r')    
    
    plt.legend()
    plt.show()       
    
def getParser():
    usage="""
    {program} original_data filter_data"""   
    parser =argparse.ArgumentParser(description="plot the orignal and filter data", usage=usage)
    parser.add_argument("input_file",help="input orignal data file name")

    parser.add_argument("filter_file",help="input filtered data file name")
    args= parser.parse_args()
    #print args
    return args



def main():
    args = getParser()
    print(args.input_file)
    plotdata(args.input_file,args.filter_file)
    


if __name__ == "__main__":
    main()