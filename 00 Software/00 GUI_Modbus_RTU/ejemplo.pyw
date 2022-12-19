#Librerias
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import sys
from enum import Enum
from diccionario_modbus import Listado_Holding_Registers, Listado_Input_Registers, Accion_Modbus, Tipo_Registro_Modbus

estado_boton = 0

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Primer GUI")
        self.initUI()

    def initUI(self):
        #etiqueta
        self.etiqueta = QtWidgets.QLabel(self)
        self.etiqueta.move(120,20)
        self.etiqueta.setText("")
        #boton
        self.boton = QtWidgets.QPushButton(self)
        self.boton.setText("Conectar")
        self.boton.move(10,20)
        self.boton.clicked.connect(self.accion_onclick_boton)
        #desplegable tipo registro
        self.desplegable = QtWidgets.QComboBox(self)
        self.desplegable.resize(180, 30)
        self.desplegable.move(10, 100)
        self.desplegable.addItems(Tipo_Registro_Modbus)
        self.desplegable.setDisabled(True)
        self.desplegable.currentIndexChanged.connect(self.cambio_tipo_registro)
        #desplegable accion
        self.desplegable1 = QtWidgets.QComboBox(self)
        self.desplegable1.resize(80, 30)
        self.desplegable1.move(10, 60)
        self.desplegable1.addItems(Accion_Modbus)
        self.desplegable1.setDisabled(True)
        #desplegable indices
        self.desplegable2 = QtWidgets.QComboBox(self)
        self.desplegable2.resize(180, 30)
        self.desplegable2.move(10, 140)
        self.desplegable2.addItems(Listado_Holding_Registers)
        self.desplegable2.setDisabled(True)

    def accion_onclick_boton(self):
        global estado_boton
        global Cricket
        if estado_boton == 0:
            estado_boton = 1
            self.boton.setText("Desconectar")
            self.desplegable.setDisabled(False)
            self.desplegable1.setDisabled(False)
            self.desplegable2.setDisabled(False)
        else:
            estado_boton= 0
            self.boton.setText("Conectar")
            self.desplegable.setDisabled(True)
            self.desplegable1.setDisabled(True)
            self.desplegable2.setDisabled(True)

    def cambio_tipo_registro(self):
        if self.desplegable.currentText() == 'Holding Register':
           self.desplegable2.clear()
           self.desplegable2.addItems(Listado_Holding_Registers)
        else:
            self.desplegable2.clear()
            self.desplegable2.addItems(Listado_Input_Registers)



#Función donde se define la ejecución de la solución desarrollada
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

#Ejecuta solución
window()
