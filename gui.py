
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QLabel, QWidget
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
import main

class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        # self.monthCount = monthCount
        # self.chartCount = chartCount
        # self.montBreak = monthBreak
        # self.num = num
        # self.Nmax = Nmax
        # self.initialBudget = initialBudget

        self.setGeometry(300, 100, 700, 700)
        self.setWindowTitle('ALGORYTM PSO - ROZWIĄZANIE')
        

    def initUI(self):
        self.b = QPushButton(self)
        self.b.setText('abcd')

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 100, 500, 500)
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
        monthCount = self.textbox1.editingFinished.connect(self.input1)


        # liczba aktyw
        self.label2 = QLabel(self)
        self.label2.setText('Liczba aktyw')
        self.label2.move(200, 125)
        self.update(self.label2)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(75, 120)
        self.textbox2.setValidator(QIntValidator())
        chartCount = self.textbox2.editingFinished.connect(self.input2)
        
        # Ograniczenie czasowe
        self.label3 = QLabel(self)
        self.label3.setText('Ograniczenie czasowe')
        self.label3.move(200, 175)
        self.update(self.label3)

        self.textbox3 = QLineEdit(self)
        self.textbox3.move(75, 170)
        self.textbox3.setValidator(QIntValidator())
        monthBreak = self.textbox3.editingFinished.connect(self.input3)

        # Liczba rozw poczatkowych
        self.label4 = QLabel(self)
        self.label4.setText('Liczba rozwiązań początkowych')
        self.label4.move(200, 225)
        self.update(self.label4)

        self.textbox4 = QLineEdit(self)
        self.textbox4.move(75, 220)
        self.textbox4.setValidator(QIntValidator())
        num = self.textbox4.editingFinished.connect(self.input4)

        # Maksymalna liczba iteracji
        self.label5 = QLabel(self)
        self.label5.setText('Maksymalna liczba iteracji')
        self.label5.move(200, 275)
        self.update(self.label5)

        self.textbox5 = QLineEdit(self)
        self.textbox5.move(75, 270)
        self.textbox5.setValidator(QIntValidator())
        Nmax = self.textbox5.editingFinished.connect(self.input5)

        # Budzet poczatkowy
        self.label6 = QLabel(self)
        self.label6.setText('Budżet początkowy')
        self.label6.move(200, 325)
        self.update(self.label6)

        self.textbox6 = QLineEdit(self)
        self.textbox6.move(75, 320)
        self.textbox6.setValidator(QIntValidator())
        initialBudget = self.textbox6.editingFinished.connect(self.input6)

        # values = [monthCount, chartCount, monthBreak, num, Nmax, initialBudget]

        # przycisk uruchom algorytm
        self.b1 = QPushButton(self)
        self.b1.setText('Uruchom algorytm')
        self.b1.move(75, 400)
        self.update(self.b1)
        self.b1.clicked.connect(self.show_newWindow)

        # przycisk wyjscia
        self.b2 = QPushButton(self)
        self.b2.setText('Wyjście')
        self.b2.move(250, 400)
        self.update(self.b2)
        self.b2.clicked.connect(self.close)

    def show_newWindow(self):
        if self.w is None:
            self.w = SecondWindow()
            self.w.show()

        else:
            self.w.close()
            self.w = None  
    
    def update(self, obj):
        obj.adjustSize()
    
    def input1(self):
        #main.monthCount = self.textbox1.text()
        return self.textbox1.text()
    
    def input2(self):
        #main.chartCount = self.textbox2.text()
        return self.textbox2.text()

    def input3(self):
        # main.monthBreak = self.textbox3.text()
        return self.textbox3.text()
    
    def input4(self):
        # main.num = self.textbox4.text()
        return self.textbox4.text()
    
    def input5(self):
        # main.Nmax = self.textbox5.text()
        return self.textbox5.text()
    
    def input6(self):
        # main.initialBudget = self.textbox6.text()
        return self.textbox6.text()

    #def startButton_clicked(self, val1, val2, val3, val4, val5, val6):
    #     if type(val1) == int and type(val2) == int and type(monthBreak) == int and\
    #          type(num) == int and type(Nmax) == int and type(initialBudget) == int:


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()