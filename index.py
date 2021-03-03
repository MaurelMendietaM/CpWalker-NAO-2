#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:23:31 2017

@author: pi
"""

import threading

import gui.IntroductionWin as Introduction   
import gui.SettingsWin as Settings  
import gui.PlayWin as Play
import gui.TherapyWin as MainTherapy
import robotController.NAO_controller as controller
import gui.BodyWin as Body
#import lib.SensorManager as manager 
from PyQt4 import QtCore, QtGui
import time
import sys
import random


class NAO_CpWalker(object):
    
    def __init__(self, settings = {'UseSensors': False,
                                   'UseRobot'  : True,
                                   'RobotIp'   : "192.168.0.100",
                                   'RobotPort' : 9559
                                  }):

        #load settings
        self.settings = settings
        self.mode = None
        #Interface Objects
        self.settingsWin = Settings.SettingsWindow()
        self.IntroductionWin = Introduction.IntroductionWindow()
        self.PlayWin = Play.PlayWindow()
        self.therapyWin = MainTherapy.TherapyWindow()
        self.bodyWin = Body.BodyWindow()   

        # Load signals

        #therapy win interface object
        

        self.settingsWin.connectIntroductionButton(self.go_to_Introduction) 
        self.settingsWin.connectTherapyButton(self.start_sessionSettings)

        self.therapyWin.connectStartButton(self.onStartThreads)
        self.therapyWin.connectStopButton(self.shutdown)
        self.settingsWin.show()  

        
        

    def go_to_Introduction(self):

        
        
        #m = self.settingsWin.get_settings_data()


        #self.settings['RobotIp'] = m['ip']

        self.settings['RobotIp'] = "192.168.0.100"

        if self.settings['UseRobot']:
            #self.RobotCaptureThread = RobotCaptureThread(interface = self)
            self.robotController = controller.RobotController({
                                                                 'name'       : "NAO",
                                                                 'ip'         : self.settings['RobotIp'],
                                                                 'port'       : self.settings['RobotPort'],
                                                                 'UseSpanish' : True,
                                                                 'MotivationTime': 300000000,
                                                                 'HeartRate_Lim': 120,
                                                                 'Cerv_Lim': 0,
                                                                 'Thor_Lim': 0
                                                              })

        self.IntroductionWin.show()
        self.settingsWin.hide()
        
        self.IntroductionWin.connectIntroductionButton(self.on_startIntroduction)

    def on_startIntroduction(self):

        self.bodyWin.hide()
        self.PlayWin.hide()
        self.IntroductionWin.show()

        patient = self.IntroductionWin.get_patient_data()
        self.robotController.patient = patient
        self.robotController.tracking_faces()
        #self.robotController.start_Introduction()
        #self.robotController.launch_SoundTracker()
        self.robotController.load_selfPresentation()
        #self.PlayWin.show()
        self.robotController.load_patientPresentation()

        self.IntroductionWin.connectnameButton(self.name_presentation)
        self.IntroductionWin.connectageButton(self.age_presentation)
        self.IntroductionWin.connectactButton(self.act_presentation)

        self.IntroductionWin.connectPassButton(self.PassWin)
        # Set Volume of the robot
        #self.shutdown()
    
    def speech_Production(self):
        volume = self.PlayWin.send_Volume()
        volume = ((float(volume))/100)*1.45

        print(volume)
        self.robotController.setVolume(volume)
        say = self.PlayWin.get_speech()
        self.robotController.load_Speech(say)

    def name_presentation(self):
        self.robotController.load_name()

    def age_presentation(self):
        self.robotController.load_age()

    def act_presentation(self):
        self.robotController.load_activity()

    def Head_Explanation(self):
        self.robotController.load_HeadExplanation()

    def ArmL_Explanation(self):
        self.robotController.load_ArmLExplanation()

    def ArmR_Explanation(self):
        self.robotController.load_ArmRExplanation()

    def LegL_Explanation(self):
        self.robotController.load_LegLExplanation()

    def LegR_Explanation(self):
        self.robotController.load_LegRExplanation()

    def elephant_Game(self):
        self.robotController.load_ElephantBehavior()

    def mouse_Game(self):
        self.robotController.load_MouseBehavior()

    def monkey_Game(self):
        self.robotController.load_gorillaBehavior()

    def butterfly_Game(self):
        self.robotController.load_butterflyBehavior()

    def bye(self):
        self.robotController.load_bye()

    def PassWin(self):
        self.IntroductionWin.hide()
        self.PlayWin.hide()
        # Set body explanation 
        self.bodyWin.show()

        self.bodyWin.connectHeadButton(self.Head_Explanation)
        self.bodyWin.connectArmLButton(self.ArmL_Explanation)
        self.bodyWin.connectArmRButton(self.ArmR_Explanation)
        self.bodyWin.connectLegLButton(self.LegL_Explanation)
        self.bodyWin.connectLegRButton(self.LegR_Explanation)

        #Speech production
        self.bodyWin.connectSpeechButton(self.speech_Production)

        #Set behaviors to right answer
        self.bodyWin.connectRightButton(self.robotController.load_Right)
        #Set behaviors to wrong answer
        self.bodyWin.connectWrongButton(self.robotController.load_Wrong)

        #Set change window
        self.bodyWin.connectPassButton(self.Pass_Win)
        self.bodyWin.connectPass1Button(self.go_to_Introduction)

    def Pass_Win(self):
        self.bodyWin.hide()
        self.IntroductionWin.hide()
        self.PlayWin.show()

        #Set animals game
        self.PlayWin.connectElephantButton(self.elephant_Game)
        self.PlayWin.connectMouseButton(self.mouse_Game)
        self.PlayWin.connectButterflyButton(self.butterfly_Game)
        self.PlayWin.connectMonkeyButton(self.monkey_Game)

        #Speech production
        self.PlayWin.connectSpeechButton(self.speech_Production)

        # Set behaviors to right answer
        self.PlayWin.connectRightButton(self.robotController.load_Right)
        #Set behaviors to wrong answer
        self.PlayWin.connectWrongButton(self.robotController.load_Wrong)

        self.PlayWin.connectPassButton(self.PassWin)

        self.PlayWin.connectFinButton(self.bye)


    def load_Speech(self):
        pass

    def start_sessionSettings(self):
    	print('Here')
        m = self.settingsWin.get_settings_data()
        battery = "85%"

        self.settings['RobotIp'] = m['ip']

        if self.settings['UseRobot']:
            self.RobotCaptureThread = RobotCaptureThread(interface = self)
            self.robotController = controller.RobotController({
                                                                 'name'       : "NAO",
                                                                 'ip'         : self.settings['RobotIp'],
                                                                 'port'       : self.settings['RobotPort'],
                                                                 'UseSpanish' : True,
                                                                 'MotivationTime': 300000000,
                                                                 'HeartRate_Lim': 120,
                                                                 'Cerv_Lim': 0,
                                                                 'Thor_Lim': 0
                                                              })
        self.therapyWin.show()
        self.therapyWin.sensorsData(m['ip'], battery)

        self.sensor_Settings()

    def onStartThreads(self):

    	self.SensorUpdateThread.start()
    	self.SensorAcquisitionThread.start()

    def sensor_Settings(self):

        self.SensorUpdateThread  = SensorUpdateThread(f =self.sensor_update, sample = 1)

        self.Manager = manager.SensorManager( ecg   = {"port":'COM3', "sample":1},
                                              EMG   = {"MuscletoUse": "1"})

        self.SensorAcquisitionThread = SensorAcquisitionThread(f=self.Manager.update_data, sample =1)

        if self.settings['UseSensors']:
            
            # set sensors
            self.Manager.set_sensors(ecg = True, emg=True)
            self.Manager.launch_Sensors()
            time.sleep(5)

    def sensor_update(self):

    	if self.settings['UseSensors']:
    		self.data = self.Manager.get_Data()
    		print('Index')
    		print(self.data)
    		self.therapyWin.update_display_data(d = { 'hr' :self.data['ecg'],
                                                      'Inclination' : self.data['emg']['contractions']
                                                      }
                                    			)
    		self.therapyWin.onSensorUpdate.emit()

    	else:
    		self.data = self.Manager.get_data()
    		self.therapyWin.update_display_data(d = {
                                                        'hr' :self.data['ecg'],
                                                        'Inclination' : self.data['emg']['contractions']
                                                      })
    		self.therapyWin.onSensorUpdate.emit()


    def shutdown(self):
    	self.SensorUpdateThread.shutdown()
    	self.SensorAcquisitionThread.shutdown()
        self.robotController.shutdown()


class RobotCaptureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 10, interface = None):
        super(RobotCaptureThread,self).__init__()
        self.Ts = sample
        self.ON = True
        self.interface = interface
        
        
        
    def run(self):
        #self.interface.robotController.posture.goToPosture("StandZero", 1.0)
        while self.ON:
            d = self.interface.ManagerRx.get_data()
            self.interface.robotController.set_data(d)
            time.sleep(self.Ts)
            
                
    def shutdown(self):
        self.ON = False

class SensorUpdateThread(QtCore.QThread):

     def __init__(self, parent = None, f = None, sample = 1):
        super(SensorUpdateThread,self).__init__()
        self.f = f
        self.Ts = sample
        self.ON = True
        
     def run(self):

        if self.f:
            while self.ON:
                self.f()
                time.sleep(self.Ts)

     def shutdown(self):
        self.ON = False

class SensorAcquisitionThread(QtCore.QThread):

	def __init__(self, parent = None, f = None, sample = 1):
		super(SensorAcquisitionThread,self).__init__()
		self.f = f
		self.Ts = sample
		self.ON = True

	def run(self):
		if self.f:
			while self.ON:
				self.f()
				time.sleep(self.Ts)

	def shutdown(self):
		self.ON = False

    #def shutdown(self):
    	#self.ON = False

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	a =NAO_CpWalker()
	sys.exit(app.exec_())
