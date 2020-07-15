# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import equation


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.equation = QtWidgets.QLabel(self.centralwidget)
        self.equation.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.equation.setFont(font)
        self.equation.setTextFormat(QtCore.Qt.RichText)
        self.equation.setAlignment(QtCore.Qt.AlignCenter)
        self.equation.setStyleSheet("image: url(:/image/eq);")
        self.equation.setText("")
        self.equation.setObjectName("equation")
        self.verticalLayout.addWidget(self.equation)
        self.graphic_holder = pg.PlotWidget(self.centralwidget)
        self.graphic_holder.setMinimumSize(QtCore.QSize(150, 150))
        self.graphic_holder.setObjectName("graphic_holder")
        self.verticalLayout.addWidget(self.graphic_holder)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.calculation = QtWidgets.QLabel(self.centralwidget)
        self.calculation.setMinimumSize(QtCore.QSize(50, 30))
        self.calculation.setMaximumSize(QtCore.QSize(130, 30))
        self.calculation.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.calculation.setObjectName("calculation")
        self.horizontalLayout_4.addWidget(self.calculation)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.max_difference = QtWidgets.QLabel(self.centralwidget)
        self.max_difference.setMinimumSize(QtCore.QSize(130, 30))
        self.max_difference.setMaximumSize(QtCore.QSize(16777215, 30))
        self.max_difference.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.max_difference.setObjectName("max_difference")
        self.horizontalLayout_2.addWidget(self.max_difference)
        self.segmentation = QtWidgets.QLabel(self.centralwidget)
        self.segmentation.setMinimumSize(QtCore.QSize(130, 30))
        self.segmentation.setMaximumSize(QtCore.QSize(16777215, 30))
        self.segmentation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.segmentation.setObjectName("segmentation")
        self.horizontalLayout_2.addWidget(self.segmentation)
        self.segments = QtWidgets.QLineEdit(self.centralwidget)
        self.segments.setMinimumSize(QtCore.QSize(100, 25))
        self.segments.setMaximumSize(QtCore.QSize(150, 25))
        self.segments.setObjectName("segments")
        self.horizontalLayout_2.addWidget(self.segments)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.refresh_graphic = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_graphic.setMinimumSize(QtCore.QSize(100, 30))
        self.refresh_graphic.setMaximumSize(QtCore.QSize(150, 30))
        self.refresh_graphic.setObjectName("refresh_graphic")
        self.horizontalLayout.addWidget(self.refresh_graphic)
        self.auto_approach = QtWidgets.QPushButton(self.centralwidget)
        self.auto_approach.setMinimumSize(QtCore.QSize(100, 30))
        self.auto_approach.setMaximumSize(QtCore.QSize(150, 30))
        self.auto_approach.setObjectName("auto_approach")
        self.horizontalLayout.addWidget(self.auto_approach)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Метод ломаных Эйлера"))
        self.equation.setText(_translate("MainWindow", ""))
        self.calculation.setText(_translate("MainWindow", "Расчет приближения:"))
        self.segmentation.setText(_translate("MainWindow", "Количество разбиений N:"))
        self.refresh_graphic.setText(_translate("MainWindow", "Обновить график"))
        self.auto_approach.setText(_translate("MainWindow", "Подобрать приближение"))
