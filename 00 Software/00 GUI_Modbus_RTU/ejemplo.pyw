#Librerias
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import sys
import serial
import time

class Hilo(QThread):
    ser = serial.Serial(port='COM5', baudrate= 9600, parity=serial.PARITY_NONE, bytesize= 8, stopbits= 1)
    def __init__(self):
        super(Hilo, self).__init__()
        self.s = self.ser.read()
        print(self.s)
        time.sleep(0.2)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Primer GUI")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Enter in Matrix")
        self.b1.move(50,18)
        self.b1.clicked.connect(self.accion_onclick_b1)

    def accion_onclick_b1(self):
        self.hilo = Hilo()
        self.hilo.start()


    def update(self):
        self.label.adjustSize()

#Función donde se define la ejecución de la solución desarrollada
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

#Ejecuta solución
window()
