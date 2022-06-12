# -*- coding: utf-8 -*-

"""
Created on Mon May  9 10:43:24 2022

@author: Felipe
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MainWindow import Ui_MainWindow
import numpy as np
import pandas as pd
import sys
import random
import pickle


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Main,self).__init__(parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.setupUi(self)
        self.resize(1100,750)
        self.model = pickle.load(open('./modelo.sav', 'rb'))
        self.correctos = {1:[0,0],2:[0,0],3:[0,0],4:[0,0],"tot":[0,0]}
        self.items = []
        self.color = [QBrush(QColor(170, 255, 127)),QBrush(QColor(19, 11, 255,150)),
                      QBrush(QColor(239, 117, 255)),QBrush(QColor(255, 170, 0, 170))]
        self.data = pd.read_csv("./Data.csv",  index_col=0)
        self.header = list(self.data.columns)
        QTimer.singleShot(0,self.table.scrollToTop)
        self.btnstart.clicked.connect(self.call_llenar_tabla)
        self.btnstop.clicked.connect(self.detener)
        
    def detener(self):
        try:
            self.timer.stop();
        except:
            pass
        
    def call_llenar_tabla(self):
        self.timer = QTimer()      
        self.timer.timeout.connect(self.llenar_tabla)
        self.timer.start(1000)
        
    def llenar_tabla(self):
        model = QStandardItemModel(1,18)
        model.setHorizontalHeaderLabels(self.header[:-1])
        indice = random.randint(1, self.data.shape[0]-1)
        ejemplo = self.data.iloc[indice]
        self.items.insert(0, ejemplo.tolist())
        for row, data in enumerate(self.items):
            color = self.color[int(float(data[-1]))-1]
            
            for i in range(18):
                item = QStandardItem()
                item.setData(data[i],Qt.DisplayRole)
                item.setBackground(color)
                model.setItem(row, i, item) 
        

        self.table.setModel(model)        
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)
        
        #Prediccion
        ejemplo = self.data.iloc[[indice]]
        #print(ejemplo)
        y_pred = self.model.predict(ejemplo.drop("STATE", axis=1))

        print(y_pred)
        if y_pred == int(ejemplo["STATE"]):
            self.correctos[int(y_pred)][0] += 1
            self.correctos["tot"][0] += 1
            self.foco.setStyleSheet("border-radius: 35px;background-color: rgb(0, 170, 127);")
        else:
            self.correctos[int(ejemplo["STATE"])][1] += 1
            self.correctos["tot"][1] += 1
            self.foco.setStyleSheet("border-radius: 35px;background-color: rgb(255, 88, 88);")

        if y_pred[0] == 1:
            self.lbcondicion.setText("Normal & Slugging")
            self.lbcondicion.setStyleSheet("font-size:15pt; color: rgb(6, 255, 14);")
            
        elif y_pred[0] == 2:
            self.lbcondicion.setText("Air Blockage")
            self.lbcondicion.setStyleSheet("font-size:15pt; color: rgba(19, 11, 255,150);")
            
        elif y_pred[0] == 3:
            self.lbcondicion.setText("Air Leakage")
            self.lbcondicion.setStyleSheet("font-size:15pt; color: rgba(239, 117, 255);")
        else: 
            self.lbcondicion.setText("Diverted Flow")
            self.lbcondicion.setStyleSheet("font-size:15pt; color: rgba(255, 170, 0, 170);")
        
        
        print(self.correctos)
        self.bar.setValue((self.correctos["tot"][0]/len(self.items))*100)
        try:
            self.barn.setValue((self.correctos[1][0]/(self.correctos[1][0]+self.correctos[1][1]))*100)
        except ZeroDivisionError:
            pass
        try:
            self.barb.setValue((self.correctos[2][0]/(self.correctos[2][0]+self.correctos[2][1]))*100)
        except ZeroDivisionError:
            pass
        try:
            self.barl.setValue((self.correctos[3][0]/(self.correctos[3][0]+self.correctos[3][1]))*100)
        except ZeroDivisionError:
            pass
        try:
            self.barf.setValue((self.correctos[4][0]/(self.correctos[4][0]+self.correctos[4][1]))*100)
        except ZeroDivisionError:
            pass
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = Main()
    obj.show()
    sys.exit(app.exec_())