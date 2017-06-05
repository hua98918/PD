
import matplotlib.pyplot as plt
import argparse
import numpy as np
import pandas as pd



windowSize = 10
highAccelerometer =  0.3
lowAccelerometer =  0.15
highGyroscope = 16
lowGyroscope =  9
highMagnetometer = 0.015
lowMagnetometer = 0.008
timeInterval = 0.6   #comes from 100HZ in one second; unit:second

i = 0

input_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525m03.txt"
output_file = "C:\pakinsen\Vicon\WALKER2016\PDkal160525\PDkal160525m03Feature.csv"


linedf = pd.DataFrame()
newdf = pd.DataFrame()
spdf = pd.DataFrame()
acdf = pd.DataFrame()
#read csv into dataframe 
df=pd.read_csv(input_file)
df = pd.read_csv(input_file, sep=",", header = None)
#print df
#fill all theNA as 0
df.fillna(0)

df.columns = ['serial','na','ToeLX','ToeLY', 'ToeLZ','HeelLX', 'HeelLY','HeelLZ','HeelRX','HeelRY','HeelRZ', \
'ToeRX','ToeRY','ToeRZ','kneeLX','kneeLY','kneeLZ','knee1X','knee1Y','knee1Z','hipLX','hipLY','hipLZ', \
'hipRX','hipRY','hipRZ','shRX','shRY','shRZ','shLX','shLY','shLZ','elbowRX','elbowRY','elbowRZ', \
'wristRX','wristRY','wristRZ','walkerLX','walkerLY','walkerLZ','walkerRX','walkerRY','walkerRZ']

    
#for index, row in df.iterrows():
for i in df.index:
   # print index , row
    ToeL = pd.Series([np.sqrt(df.ix[i,'ToeLX']**2+df.ix[i,'ToeLY']**2+df.ix[i,'ToeLZ']**2)])   
    HeelL = pd.Series([np.sqrt(df.ix[i,'HeelLX']**2+df.ix[i,'HeelLY']**2+df.ix[i,'HeelLZ']**2)])         
    HeelR = pd.Series([np.sqrt(df.ix[i,'HeelRX']**2+df.ix[i,'HeelRY']**2+df.ix[i,'HeelRZ']**2)]) 
    ToeR = pd.Series([np.sqrt(df.ix[i,'ToeRX']**2+df.ix[i,'ToeRY']**2+df.ix[i,'ToeRZ']**2)]) 
    kneeL = pd.Series([np.sqrt(df.ix[i,'kneeLX']**2+df.ix[i,'kneeLY']**2+df.ix[i,'kneeLZ']**2)]) 
    knee1 = pd.Series([np.sqrt(df.ix[i,'knee1X']**2+df.ix[i,'knee1Y']**2+df.ix[i,'knee1Z']**2)])
    hipL = pd.Series([np.sqrt(df.ix[i,'hipLX']**2+df.ix[i,'hipLY']**2+df.ix[i,'hipLZ']**2)])
    hipR = pd.Series([np.sqrt(df.ix[i,'hipRX']**2+df.ix[i,'hipRY']**2+df.ix[i,'hipRZ']**2)])
    shR = pd.Series([np.sqrt(df.ix[i,'shRX']**2+df.ix[i,'shRY']**2+df.ix[i,'shRZ']**2)]) 
    shL = pd.Series([np.sqrt(df.ix[i,'shLX']**2+df.ix[i,'shLY']**2+df.ix[i,'shLZ']**2)])
    elbowR = pd.Series([np.sqrt(df.ix[i,'elbowRX']**2+df.ix[i,'elbowRY']**2+df.ix[i,'elbowRZ']**2)]) 
    wristR = pd.Series([np.sqrt(df.ix[i,'wristRX']**2+df.ix[i,'wristRY']**2+df.ix[i,'wristRZ']**2)])
    walkerL = pd.Series([np.sqrt(df.ix[i,'walkerLX']**2+df.ix[i,'walkerLY']**2+df.ix[i,'walkerLZ']**2)])
    walkerR = pd.Series([np.sqrt(df.ix[i,'walkerRX']**2+df.ix[i,'walkerRY']**2+df.ix[i,'walkerRZ']**2)])  
    #wristR = pd.Series([np.sqrt(df[df.columns[44:45]]**2+df[df.columns[45:46]]**2+df[df.columns[46:47]]**2)])    
    #print ToeL    
    linedf = pd.concat([ToeL,HeelL,HeelR,ToeR,kneeL,knee1,hipL,hipR,shR,shL,elbowR,wristR,walkerL,walkerR],axis=1)  #axis=1 means concat to colume, axis =0 means contact to lines; concat 2 series to a 1 dataFrame
    newdf = newdf.append(linedf)     

#reset index from 0 to sequential number
newdf = newdf.reset_index(drop=True)    
#print newdf
newdf.columns = ['ToeL', 'HeelL', 'HeelR', 'ToeR','kneeL','knee1','hipL','hipR','shR','shL','elbowR','wristR','walkerL','walkerR']
#print finaldf

