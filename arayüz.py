# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 800))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 321, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTabletTracking(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 321, 151))
        self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(281, 0))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(279, 0))
        self.horizontalSlider_2.setMaximum(180)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_3.setMinimumSize(QtCore.QSize(279, 0))
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout.addWidget(self.horizontalSlider_3)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_4.setMinimumSize(QtCore.QSize(279, 0))
        self.horizontalSlider_4.setMaximum(255)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout.addWidget(self.horizontalSlider_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTabletTracking(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 290, 321, 151))
        self.verticalLayoutWidget_2.setMinimumSize(QtCore.QSize(281, 0))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_5.setMinimumSize(QtCore.QSize(279, 0))
        self.horizontalSlider_5.setMaximum(180)
        self.horizontalSlider_5.setSliderPosition(180)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.verticalLayout_2.addWidget(self.horizontalSlider_5)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_6.setMinimumSize(QtCore.QSize(279, 0))
        self.horizontalSlider_6.setMaximum(255)
        self.horizontalSlider_6.setSliderPosition(255)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.verticalLayout_2.addWidget(self.horizontalSlider_6)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_7.setMinimumSize(QtCore.QSize(279, 0))
        self.horizontalSlider_7.setMaximum(255)
        self.horizontalSlider_7.setSliderPosition(255)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.verticalLayout_2.addWidget(self.horizontalSlider_7)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 580, 341, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(350, 100, 41, 151))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 11, 0, 36)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(350, 300, 41, 151))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 11, 0, 36)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.FeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.FeedLabel.setGeometry(QtCore.QRect(410, 50, 471, 311))
        self.FeedLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FeedLabel.setText("")
        self.FeedLabel.setObjectName("FeedLabel")
        self.FeedLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.FeedLabel_2.setGeometry(QtCore.QRect(410, 390, 471, 311))
        self.FeedLabel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FeedLabel_2.setText("")
        self.FeedLabel_2.setObjectName("FeedLabel_2")
        self.FeedLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.FeedLabel_3.setGeometry(QtCore.QRect(910, 50, 471, 311))
        self.FeedLabel_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FeedLabel_3.setText("")
        self.FeedLabel_3.setObjectName("FeedLabel_3")
        self.FeedLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.FeedLabel_4.setGeometry(QtCore.QRect(910, 390, 471, 311))
        self.FeedLabel_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FeedLabel_4.setText("")
        self.FeedLabel_4.setObjectName("FeedLabel_4")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 520, 311, 20))
        self.horizontalSlider.setMaximum(20000)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setSliderPosition(600)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 480, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 515, 41, 21))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalSlider_2.valueChanged['int'].connect(MainWindow.lower_1) # type: ignore
        self.horizontalSlider_3.valueChanged['int'].connect(MainWindow.lower_2) # type: ignore
        self.horizontalSlider_4.valueChanged['int'].connect(MainWindow.lower_3) # type: ignore
        self.horizontalSlider_5.valueChanged['int'].connect(MainWindow.upper_1) # type: ignore
        self.horizontalSlider_6.valueChanged['int'].connect(MainWindow.upper_2) # type: ignore
        self.horizontalSlider_7.valueChanged['int'].connect(MainWindow.upper_3) # type: ignore
        self.horizontalSlider_7.valueChanged['int'].connect(self.label_9.setNum) # type: ignore
        self.horizontalSlider_6.valueChanged['int'].connect(self.label_8.setNum) # type: ignore
        self.horizontalSlider_5.valueChanged['int'].connect(self.label_7.setNum) # type: ignore
        self.horizontalSlider_4.valueChanged['int'].connect(self.label_6.setNum) # type: ignore
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_4.setNum) # type: ignore
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_5.setNum) # type: ignore
        self.pushButton.clicked.connect(MainWindow.kamera_ac) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.kamera_kapat) # type: ignore
        self.horizontalSlider.valueChanged['int'].connect(self.label_11.setNum) # type: ignore
        self.horizontalSlider.valueChanged['int'].connect(MainWindow.hassasiyet) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HSV DEĞER ARALIĞI "))
        self.label_2.setText(_translate("MainWindow", "LOWER:"))
        self.label_3.setText(_translate("MainWindow", "UPPER:"))
        self.pushButton.setText(_translate("MainWindow", "KAMERAYI AÇ "))
        self.pushButton_2.setText(_translate("MainWindow", "KAMERAYI KAPAT"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "180"))
        self.label_8.setText(_translate("MainWindow", "255"))
        self.label_9.setText(_translate("MainWindow", "255"))
        self.label_10.setText(_translate("MainWindow", "HASSSASİYET :"))
        self.label_11.setText(_translate("MainWindow", "600"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
