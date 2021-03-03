# -*- coding: utf-8 -*-import sys
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes

class SettingsWindow(QtGui.QMainWindow):


    def __init__(self):
        super(SettingsWindow,self).__init__()

        self.init_ui()
         
    def init_ui(self):
        #Window Title
        self.robot_Settings = {'ip' : None ,'UseRobot' : None}
        self.setWindowTitle("NAO-CPWalker Settings")
        #Window Size
        self.user32=ctypes.windll.user32
        self.screensize=self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1),
        #Resizing MainWindoe to a percentage of the total
        self.winsize_h=int(self.screensize[0])
        self.winsize_v=int(self.screensize[1])
        self.resize(self.winsize_h,self.winsize_v)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Setting the Background Image

        #setting backgroung image
        self.label_background=QtGui.QLabel(self)
        self.label_background.setGeometry(QtCore.QRect(0,0,self.winsize_h,self.winsize_v))
        self.label_background.setPixmap(QtGui.QPixmap("img/Back_1.png"))
        self.label_background.setScaledContents(True)

        #Setting Close Image 
        self.close1=QtGui.QLabel(self)
        self.close1.setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045))
        Icon1=QtGui.QPixmap("img/closebtn.PNG")
        Icon_resize1= Icon1.scaled(self.winsize_h*0.045,self.winsize_h*0.045,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.close1.setPixmap(Icon_resize1)
        # Setting First time Image
        self.start=QtGui.QLabel(self)
        self.start.setGeometry(QtCore.QRect(self.winsize_h*0.15,self.winsize_v*0.35,self.winsize_h*0.3,self.winsize_h*0.3))
        start=QtGui.QPixmap("img/Intro_button.png")
        start_resized= start.scaled(self.winsize_h*0.3,self.winsize_h*0.3,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.start.setPixmap(start_resized)
        #Setting Start Image 
        self.Therapy=QtGui.QLabel(self)
        self.Therapy.setGeometry(QtCore.QRect(self.winsize_h*0.57,self.winsize_v*0.35,self.winsize_h*0.3,self.winsize_h*0.3))
        Therapy=QtGui.QPixmap("img/start_therapy.png")
        Therapy_resized= Therapy.scaled(self.winsize_h*0.3,self.winsize_h*0.3,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Therapy.setPixmap(Therapy_resized)
       




        # Setting the buttons of the interface:
        self.controlButtons={}
        #Close Button
        self.controlButtons['close'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['close'].setIconSize(QSize(0,0))
        self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045)) 
        
        # Introduction Button:

        self.controlButtons['Introduction'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Introduction'].setIconSize(QSize(0,0))
        self.controlButtons['Introduction'].setGeometry(QtCore.QRect(self.winsize_h*0.15,self.winsize_v*0.38,self.winsize_h*0.3,self.winsize_h*0.25)) 

        # Therapy measurments button:
        self.controlButtons['Therapy'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Therapy'].setIconSize(QSize(0,0))
        self.controlButtons['Therapy'].setGeometry(QtCore.QRect(self.winsize_h*0.57,self.winsize_v*0.38,self.winsize_h*0.3,self.winsize_h*0.25)) 



        # Setting the input text for the robot settings
        self.DataDisplay = {}
        #IP Display
        self.DataDisplay['ip'] = QtGui.QLineEdit(self)
        self.DataDisplay['ip'].setStyleSheet("font-size:25px; Arial")
        self.DataDisplay['ip'].setGeometry(QtCore.QRect(self.winsize_h*0.48,self.winsize_v*0.15,self.winsize_h*0.15 ,self.winsize_h*0.02))
        
        self.DataDisplay['ip1'] = QtGui.QComboBox(self)
        self.DataDisplay['ip1'].setStyleSheet("font-size:25px; Arial")
        self.DataDisplay['ip1'].setGeometry(QtCore.QRect(self.winsize_h*0.28,self.winsize_v*0.15,self.winsize_h*0.15 ,self.winsize_h*0.02))   
        self.DataDisplay['ip1'].addItem("192.168.0.100")
        self.DataDisplay['ip1'].addItem("Cambiar direccion IP") 

        #Use robot comboBox
        self.DataDisplay['UseRobot'] = QtGui.QComboBox(self)
        self.DataDisplay['UseRobot'].setStyleSheet("font-size:25px; Arial")
        self.DataDisplay['UseRobot'].setGeometry(QtCore.QRect(self.winsize_h*0.28,self.winsize_v*0.19,self.winsize_h*0.15 ,self.winsize_h*0.02))   
        self.DataDisplay['UseRobot'].addItem("Si")
        self.DataDisplay['UseRobot'].addItem("No")        

        self.show()
        self.connectCloseButton();
        #self.connectBWSButton()
        
    def connectCloseButton(self):
        self.controlButtons['close'].clicked.connect(self.close)       
        
    def connectIntroductionButton(self,f):
        self.controlButtons['Introduction'].clicked.connect(f)

    def connectTherapyButton(self,f):
        self.controlButtons['Therapy'].clicked.connect(f)

    def get_settings_data(self):

        ip  = str(self.DataDisplay['ip1'].currentText())
        if ip == "192.168.1.75":
            ip = "192.168.1.75"
        else:
            ip = str(self.DataDisplay['ip'].text())

        UseRobot  = str(self.DataDisplay['UseRobot'].currentText())
  
        self.robot_Settings = {'ip' : ip ,'UseRobot' : UseRobot}

        return(self.robot_Settings)



def test():
    app=QtGui.QApplication(sys.argv)
    GUI=SettingsWindow()
    sys.exit(app.exec_())
A=test()

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    GUI=SettingsWindow()
    sys.exit(app.exec_())