meanToeL = newdf[newdf.columns[0:1]].rolling(windowSize).mean() 
varToeL = np.sqrt(newdf[newdf.columns[0:1]].rolling(windowSize).var())
kurtToeL = newdf[newdf.columns[0:1]].rolling(windowSize).kurt() 
skewToeL = newdf[newdf.columns[0:1]].rolling(windowSize).skew() 
stdToeL = newdf[newdf.columns[0:1]].rolling(windowSize).std() 
ToeLdf = pd.concat([meanToeL,varToeL,kurtToeL,skewToeL,stdToeL],axis=1)
ToeLdf.columns = ['meanToeL', 'varToeL', 'kurtToeL', 'skewToeL','stdToeL']

meanHeelL = newdf[newdf.columns[1:2]].rolling(windowSize).mean() 
varHeelL = np.sqrt(newdf[newdf.columns[1:2]].rolling(windowSize).var())
kurtHeelL = newdf[newdf.columns[1:2]].rolling(windowSize).kurt() 
skewHeelL = newdf[newdf.columns[1:2]].rolling(windowSize).skew() 
stdHeelL= newdf[newdf.columns[1:2]].rolling(windowSize).std() 
HeelLdf = pd.concat([meanHeelL,varHeelL,kurtHeelL,skewHeelL,stdHeelL],axis=1)
HeelLdf.columns = ['meanHeelL', 'varHeelL', 'kurtHeelL', 'skewHeelL','stdHeelL']

meanHeelR = newdf[newdf.columns[2:3]].rolling(windowSize).mean() 
varHeelR = np.sqrt(newdf[newdf.columns[2:3]].rolling(windowSize).var())
kurtHeelR = newdf[newdf.columns[2:3]].rolling(windowSize).kurt() 
skewHeelR = newdf[newdf.columns[2:3]].rolling(windowSize).skew() 
stdHeelR = newdf[newdf.columns[2:3]].rolling(windowSize).std() 
HeelRdf = pd.concat([meanHeelR,varHeelR,kurtHeelR,skewHeelR,stdHeelR],axis=1)
HeelRdf.columns = ['meanHeelR', 'varHeelR', 'kurtHeelR', 'skewHeelR','stdHeelR']

meanToeR = newdf[newdf.columns[3:4]].rolling(windowSize).mean() 
varToeR = np.sqrt(newdf[newdf.columns[3:4]].rolling(windowSize).var())
kurtToeR = newdf[newdf.columns[3:4]].rolling(windowSize).kurt() 
skewToeR = newdf[newdf.columns[3:4]].rolling(windowSize).skew() 
stdToeR = newdf[newdf.columns[3:4]].rolling(windowSize).std() 
ToeRdf = pd.concat([meanToeR,varToeR,kurtToeR,skewToeR,stdToeR],axis=1)
ToeRdf.columns = ['meanToeR', 'varToeR', 'kurtToeR', 'skewToeR','stdToeR']

meankneeL = newdf[newdf.columns[4:5]].rolling(windowSize).mean() 
varkneeL = np.sqrt(newdf[newdf.columns[4:5]].rolling(windowSize).var())
kurtkneeL = newdf[newdf.columns[4:5]].rolling(windowSize).kurt() 
skewkneeL = newdf[newdf.columns[4:5]].rolling(windowSize).skew() 
stdkneeL = newdf[newdf.columns[4:5]].rolling(windowSize).std() 
kneeLdf = pd.concat([meankneeL,varkneeL,kurtkneeL,skewkneeL,stdkneeL],axis=1)
kneeLdf.columns = ['meankneeL', 'varkneeL', 'kurtkneeL', 'skewkneeL','stdkneeL']

meankneeR = newdf[newdf.columns[5:6]].rolling(windowSize).mean() 
varkneeR = np.sqrt(newdf[newdf.columns[5:6]].rolling(windowSize).var())
kurtkneeR = newdf[newdf.columns[5:6]].rolling(windowSize).kurt() 
skewkneeR = newdf[newdf.columns[5:6]].rolling(windowSize).skew() 
stdkneeR = newdf[newdf.columns[5:6]].rolling(windowSize).std() 
kneeRdf = pd.concat([meankneeR,varkneeR,kurtkneeR,skewkneeR,stdkneeR],axis=1)
kneeRdf.columns = ['meankneeR', 'varkneeR', 'kurtkneeR', 'skewkneeR','stdkneeR']


finaldf = pd.concat([spdf,acdf,newdf,ToeLdf,HeelLdf,HeelRdf,ToeRdf,kneeLdf,kneeRdf],axis=1)
#set column name for plot to handle them
#print finaldf

with open(output_file, 'a') as f:
    finaldf.to_csv(f,sep=',',header=True)
    
    
fig = plt.figure() 

ax1 = fig.add_subplot(331) 
#ax1 = plt.subplot2grid((3,3), (0, 0), rowspan=1, colspan=4)
ax1.plot(finaldf.index.values, finaldf[['ToeL']], label='ToeL Trajectoy')
ax1.plot(finaldf.index.values, finaldf[['meanToeL']], label='Mean ToeL')
ax1.plot(finaldf.index.values, finaldf[['varToeL']], label='Local Variance varToeL')
ax1.plot(finaldf.index.values, finaldf[['varToeL']], label='Local Variance varToeL')
ax1.plot(finaldf.index.values, finaldf[['varToeL']], label='Local Variance varToeL')
#main.axes.xaxis.set_ticklabels([])[]
plt.title('Step detection with ToeL Trajectoy reading')
plt.legend() 



plt.tight_layout()
plt.show()

