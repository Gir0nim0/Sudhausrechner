# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Sudhausrechner.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 333)
        self.shaBox = QtWidgets.QGroupBox(MainWindow)
        self.shaBox.setGeometry(QtCore.QRect(10, 20, 161, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.shaBox.setFont(font)
        self.shaBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shaBox.setFlat(False)
        self.shaBox.setCheckable(False)
        self.shaBox.setObjectName("shaBox")
        self.label_2 = QtWidgets.QLabel(self.shaBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.schuettung = QtWidgets.QLineEdit(self.shaBox)
        self.schuettung.setGeometry(QtCore.QRect(100, 20, 31, 20))
        self.schuettung.setText("")
        self.schuettung.setAlignment(QtCore.Qt.AlignCenter)
        self.schuettung.setObjectName("schuettung")
        self.label_3 = QtWidgets.QLabel(self.shaBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stammwuerze = QtWidgets.QLineEdit(self.shaBox)
        self.stammwuerze.setGeometry(QtCore.QRect(100, 50, 31, 20))
        self.stammwuerze.setText("")
        self.stammwuerze.setAlignment(QtCore.Qt.AlignCenter)
        self.stammwuerze.setObjectName("stammwuerze")
        self.label = QtWidgets.QLabel(self.shaBox)
        self.label.setGeometry(QtCore.QRect(10, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ausschlagwuerze = QtWidgets.QLineEdit(self.shaBox)
        self.ausschlagwuerze.setGeometry(QtCore.QRect(110, 80, 21, 20))
        self.ausschlagwuerze.setText("")
        self.ausschlagwuerze.setAlignment(QtCore.Qt.AlignCenter)
        self.ausschlagwuerze.setObjectName("ausschlagwuerze")
        self.label_4 = QtWidgets.QLabel(self.shaBox)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sha = QtWidgets.QLabel(self.shaBox)
        self.sha.setGeometry(QtCore.QRect(10, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sha.setFont(font)
        self.sha.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sha.setText("")
        self.sha.setAlignment(QtCore.Qt.AlignCenter)
        self.sha.setObjectName("sha")
        self.shaButton = QtWidgets.QPushButton(self.shaBox)
        self.shaButton.setGeometry(QtCore.QRect(10, 110, 91, 23))
        self.shaButton.setObjectName("shaButton")
        self.label_17 = QtWidgets.QLabel(self.shaBox)
        self.label_17.setGeometry(QtCore.QRect(140, 50, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.shaBox)
        self.label_18.setGeometry(QtCore.QRect(140, 20, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.shaBox)
        self.label_19.setGeometry(QtCore.QRect(140, 80, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.exitButton = QtWidgets.QPushButton(MainWindow)
        self.exitButton.setGeometry(QtCore.QRect(490, 280, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.refraktometerBox = QtWidgets.QGroupBox(MainWindow)
        self.refraktometerBox.setGeometry(QtCore.QRect(200, 20, 251, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.refraktometerBox.setFont(font)
        self.refraktometerBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.refraktometerBox.setObjectName("refraktometerBox")
        self.label_5 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stammwuerzeRefrKorr = QtWidgets.QLineEdit(self.refraktometerBox)
        self.stammwuerzeRefrKorr.setGeometry(QtCore.QRect(160, 20, 31, 20))
        self.stammwuerzeRefrKorr.setText("")
        self.stammwuerzeRefrKorr.setCursorPosition(0)
        self.stammwuerzeRefrKorr.setAlignment(QtCore.Qt.AlignCenter)
        self.stammwuerzeRefrKorr.setObjectName("stammwuerzeRefrKorr")
        self.refrMessWert = QtWidgets.QLineEdit(self.refraktometerBox)
        self.refrMessWert.setGeometry(QtCore.QRect(160, 50, 31, 20))
        self.refrMessWert.setText("")
        self.refrMessWert.setCursorPosition(0)
        self.refrMessWert.setAlignment(QtCore.Qt.AlignCenter)
        self.refrMessWert.setObjectName("refrMessWert")
        self.refraktometerButton = QtWidgets.QPushButton(self.refraktometerBox)
        self.refraktometerButton.setGeometry(QtCore.QRect(10, 110, 91, 23))
        self.refraktometerButton.setObjectName("refraktometerButton")
        self.label_7 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_7.setGeometry(QtCore.QRect(40, 150, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_9.setGeometry(QtCore.QRect(40, 190, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.resultSchRestExtrakt = QtWidgets.QLabel(self.refraktometerBox)
        self.resultSchRestExtrakt.setGeometry(QtCore.QRect(200, 150, 51, 16))
        self.resultSchRestExtrakt.setText("")
        self.resultSchRestExtrakt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resultSchRestExtrakt.setObjectName("resultSchRestExtrakt")
        self.resultSchVergaerungsgrad = QtWidgets.QLabel(self.refraktometerBox)
        self.resultSchVergaerungsgrad.setGeometry(QtCore.QRect(200, 170, 51, 16))
        self.resultSchVergaerungsgrad.setText("")
        self.resultSchVergaerungsgrad.setObjectName("resultSchVergaerungsgrad")
        self.resultAlkohol = QtWidgets.QLabel(self.refraktometerBox)
        self.resultAlkohol.setGeometry(QtCore.QRect(200, 190, 51, 20))
        self.resultAlkohol.setText("")
        self.resultAlkohol.setObjectName("resultAlkohol")
        self.label_15 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_15.setGeometry(QtCore.QRect(200, 20, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_16.setGeometry(QtCore.QRect(200, 50, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_20 = QtWidgets.QLabel(self.refraktometerBox)
        self.label_20.setGeometry(QtCore.QRect(10, 210, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        font.setKerning(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.groupBox = QtWidgets.QGroupBox(MainWindow)
        self.groupBox.setGeometry(QtCore.QRect(480, 20, 101, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 41, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 41, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 100, 41, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 130, 31, 21))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.inputAnzahl033L = QtWidgets.QLineEdit(self.groupBox)
        self.inputAnzahl033L.setGeometry(QtCore.QRect(60, 40, 21, 20))
        self.inputAnzahl033L.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputAnzahl033L.setAlignment(QtCore.Qt.AlignCenter)
        self.inputAnzahl033L.setObjectName("inputAnzahl033L")
        self.inputAnzahl05L = QtWidgets.QLineEdit(self.groupBox)
        self.inputAnzahl05L.setGeometry(QtCore.QRect(60, 70, 21, 20))
        self.inputAnzahl05L.setAlignment(QtCore.Qt.AlignCenter)
        self.inputAnzahl05L.setObjectName("inputAnzahl05L")
        self.inputAnzahl075L = QtWidgets.QLineEdit(self.groupBox)
        self.inputAnzahl075L.setGeometry(QtCore.QRect(60, 100, 21, 20))
        self.inputAnzahl075L.setAlignment(QtCore.Qt.AlignCenter)
        self.inputAnzahl075L.setObjectName("inputAnzahl075L")
        self.inputAnzahl1L = QtWidgets.QLineEdit(self.groupBox)
        self.inputAnzahl1L.setGeometry(QtCore.QRect(60, 130, 21, 20))
        self.inputAnzahl1L.setAlignment(QtCore.Qt.AlignCenter)
        self.inputAnzahl1L.setObjectName("inputAnzahl1L")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(50, 20, 41, 16))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.buttonFlaschenrechner = QtWidgets.QPushButton(self.groupBox)
        self.buttonFlaschenrechner.setGeometry(QtCore.QRect(10, 160, 91, 23))
        self.buttonFlaschenrechner.setObjectName("buttonFlaschenrechner")
        self.flaschenrechnerResult = QtWidgets.QLabel(self.groupBox)
        self.flaschenrechnerResult.setGeometry(QtCore.QRect(10, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.flaschenrechnerResult.setFont(font)
        self.flaschenrechnerResult.setText("")
        self.flaschenrechnerResult.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.flaschenrechnerResult.setObjectName("flaschenrechnerResult")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudhausrechner | Panke Bräu"))
        self.shaBox.setTitle(_translate("MainWindow", "Sudhausausbeute ermitteln"))
        self.label_2.setText(_translate("MainWindow", "Schüttung"))
        self.label_3.setText(_translate("MainWindow", "Stammwürze"))
        self.label.setText(_translate("MainWindow", "Ausschlagwürze"))
        self.label_4.setText(_translate("MainWindow", "Sudhausausbeute bei 20°C:"))
        self.shaButton.setText(_translate("MainWindow", "berechnen"))
        self.label_17.setText(_translate("MainWindow", "°P"))
        self.label_18.setText(_translate("MainWindow", "Kg"))
        self.label_19.setText(_translate("MainWindow", "L"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.refraktometerBox.setTitle(_translate("MainWindow", "Refraktometer-Korrektur"))
        self.label_5.setText(_translate("MainWindow", "Stammwürze"))
        self.label_6.setText(_translate("MainWindow", "Refraktometer Messwert"))
        self.refraktometerButton.setText(_translate("MainWindow", "berechnen"))
        self.label_7.setText(_translate("MainWindow", "Scheinbarer Restextrakt:"))
        self.label_8.setText(_translate("MainWindow", "Scheinbarer Vergärungsgrad:"))
        self.label_9.setText(_translate("MainWindow", "Alkoholgehalt:"))
        self.label_15.setText(_translate("MainWindow", "°P"))
        self.label_16.setText(_translate("MainWindow", "Brix"))
        self.label_20.setText(_translate("MainWindow", "(Nach Terrill Formel)"))
        self.groupBox.setTitle(_translate("MainWindow", "Flaschenrechner"))
        self.label_10.setText(_translate("MainWindow", "0,33 L"))
        self.label_11.setText(_translate("MainWindow", "0,5 L"))
        self.label_12.setText(_translate("MainWindow", "0,75 L"))
        self.label_13.setText(_translate("MainWindow", "1 L"))
        self.inputAnzahl033L.setText(_translate("MainWindow", "0"))
        self.inputAnzahl05L.setText(_translate("MainWindow", "0"))
        self.inputAnzahl075L.setText(_translate("MainWindow", "0"))
        self.inputAnzahl1L.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "Anzahl"))
        self.buttonFlaschenrechner.setText(_translate("MainWindow", "berechnen"))


