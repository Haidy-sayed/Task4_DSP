# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task4GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QFrame, QWidget, QInputDialog, QLineEdit,QComboBox
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import sys 
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor ,QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols
from pyqtgraph.graphicsItems.ImageItem import ImageItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import io
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft, ifft
from scipy import signal
import cmath
from scipy.io.wavfile import write
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.exporters
from fpdf import FPDF
import statistics
from pyqtgraph import PlotWidget
import pyqtgraph
from pyqtgraph import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, PlotItem
#from matplotlib.pyplot import draw
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QFrame, QWidget, QInputDialog, QLineEdit,QComboBox
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import sys 
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols
from pyqtgraph.graphicsItems.ImageItem import ImageItem
from matplotlib.figure import Figure
import io
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft, ifft
from scipy import signal
import cmath
import cv2
pg.setConfigOption('background', 'w')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FittingOptionsContianer = QtWidgets.QWidget(self.centralwidget)
        self.FittingOptionsContianer.setMaximumSize(QtCore.QSize(150, 16777215))
        self.FittingOptionsContianer.setObjectName("FittingOptionsContianer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.FittingOptionsContianer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FittingOptionsLabel = QtWidgets.QLabel(self.FittingOptionsContianer)
        self.FittingOptionsLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FittingOptionsLabel.setFont(font)
        self.FittingOptionsLabel.setObjectName("FittingOptionsLabel")
        self.verticalLayout_2.addWidget(self.FittingOptionsLabel)
        self.toolBox = QtWidgets.QToolBox(self.FittingOptionsContianer)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 132, 448))
        self.page.setObjectName("page")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ExtrapolationEfficiencySlider = QtWidgets.QSlider(self.page)
        self.ExtrapolationEfficiencySlider.setGeometry(QtCore.QRect(50, 140, 22, 231))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ExtrapolationEfficiencySlider.setFont(font)
        self.ExtrapolationEfficiencySlider.setMinimum(1)
        self.ExtrapolationEfficiencySlider.setMaximum(10)
        self.ExtrapolationEfficiencySlider.setSingleStep(1)
        self.ExtrapolationEfficiencySlider.setPageStep(1)
        self.ExtrapolationEfficiencySlider.setSliderPosition(10)
        self.ExtrapolationEfficiencySlider.setTracking(True)
        self.ExtrapolationEfficiencySlider.setOrientation(QtCore.Qt.Vertical)
        self.ExtrapolationEfficiencySlider.setInvertedAppearance(False)
        self.ExtrapolationEfficiencySlider.setInvertedControls(False)
        self.ExtrapolationEfficiencySlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ExtrapolationEfficiencySlider.setTickInterval(0)
        self.ExtrapolationEfficiencySlider.setObjectName("ExtrapolationEfficiencySlider")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(0, 135, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(10, 355, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(0, 0, 131, 89))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.OneChunkRadioButton = QtWidgets.QRadioButton(self.widget)
        self.OneChunkRadioButton.setObjectName("OneChunkRadioButton")
        self.verticalLayout_3.addWidget(self.OneChunkRadioButton)
        self.MultipleChunksRadioButton = QtWidgets.QRadioButton(self.widget)
        self.MultipleChunksRadioButton.setObjectName("MultipleChunksRadioButton")
        self.verticalLayout_3.addWidget(self.MultipleChunksRadioButton)
        self.NumberChunksSpinBox = QtWidgets.QSpinBox(self.widget)
        self.NumberChunksSpinBox.setMaximum(10)
        self.NumberChunksSpinBox.setObjectName("NumberChunksSpinBox")
        self.verticalLayout_3.addWidget(self.NumberChunksSpinBox)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 132, 448))
        self.page_2.setObjectName("page_2")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(0, 180, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.InterPolationOrderSlider = QtWidgets.QSlider(self.page_2)
        self.InterPolationOrderSlider.setGeometry(QtCore.QRect(80, 210, 22, 171))
        self.InterPolationOrderSlider.setMaximum(9)
        self.InterPolationOrderSlider.setPageStep(9)
        self.InterPolationOrderSlider.setOrientation(QtCore.Qt.Vertical)
        self.InterPolationOrderSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.InterPolationOrderSlider.setObjectName("InterPolationOrderSlider")
        self.order1Label = QtWidgets.QLabel(self.page_2)
        self.order1Label.setGeometry(QtCore.QRect(10, 370, 47, 13))
        self.order1Label.setObjectName("order1Label")
        self.order10Label = QtWidgets.QLabel(self.page_2)
        self.order10Label.setGeometry(QtCore.QRect(0, 210, 61, 16))
        self.order10Label.setObjectName("order10Label")
        self.lcdOrder = QtWidgets.QLCDNumber(self.page_2)
        self.lcdOrder.setGeometry(QtCore.QRect(10, 400, 41, 31))
        self.lcdOrder.setObjectName("lcdOrder")
        self.LCDOrderLabel = QtWidgets.QLabel(self.page_2)
        self.LCDOrderLabel.setGeometry(QtCore.QRect(70, 405, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LCDOrderLabel.setFont(font)
        self.LCDOrderLabel.setObjectName("LCDOrderLabel")
        self.widget1 = QtWidgets.QWidget(self.page_2)
        self.widget1.setGeometry(QtCore.QRect(0, 10, 121, 42))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.ChunkNumberComboBox = QtWidgets.QComboBox(self.widget1)
        self.ChunkNumberComboBox.setObjectName("ChunkNumberComboBox")
        self.verticalLayout_6.addWidget(self.ChunkNumberComboBox)
        self.widget2 = QtWidgets.QWidget(self.page_2)
        self.widget2.setGeometry(QtCore.QRect(0, 60, 122, 108))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.LinearInterpRadioBtn = QtWidgets.QRadioButton(self.widget2)
        self.LinearInterpRadioBtn.setObjectName("LinearInterpRadioBtn")
        self.verticalLayout_4.addWidget(self.LinearInterpRadioBtn)
        self.PolynomialInterpRadioBtn = QtWidgets.QRadioButton(self.widget2)
        self.PolynomialInterpRadioBtn.setObjectName("PolynomialInterpRadioBtn")
        self.verticalLayout_4.addWidget(self.PolynomialInterpRadioBtn)
        self.SplineInterpRadioBtn = QtWidgets.QRadioButton(self.widget2)
        self.SplineInterpRadioBtn.setObjectName("SplineInterpRadioBtn")
        self.verticalLayout_4.addWidget(self.SplineInterpRadioBtn)
        self.PieceWiseRadioBtn = QtWidgets.QRadioButton(self.widget2)
        self.PieceWiseRadioBtn.setObjectName("PieceWiseRadioBtn")
        self.verticalLayout_4.addWidget(self.PieceWiseRadioBtn)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_2.addWidget(self.toolBox)
        self.horizontalLayout.addWidget(self.FittingOptionsContianer)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.DataContainer = QtWidgets.QWidget(self.centralwidget)
        self.DataContainer.setMinimumSize(QtCore.QSize(100, 0))
        self.DataContainer.setObjectName("DataContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DataContainer)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.MathematicsLabel = QtWidgets.QLabel(self.DataContainer)
        self.MathematicsLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.MathematicsLabel.setFont(font)
        self.MathematicsLabel.setObjectName("MathematicsLabel")
        self.verticalLayout_5.addWidget(self.MathematicsLabel)
        self.MathDisplayArea = QtWidgets.QWidget(self.DataContainer)
        self.MathDisplayArea.setObjectName("MathDisplayArea")
        self.verticalLayout_5.addWidget(self.MathDisplayArea)
        self.ErrorMappingLabel_2 = QtWidgets.QLabel(self.DataContainer)
        self.ErrorMappingLabel_2.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMappingLabel_2.setFont(font)
        self.ErrorMappingLabel_2.setObjectName("ErrorMappingLabel_2")
        self.verticalLayout_5.addWidget(self.ErrorMappingLabel_2)
        self.widget_3 = QtWidgets.QWidget(self.DataContainer)
        self.widget_3.setObjectName("widget_3")
        self.ErrorMappingButton = QtWidgets.QPushButton(self.widget_3)
        self.ErrorMappingButton.setGeometry(QtCore.QRect(10, 200, 75, 23))
        self.ErrorMappingButton.setObjectName("ErrorMappingButton")
        self.ErrorMappingProgressBar = QtWidgets.QProgressBar(self.widget_3)
        self.ErrorMappingProgressBar.setGeometry(QtCore.QRect(100, 200, 171, 23))
        self.ErrorMappingProgressBar.setProperty("value", 0)
        self.ErrorMappingProgressBar.setTextVisible(True)
        self.ErrorMappingProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ErrorMappingProgressBar.setInvertedAppearance(False)
        self.ErrorMappingProgressBar.setObjectName("ErrorMappingProgressBar")
        self.verticalLayout_5.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.DataContainer)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.GraphingContainer = QtWidgets.QWidget(self.centralwidget)
        self.GraphingContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.GraphingContainer.setMaximumSize(QtCore.QSize(600, 16777215))
        self.GraphingContainer.setObjectName("GraphingContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.GraphingContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CurveFittingLabel = QtWidgets.QLabel(self.GraphingContainer)
        self.CurveFittingLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.CurveFittingLabel.setFont(font)
        self.CurveFittingLabel.setObjectName("CurveFittingLabel")
        self.verticalLayout.addWidget(self.CurveFittingLabel)
        self.CurveFittingGraph = PlotWidget(self.GraphingContainer)
        self.CurveFittingGraph.setObjectName("CurveFittingGraph")
        self.verticalLayout.addWidget(self.CurveFittingGraph)
        self.line_3 = QtWidgets.QFrame(self.GraphingContainer)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.ErrorMappingLabel = QtWidgets.QLabel(self.GraphingContainer)
        self.ErrorMappingLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMappingLabel.setFont(font)
        self.ErrorMappingLabel.setObjectName("ErrorMappingLabel")
        self.verticalLayout.addWidget(self.ErrorMappingLabel)
        self.ErrorMappingGraph = PlotWidget(self.GraphingContainer)
        self.ErrorMappingGraph.setObjectName("ErrorMappingGraph")
        self.verticalLayout.addWidget(self.ErrorMappingGraph)
        self.horizontalLayout.addWidget(self.GraphingContainer)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGraphs_Options = QtWidgets.QMenu(self.menubar)
        self.menuGraphs_Options.setObjectName("menuGraphs_Options")
        self.menuCurve_Fitting = QtWidgets.QMenu(self.menuGraphs_Options)
        self.menuCurve_Fitting.setObjectName("menuCurve_Fitting")
        self.menuError_Mapping = QtWidgets.QMenu(self.menuGraphs_Options)
        self.menuError_Mapping.setObjectName("menuError_Mapping")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_Curve_fitting_IMG = QtWidgets.QAction(MainWindow)
        self.actionSave_Curve_fitting_IMG.setObjectName("actionSave_Curve_fitting_IMG")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCurveZoom_in = QtWidgets.QAction(MainWindow)
        self.actionCurveZoom_in.setObjectName("actionCurveZoom_in")
        self.actioncurveZoom_out = QtWidgets.QAction(MainWindow)
        self.actioncurveZoom_out.setObjectName("actioncurveZoom_out")
        self.actionRun_EM = QtWidgets.QAction(MainWindow)
        self.actionRun_EM.setObjectName("actionRun_EM")
        self.actionErrorZoom_in_2 = QtWidgets.QAction(MainWindow)
        self.actionErrorZoom_in_2.setObjectName("actionErrorZoom_in_2")
        self.actionErrorZoom_out_2 = QtWidgets.QAction(MainWindow)
        self.actionErrorZoom_out_2.setObjectName("actionErrorZoom_out_2")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_Curve_fitting_IMG)
        self.menuFile.addAction(self.actionExit)
        self.menuCurve_Fitting.addAction(self.actionCurveZoom_in)
        self.menuCurve_Fitting.addAction(self.actioncurveZoom_out)
        self.menuError_Mapping.addAction(self.actionErrorZoom_in_2)
        self.menuError_Mapping.addAction(self.actionErrorZoom_out_2)
        self.menuGraphs_Options.addAction(self.menuCurve_Fitting.menuAction())
        self.menuGraphs_Options.addSeparator()
        self.menuGraphs_Options.addAction(self.menuError_Mapping.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGraphs_Options.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FittingOptionsLabel.setText(_translate("MainWindow", "Fitting Options"))
        self.label_3.setText(_translate("MainWindow", "Extrapolation %"))
        self.label_4.setText(_translate("MainWindow", "100%"))
        self.label_5.setText(_translate("MainWindow", "10%"))
        self.label.setText(_translate("MainWindow", "Num Chunks"))
        self.OneChunkRadioButton.setText(_translate("MainWindow", "One Chunk"))
        self.MultipleChunksRadioButton.setText(_translate("MainWindow", "Multiple Chunks"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.label_6.setText(_translate("MainWindow", "Order of Interpolation"))
        self.order1Label.setText(_translate("MainWindow", "1st order"))
        self.order10Label.setText(_translate("MainWindow", "10th order"))
        self.LCDOrderLabel.setText(_translate("MainWindow", "Order"))
        self.label_7.setText(_translate("MainWindow", "Chunk Number"))
        self.label_2.setText(_translate("MainWindow", "Type of Interpolation"))
        self.LinearInterpRadioBtn.setText(_translate("MainWindow", "Linear"))
        self.PolynomialInterpRadioBtn.setText(_translate("MainWindow", "Polynomial"))
        self.SplineInterpRadioBtn.setText(_translate("MainWindow", "Spline"))
        self.PieceWiseRadioBtn.setText(_translate("MainWindow", "PieceWise"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.MathematicsLabel.setText(_translate("MainWindow", "Mathematics"))
        self.ErrorMappingLabel_2.setText(_translate("MainWindow", "Error Mapping "))
        self.ErrorMappingButton.setText(_translate("MainWindow", "Run EM"))
        self.CurveFittingLabel.setText(_translate("MainWindow", "Curve Fitting Area"))
        self.ErrorMappingLabel.setText(_translate("MainWindow", "Error Mapping Area"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuGraphs_Options.setTitle(_translate("MainWindow", "Graphs Options"))
        self.menuCurve_Fitting.setTitle(_translate("MainWindow", "Curve Fitting"))
        self.menuError_Mapping.setTitle(_translate("MainWindow", "Error Mapping"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Curve_fitting_IMG.setText(_translate("MainWindow", "Save Curve fitting IMG"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionCurveZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionCurveZoom_in.setShortcut(_translate("MainWindow", "+"))
        self.actioncurveZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actioncurveZoom_out.setShortcut(_translate("MainWindow", "-"))
        self.actionRun_EM.setText(_translate("MainWindow", "Run EM"))
        self.actionRun_EM.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionErrorZoom_in_2.setText(_translate("MainWindow", "Zoom in"))
        self.actionErrorZoom_in_2.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.actionErrorZoom_out_2.setText(_translate("MainWindow", "Zoom out"))
        self.actionErrorZoom_out_2.setShortcut(_translate("MainWindow", "Ctrl+-"))

        #buttons connections 
        self.actionOpen_File.triggered.connect(lambda: self.openFile())
        self.actionCurveZoom_in.triggered.connect(lambda: self.zoomIn(0))
        self.actionErrorZoom_in_2.triggered.connect(lambda: self.zoomIn(1))
        self.actioncurveZoom_out.triggered.connect(lambda: self.zoomOut(0))
        self.actionErrorZoom_out_2.triggered.connect(lambda: self.zoomOut(1))

        #golbal varaibles of constants declaration
        self.time1=0
        self.amp1=0
        self.ampArray=0
        self.signalYMin=0
        self.signalYMax=0
        self.signalXmin=0
        self.signalXmax=0
        

        #Functions declarations
    def openFile(self):
      file_path=QFileDialog.getOpenFileName()
      self.file_name=file_path[0].split('/')[-1]
      self.read_data(self.file_name)

    def read_data(self,file_name):
        """loads the data from chosen file"""
        dataFile=pd.read_csv(file_name)
        self.label1=file_name
        self.time1=list(pd.to_numeric(dataFile['time'],downcast="float"))
        self.amp1=list(pd.to_numeric(dataFile['amplitude'],downcast="float"))
        self.signalYMin=min(self.amp1)
        self.signalYMax=max(self.amp1)
        self.signalXMin=min(self.time1)
        self.signalXMax=max(self.time1)
        self.settingCurveLimits()
        self.draw(self.time1,self.amp1)

    def settingCurveLimits(self):
        self.CurveFittingGraph.setLimits(xMin=self.signalXMin)
        self.CurveFittingGraph.setLimits(xMax=self.signalXMax)
        self.CurveFittingGraph.setLimits(yMin=self.signalYMin)
        self.CurveFittingGraph.setLimits(yMax=self.signalYMax)

        self.ErrorMappingGraph.setLimits(xMin=self.signalXMin)
        self.ErrorMappingGraph.setLimits(xMax=self.signalXMax)


    def draw(self,time,amp):
        """sets up our canvas to plot"""
        self.amp1=amp
        self.index=0  
        self.CurveFittingGraph.plot(self.time1[0:self.index+1000], self.amp1[0:self.index+1000], pen="#683b94")

    def zoomIn(self, val):
        if val==0:
            self.CurveFittingGraph.getViewBox().scaleBy((0.5,0.5))
        elif val==1:
            self.ErrorMappingGraph.getViewBox().scaleBy((0.5,0.5))
        else:
            pass
    
    def zoomOut(self, val):
        if val==0:
            self.CurveFittingGraph.getViewBox().scaleBy((2,2))
        elif val==1:
            self.ErrorMappingGraph.getViewBox().scaleBy((2,2))
        else:
            pass
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
