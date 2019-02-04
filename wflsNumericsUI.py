# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wflsNumerics.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from wflsNumerics import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 609)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menuIzquierdo = QtWidgets.QFrame(self.centralwidget)
        self.menuIzquierdo.setGeometry(QtCore.QRect(0, -1, 91, 611))
        self.menuIzquierdo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuIzquierdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuIzquierdo.setObjectName("menuIzquierdo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.menuIzquierdo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 93, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.btn_raices = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon.fromTheme("labplot-xy-fourier-transform-curve")
        self.btn_raices.setIcon(icon)
        self.btn_raices.setIconSize(QtCore.QSize(25, 25))
        self.btn_raices.setObjectName("btn_raices")
        self.verticalLayout.addWidget(self.btn_raices)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.menuIzquierdo)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 91, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_atras = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_atras.setText("")
        icon = QtGui.QIcon.fromTheme("draw-arrow-back")
        self.btn_atras.setIcon(icon)
        self.btn_atras.setIconSize(QtCore.QSize(50, 50))
        self.btn_atras.setObjectName("btn_atras")
        self.verticalLayout_2.addWidget(self.btn_atras)
        self.frm_contenido = QtWidgets.QFrame(self.centralwidget)
        self.frm_contenido.setGeometry(QtCore.QRect(90, 0, 891, 611))
        self.frm_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_contenido.setObjectName("frm_contenido")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frm_contenido)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 661, 591))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stk_page_0 = QtWidgets.QWidget()
        self.stk_page_0.setObjectName("stk_page_0")
        self.stackedWidget.addWidget(self.stk_page_0)
        self.stk_polMet = QtWidgets.QWidget()
        self.stk_polMet.setObjectName("stk_polMet")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.stk_polMet)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 220, 340, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_polHorner = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_polHorner.setObjectName("btn_polHorner")
        self.horizontalLayout.addWidget(self.btn_polHorner)
        self.btn_binSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_binSearch.setObjectName("btn_binSearch")
        self.horizontalLayout.addWidget(self.btn_binSearch)
        self.btn_false = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_false.setObjectName("btn_false")
        self.horizontalLayout.addWidget(self.btn_false)
        self.stackedWidget.addWidget(self.stk_polMet)
        self.stk_polComp_2 = QtWidgets.QStackedWidget(self.frm_contenido)
        self.stk_polComp_2.setGeometry(QtCore.QRect(680, 10, 191, 589))
        self.stk_polComp_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.stk_polComp_2.setObjectName("stk_polComp_2")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stk_polComp_2.addWidget(self.page_2)
        self.pg_pol_2 = QtWidgets.QWidget()
        self.pg_pol_2.setObjectName("pg_pol_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.pg_pol_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 191, 581))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spn_from_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.spn_from_2.setObjectName("spn_from_2")
        self.gridLayout_4.addWidget(self.spn_from_2, 6, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_4.addWidget(self.pushButton_15, 14, 0, 1, 2)
        self.spn_to_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.spn_to_2.setObjectName("spn_to_2")
        self.gridLayout_4.addWidget(self.spn_to_2, 6, 1, 1, 1)
        self.ln_exp_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.ln_exp_2.setObjectName("ln_exp_2")
        self.gridLayout_4.addWidget(self.ln_exp_2, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 10, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 11, 0, 1, 2)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 13, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setAutoFillBackground(False)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 2)
        self.btn_plotInd = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_plotInd.setObjectName("btn_plotInd")
        self.gridLayout_4.addWidget(self.btn_plotInd, 9, 0, 1, 2)
        self.btn_calcular_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.btn_calcular_2.setObjectName("btn_calcular_2")
        self.gridLayout_4.addWidget(self.btn_calcular_2, 2, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 12, 0, 1, 2)
        self.stk_polComp_2.addWidget(self.pg_pol_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stk_polComp_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.exp = WflsNumerics()
        self.setConections()
        self.setStartState()
        self.type = 0
        self.method = 0
    
    def setConections(self):
        self.btn_atras.clicked.connect(lambda: self.setStartState())
        self.btn_raices.clicked.connect(lambda: self.setTypeState(1))

        ### set flag to user the correct polinomial root method
        self.btn_polHorner.clicked.connect(lambda: self.setMethodState(1))
        self.btn_binSearch.clicked.connect(lambda: self.setMethodState(2))
        self.btn_false.clicked.connect(lambda: self.setMethodState(3))
        
        self.btn_calcular_2.clicked.connect(lambda: self.calculatePoolinomialRoots())
        self.btn_plotInd.clicked.connect(lambda: self.plotIndependent())

    def plotIndependent(self):
        fromm = float(self.spn_from_2.text())
        to = float(self.spn_to_2.text())
        expression = self.ln_exp_2.text()
        print expression, fromm, to
        self.exp.plotIndependetExpression(expression, fromm, to)

    def calculatePoolinomialRoots(self):
        expression = self.ln_exp_2.text()
        roots = 0
        ### calculate by hornerWfls
        if self.method == 1:
            roots = self.exp.hornerWfls(expression)
        ### calculate by bisecction
        elif self.method == 2:
            print 'bisec'

        for ri in roots:
            self.label_5.setText( self.label_5.text() + str(ri) + ', ' )
        

    def setStartState(self):
        self.stk_polComp_2.hide()
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 871, 591))

    def setMethodState(self, method = 0):
        self.method = method
        self.stk_polComp_2.show()
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 661, 591))
        self.stackedWidget.setCurrentIndex(0)

    def setTypeState(self, type = 1):
        self.type = type
        self.stackedWidget.setCurrentIndex(type)
        self.stk_polComp_2.hide()
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 871, 591))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.btn_raices.setText(_translate("MainWindow", "Raices"))
        self.btn_polHorner.setText(_translate("MainWindow", "Horner/WFLS"))
        self.btn_binSearch.setText(_translate("MainWindow", "Binary search"))
        self.btn_false.setText(_translate("MainWindow", "False position"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.ln_exp_2.setPlaceholderText(_translate("MainWindow", "Enter a Polinomial Function"))
        self.label_13.setText(_translate("MainWindow", "From"))
        self.label_14.setText(_translate("MainWindow", "Total Roots"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.label_15.setText(_translate("MainWindow", "To"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.btn_plotInd.setText(_translate("MainWindow", "Plot Independent"))
        self.btn_calcular_2.setText(_translate("MainWindow", "Calculate Roots"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

