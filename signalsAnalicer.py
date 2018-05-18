# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GraficadorSeñales.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import funcion

import matplotlib.pyplot as plt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):

    def __init(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(Ui_MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1198, 643)
        MainWindow.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(810, 0, 391, 111))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.txt_funcionEntrada = QtGui.QLineEdit(self.groupBox)
        self.txt_funcionEntrada.setGeometry(QtCore.QRect(10, 20, 291, 31))
        self.txt_funcionEntrada.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.txt_funcionEntrada.setObjectName(_fromUtf8("txt_funcionEntrada"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spn_Init = QtGui.QDoubleSpinBox(self.groupBox)
        self.spn_Init.setGeometry(QtCore.QRect(10, 70, 62, 27))
        self.spn_Init.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Init.setMinimum(-1000000.0)
        self.spn_Init.setMaximum(1000000.0)
        self.spn_Init.setObjectName(_fromUtf8("spn_Init"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(110, 50, 61, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(210, 50, 91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_AddFun = QtGui.QPushButton(self.groupBox)
        self.btn_AddFun.setGeometry(QtCore.QRect(310, 20, 71, 41))
        self.btn_AddFun.setObjectName(_fromUtf8("btn_AddFun"))
        self.spn_Muestras = QtGui.QDoubleSpinBox(self.groupBox)
        self.spn_Muestras.setGeometry(QtCore.QRect(210, 70, 91, 27))
        self.spn_Muestras.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Muestras.setMinimum(-100000)
        self.spn_Muestras.setMaximum(100000)
        self.spn_Muestras.setObjectName(_fromUtf8("spn_Muestras"))
        self.spn_To = QtGui.QDoubleSpinBox(self.groupBox)
        self.spn_To.setGeometry(QtCore.QRect(110, 70, 62, 27))
        self.spn_To.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_To.setMinimum(-1000000.0)
        self.spn_To.setMaximum(1000000.0)
        self.spn_To.setObjectName(_fromUtf8("spn_To"))
        self.btn_RemFun = QtGui.QPushButton(self.groupBox)
        self.btn_RemFun.setGeometry(QtCore.QRect(310, 60, 71, 41))
        self.btn_RemFun.setObjectName(_fromUtf8("btn_RemFun"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 811, 641))
        self.label_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 230, 391, 61))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.spn_Corri = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.spn_Corri.setGeometry(QtCore.QRect(320, 30, 62, 27))
        self.spn_Corri.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Corri.setMinimum(-1000000.0)
        self.spn_Corri.setMaximum(1000000.0)
        self.spn_Corri.setObjectName(_fromUtf8("spn_Corri"))
        self.cmb_Corr = QtGui.QComboBox(self.groupBox_2)
        self.cmb_Corr.setGeometry(QtCore.QRect(10, 30, 301, 27))
        self.cmb_Corr.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_Corr.setObjectName(_fromUtf8("cmb_Corr"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(810, 170, 391, 61))
        self.groupBox_3.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.spn_Inv = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spn_Inv.setGeometry(QtCore.QRect(320, 30, 62, 27))
        self.spn_Inv.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Inv.setMinimum(-1000000.0)
        self.spn_Inv.setMaximum(1000000.0)
        self.spn_Inv.setObjectName(_fromUtf8("spn_Inv"))
        self.cmb_Inv = QtGui.QComboBox(self.groupBox_3)
        self.cmb_Inv.setGeometry(QtCore.QRect(10, 30, 301, 27))
        self.cmb_Inv.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_Inv.setFrame(True)
        self.cmb_Inv.setObjectName(_fromUtf8("cmb_Inv"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(810, 110, 391, 61))
        self.groupBox_4.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.spn_Inc = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.spn_Inc.setGeometry(QtCore.QRect(320, 30, 62, 27))
        self.spn_Inc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Inc.setMinimum(-1000000.0)
        self.spn_Inc.setMaximum(1000000.0)
        self.spn_Inc.setObjectName(_fromUtf8("spn_Inc"))
        self.cmb_Inc = QtGui.QComboBox(self.groupBox_4)
        self.cmb_Inc.setGeometry(QtCore.QRect(10, 30, 301, 27))
        self.cmb_Inc.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_Inc.setObjectName(_fromUtf8("cmb_Inc"))
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(810, 290, 391, 121))
        self.groupBox_5.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.cmb_F1 = QtGui.QComboBox(self.groupBox_5)
        self.cmb_F1.setGeometry(QtCore.QRect(10, 30, 371, 27))
        self.cmb_F1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_F1.setObjectName(_fromUtf8("cmb_F1"))
        self.cmb_F2 = QtGui.QComboBox(self.groupBox_5)
        self.cmb_F2.setGeometry(QtCore.QRect(10, 90, 371, 27))
        self.cmb_F2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_F2.setObjectName(_fromUtf8("cmb_F2"))
        self.cmb_Opr = QtGui.QComboBox(self.groupBox_5)
        self.cmb_Opr.setGeometry(QtCore.QRect(130, 60, 121, 23))
        self.cmb_Opr.setAcceptDrops(False)
        self.cmb_Opr.setAutoFillBackground(False)
        self.cmb_Opr.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(221, 73, 0);\n"
""))
        self.cmb_Opr.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.cmb_Opr.setIconSize(QtCore.QSize(0, 0))
        self.cmb_Opr.setObjectName(_fromUtf8("cmb_Opr"))
        self.cmb_Opr.addItem(_fromUtf8(""))
        self.cmb_Opr.addItem(_fromUtf8(""))
        self.cmb_Opr.addItem(_fromUtf8(""))
        self.cmb_Opr.addItem(_fromUtf8(""))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(810, 410, 391, 131))
        self.groupBox_6.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.comboBox_7 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 100, 371, 27))
        self.comboBox_7.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 30, 71, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 30, 71, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 30, 71, 61))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 30, 71, 61))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 30, 71, 61))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.coleccion_Funciones=[]

        ### conectar el boton con el slot
        self.btn_AddFun.clicked.connect(self.agregar_Funcion)
        self.btn_RemFun.clicked.connect(self.remover_Funcion)
        self.cmb_Opr.activated.connect(self.slot_Operaciones)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficador", None))
        self.groupBox.setTitle(_translate("MainWindow", "Panel de Entrada", None))
        self.txt_funcionEntrada.setToolTip(_translate("MainWindow", "<html><head/><body><p>Introduzca Una nueva funcion</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "De", None))
        self.label_3.setText(_translate("MainWindow", "Hasta", None))
        self.label_4.setText(_translate("MainWindow", "Muestras", None))
        self.btn_AddFun.setText(_translate("MainWindow", "+", None))
        self.btn_RemFun.setText(_translate("MainWindow", "-", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Corrimiento", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Inversion", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Incremento", None))
        self.cmb_Inc.setStatusTip(_translate("MainWindow", "Selecciones incremento", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Operaciones", None))
        self.cmb_Opr.setToolTip(_translate("MainWindow", "<html><head/><body><p>Seleccione la Operacion a realizar</p></body></html>", None))
        self.cmb_Opr.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Debe seleccionar una operacion</p></body></html>", None))
        self.cmb_Opr.setItemText(0, _translate("MainWindow", "+", None))
        self.cmb_Opr.setItemText(1, _translate("MainWindow", "-", None))
        self.cmb_Opr.setItemText(2, _translate("MainWindow", "x", None))
        self.cmb_Opr.setItemText(3, _translate("MainWindow", "Combolusion", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Opciones", None))
        self.pushButton_3.setText(_translate("MainWindow", "+", None))
        self.pushButton_4.setText(_translate("MainWindow", "+", None))
        self.pushButton_5.setText(_translate("MainWindow", "+", None))
        self.pushButton_6.setText(_translate("MainWindow", "+", None))
        self.pushButton_7.setText(_translate("MainWindow", "+", None))

    def remover_Funcion(self):
        fn= str(self.txt_funcionEntrada.text())

        for fni in self.coleccion_Funciones:
            if fni.funcion_Texto == fn:
                self.coleccion_Funciones.remove(fni)
            fni.limpiar()

            if len( self.coleccion_Funciones ) == 0:
                fni.limpiar()
                q = QtGui.QPixmap(self.label_6.width(), self.label_6.height())
                q.fill(color=QtCore.Qt.white)
                self.label_6.setPixmap(q)

        
        for fni in self.coleccion_Funciones:

            print(fni.funcion_Texto)
            q = QtGui.QPixmap.fromImage(QtGui.QImage(fni.graficar('graficaPrincipal')))
            self.label_6.setPixmap(q.scaled(self.label_6.width(), self.label_6.height(), QtCore.Qt.KeepAspectRatio))


        self.borrar_Cmbx()
        self.reagregar_combos()
        self.txt_funcionEntrada.clear()


    ##agregar una nueva funcion a la lista de funciones"""
    def agregar_Funcion(self):

        ### conseguir los valores del rango
        rango = [self.spn_Init.value(),self.spn_To.value(),self.spn_Muestras.value() ]
        idntf = str( self.txt_funcionEntrada.text())

        fn = funcion.Funcion(rango,idntf,idntf)

        ### agregar la funcion a la coleccion_Funciones
        self.coleccion_Funciones.append(fn)
        self.agregar_Funcion_Combo(fn)

        #plt.legend()
        #for fni in self.coleccion_Funciones:
        #    markerline, stemlines, baseline = plt.stem(fni.rango,fni.dominio, markerfmt='o',label=fni.funcion_Texto)
        #    plt.setp(stemlines, 'color', plt.getp(markerline,'color'))
        #fn.graficar()
        q = QtGui.QPixmap.fromImage(QtGui.QImage(fn.graficar('graficaPrincipal')))
        self.label_6.setPixmap(q.scaled(self.label_6.width(), self.label_6.height(),QtCore.Qt.KeepAspectRatio))

    ## aregar una nueva funcion a los combos y graficarlos
    def funcion_Resultado(self,fn):
        self.coleccion_Funciones.append(fn)
        self.agregar_Funcion_Combo(fn)

        q = QtGui.QPixmap.fromImage(QtGui.QImage(fn.graficar('graficaPrincipal')))
        self.label_6.setPixmap(q.scaled(self.label_6.width(), self.label_6.height(),QtCore.Qt.KeepAspectRatio))

    ## buscar la funcion enviada en la lista
    def buscar_FuncionComoTexto (self, fnText):
        for fni in self.coleccion_Funciones:
            if fni.funcion_Texto == fnText:
                return fni
        return 0

    ## slot para la señal del cambio del combo
    def slot_Operaciones (self):
        f1 = self.buscar_FuncionComoTexto( str(self.cmb_F1.currentText()))
        f2 = self.buscar_FuncionComoTexto( str(self.cmb_F2.currentText()))
        f3 = 0

        if(f1 != 0 and f2 != 0):
            ## seleccionar operacion
            operacion = str( self.cmb_Opr.currentText() )
            print(operacion)
            if( operacion == '+'):
                f3 = f1+f2
            elif( operacion =='-'):
                f3 = f1-f2
            elif( operacion == 'x'):
                f3 = f1*f2
            elif( operacion == 'combolusion'):
                f3 = f2+f3
            self.funcion_Resultado(f3)
        return f3

    def agregar_Funcion_Combo (self, funcionNueva ):
        self.cmb_F1.addItem(funcionNueva.funcion_Texto)
        self.cmb_F2.addItem(funcionNueva.funcion_Texto)
        self.cmb_Inc.addItem(funcionNueva.funcion_Texto)
        self.cmb_Corr.addItem(funcionNueva.funcion_Texto)
        self.cmb_Inv.addItem(funcionNueva.funcion_Texto)
        self.comboBox_7.addItem(funcionNueva.funcion_Texto)

    def reagregar_combos(self):
        for fni in self.coleccion_Funciones:
            self.cmb_F1.addItem(fni.funcion_Texto)
            self.cmb_F2.addItem(fni.funcion_Texto)
            self.cmb_Inc.addItem(fni.funcion_Texto)
            self.cmb_Corr.addItem(fni.funcion_Texto)
            self.cmb_Inv.addItem(fni.funcion_Texto)
            self.comboBox_7.addItem(fni.funcion_Texto)

    def borrar_Cmbx (self):
        self.cmb_F1.clear()
        self.cmb_F2.clear()
        self.cmb_Inc.clear()
        self.cmb_Corr.clear()
        self.cmb_Inv.clear()
        self.comboBox_7.clear()




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
