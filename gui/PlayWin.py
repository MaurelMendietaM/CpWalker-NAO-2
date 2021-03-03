# -*- coding: utf-8 -*-import sys
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes

class PlayWindow(QtGui.QMainWindow):

    onClose = QtCore.pyqtSignal()

    def __init__(self):
        super(PlayWindow,self).__init__()
        self.init_ui()
         
    def init_ui(self):
        #Window Title
        self.setWindowTitle("NAO-CPWalker Play")
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
        self.label_background.setScaledContents(True)
        #self.label_background.setPixmap(QtGui.QPixmap("gui/img/Back.png"))
        self.label_background.setPixmap(QtGui.QPixmap("img/Back.png"))

        #Setting Close Image 
        self.close1=QtGui.QLabel(self)
        self.close1.setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045))
        #Icon1=QtGui.QPixmap("gui/img/closebtn.PNG")
        Icon1=QtGui.QPixmap("img/closebtn.PNG")
        Icon_resize1= Icon1.scaled(self.winsize_h*0.045,self.winsize_h*0.045,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.close1.setPixmap(Icon_resize1)

        #Setting speech start button
        self.speech_start=QtGui.QLabel(self)
        self.speech_start.setGeometry(QtCore.QRect(self.winsize_h*0.53,self.winsize_v*0.17,self.winsize_h*0.03,self.winsize_h*0.03))
        #speech_start=QtGui.QPixmap("gui/img/Speech.png")
        speech_start=QtGui.QPixmap("img/Speech.png")
        speech_start= speech_start.scaled(self.winsize_h*0.03,self.winsize_h*0.03,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.speech_start.setPixmap(speech_start)

        #Setting Elephant Image 
        self.Elephant=QtGui.QLabel(self)
        self.Elephant.setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2))
        #Elephant=QtGui.QPixmap("gui/img/elephant_butt.png")
        Elephant=QtGui.QPixmap("img/elephant_butt.png")
        Elephant= Elephant.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Elephant.setPixmap(Elephant)

        
        #Setting Mouse Image 
        self.Mouse=QtGui.QLabel(self)
        self.Mouse.setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2))
        #Mouse = QtGui.QPixmap("gui/img/mouse_butt.png")
        Mouse = QtGui.QPixmap("img/mouse_butt.png")
        Mouse = Mouse.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Mouse.setPixmap(Mouse)

        #Setting butterfly Image 
        self.butterfly=QtGui.QLabel(self)
        self.butterfly.setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.59,self.winsize_h*0.2,self.winsize_h*0.2))
        #butterfly = QtGui.QPixmap("gui/img/butterfly_butt.png")
        butterfly = QtGui.QPixmap("img/butterfly_butt.png")
        butterfly = butterfly.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.butterfly.setPixmap(butterfly)

        #Setting monkey Image 
        self.monkey=QtGui.QLabel(self)
        self.monkey.setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.59,self.winsize_h*0.2,self.winsize_h*0.2))
        #monkey = QtGui.QPixmap("gui/img/monkey_butt.png")
        monkey = QtGui.QPixmap("img/monkey_butt.png")
        monkey = monkey.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.monkey.setPixmap(monkey)

        #Setting Pass Image 
        self.Pass=QtGui.QLabel(self)
        self.Pass.setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))
        #Pass = QtGui.QPixmap("gui/img/flecha_1.PNG")
        Pass= QtGui.QPixmap("img/flecha_1.PNG")
        Pass = Pass.scaled(self.winsize_h*0.045,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Pass.setPixmap(Pass)

        # Setting yes image

        self.yes=QtGui.QLabel(self)
        self.yes.setGeometry(QtCore.QRect(self.winsize_h*0.65,self.winsize_v*0.45,self.winsize_h*0.12,self.winsize_h*0.12))
        #yes = QtGui.QPixmap("gui/img/yes_1.png")
        yes = QtGui.QPixmap("img/yes_1.png")
        yes = yes.scaled(self.winsize_h*0.12,self.winsize_h*0.12,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.yes.setPixmap(yes)


        # Setting no images

        self.no=QtGui.QLabel(self)
        self.no.setGeometry(QtCore.QRect(self.winsize_h*0.8,self.winsize_v*0.45,self.winsize_h*0.12,self.winsize_h*0.12))
        #no = QtGui.QPixmap("gui/img/no_1.png")
        no = QtGui.QPixmap("img/no_1.png")
        no = no.scaled(self.winsize_h*0.12,self.winsize_h*0.12,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.no.setPixmap(no)

        # final Image
        self.fin=QtGui.QLabel(self)
        self.fin.setGeometry(QtCore.QRect(self.winsize_h*0.775,self.winsize_v*0.822,self.winsize_h*0.09,self.winsize_h*0.09))
        #fin=QtGui.QPixmap("gui/img/final.png")
        fin=QtGui.QPixmap("img/final.png")
        fin= fin.scaled(self.winsize_h*0.09,self.winsize_h*0.09,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.fin.setPixmap(fin)

        #Setting volume slider 

        self.volume = QtGui.QSlider(self)
        self.volume.setMinimum(0)
        self.volume.setMaximum(100)
        self.volume.setTickPosition(QSlider.TicksBelow)
        self.volume.setTickInterval(5)
        self.volume.setGeometry(QtCore.QRect(self.winsize_h*0.68,self.winsize_v*0.15,self.winsize_h*0.2 ,self.winsize_h*0.12))
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setValue(50)
        
        self.VolumeText = {}
        self.VolumeText['name'] = QtGui.QLabel(self)
        self.VolumeText['name'].setText("Ingresa el volumen :")
        self.VolumeText['name'].setStyleSheet("font-size:25px; Arial")
        self.VolumeText['name'].setGeometry(QtCore.QRect(self.winsize_h*0.7,self.winsize_v*0.1,self.winsize_h*0.2 ,self.winsize_h*0.02))

        self.VolumeText['lcd'] = QtGui.QLCDNumber(self)
        self.VolumeText['lcd'].setGeometry(QtCore.QRect(self.winsize_h*0.6,self.winsize_v*0.195,self.winsize_h*0.05 ,self.winsize_h*0.02))
        #Altura Label:
        self.SpeechText = {}
        
        self.SpeechText['name'] = QtGui.QLabel(self)
        self.SpeechText['name'].setText("Ingresa el texto :")
        self.SpeechText['name'].setStyleSheet("font-size:25px; Arial")
        self.SpeechText['name'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.1,self.winsize_h*0.2 ,self.winsize_h*0.05))

        # ID Display
        self.SpeechText['read'] = QtGui.QLineEdit(self)
        self.SpeechText['read'].setStyleSheet("font-size:35px; Arial")
        self.SpeechText['read'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.17,self.winsize_h*0.35 ,self.winsize_h*0.04))   
        
        # Setting the buttons of the interface:
        self.controlButtons={}
        #Close Button
        self.controlButtons['close'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['close'].setIconSize(QSize(0,0))
        self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045)) 
        
        #Speech Button
        self.controlButtons['speech'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['speech'].setIconSize(QSize(0,0))
        self.controlButtons['speech'].setGeometry(QtCore.QRect(self.winsize_h*0.53,self.winsize_v*0.17,self.winsize_h*0.03,self.winsize_h*0.03)) 
        
        # Elephant Button:

        self.controlButtons['Elephant'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Elephant'].setIconSize(QSize(0,0))
        self.controlButtons['Elephant'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2)) 

        # Monkey measurments button:
        self.controlButtons['monkey'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['monkey'].setIconSize(QSize(0,0))
        self.controlButtons['monkey'].setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.59,self.winsize_h*0.2,self.winsize_h*0.2)) 

        # Butterfly measurments button:
        self.controlButtons['butterfly'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['butterfly'].setIconSize(QSize(0,0))
        self.controlButtons['butterfly'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.59,self.winsize_h*0.2,self.winsize_h*0.2))

        # Butterfly measurments button:
        self.controlButtons['Mouse'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Mouse'].setIconSize(QSize(0,0))
        self.controlButtons['Mouse'].setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2))


        # Pass measurments button:
        self.controlButtons['Pass'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Pass'].setIconSize(QSize(0,0))
        self.controlButtons['Pass'].setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))

        # yes button

        self.controlButtons['yes'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['yes'].setIconSize(QSize(0,0))
        self.controlButtons['yes'].setGeometry(QtCore.QRect(self.winsize_h*0.65,self.winsize_v*0.45,self.winsize_h*0.12,self.winsize_h*0.12))

        # No button
        self.controlButtons['no'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['no'].setIconSize(QSize(0,0))
        self.controlButtons['no'].setGeometry(QtCore.QRect(self.winsize_h*0.8,self.winsize_v*0.45,self.winsize_h*0.12,self.winsize_h*0.12))

        # Fin button
        self.controlButtons['fin'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['fin'].setIconSize(QSize(0,0))
        self.controlButtons['fin'].setGeometry(QtCore.QRect(self.winsize_h*0.775,self.winsize_v*0.822,self.winsize_h*0.09,self.winsize_h*0.09))

        self.show()

        self.connectCloseButton();
        self.connectVolumeSlider(self.get_Volume)

    def connectSpeechButton(self,f):
        self.controlButtons['speech'].clicked.connect(f) 

    def connectCloseButton(self):
        self.controlButtons['close'].clicked.connect(self.close)
        self.onClose.emit()

    def connectVolumeSlider(self,f):
        self.volume.valueChanged.connect(f)

    def get_Volume(self):
        self.volume_data = self.volume.value()
        self.VolumeText['lcd'].display(self.volume_data)

    def send_Volume(self):
        self.volume_data = self.volume.value()
        return(self.volume_data)

    def connectElephantButton(self,f): 
        self.controlButtons['Elephant'].clicked.connect(f) 

    def connectMouseButton(self,f): 
        self.controlButtons['Mouse'].clicked.connect(f)

    def connectButterflyButton(self,f): 
        self.controlButtons['butterfly'].clicked.connect(f)

    def connectMonkeyButton(self,f): 
        self.controlButtons['monkey'].clicked.connect(f)

    def connectPassButton(self,f): 
        self.controlButtons['Pass'].clicked.connect(f)

    def connectFinButton(self,f): 
        self.controlButtons['fin'].clicked.connect(f)

    def get_speech(self):

        speech  = str(self.SpeechText['read'].text())
        return(speech)

    def connectRightButton(self,f):
        self.controlButtons['yes'].clicked.connect(f)

    def connectWrongButton(self,f):
        self.controlButtons['no'].clicked.connect(f)


def test():
    app=QtGui.QApplication(sys.argv)
    GUI=PlayWindow()
    sys.exit(app.exec_())
A=test()       



        