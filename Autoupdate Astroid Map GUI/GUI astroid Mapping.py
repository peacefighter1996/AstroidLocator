# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, projection='3d')
        self.axes.set_xlabel("X Coordinates")
        self.axes.set_ylabel("Y Coordinates")
        self.axes.set_zlabel("Z Coordinates")
        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.xcoordinates = []
        self.ycoordinates = []
        self.zcoordinates = []
        self.xperson=0
        self.yperson=0
        self.zperson=0
    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        pullData = open("sampletext.txt","r").read()
        dataArray = pullData.split('\n')
        commandstring=[]
        counter=0;
        for eachLine in dataArray:
            if len(eachLine)>1:
                if counter>1:
                    _,name,xnum,ynum,znum,_ = eachLine.split(':')
                    if (len(commandstring)==0):
                        self.xcoordinates.append(float(xnum))
                        self.ycoordinates.append(float(ynum))
                        self.zcoordinates.append(float(znum))
                    elif (len(commandstring)==1):
                        if (name.find(commandstring[0])>=0):
                            self.xcoordinates.append(float(xnum))
                            self.ycoordinates.append(float(ynum))
                            self.zcoordinates.append(float(znum))
                    elif (commandstring[0]=="ALL"):
                        find=True;
                        for i in range (1,len(commandstring)):
                            if (name.find(commandstring[i])<0):
                                find = False
                        if (find):
                            self.xcoordinates.append(float(xnum))
                            self.ycoordinates.append(float(ynum))
                            self.zcoordinates.append(float(znum))
                    else: #(commandstring[0]=="OR"):
                        for i in range (1,len(commandstring)):
                            if (name.find(commandstring[i])>=0):
                                self.xcoordinates.append(float(xnum))
                                self.ycoordinates.append(float(ynum))
                                self.zcoordinates.append(float(znum))
                                break 
                    
                elif counter==0:
                    _,name,xnum,ynum,znum,_ = eachLine.split(':')
                    self.xperson=float(xnum)
                    self.yperson=float(ynum)
                    self.zperson=float(znum)
                    
                elif counter==1:
                    commandstring = eachLine.split(':')
                counter+=1
        self.axes.clear()
        self.axes.scatter( self.xcoordinates,  self.ycoordinates,  self.zcoordinates, c='r', marker='o')
        self.axes.scatter(self.xperson, self.yperson, self.zperson, c='b', marker='x')
        #self.axes.cla()
        #self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)
        self.defineFilterForm()
        
        l = QtWidgets.QVBoxLayout(self.main_widget)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4)
        #l.addWidget(sc)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)
        
    def defineFilterForm(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        self.PlayerGPSCode = QLineEdit(self)
        self.PlayerGPSCode.resize(280,20)
        self.filtertype = QComboBox()
        self.filtermaterial = QLineEdit(self)
        self.filtermaterial.resize(280,20)
        layout.addRow(QLabel("filterType:"), self.PlayerGPSCode)
        layout.addRow(QLabel("filterType:"), self.filtertype)
        layout.addRow(QLabel("filterType:"), self.filtermaterial)
        self.formGroupBox.setLayout(layout)


    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    """embedding_in_qt5.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen

This program is a simple example of a Qt5 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.

This is modified from the embedding in qt4 example to show the difference
between qt4 and qt5"""
                                )


qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()