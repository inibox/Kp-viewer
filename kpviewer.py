#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:17:40 2018

@author: eric
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import matplotlib.dates as mdates
#import datetime as dt
import dateutil.parser



def plot_kp(date_time,kp):
    fig, ax = plt.subplots()
#    ax.plot(date_time,kp,drawstyle='steps')
    ax.bar(date_time, kp)   
    ax.set_title('Kp based on NOAA')
    ax.set_ylim(0,12)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.gcf().autofmt_xdate()
    plt.ylabel("Kp value")
    plt.xlabel("Date time")
#    plt.tight_layout()
    plt.show()
    return()

# new routine
def plot_kp2(date_time,kp):
    fig, ax = plt.subplots()
#    ax.plot(date_time,kp,drawstyle='steps')

#    array = np.random.randn(100)
    greater_than_four = kp > 4
    lesser_than_four = kp < 4
    equal_four = kp == 4
    cax = plt.subplot(111)
    # plot a dummy plot to get the x-axis date time visible
    cax.bar(date_time,0)
    plt.ylabel("Kp value")
    plt.xlabel("Date time")    
    # plot the kp values in color style with x axis hidden
    cax2 = cax.twiny()
    cax2.axes.get_xaxis().set_ticks([])
    cax2.bar(np.arange(len(kp))[greater_than_four], kp[greater_than_four], color='r')
    cax2.bar(np.arange(len(kp))[lesser_than_four], kp[lesser_than_four], color='g')
    cax2.bar(np.arange(len(kp))[equal_four], kp[equal_four], color='y')
    cax2.set_title('Kp NOAA')
    cax.set_ylim(0,12)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.gcf().autofmt_xdate()

    plt.tight_layout()
    plt.show()
    return()


#file='StaffExport_20180418_141931.xls'    
file='StaffExport_20180626_101523.xls'
df = pd.read_excel(file, sheet_name=0)

# Skip the header part and read the data - these are strings!
df = df.iloc[4:len(df)].values
date_time=df[:,0]
# dt=df[:0]
# print(date_time)

for i in range(len(date_time)):
    date_time[i]=dateutil.parser.parse(date_time[i])

# print(date_time)
# date_time=dateutil.parser.parse(df[:,0])
# dateutil.parser.parse(datestring)


kp=df[:,1]              # kp values in file are strings
kp=pd.to_numeric(kp)    # convert to floats

#print(date_time)
#print(kp)
plot_kp2(date_time,kp)

