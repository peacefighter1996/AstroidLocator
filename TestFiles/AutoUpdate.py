# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 02:34:15 2017

@author: Ian-A
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.set_zlabel('Z Label')
commandStringOld = ["init"]
x = []
y = []
z = []
xperson=0
yperson=0
zperson=0
def animate(i):
    pullData = open("sampletext.txt","r").read()
    dataArray = pullData.split('\n')
    commandstring=[]
    counter=0;
    for eachLine in dataArray:
        if len(eachLine)>1:
            if counter>1:
                _,name,xnum,ynum,znum,_ = eachLine.split(':')
                if (len(commandstring)==0):
                    x.append(float(xnum))
                    y.append(float(ynum))
                    z.append(float(znum))
                elif (len(commandstring)==1):
                    if (name.find(commandstring[0])>=0):
                        x.append(float(xnum))
                        y.append(float(ynum))
                        z.append(float(znum))
                elif (commandstring[0]=="ALL"):
                    find=True;
                    for i in range (1,len(commandstring)):
                        if (name.find(commandstring[i])<0):
                            find = False
                    if (find):
                        x.append(float(xnum))
                        y.append(float(ynum))
                        z.append(float(znum))
                elif (commandstring[0]=="OR"):
                    for i in range (1,len(commandstring)):
                        if (name.find(commandstring[i])>=0):
                            x.append(float(xnum))
                            y.append(float(ynum))
                            z.append(float(znum))
                            break 
                
            elif counter==0:
                _,name,xnum,ynum,znum,_ = eachLine.split(':')
                xperson=float(xnum)
                yperson=float(ynum)
                zperson=float(znum)
                
            elif counter==1:
                commandstring = eachLine.split(':')
            counter+=1
    ax1.clear()
    ax1.scatter(x, y, z, c='r', marker='o')
    ax1.scatter(xperson, yperson, zperson, c='b', marker='x')
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()