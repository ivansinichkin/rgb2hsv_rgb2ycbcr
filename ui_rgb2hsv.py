# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lab1_hsv.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RGB_2_HSV_2_RGB(object):
    def setupUi(self, RGB_2_HSV_2_RGB):
        RGB_2_HSV_2_RGB.setObjectName("RGB_2_HSV_2_RGB")
        RGB_2_HSV_2_RGB.resize(845, 625)
        self.centralwidget = QtWidgets.QWidget(RGB_2_HSV_2_RGB)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_selectF = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectF.setGeometry(QtCore.QRect(0, 0, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_selectF.setFont(font)
        self.pushButton_selectF.setObjectName("pushButton_selectF")
        self.labelImage_S = QtWidgets.QLabel(self.centralwidget)
        self.labelImage_S.setGeometry(QtCore.QRect(370, 360, 220, 220))
        self.labelImage_S.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelImage_S.setText("")
        self.labelImage_S.setScaledContents(False)
        self.labelImage_S.setWordWrap(False)
        self.labelImage_S.setObjectName("labelImage_S")
        self.pushButton_execute = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_execute.setGeometry(QtCore.QRect(0, 150, 131, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_execute.setFont(font)
        self.pushButton_execute.setObjectName("pushButton_execute")
        self.labelImage_H = QtWidgets.QLabel(self.centralwidget)
        self.labelImage_H.setGeometry(QtCore.QRect(140, 360, 220, 220))
        self.labelImage_H.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelImage_H.setText("")
        self.labelImage_H.setScaledContents(False)
        self.labelImage_H.setWordWrap(False)
        self.labelImage_H.setObjectName("labelImage_H")
        self.valueLabelS = QtWidgets.QLabel(self.centralwidget)
        self.valueLabelS.setGeometry(QtCore.QRect(40, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valueLabelS.setFont(font)
        self.valueLabelS.setObjectName("valueLabelS")
        self.labelImageBase = QtWidgets.QLabel(self.centralwidget)
        self.labelImageBase.setGeometry(QtCore.QRect(140, 0, 330, 330))
        self.labelImageBase.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelImageBase.setText("")
        self.labelImageBase.setScaledContents(False)
        self.labelImageBase.setWordWrap(False)
        self.labelImageBase.setObjectName("labelImageBase")
        self.labelImageResult = QtWidgets.QLabel(self.centralwidget)
        self.labelImageResult.setGeometry(QtCore.QRect(489, 0, 330, 330))
        self.labelImageResult.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelImageResult.setText("")
        self.labelImageResult.setScaledContents(False)
        self.labelImageResult.setWordWrap(False)
        self.labelImageResult.setObjectName("labelImageResult")
        self.sliderV = QtWidgets.QSlider(self.centralwidget)
        self.sliderV.setGeometry(QtCore.QRect(0, 110, 131, 22))
        self.sliderV.setMouseTracking(False)
        self.sliderV.setAccessibleName("")
        self.sliderV.setMaximum(200)
        self.sliderV.setProperty("value", 100)
        self.sliderV.setTracking(True)
        self.sliderV.setOrientation(QtCore.Qt.Horizontal)
        self.sliderV.setInvertedAppearance(False)
        self.sliderV.setInvertedControls(False)
        self.sliderV.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderV.setTickInterval(10)
        self.sliderV.setObjectName("sliderV")
        self.valueLabelV = QtWidgets.QLabel(self.centralwidget)
        self.valueLabelV.setGeometry(QtCore.QRect(40, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.valueLabelV.setFont(font)
        self.valueLabelV.setObjectName("valueLabelV")
        self.labelImage_V = QtWidgets.QLabel(self.centralwidget)
        self.labelImage_V.setGeometry(QtCore.QRect(600, 360, 220, 220))
        self.labelImage_V.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelImage_V.setText("")
        self.labelImage_V.setScaledContents(False)
        self.labelImage_V.setWordWrap(False)
        self.labelImage_V.setObjectName("labelImage_V")
        self.sliderS = QtWidgets.QSlider(self.centralwidget)
        self.sliderS.setGeometry(QtCore.QRect(0, 70, 131, 22))
        self.sliderS.setMouseTracking(False)
        self.sliderS.setAccessibleName("")
        self.sliderS.setMaximum(200)
        self.sliderS.setSingleStep(1)
        self.sliderS.setProperty("value", 100)
        self.sliderS.setTracking(True)
        self.sliderS.setOrientation(QtCore.Qt.Horizontal)
        self.sliderS.setInvertedAppearance(False)
        self.sliderS.setInvertedControls(False)
        self.sliderS.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderS.setTickInterval(10)
        self.sliderS.setObjectName("sliderS")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 580, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 580, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 330, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 330, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(710, 580, 21, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        RGB_2_HSV_2_RGB.setCentralWidget(self.centralwidget)

        self.retranslateUi(RGB_2_HSV_2_RGB)
        QtCore.QMetaObject.connectSlotsByName(RGB_2_HSV_2_RGB)

    def retranslateUi(self, RGB_2_HSV_2_RGB):
        _translate = QtCore.QCoreApplication.translate
        RGB_2_HSV_2_RGB.setWindowTitle(_translate("RGB_2_HSV_2_RGB", "RGB_2_HSV_2_RGB"))
        self.label.setText(_translate("RGB_2_HSV_2_RGB", "S"))
        self.label_2.setText(_translate("RGB_2_HSV_2_RGB", "V"))
        self.pushButton_selectF.setText(_translate("RGB_2_HSV_2_RGB", "Выбрать картинку"))
        self.pushButton_execute.setText(_translate("RGB_2_HSV_2_RGB", "RGB_2_HSV_2_RGB"))
        self.valueLabelS.setText(_translate("RGB_2_HSV_2_RGB", "100"))
        self.valueLabelV.setText(_translate("RGB_2_HSV_2_RGB", "100"))
        self.label_8.setText(_translate("RGB_2_HSV_2_RGB", "S"))
        self.label_7.setText(_translate("RGB_2_HSV_2_RGB", "H"))
        self.label_4.setText(_translate("RGB_2_HSV_2_RGB", "Исходное изображение"))
        self.label_6.setText(_translate("RGB_2_HSV_2_RGB", "Итоговое изображение"))
        self.label_9.setText(_translate("RGB_2_HSV_2_RGB", "V"))