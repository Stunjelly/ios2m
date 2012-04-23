# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Apr 23 17:02:13 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(820, 582)
        MainWindow.setMinimumSize(QtCore.QSize(820, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/iBooks.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.header().setDefaultSectionSize(110)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 60))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.btn_source = QtGui.QPushButton(self.widget)
        self.btn_source.setGeometry(QtCore.QRect(90, 0, 111, 23))
        self.btn_source.setObjectName(_fromUtf8("btn_source"))
        self.btnfix = QtGui.QPushButton(self.widget)
        self.btnfix.setGeometry(QtCore.QRect(0, 0, 81, 23))
        self.btnfix.setObjectName(_fromUtf8("btnfix"))
        self.btnabout = QtGui.QPushButton(self.widget)
        self.btnabout.setGeometry(QtCore.QRect(0, 30, 81, 23))
        self.btnabout.setObjectName(_fromUtf8("btnabout"))
        self.btn_dest = QtGui.QPushButton(self.widget)
        self.btn_dest.setGeometry(QtCore.QRect(90, 30, 111, 23))
        self.btn_dest.setObjectName(_fromUtf8("btn_dest"))
        self.sourcelabel = QtGui.QLabel(self.widget)
        self.sourcelabel.setGeometry(QtCore.QRect(210, 0, 601, 21))
        self.sourcelabel.setText(_fromUtf8(""))
        self.sourcelabel.setObjectName(_fromUtf8("sourcelabel"))
        self.destlabel = QtGui.QLabel(self.widget)
        self.destlabel.setGeometry(QtCore.QRect(210, 30, 601, 21))
        self.destlabel.setText(_fromUtf8(""))
        self.destlabel.setObjectName(_fromUtf8("destlabel"))
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "iOS2M - Stunjelly eBook Services", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Images Found", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Requires Fix", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_source.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.btnfix.setText(QtGui.QApplication.translate("MainWindow", "Fix EPUBs", None, QtGui.QApplication.UnicodeUTF8))
        self.btnabout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dest.setText(QtGui.QApplication.translate("MainWindow", "Destination", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
