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
        MainWindow.resize(1198, 670)
        MainWindow.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(810, 0, 391, 211))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.txt_funcionEntrada = QtGui.QLineEdit(self.groupBox)
        self.txt_funcionEntrada.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.txt_funcionEntrada.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.txt_funcionEntrada.setObjectName(_fromUtf8("txt_funcionEntrada"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spn_Init = QtGui.QDoubleSpinBox(self.groupBox)
        self.spn_Init.setGeometry(QtCore.QRect(10, 80, 62, 27))
        self.spn_Init.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Init.setMinimum(-1000000.0)
        self.spn_Init.setMaximum(1000000.0)
        self.spn_Init.setObjectName(_fromUtf8("spn_Init"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 61, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(210, 60, 91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_AddFun = QtGui.QPushButton(self.groupBox)
        self.btn_AddFun.setGeometry(QtCore.QRect(310, 60, 71, 41))
        self.btn_AddFun.setObjectName(_fromUtf8("btn_AddFun"))
        self.spn_Muestras = QtGui.QDoubleSpinBox(self.groupBox)
        self.spn_Muestras.setGeometry(QtCore.QRect(210, 80, 91, 27))
        self.spn_Muestras.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Muestras.setMinimum(-100000)
        self.spn_Muestras.setMaximum(100000)
        self.spn_Muestras.setObjectName(_fromUtf8("spn_Muestras"))
        self.spn_To = QtGui.QDoubleSpinBox(self.groupBox)
        self.spn_To.setGeometry(QtCore.QRect(110, 80, 62, 27))
        self.spn_To.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_To.setMinimum(-1000000.0)
        self.spn_To.setMaximum(1000000.0)
        self.spn_To.setObjectName(_fromUtf8("spn_To"))
        self.btn_RemFun = QtGui.QPushButton(self.groupBox)
        self.btn_RemFun.setGeometry(QtCore.QRect(310, 100, 71, 41))
        self.btn_RemFun.setObjectName(_fromUtf8("btn_RemFun"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 140, 371, 27))
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.rd_Actual = QtGui.QRadioButton(self.groupBox)
        self.rd_Actual.setGeometry(QtCore.QRect(10, 170, 141, 22))
        self.rd_Actual.setObjectName(_fromUtf8("rd_Actual"))
        self.rd_Todas = QtGui.QRadioButton(self.groupBox)
        self.rd_Todas.setGeometry(QtCore.QRect(310, 170, 71, 21))
        self.rd_Todas.setObjectName(_fromUtf8("rd_Todas"))
        self.chck_Esc = QtGui.QCheckBox(self.groupBox)
        self.chck_Esc.setGeometry(QtCore.QRect(10, 110, 99, 22))
        self.chck_Esc.setObjectName(_fromUtf8("chck_Esc"))
        self.chck_Imp = QtGui.QCheckBox(self.groupBox)
        self.chck_Imp.setGeometry(QtCore.QRect(220, 110, 81, 22))
        self.chck_Imp.setObjectName(_fromUtf8("chck_Imp"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 190, 371, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 811, 671))
        self.label_6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 320, 391, 81))
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
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(10, 68, 371, 10))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.SignalAnalicer = QtGui.QGroupBox(self.centralwidget)
        self.SignalAnalicer.setGeometry(QtCore.QRect(810, 260, 391, 61))
        self.SignalAnalicer.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.SignalAnalicer.setObjectName(_fromUtf8("SignalAnalicer"))
        self.spn_Inv = QtGui.QDoubleSpinBox(self.SignalAnalicer)
        self.spn_Inv.setGeometry(QtCore.QRect(320, 30, 62, 27))
        self.spn_Inv.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.spn_Inv.setMinimum(-1000000.0)
        self.spn_Inv.setMaximum(1000000.0)
        self.spn_Inv.setObjectName(_fromUtf8("spn_Inv"))
        self.cmb_Inv = QtGui.QComboBox(self.SignalAnalicer)
        self.cmb_Inv.setGeometry(QtCore.QRect(10, 30, 301, 27))
        self.cmb_Inv.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_Inv.setFrame(True)
        self.cmb_Inv.setObjectName(_fromUtf8("cmb_Inv"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(810, 200, 391, 61))
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
        self.groupBox_5.setGeometry(QtCore.QRect(810, 400, 391, 161))
        self.groupBox_5.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.cmb_F1 = QtGui.QComboBox(self.groupBox_5)
        self.cmb_F1.setGeometry(QtCore.QRect(10, 40, 371, 27))
        self.cmb_F1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_F1.setObjectName(_fromUtf8("cmb_F1"))
        self.cmb_F2 = QtGui.QComboBox(self.groupBox_5)
        self.cmb_F2.setGeometry(QtCore.QRect(10, 100, 371, 27))
        self.cmb_F2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.cmb_F2.setObjectName(_fromUtf8("cmb_F2"))
        self.cmb_Opr = QtGui.QComboBox(self.groupBox_5)
        self.cmb_Opr.setGeometry(QtCore.QRect(130, 70, 121, 23))
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
        self.line_4 = QtGui.QFrame(self.groupBox_5)
        self.line_4.setGeometry(QtCore.QRect(10, 144, 371, 10))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(810, 560, 391, 111))
        self.groupBox_6.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.comboBox_7 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 70, 371, 27))
        self.comboBox_7.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(231, 77, 0);"))
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 20, 71, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 20, 71, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 20, 71, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 20, 71, 41))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 20, 71, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.coleccion_Funciones=[]

        ### conceccin de senales con slots
        self.btn_AddFun.clicked.connect(self.agregar_Funcion)
        self.btn_RemFun.clicked.connect(self.remover_Funcion)
        self.cmb_Opr.activated.connect(self.slot_Operaciones)
        self.spn_Corri.valueChanged.connect(self.slot_SpinCorrimiento)
        self.spn_Inc.valueChanged.connect(self.slot_SpinEscalamiento)
        self.spn_Inv.valueChanged.connect(self.slot_SpinInvercion)
        self.comboBox.activated.connect(self.slot_SeleccionarSignal)
        self.rd_Todas.clicked.connect(self.graficar_Todas)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficador", None))
        self.groupBox.setTitle(_translate("MainWindow", "Panel de Entrada", None))
        self.txt_funcionEntrada.setToolTip(_translate("MainWindow", "<html><head/><body><p>Introduzca Una nueva funcion</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "De", None))
        self.label_3.setText(_translate("MainWindow", "Hasta", None))
        self.label_4.setText(_translate("MainWindow", "Pasos", None))
        self.btn_AddFun.setText(_translate("MainWindow", "+", None))
        self.btn_RemFun.setText(_translate("MainWindow", "-", None))
        self.rd_Actual.setText(_translate("MainWindow", "funcion Actual", None))
        self.rd_Todas.setText(_translate("MainWindow", "Todas", None))
        self.chck_Esc.setText(_translate("MainWindow", "Escalon ", None))
        self.chck_Imp.setText(_translate("MainWindow", "Impulso", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Corrimiento", None))
        self.SignalAnalicer.setTitle(_translate("MainWindow", "Inversion", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Escalamieno", None))
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

    ## ejecutar slot cuando una funcion sea seleccionada
    def slot_SeleccionarSignal(self):
        ### graficar solo la funcion seleccionada
        plt.clf()
        if ( self.rd_Actual.isChecked() ):
            fn = self.buscar_FuncionComoTexto(self.comboBox.currentText())
            self.graficar_FuncionSeleccionada( fn )


    def remover_Funcion(self):
        fn= str(self.comboBox.currentText())

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

    def slot_SpinCorrimiento (self):
        t0 = self.spn_Corri.value()
        txt_fn = str(self.cmb_Corr.currentText())
        fn = self.buscar_FuncionComoTexto(txt_fn)
        f3 = fn.corrimiento(t0)

        self.funcion_Resultado(f3)

    def slot_SpinEscalamiento (self):
        t0 = self.spn_Inc.value()
        txt_fn = str(self.cmb_Inc.currentText())
        fn = self.buscar_FuncionComoTexto(txt_fn)
        f3 = fn.escalamiento(t0)

        self.funcion_Resultado(f3)

    def slot_SpinInvercion(self):
        t0 = self.spn_Inv.value()
        txt_fn = str(self.cmb_Inv.currentText())
        fn = self.buscar_FuncionComoTexto(txt_fn)
        f3 = fn.inversion(t0)

        self.funcion_Resultado(f3)


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

    def graficar_FuncionSeleccionada(self, fn):
        q = QtGui.QPixmap.fromImage(QtGui.QImage(fn.graficar('graficaPrincipal')))
        self.label_6.setPixmap(q.scaled(self.label_6.width(), self.label_6.height(),QtCore.Qt.KeepAspectRatio))

    def graficar_Todas(self):
        plt.clf()
        for fn in self.coleccion_Funciones:
            self.graficar_FuncionSeleccionada(fn)


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
        self.comboBox.addItem(funcionNueva.funcion_Texto)

    def reagregar_combos(self):
        for fni in self.coleccion_Funciones:
            self.cmb_F1.addItem(fni.funcion_Texto)
            self.cmb_F2.addItem(fni.funcion_Texto)
            self.cmb_Inc.addItem(fni.funcion_Texto)
            self.cmb_Corr.addItem(fni.funcion_Texto)
            self.cmb_Inv.addItem(fni.funcion_Texto)
            self.comboBox_7.addItem(fni.funcion_Texto)
            self.comboBox.addItem(fni.funcion_Texto)


    def borrar_Cmbx (self):
        self.cmb_F1.clear()
        self.cmb_F2.clear()
        self.cmb_Inc.clear()
        self.cmb_Corr.clear()
        self.cmb_Inv.clear()
        self.comboBox_7.clear()
        self.comboBox.clear()

    ## regresar el indice del valor 0
    def buscar_Cero(self, coleccion ):
        return coleccion.index(0)





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
