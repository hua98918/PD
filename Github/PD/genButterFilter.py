# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:27:20 2016

@author: zhang
"""
import argparse
import csv
import os
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Sample rate and desired cutoff frequencies (in Hz).
fs = 64
lowcut = 3.0
highcut = 8.0

N = 0
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
k = []
l = []


def filterData(inFile):
    with open(inFile,'r') as f1:
        global N,a,b,c,d,e,f,g,h,k,l
        reader = csv.reader(f1, delimiter=',')
        fields = reader.next()   # read header row, and omit the header
           # print fields
        for row in reader:
            N +=1
            a.append(int(row[0]))  #package
            b.append(float(row[1]))  #gyroX
            c.append(float(row[2]))  #gyroY
            d.append(float(row[3]))  #gyroZ
            e.append(float(row[4]))  #accelX
            f.append(float(row[5]))  #accelY
            g.append(float(row[6]))  #accelZ
            h.append(float(row[7]))  #magetX
            k.append(float(row[8]))  #magetY
            l.append(float(row[9]))  #magetZ
                        
    b = butter_bandpass_filter(b, lowcut, highcut, fs, order=5)
    c = butter_bandpass_filter(c, lowcut, highcut, fs, order=5)
    d = butter_bandpass_filter(d, lowcut, highcut, fs, order=5)
    e = butter_bandpass_filter(e, lowcut, highcut, fs, order=5)
    f = butter_bandpass_filter(f, lowcut, highcut, fs, order=5)
    g = butter_bandpass_filter(g, lowcut, highcut, fs, order=5)  
    h = butter_bandpass_filter(h, lowcut, highcut, fs, order=5)
    k = butter_bandpass_filter(k, lowcut, highcut, fs, order=5)
    l = butter_bandpass_filter(l, lowcut, highcut, fs, order=5)              

def copyData(outFile,user,action,placement,trail):
    with open(outFile,'a') as f2:
        writer = csv.writer(f2,delimiter = ',')
        for i in range(N):
            row = [i,a[i], b[i],c[i],d[i],e[i],f[i],g[i],h[i],k[i],l[i],user,action,placement,trail]
            writer.writerow(row)

def out_first_line(filename):
    if not os.path.exists(filename):
        with open(filename, mode='a') as f:
            f.write("Serial,Packet,GyroscopeX,GyroscopeY,GyroscopeZ,AccelerometerX,AccelerometerY,AccelerometerZ,MagnetometerX,MagnetometerY,MagnetometerZ,user,action,placement,trail\n")     

def getParser():
    usage="""
    {program} input_file output_file"""   
    parser =argparse.ArgumentParser(description="apply butterworth Filter(band filter) on the orignal data", usage=usage)
    parser.add_argument("input_file",help="input file name")
    parser.add_argument("output_file",help="output file name")
    parser.add_argument("user",help="user id, sequential number")
    parser.add_argument("action",help="user action, straight:1, zigzag:2, stairs:3")
    parser.add_argument("placement",help="foot:1, lowerback:2")
    parser.add_argument("trail",help="number")
    args= parser.parse_args()
    #print args
    return args


def main():
    args = getParser()
    print(args.input_file)
    out_first_line(args.output_file)
    filterData(args.input_file)
    copyData(args.output_file,args.user,args.action,args.placement,args.trail)

if __name__ == "__main__":
    main()