# -*- coding: utf-8 -*-import sys
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes

class BodyWindow(QtGui.QMainWindow):

    onClose = QtCore.pyqtSignal()

    def __init__(self):
        super(BodyWindow,self).__init__()
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

        #Setting Head Image 
        self.Head=QtGui.QLabel(self)
        self.Head.setGeometry(QtCore.QRect(self.winsize_h*0.58,self.winsize_v*0.45,self.winsize_h*0.2,self.winsize_h*0.2))
        #Head=QtGui.QPixmap("gui/img/cabeza.png")
        Head=QtGui.QPixmap("img/cabeza.png")
        Head= Head.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Head.setPixmap(Head)

        #Setting ArmL Image 
        self.ArmL=QtGui.QLabel(self)
        self.ArmL.setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2))
        #ArmL = QtGui.QPixmap("gui/img/brazoiz.png")
        ArmL = QtGui.QPixmap("img/brazoiz.png")
        ArmL = ArmL.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ArmL.setPixmap(ArmL)

        #Setting ArmR Image 
        self.ArmR=QtGui.QLabel(self)
        self.ArmR.setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2))
        #ArmR = QtGui.QPixmap("gui/img/brazodr.png")
        ArmR = QtGui.QPixmap("img/brazodr.png")
        ArmR = ArmR.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ArmR.setPixmap(ArmR)

        #Setting LegL Image 
        self.LegL=QtGui.QLabel(self)
        self.LegL.setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.62,self.winsize_h*0.2,self.winsize_h*0.2))
        #LegL = QtGui.QPixmap("gui/img/piernaiz.png")
        LegL = QtGui.QPixmap("img/piernaiz.png")
        LegL = LegL.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.LegL.setPixmap(LegL)

        #Setting LegR Image 
        self.LegR=QtGui.QLabel(self)
        self.LegR.setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.62,self.winsize_h*0.2,self.winsize_h*0.2))
        #LegR = QtGui.QPixmap("gui/img/piernadr.png")
        LegR = QtGui.QPixmap("img/piernadr.png")
        LegR = LegR.scaled(self.winsize_h*0.2,self.winsize_h*0.2,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.LegR.setPixmap(LegR)

        #Setting Pass Image 
        self.Pass=QtGui.QLabel(self)
        self.Pass.setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))
        #Pass = QtGui.QPixmap("gui/img/flecha.png")
        Pass= QtGui.QPixmap("img/flecha.PNG")
        Pass = Pass.scaled(self.winsize_h*0.045,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Pass.setPixmap(Pass)

        #Setting Pass1 Image 
        self.Pass1=QtGui.QLabel(self)
        self.Pass1.setGeometry(QtCore.QRect(self.winsize_h*0.83,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))
        #Pass1 = QtGui.QPixmap("gui/img/flecha_1.jpg")
        Pass1= QtGui.QPixmap("img/flecha_1.PNG")
        Pass1 = Pass1.scaled(self.winsize_h*0.045,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Pass1.setPixmap(Pass1)

        # Setting yes image
        self.yes=QtGui.QLabel(self)
        self.yes.setGeometry(QtCore.QRect(self.winsize_h*0.8,self.winsize_v*0.4,self.winsize_h*0.12,self.winsize_h*0.12))
        #yes = QtGui.QPixmap("gui/img/yes_1.png")
        yes = QtGui.QPixmap("img/yes_1.png")
        yes = yes.scaled(self.winsize_h*0.12,self.winsize_h*0.12,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.yes.setPixmap(yes)

        # Setting no images
        self.no=QtGui.QLabel(self)
        self.no.setGeometry(QtCore.QRect(self.winsize_h*0.8,self.winsize_v*0.6,self.winsize_h*0.12,self.winsize_h*0.12))
        #no = QtGui.QPixmap("gui/img/no_1.png")
        no = QtGui.QPixmap("img/no_1.png")
        no = no.scaled(self.winsize_h*0.12,self.winsize_h*0.12,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.no.setPixmap(no)

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
        self.VolumeText['name'].setGeometry(QtCore.QRect(self.winsize_h*0.7,self.winsize_v*0.13,self.winsize_h*0.2 ,self.winsize_h*0.02))

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
        
        # Head measurments button:
        self.controlButtons['Head'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Head'].setIconSize(QSize(0,0))
        self.controlButtons['Head'].setGeometry(QtCore.QRect(self.winsize_h*0.58,self.winsize_v*0.45,self.winsize_h*0.2,self.winsize_h*0.2)) 

        # ArmL measurments button:
        self.controlButtons['ArmL'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['ArmL'].setIconSize(QSize(0,0))
        self.controlButtons['ArmL'].setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2)) 

        # ArmR measurments button:
        self.controlButtons['ArmR'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['ArmR'].setIconSize(QSize(0,0))
        self.controlButtons['ArmR'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.32,self.winsize_h*0.2,self.winsize_h*0.2))

        # LegL measurments button:
        self.controlButtons['LegL'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['LegL'].setIconSize(QSize(0,0))
        self.controlButtons['LegL'].setGeometry(QtCore.QRect(self.winsize_h*0.35,self.winsize_v*0.62,self.winsize_h*0.2,self.winsize_h*0.2))

        # LegR measurments button:
        self.controlButtons['LegR'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['LegR'].setIconSize(QSize(0,0))
        self.controlButtons['LegR'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.62,self.winsize_h*0.2,self.winsize_h*0.2))

        # Pass measurments button:
        self.controlButtons['Pass'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Pass'].setIconSize(QSize(0,0))
        self.controlButtons['Pass'].setGeometry(QtCore.QRect(self.winsize_h*0.88,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))

        # Pass1 measurments button:
        self.controlButtons['Pass1'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['Pass1'].setIconSize(QSize(0,0))
        self.controlButtons['Pass1'].setGeometry(QtCore.QRect(self.winsize_h*0.83,self.winsize_v*0.055,self.winsize_h*0.045,self.winsize_h*0.04))

        # yes button
        self.controlButtons['yes'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['yes'].setIconSize(QSize(0,0))
        self.controlButtons['yes'].setGeometry(QtCore.QRect(self.winsize_h*0.8,self.winsize_v*0.4,self.winsize_h*0.12,self.winsize_h*0.12))

        # No button
        self.controlButtons['no'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['no'].setIconSize(QSize(0,0))
        self.controlButtons['no'].setGeometry(QtCore.QRect(self.winsize_h*0.8,self.winsize_v*0.6,self.winsize_h*0.12,self.winsize_h*0.12))

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

    def connectHeadButton(self,f): 
        self.controlButtons['Head'].clicked.connect(f) 

    def connectArmLButton(self,f): 
        self.controlButtons['ArmL'].clicked.connect(f)

    def connectArmRButton(self,f): 
        self.controlButtons['ArmR'].clicked.connect(f)

    def connectLegLButton(self,f): 
        self.controlButtons['LegL'].clicked.connect(f)

    def connectLegRButton(self,f): 
        self.controlButtons['LegR'].clicked.connect(f)

    def connectPassButton(self,f): 
        self.controlButtons['Pass'].clicked.connect(f)

    def connectPass1Button(self,f): 
        self.controlButtons['Pass1'].clicked.connect(f)

    def get_speech(self):

        speech  = str(self.SpeechText['read'].text())
        return(speech)

    def connectRightButton(self,f):
        self.controlButtons['yes'].clicked.connect(f)

    def connectWrongButton(self,f):
        self.controlButtons['no'].clicked.connect(f)


def test():
    app=QtGui.QApplication(sys.argv)
    GUI=BodyWindow()
    sys.exit(app.exec_())
A=test()       
