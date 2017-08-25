# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 23:59:07 2017

@author: Ian-A
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[]
y =[]
z =[]

Coordinates=[[-14248,26521,685,""],[-22119,37043,-9811,""],[-19564,-19564,-12644,""],
             [-22398,28415,-12212,""],[5736,4366,23150,""],[1012,5202,29311,"AST #1Pe AuFe"],
             [-3119,7476,30789,"AST #2Pe Unknown"],[-2088,5904,31333,"AST #3Pe Unknown"],[-3826,1259,30415,"AST #4Pe Unknown"],
             [-2926.15,3132.79,-20897.64,"AST #1So AgPtUFeO2"],[-6558,1235,13300,"AST #5Pe Unknown"],[4075,25327,14357,"AST #6Pe Unknown"],
             [3975,-22909,14061,"AST #7Pe Unknown"],[4390,-23314,17391,"AST #8Pe Unknown"],[6453,-26976,19609,"AST #9Pe Unknown"],
             [9101,-20387,22516,"AST #10Pe Unknown"],[9715,-21129,25093,"AST #11Pe Unknown"],[9079,-11371,22997,"AST #12Pe Unknown"],
             [4808,18850,-4162,"AST #13Pe Unknown"],[4301,18755,-4156,"AST #15Pe Unknown"],[5650,19522,-4894,"AST #16Pe Unknown"],
             [3258,13835,-6698,"AST #14Pe Unknown"],[2734,13660,-7279,"AST #17Pe Unknown"],[3026,13478,-7462,"AST #18Pe Unknown"],
             [-1214,13044,-10527,"AST #19Pe Unknown"],[-3523,8053,-12492,""],[-5464,6702,-18737,""],
             [-1070,-894,-27065,""],[2484,-8324,-32848,""],[4869,-12800,-37840,""],
             [10148,-17288,-37849,""],[7220,-16044,-45139,""],[18777.11,-2578.71,1745.57,"AST #19 SiFeO2"]]


for num in range(0,len(Coordinates)):
        x.append(Coordinates[num][0])
        y.append(Coordinates[num][1])
        z.append(Coordinates[num][2])
        



ax.scatter(x, y, z, c='r', marker='o')
ax.scatter(Coordinates[num][0], Coordinates[num][1], Coordinates[num][2], c='b', marker='x')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()