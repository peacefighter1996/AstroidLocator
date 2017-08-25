# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:35:20 2017

@author: Ian-A
"""

## build a QApplication before building other widgets
from __future__ import unicode_literals
from __future__ import unicode_literals
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

progname = os.path.basename(sys.argv[0])
progversion = "0.1"
## make a widget for displaying 3D objects
import pyqtgraph.opengl as gl
view = gl.GLViewWidget()
view.show()

## create three grids, add each to the view
#xgrid = gl.GLGridItem()
#ygrid = gl.GLGridItem()
#zgrid = gl.GLGridItem()
#view.addItem(xgrid)
#view.addItem(ygrid)
#view.addItem(zgrid)

## rotate x and y grids to face the correct direction
#xgrid.rotate(90, 0, 1, 0)
#ygrid.rotate(90, 1, 0, 0)

## scale each grid differently
#xgrid.scale(0.2, 0.1, 0.1)
#ygrid.scale(0.2, 0.1, 0.1)
#zgrid.scale(0.1, 0.2, 0.1)
point=gl.GLScatterPlotItem()

view.addItem(point)

class Astroiddrawer():
    def __init__(self, parent=None):
        self.view = gl.GLViewWidget()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)
        
    def compute_initial_figure(self):
        xgrid = gl.GLGridItem()
        ygrid = gl.GLGridItem()
        zgrid = gl.GLGridItem()
        self.view.addItem(xgrid)
        self.view.addItem(ygrid)
        self.view.addItem(zgrid)
        xgrid.rotate(90, 0, 1, 0)
        ygrid.rotate(90, 1, 0, 0)
        xgrid.scale(0.2, 0.1, 0.1)
        ygrid.scale(0.2, 0.1, 0.1)
        zgrid.scale(0.1, 0.2, 0.1)

    def update_figure(self):
        _=0
        #view.show()

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

        l = QtWidgets.QVBoxLayout(self.main_widget)
        #l.addWidget(sc)
        #l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

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