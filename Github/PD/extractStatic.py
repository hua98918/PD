# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:09:14 2016

@author: zhang
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

SampleNumber = 164   #2.56 sec* 64HZ 
Overlapping = 82  # overlapping half, means each segment will -82,then begin a new one 




class Feature(object):
    def __init__(self,sampleid, sample_list):
        self.sampleid = sampleid
        self.sample_list = sample_list

    def output(self,featureouput):
        if os.path.isfile(featureouput):
            with open(featureouput, mode='a') as f:
                f.write(self.get_mean(sample_list))
                f.write(",")
                f.write(str(self.get_period()))  #period =  float(doty.timestamp) - float(dotx.timestamp)
                f.write(",")
                f.write(str(self.dotx.x))  #x_start = dotx.x
                f.write(",")
                f.write(str(self.doty.x))  #x_stop = doty.x
                f.write(",")
                f.write(str(self.dotx.y))  #y_start = dotx.y
                f.write("\n")  
        
    
    def get_mean(self,td):
        #print((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6)
        return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6

    def get_period(self):
        #print(datetime.strptime(self.doty.timestamp,'%H:%M:%S:%f')- datetime.strptime(self.dotx.timestamp,'%H:%M:%S:%f'))
        return self.get_sec(datetime.strptime(self.doty.timestamp,'%H:%M:%S:%f')- datetime.strptime(self.dotx.timestamp,'%H:%M:%S:%f'))
        
        
class Windows(object):
    def __init__(self, sampleid):
        self.sample_list = []   
        self.sampleId = sampleid
        
    def add_sample(self, sample):   #input 
        self.sample_list.append(sample)
    
    def output(self,  featurefile):  # output
        features = Feature.create_feature(self.sampleid, self.sample_list)
        #print(len(features))
        for feature in features:
            print("there is line\n")
            Feature.output(featurefile)
            
        
def parse_file(inputFile):
    #print ("start parsing file %s" %(filename))
    windows = []
    windowsId = 0 
    rowNumber = 0
    while(rowNumber < 164)  #2.56 sec* 64HZ 
        with open(inputFile, mode='r') as f:
            reader = csv.reader(f1, delimiter=',')
            reader.next()   # read header row, and omit the header
            # print fields
            for row in reader:
                N +=1
                serial.append(int(row[0]))  #serial
                packet.append(int(row[1]))  #packet
                b.append(float(row[1]))  #gyroX
                c.append(float(row[2]))  #gyroY
                d.append(float(row[3]))  #gyroZ
                e.append(float(row[4]))  #accelX
                f.append(float(row[5]))  #accelY
                g.append(float(row[6]))  #accelZ
                h.append(float(row[7]))  #magetX
                k.append(float(row[8]))  #magetY
                l.append(float(row[9]))  #magetZ 
            
            
            
                '''for i, line in f:      
                line = line.strip("\n").strip()
                check = re.compile("^(\d)\,(\d)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,([-+]?\d+\.\d+(e-\d+)?)\,(\d)\,(\d)\,(\d)\,(\d)")
                groups = check.match(line)
                sample = []
                row["timestamp"]=groups.group(1).strip()  
                row["cell_orient"]=groups.group(2).strip()
                row["time"]=groups.group(3).strip()
                row["tracking_id"]=groups.group(4)
                row["x_coordinate"]=groups.group(5)
                row["y_coordinate"]= groups.group(6)
                row["pressure"]=groups.group(7)
                row["touch_major"]= groups.group(8)
                row["touch_minor"]=groups.group(9)
                row["finger_orient"]=groups.group(10)
                if last_action is None or last_action.trackingid != row["tracking_id"]:   #if tracking id is new or no tracking id, means new action
                    last_action = Action(row["tracking_id"])      #new an action object
                    actions.append(last_action)      #same tracking_id in one action object
                dot = Dot.create_dot(row)    #every row is a dot, create dot object
                last_action.add_dot(dot)     #add dot object into action object'''
            
    return actions

        
        
        for i,row in reader:      
            if i< SampleNumber
                sample = []   #sample is tuple  
                serial.append(int(row[0]))  #serial
                packet.append(int(row[1]))  #packet
                gyroX.append(float(row[2]))  #gyroX
                gyroY.append(float(row[3]))  #gyroY
                gyroZ.append(float(row[4]))  #gyroZ
                accelX.append(float(row[5]))  #accelX
                accelY.append(float(row[6]))  #accelY
                accelZ.append(float(row[7]))  #accelZ
                magetX.append(float(row[8]))  #magetX
                magetY.append(float(row[9]))  #magetY
                magetZ.append(float(row[10]))  #magetZ
        if row[0] == SampleNumber-1 
            
            '''
            if last_action is None or last_action.trackingid != row["tracking_id"]:   #if tracking id is new or no tracking id, means new action
                last_action = Action(row["tracking_id"])      #new an action object
                actions.append(last_action)      #same tracking_id in one action object
            dot = Dot.create_dot(row)    #every row is a dot, create dot object
            last_action.add_dot(dot)     #add dot object into action object
            '''
    return windows    


def getParser():
    usage="""
    {program} input_file output_file"""   
    parser =argparse.ArgumentParser(description="apply butterworth Filter(band filter) on the orignal data", usage=usage)
    parser.add_argument("input_file",help="input file name")
    parser.add_argument("output_file",help="output file name")
    args= parser.parse_args()
    #print args
    return args


def main():
    args = getParser()
    windows = parse_file(args.input_file)  #read the original file, devived into windows
    #print(len(windows)) 
    for window in windows:     #e. action.output will identify the dot and line action,and output to different csv
        window.output(args.lineoutput,args.dotouput)

if __name__ == "__main__":
    main()