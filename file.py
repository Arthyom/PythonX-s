# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ps.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(230, 120, 411, 321))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.pushButton = QtWidgets.QPushButton(self.page_0)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_0)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 230, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_0)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 230, 88, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.page_0)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 120, 175, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.spinBox = QtWidgets.QSpinBox(self.page_0)
        self.spinBox.setGeometry(QtCore.QRect(80, 40, 52, 32))
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(self.page_0)
        self.comboBox.setGeometry(QtCore.QRect(290, 90, 81, 32))
        self.comboBox.setObjectName("comboBox")
        self.toolButton = QtWidgets.QToolButton(self.page_0)
        self.toolButton.setGeometry(QtCore.QRect(10, 60, 33, 34))
        self.toolButton.setObjectName("toolButton")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 160, 88, 34))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(110, 100, 58, 18))
        self.label.setObjectName("label")
        self.spinBox_4 = QtWidgets.QSpinBox(self.page_1)
        self.spinBox_4.setGeometry(QtCore.QRect(290, 70, 52, 32))
        self.spinBox_4.setObjectName("spinBox_4")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 160, 131, 34))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(210, 100, 58, 18))
        self.label_2.setObjectName("label_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.page_2)
        self.spinBox_3.setGeometry(QtCore.QRect(100, 80, 52, 32))
        self.spinBox_3.setObjectName("spinBox_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 150, 131, 34))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 58, 18))
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_3)
        self.spinBox_2.setGeometry(QtCore.QRect(300, 60, 52, 32))
        self.spinBox_2.setObjectName("spinBox_2")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.spinBox.valueChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.spinBox_4.valueChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.spinBox_3.valueChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        self.spinBox_2.valueChanged['int'].connect(self.stackedWidget.setCurrentIndex)
       
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "pagina 1"))
        self.pushButton_2.setText(_translate("MainWindow", "pagina 2"))
        self.pushButton_3.setText(_translate("MainWindow", "pagina 3"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "volver a home"))
        self.label.setText(_translate("MainWindow", "pagina 1"))
        self.pushButton_5.setText(_translate("MainWindow", "volver a home"))
        self.label_2.setText(_translate("MainWindow", "pagina 2"))
        self.pushButton_6.setText(_translate("MainWindow", "volver a home"))
        self.label_3.setText(_translate("MainWindow", "pagina 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

