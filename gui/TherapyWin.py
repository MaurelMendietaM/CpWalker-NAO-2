# -*- coding: utf-8 -*-import sys
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes
import pyqtgraph
from pyqtgraph import PlotWidget

class TherapyWindow(QtGui.QMainWindow):

    onClose = QtCore.pyqtSignal()
    onData = QtCore.pyqtSignal()
    onSensorUpdate = QtCore.pyqtSignal()  

    def __init__(self):
        super(TherapyWindow,self).__init__()
        self.Muscle = None
        self.init_ui()
        self.dataToDisplay={'hr':0,
                            'Inclination':0,
                            }
        self.set_signals()

         
    def init_ui(self):
        #Window Title
        self.setWindowTitle("NAO-CPWalker TherapyWindow")
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

        #Setting Robot conexions Image
        self.robot =QtGui.QLabel(self)
        self.robot.setGeometry(QtCore.QRect(self.winsize_h*0.06,self.winsize_v*0.42,self.winsize_h*0.07,self.winsize_h*0.07))
        #robot=QtGui.QPixmap("gui/img/Nao_head.PNG")
        robot=QtGui.QPixmap("img/Nao_head.PNG")
        robot= robot.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.robot.setPixmap(robot)

        #Setting Sensors conexion Image

        self.Sensors =QtGui.QLabel(self)
        self.Sensors.setGeometry(QtCore.QRect(self.winsize_h*0.06,self.winsize_v*0.54,self.winsize_h*0.07,self.winsize_h*0.07))
        #Sensors=QtGui.QPixmap("gui/img/conex.PNG")
        Sensors=QtGui.QPixmap("img/conex.PNG")
        Sensors= Sensors.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.Sensors.setPixmap(Sensors)

        self.Sensorsc = {}
        # self.Sensorsc['ECG'] = QtGui.QLabel(self)
        # self.Sensorsc['ECG'].setText("ECG:")
        # self.Sensorsc['ECG'].setStyleSheet("font-size:25px; Arial")
        # self.Sensorsc['ECG'].setGeometry(QtCore.QRect(self.winsize_h*0.19,self.winsize_v*0.7,self.winsize_h*0.25 ,self.winsize_h*0.02))

        
        # self.Sensorsc['IMU'] = QtGui.QLabel(self)
        # self.Sensorsc['IMU'].setText("IMU:")
        # self.Sensorsc['IMU'].setStyleSheet("font-size:25px; Arial")
        # self.Sensorsc['IMU'].setGeometry(QtCore.QRect(self.winsize_h*0.14,self.winsize_v*0.57,self.winsize_h*0.25 ,self.winsize_h*0.02))

        self.Sensorsc['EMG'] = QtGui.QLabel(self)
        self.Sensorsc['EMG'].setText("EMG:")
        self.Sensorsc['EMG'].setStyleSheet("font-size:25px; Arial")
        self.Sensorsc['EMG'].setGeometry(QtCore.QRect(self.winsize_h*0.14,self.winsize_v*0.61,self.winsize_h*0.25 ,self.winsize_h*0.02))

        self.Sensorsc['robot'] = QtGui.QLabel(self)
        self.Sensorsc['robot'].setText("Ip:")
        self.Sensorsc['robot'].setStyleSheet("font-size:25px; Arial")
        self.Sensorsc['robot'].setGeometry(QtCore.QRect(self.winsize_h*0.14,self.winsize_v*0.45,self.winsize_h*0.25 ,self.winsize_h*0.02))


        self.Sensorsc['robot_battery'] = QtGui.QLabel(self)
        self.Sensorsc['robot_battery'].setText("Bateria:")
        self.Sensorsc['robot_battery'].setStyleSheet("font-size:25px; Arial")
        self.Sensorsc['robot_battery'].setGeometry(QtCore.QRect(self.winsize_h*0.14,self.winsize_v*0.48,self.winsize_h*0.25 ,self.winsize_h*0.02))



        #Setting HR Image

        # self.heart=QtGui.QLabel(self)
        # self.heart.setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.33,self.winsize_h*0.04,self.winsize_h*0.04))
        # #heart=QtGui.QPixmap("gui/img/heart.PNG")
        # heart=QtGui.QPixmap("img/heart.PNG")
        # heart= heart.scaled(self.winsize_h*0.04,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        # self.heart.setPixmap(heart)

        # self.heart_label=QtGui.QLabel(self)
        # self.heart_label.setGeometry(QtCore.QRect(self.winsize_h*0.24,self.winsize_v*0.34,self.winsize_h*0.25,self.winsize_h*0.03))
        # #heart_label=QtGui.QPixmap("gui/img/rect5562.PNG")
        # heart_label=QtGui.QPixmap("img/rect5562.PNG")
        # heart_label= heart_label.scaled(self.winsize_h*0.3,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        # self.heart_label.setPixmap(heart_label)

        #Setting posture Image

        # self.posture=QtGui.QLabel(self)
        # self.posture.setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.43,self.winsize_h*0.04,self.winsize_h*0.04))
        # #posture =QtGui.QPixmap("gui/img/posture.PNG")
        # posture =QtGui.QPixmap("img/posture.PNG")
        # posture = posture.scaled(self.winsize_h*0.04,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        # self.posture.setPixmap(posture)

        #Setting play and stop Images

        self.play=QtGui.QLabel(self)
        self.play.setGeometry(QtCore.QRect(self.winsize_h*0.85,self.winsize_v*0.8,self.winsize_h*0.07,self.winsize_h*0.07))
        #play =QtGui.QPixmap("gui/img/begin.PNG")
        play =QtGui.QPixmap("img/begin.PNG")
        play = play.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.play.setPixmap(play)

        self.stop=QtGui.QLabel(self)
        self.stop.setGeometry(QtCore.QRect(self.winsize_h*0.75,self.winsize_v*0.8,self.winsize_h*0.07,self.winsize_h*0.07))
        #stop =QtGui.QPixmap("gui/img/stop1.PNG")
        stop =QtGui.QPixmap("img/stop1.PNG")
        stop = stop.scaled(self.winsize_h*0.07,self.winsize_h*0.07,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.stop.setPixmap(stop)





        # self.posture_label=QtGui.QLabel(self)
        # self.posture_label.setGeometry(QtCore.QRect(self.winsize_h*0.24,self.winsize_v*0.44,self.winsize_h*0.25,self.winsize_h*0.03))
        # #posture_label=QtGui.QPixmap("gui/img/rect5562.PNG")
        # posture_label=QtGui.QPixmap("img/rect5562.PNG")
        # posture_label= heart_label.scaled(self.winsize_h*0.3,self.winsize_h*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        # self.posture_label.setPixmap(posture_label)

        # Settings patient name
        self.Patient = {}
        self.Patient['name'] = QtGui.QLabel(self)
        self.Patient['name'].setText("Nombre del paciente :")
        self.Patient['name'].setStyleSheet("font-size:25px; Arial")
        self.Patient['name'].setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.85,self.winsize_h*0.25 ,self.winsize_h*0.02))

        self.Patient['id'] = QtGui.QLabel(self)
        self.Patient['id'].setText("ID del paciente :")
        self.Patient['id'].setStyleSheet("font-size:25px; Arial")
        self.Patient['id'].setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.89,self.winsize_h*0.25 ,self.winsize_h*0.02))

        self.Patient['start'] = QtGui.QLabel(self)
        self.Patient['start'].setText("Iniciar")
        self.Patient['start'].setStyleSheet("font-size:25px; Arial")
        self.Patient['start'].setGeometry(QtCore.QRect(self.winsize_h*0.86,self.winsize_v*0.90,self.winsize_h*0.25 ,self.winsize_h*0.02))

        self.Patient['end'] = QtGui.QLabel(self)
        self.Patient['end'].setText("Finalizar")
        self.Patient['end'].setStyleSheet("font-size:25px; Arial")
        self.Patient['end'].setGeometry(QtCore.QRect(self.winsize_h*0.75,self.winsize_v*0.90,self.winsize_h*0.25 ,self.winsize_h*0.02))


        
        #Setting priority texts
        self.PriorityText = {}
        self.PriorityText['name'] = QtGui.QLabel(self)
        self.PriorityText['name'].setText("Ingresa el numero de sensores a realimentar:")
        self.PriorityText['name'].setStyleSheet("font-size:25px; Arial")
        self.PriorityText['name'].setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.12,self.winsize_h*0.38 ,self.winsize_h*0.02))

        self.Options = {}
        # self.Options['name_first'] = QtGui.QLabel(self)
        # self.Options['name_first'].setText("1:")
        # self.Options['name_first'].setStyleSheet("font-size:25px; Arial")
        # self.Options['name_first'].setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.15,self.winsize_h*0.05 ,self.winsize_h*0.02))

        # self.Options = {}
        # self.Options['name_second'] = QtGui.QLabel(self)
        # self.Options['name_second'].setText("2:")
        # self.Options['name_second'].setStyleSheet("font-size:25px; Arial")
        # self.Options['name_second'].setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.20,self.winsize_h*0.05 ,self.winsize_h*0.02))

        #Priority Options
        self.Options['read_first'] = QtGui.QComboBox(self)
        self.Options['read_first'].setStyleSheet("font-size:20px; Arial")
        self.Options['read_first'].setGeometry(QtCore.QRect(self.winsize_h*0.064,self.winsize_v*0.172,self.winsize_h*0.15 ,self.winsize_h*0.02))   
        self.Options['read_first'].addItem("2")
        self.Options['read_first'].addItem("4") 
        self.Options['read_first'].addItem("6")
        self.Options['read_first'].addItem("8")

        # self.Options['read_second'] = QtGui.QComboBox(self)
        # self.Options['read_second'].setStyleSheet("font-size:25px; Arial")
        # self.Options['read_second'].setGeometry(QtCore.QRect(self.winsize_h*0.067,self.winsize_v*0.20,self.winsize_h*0.15 ,self.winsize_h*0.02))   
        # self.Options['read_second'].addItem("EMG (pierna izquierda)")
        # self.Options['read_second'].addItem("EMG (pierna derecha)") 


        self.Options['EMG_Muscle'] = QtGui.QComboBox(self)
        self.Options['EMG_Muscle'].setStyleSheet("font-size:20px; Arial")
        self.Options['EMG_Muscle'].setGeometry(QtCore.QRect(self.winsize_h*0.23,self.winsize_v*0.172,self.winsize_h*0.25 ,self.winsize_h*0.02))   
        self.Options['EMG_Muscle'].addItem("Gluteo derecho - Gluteo izquierdo")
        self.Options['EMG_Muscle'].addItem("Quadriceps derecho - Quadriceps izquierdo")
        self.Options['EMG_Muscle'].addItem("Triceps derecho - Triceps izquierdo")
        self.Options['EMG_Muscle'].addItem("Hamstring derecho - Hamstring izquierdo")



        # Sensor labels and text

        # self.ECG = {}
        # self.ECG['name'] = QtGui.QLabel(self)
        # self.ECG['name'].setText("Ritmo Cardiaco:")
        # self.ECG['name'].setStyleSheet("font-size:40px; Arial")
        # self.ECG['name'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.35,self.winsize_h*0.3 ,self.winsize_h*0.02))

        # self.ECG['lcd'] = QtGui.QLCDNumber(self)
        # self.ECG['lcd'].setGeometry(QtCore.QRect(self.winsize_h*0.24,self.winsize_v*0.34,self.winsize_h*0.168 ,self.winsize_h*0.03))

        # self.Inclination = {}
        # self.Inclination['name'] = QtGui.QLabel(self)
        # self.Inclination['name'].setText("Grado de inclinacion:")
        # self.Inclination['name'].setStyleSheet("font-size:40px; Arial")
        # self.Inclination['name'].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.45,self.winsize_h*0.3 ,self.winsize_h*0.02))

        # self.Inclination['lcd'] = QtGui.QLCDNumber(self)
        # self.Inclination['lcd'].setGeometry(QtCore.QRect(self.winsize_h*0.24,self.winsize_v*0.44,self.winsize_h*0.168,self.winsize_h*0.03))

        # Setting the buttons of the interface:
        self.controlButtons={}
        #Close Button
        self.controlButtons['close'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['close'].setIconSize(QSize(0,0))
        self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.93,self.winsize_v*0.05,self.winsize_h*0.045,self.winsize_h*0.045)) 

        self.controlButtons['start'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['start'].setIconSize(QSize(0,0))
        self.controlButtons['start'].setGeometry(QtCore.QRect(self.winsize_h*0.85,self.winsize_v*0.8,self.winsize_h*0.07,self.winsize_h*0.07))

        self.controlButtons['stop'] = QtGui.QCommandLinkButton(self)
        self.controlButtons['stop'].setIconSize(QSize(0,0))
        self.controlButtons['stop'].setGeometry(QtCore.QRect(self.winsize_h*0.75,self.winsize_v*0.8,self.winsize_h*0.07,self.winsize_h*0.07)) 
        


        #Graphic Plot Widget

        self.EMGDisplay={}
        self.EMGDisplay['name'] = QtGui.QLabel(self)
        self.EMGDisplay['name'].setText("Grafica Electromiografia")
        self.EMGDisplay['name'].setStyleSheet("font-size:25px; Arial")
        self.EMGDisplay['name'].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.14,self.winsize_h*0.2,self.winsize_h*0.1))
        
        self.EMGDisplay['display']= PlotWidget(self)
        self.EMGDisplay['display'].setGeometry(QtCore.QRect(self.winsize_h*0.3,self.winsize_v*0.25,self.winsize_h*0.6,self.winsize_h*0.3))
        self.EMGDisplay['display'].plotItem.showGrid(True, True, 0.7)

        self.emg =QtGui.QLabel(self)
        self.emg.setGeometry(QtCore.QRect(self.winsize_h*0.3,self.winsize_v*0.25,self.winsize_h*0.6,self.winsize_h*0.3))
        self.emg.setScaledContents(True)
        #emg= emg.scaled(self.winsize_h*0.6,self.winsize_h*0.3,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.emg.setPixmap(QtGui.QPixmap("img/Dorsiflexion.JPG"))


       
        self.show()

        self.connectCloseButton()


    def connectStartButton(self, f):

        self.controlButtons['start'].clicked.connect(f)

    def connectStopButton(self, f):
        self.controlButtons['stop'].clicked.connect(f)

    def set_signals(self):

        self.onData.connect(self.display_data)
                            
                                            
    def connectCloseButton(self):
        self.controlButtons['close'].clicked.connect(self.close)
        self.onClose.emit()

    def setInfoData(self, value, id_patient):

        value =str(value) 
        self.SetPatient = {}
        self.SetPatient['name'] = QtGui.QLabel(self)
        self.SetPatient['name'].setText(value)
        self.SetPatient['name'].setStyleSheet("font-size:30px; Arial")
        self.SetPatient['name'].setGeometry(QtCore.QRect(self.winsize_h*0.18,self.winsize_v*0.90,self.winsize_h*0.25 ,self.winsize_h*0.02))
        self.SetPatient['name'].show()

        id_patient =str(id_patient)
        self.SetPatient['id'] = QtGui.QLabel(self)
        self.SetPatient['id'].setText(id_patient)
        self.SetPatient['id'].setStyleSheet("font-size:30px; Arial")
        self.SetPatient['id'].setGeometry(QtCore.QRect(self.winsize_h*0.18,self.winsize_v*0.93,self.winsize_h*0.25 ,self.winsize_h*0.02))
        self.SetPatient['id'].show()

    def sensorsData(self, ip, battery):

        ip = str(ip)
        self.SetRobot = {}
        self.SetRobot['ip'] = QtGui.QLabel(self)
        self.SetRobot['ip'].setText(ip)
        self.SetRobot['ip'].setStyleSheet("font-size:30px; Arial")
        self.SetRobot['ip'].setGeometry(QtCore.QRect(self.winsize_h*0.26,self.winsize_v*0.59,self.winsize_h*0.25 ,self.winsize_h*0.02))
        self.SetRobot['ip'].show()

        battery = str(battery)

        self.SetRobot['battery'] = QtGui.QLabel(self)
        self.SetRobot['battery'].setText(battery)
        self.SetRobot['battery'].setStyleSheet("font-size:20px; Arial")
        self.SetRobot['battery'].setGeometry(QtCore.QRect(self.winsize_h*0.26,self.winsize_v*0.62,self.winsize_h*0.25 ,self.winsize_h*0.02))
        self.SetRobot['battery'].show()

    def get_OptionsData(self):

       

        priority1  = str(self.Options['read_first'].currentText())
        priority2 = str(self.Options['read_second'].currentText())

        if priority1 == "EMG":
            priority1 = "EMG"
            priority2 == "IMU"
        elif priority1 == "IMU":
            priority1 == "IMU"
            priority2 =="EMG"

        emgMuscle = str(self.Options['EMG_Muscle'].currentText())

        self.Options['EMG_Muscle'].addItem("Gluteo derecho - Gluteo izquierdo")
        self.Options['EMG_Muscle'].addItem("Quadriceps derecho - Quadriceps izquierdo")
        self.Options['EMG_Muscle'].addItem("Triceps derecho - Triceps izquierdo")
        self.Options['EMG_Muscle'].addItem("Hamstring derecho - Hamstring izquierdo")

        if emgMuscle == "Gluteo derecho - Gluteo izquierdo":
            self.Muscle = "1"
        elif emgMuscle == "Quadriceps derecho - Quadriceps izquierdo":
            self.Muscle = "2"
        elif emgMuscle == "Triceps derecho - Triceps izquierdo":
            self.Muscle = "3"
        elif emgMuscle == "Hamstring derecho - Hamstring izquierdo":
            self.Muscle = "4"
  
        self.sensors_Settings = {'priority1' : priority1,'priority2': priority2 ,'Muscle' : self.Muscle}

        return(self.sensors_Settings)

    def display_data(self):

    
        self.ECG['lcd'].setDigitCount(7)
        self.ECG['lcd'].display(self.dataToDisplay['hr'])
        self.Inclination['lcd'].setDigitCount(7)
        self.Inclination['lcd'].display(self.dataToDisplay['Inclination'])

    def update_display_data(self,
                            d = {
                                'hr' : 0,
                                'Inclination' :0
                                }
                            ):
        print("ACA ESTOY")
        self.dataToDisplay =  d
        self.onData.emit()

    def onStopClicked(self):
        self.onStop.emit()
        print('stop clicked')
        self.update_display_data(d = {
                                        'hr' : 0,
                                        'Inclination' : 0,
                                        }
                                        )
    




def test():
    app=QtGui.QApplication(sys.argv)
    GUI=TherapyWindow()
    sys.exit(app.exec_())
A=test()       


