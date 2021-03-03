# -*- coding: utf-8 -*-import sys
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes

class IntroductionWindow(QtGui.QMainWindow):


    def __init__(self):
        super(IntroductionWindow,self).__init__()
        self.init_ui()
         
    def init_ui(self):
        #Window Title
        self.setWindowTitle("NAO-CPWalker Therapy")
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
        #self.label_background.setPixmap(QtGui.QPixmap("gui/img/Introduction_background.png"))
        self.label_background.setPixmap(QtGui.QPixmap("img/Introduction_background.png"))
        self.label_background.setScaledContents(True)

        #Setting Close Image 
        self.close1=QtGui.QLabel(self)
        self.close1.setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045))
        Icon1=QtGui.QPixmap("img/closebtn.PNG")
        Icon_resize1= Icon1.scaled(self.winsize_h*0.045,self.winsize_h*0.045,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.close1.setPixmap(Icon_resize1)

        # Setting Intruction Image
        self.start=QtGui.QLabel(self)
        self.start.setGeometry(QtCore.QRect(self.winsize_h*0.775,self.winsize_v*0.822,self.winsize_h*0.09,self.winsize_h*0.09))
        start=QtGui.QPixmap("img/start.png")
        start_resized= start.scaled(self.winsize_h*0.09,self.winsize_h*0.09,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.start.setPixmap(start_resized)

        #Setting Pass Image 
        self.Pass=QtGui.QLabel(self)
        self.Pass.setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))
        Pass = QtGui.QPixmap("img/flecha.PNG")
        #Pass= QtGui.QPixmap("img/flecha.PNG")
        Pass = Pass.scaled(self.winsize_h*0.045,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Pass.setPixmap(Pass)

        #Setting name Image 
        self.name=QtGui.QLabel(self)
        self.name.setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.45,self.winsize_h*0.07,self.winsize_h*0.07))
        name = QtGui.QPixmap("img/name.PNG")
        #Pass= QtGui.QPixmap("img/flecha.PNG")
        name = name.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.name.setPixmap(name)

        #Setting age Image 
        self.age=QtGui.QLabel(self)
        self.age.setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.58,self.winsize_h*0.07,self.winsize_h*0.07))
        age = QtGui.QPixmap("img/age.PNG")
        #Pass= QtGui.QPixmap("img/flecha.PNG")
        age = age.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.age.setPixmap(age)

        #Setting act Image 
        self.act=QtGui.QLabel(self)
        self.act.setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.7,self.winsize_h*0.07,self.winsize_h*0.07))
        act = QtGui.QPixmap("img/act.PNG")
        #Pass= QtGui.QPixmap("img/flecha.PNG")
        act = act.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.act.setPixmap(act)

        # Setting the buttons of the interface:
        self.controlButtons={}

        #Close Button
        self.controlButtons['close'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['close'].setIconSize(QSize(0,0))
        self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045)) 
        
        # Introduction Button:
        self.controlButtons['Introduction'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Introduction'].setIconSize(QSize(0,0))
        self.controlButtons['Introduction'].setGeometry(QtCore.QRect(self.winsize_h*0.775,self.winsize_v*0.822,self.winsize_h*0.09,self.winsize_h*0.09)) 

        # Pass measurments button:
        self.controlButtons['Pass'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Pass'].setIconSize(QSize(0,0))
        self.controlButtons['Pass'].setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))

        # name Button:
        self.controlButtons['name'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['name'].setIconSize(QSize(0,0))
        self.controlButtons['name'].setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.45,self.winsize_h*0.07,self.winsize_h*0.07)) 

        # age measurments button:
        self.controlButtons['age'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['age'].setIconSize(QSize(0,0))
        self.controlButtons['age'].setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.58,self.winsize_h*0.07,self.winsize_h*0.07))

        # act Button:
        self.controlButtons['act'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['act'].setIconSize(QSize(0,0))
        self.controlButtons['act'].setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.7,self.winsize_h*0.07,self.winsize_h*0.07)) 

        # Setting the input text for Patient data
        self.DataDisplay = {}
        #Name Display
        self.DataDisplay['name'] = QtGui.QLineEdit(self)
        self.DataDisplay['name'].setStyleSheet("font-size:35px; Arial")
        self.DataDisplay['name'].setGeometry(QtCore.QRect(self.winsize_h*0.615,self.winsize_v*0.435,self.winsize_h*0.25 ,self.winsize_h*0.03))
        #Age display
        self.DataDisplay['Age'] = QtGui.QLineEdit(self)
        self.DataDisplay['Age'].setStyleSheet("font-size:35px; Arial")
        self.DataDisplay['Age'].setGeometry(QtCore.QRect(self.winsize_h*0.615,self.winsize_v*0.515,self.winsize_h*0.25 ,self.winsize_h*0.03))   
        # Gender display
        self.DataDisplay['Gender'] = QtGui.QComboBox(self)
        self.DataDisplay['Gender'].setStyleSheet("font-size:35px; Arial")
        self.DataDisplay['Gender'].setGeometry(QtCore.QRect(self.winsize_h*0.615,self.winsize_v*0.605,self.winsize_h*0.25 ,self.winsize_h*0.03))   
        self.DataDisplay['Gender'].addItem("Masculino")
        self.DataDisplay['Gender'].addItem("Femenino")
        # Pathology Display
        self.DataDisplay['Pathology'] = QtGui.QLineEdit(self)
        self.DataDisplay['Pathology'].setStyleSheet("font-size:35px; Arial")
        self.DataDisplay['Pathology'].setGeometry(QtCore.QRect(self.winsize_h*0.615,self.winsize_v*0.695,self.winsize_h*0.25 ,self.winsize_h*0.03))   
        # ID Display
        self.DataDisplay['ID'] = QtGui.QLineEdit(self)
        self.DataDisplay['ID'].setStyleSheet("font-size:35px; Arial")
        self.DataDisplay['ID'].setGeometry(QtCore.QRect(self.winsize_h*0.615,self.winsize_v*0.775,self.winsize_h*0.25 ,self.winsize_h*0.03))   

        self.show()
        self.connectCloseButton();
        #self.connectBWSButton()
        
    def connectCloseButton(self):
        self.controlButtons['close'].clicked.connect(self.close)       
        
    def connectIntroductionButton(self,f):
        self.controlButtons['Introduction'].clicked.connect(f)

    def connectPassButton(self,f): 
        self.controlButtons['Pass'].clicked.connect(f)

    def connectnameButton(self,f): 
        self.controlButtons['name'].clicked.connect(f)

    def connectageButton(self,f): 
        self.controlButtons['age'].clicked.connect(f)

    def connectactButton(self,f): 
        self.controlButtons['act'].clicked.connect(f)

    def get_patient_data(self):

        name      = str(self.DataDisplay['name'].text())
        age       = str(self.DataDisplay['Age'].text())
        gender    = str(self.DataDisplay['Gender'].currentText())
        pathology = str(self.DataDisplay['Pathology'].text())
        id_number = str(self.DataDisplay['ID'].text())

        self.patient = {'name' : name ,'id' : id_number,'age':age,'gender':gender,'pathology': pathology}
        return(self.patient)



def test():
    app=QtGui.QApplication(sys.argv)
    GUI=IntroductionWindow()
    sys.exit(app.exec_())
A=test()

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    GUI=ModalityWindow()
    sys.exit(app.exec_())
