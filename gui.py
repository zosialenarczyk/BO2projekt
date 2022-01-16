
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QLabel, QWidget
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
import main
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, costPoints, Nmax):
        fig, self.ax = plt.subplots()
        self.costPoints = costPoints
        self.Nmax = Nmax

        super().__init__(fig)
        self.setGeometry(1100, 100, 800, 500)
        self.setWindowTitle('FUNKCJA CELU')
        x: np.ndarray = np.arange(self.Nmax)
        
        self.ax.plot(x, self.costPoints)
        self.ax.set(xlabel='Iteracje', ylabel='Wartość funkcji', title='Funkcja celu')
        self.ax.grid()


class SecondWindow(QWidget):
    def __init__(self, monthCount, chartCount, monthBreak, num, Nmax, initialBudget, fraction):
        super(SecondWindow, self).__init__()

        self.w = None

        self.monthCount = monthCount
        self.chartCount = chartCount
        self.monthBreak = monthBreak
        self.num = num
        self.Nmax = Nmax
        self.initialBudget = initialBudget
        self.fraction = fraction

        self.setGeometry(700, 100, 400, 500)
        self.setWindowTitle('ALGORYTM PSO - ROZWIĄZANIE')

        self.globalSolution, self.cost_function, self.startSolution, self.costPoints = main.main(monthCount, chartCount, monthBreak, num, Nmax, initialBudget, fraction)

        self.label1 = QLabel(self)
        self.label1.setText(f'Funkcja celu: {self.cost_function}')
        self.label1.move(75, 75)
        self.label1.adjustSize()

        self.label2 = QLabel(self)
        self.label2.setText(f"ROZWIĄZANIE POCZĄTKOWE: \n\n{self.startSolution}")
        self.label2.move(75, 120)
        self.label2.adjustSize()

        self.label3 = QLabel(self)
        self.label3.setText(f"ROZWIĄZANIE KOŃCOWE: \n\n{self.globalSolution}")
        self.label3.move(75, 250)
        self.label3.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.setText('Wyświetl funkcję celu')
        self.button1.move(75, 400)
        self.button1.adjustSize
        self.button1.clicked.connect(self.show_canvas)

    def show_canvas(self):
        if self.w is None:
            self.w = Canvas(self.costPoints, self.Nmax)
            self.w.show()

        else:
            self.w.close()
            self.w = None  
        


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 100, 500, 500)
        self.setWindowTitle('ALGORYTM PSO - PARAMETRY')
        self.initUI()
    
    def initUI(self):

        self.w = None

        # Naglowek parametrow
        self.mainLabel = QLabel(self)
        self.mainLabel.setText('Parametry algorytmu:')
        self.mainLabel.move(100, 30)
        self.update(self.mainLabel)

        # liczba miesięcy
        self.label1 = QLabel(self)
        self.label1.setText('Liczba miesięcy')
        self.label1.move(200, 75)
        self.update(self.label1)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(75, 70)
        self.textbox1.setValidator(QIntValidator())
        self.textbox1.editingFinished.connect(self.input1)

        # liczba aktyw
        self.label2 = QLabel(self)
        self.label2.setText('Liczba aktyw')
        self.label2.move(200, 125)
        self.update(self.label2)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(75, 120)
        self.textbox2.setValidator(QIntValidator())
        self.textbox2.editingFinished.connect(self.input2)
        
        # Ograniczenie czasowe
        self.label3 = QLabel(self)
        self.label3.setText('Ograniczenie czasowe')
        self.label3.move(200, 175)
        self.update(self.label3)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(75, 170)
        self.textbox3.setValidator(QIntValidator())
        self.textbox3.editingFinished.connect(self.input3)

        # Liczba rozw poczatkowych
        self.label4 = QLabel(self)
        self.label4.setText('Liczba rozwiązań początkowych')
        self.label4.move(200, 225)
        self.update(self.label4)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(75, 220)
        self.textbox4.setValidator(QIntValidator())
        self.textbox4.editingFinished.connect(self.input4)

        # Maksymalna liczba iteracji
        self.label5 = QLabel(self)
        self.label5.setText('Maksymalna liczba iteracji')
        self.label5.move(200, 275)
        self.update(self.label5)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(75, 270)
        self.textbox5.setValidator(QIntValidator())
        self.textbox5.editingFinished.connect(self.input5)

        # Budzet poczatkowy
        self.label6 = QLabel(self)
        self.label6.setText('Budżet początkowy')
        self.label6.move(200, 325)
        self.update(self.label6)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(75, 320)
        self.textbox6.setValidator(QIntValidator())
        self.textbox6.editingFinished.connect(self.input6)

        # Ułamek
        self.label7 = QLabel(self)
        self.label7.setText('Współczynnik funkcji kary')
        self.label7.move(200, 375)
        self.update(self.label7)

        self.textbox7 = QLineEdit(self)
        self.textbox7.move(75, 370)
        self.textbox7.setValidator(QDoubleValidator())
        self.textbox7.editingFinished.connect(self.input7)

        # values = [monthCount, chartCount, monthBreak, num, Nmax, initialBudget]

        # przycisk uruchom algorytm
        self.b1 = QPushButton(self)
        self.b1.setText('Uruchom algorytm')
        self.b1.move(75, 425)
        self.update(self.b1)
        self.b1.clicked.connect(self.show_newWindow)

        # przycisk wyjscia
        self.b2 = QPushButton(self)
        self.b2.setText('Wyjście')
        self.b2.move(250, 425)
        self.update(self.b2)
        self.b2.clicked.connect(self.close)

    def show_newWindow(self):
        if self.w is None:
            self.w = SecondWindow(self.monthCount, self.chartCount, self.monthBreak, self.num, self.Nmax, self.initialBudget, self.fraction)
            self.w.show()

        else:
            self.w.close()
            self.w = None  
    
    def update(self, obj):
        obj.adjustSize()
    
    def input1(self):
        #main.monthCount = self.textbox1.text()
        self.monthCount = int(self.textbox1.text())
    
    def input2(self):
        #main.chartCount = self.textbox2.text()
        self.chartCount =  int(self.textbox2.text())

    def input3(self):
        # main.monthBreak = self.textbox3.text()
        self.monthBreak =  int(self.textbox3.text())
    
    def input4(self):
        # main.num = self.textbox4.text()
        self.num =  int(self.textbox4.text())
    
    def input5(self):
        # main.Nmax = self.textbox5.text()
        self.Nmax =  int(self.textbox5.text())
    
    def input6(self):
        # main.initialBudget = self.textbox6.text()
        self.initialBudget =  int(self.textbox6.text())

    def input7(self):
        # main.fraction = self.textbox7.text()
        self.fraction =  float(self.textbox7.text().replace(',', '.'))

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()