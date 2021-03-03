# -*- coding: cp1252 -*-
import sys
import qi
from naoqi import ALModule
from naoqi import ALBroker
#importing NAO dialogs
import resources.dialogs as dialogs
import soundTracker as soundTracker
#import almath
import logging
import time
import random
import threading
import functools

class RobotController(object):

    def __init__(self, settings = { 'name'           : "NAO",
                                   'ip'             : '192.168.0.100',
                                   'port'           : 9559,
                                   'UseSpanish'     : True,
                                   'MotivationTime' : 300000000,
                                   'HeartRate_Lim'  : 140,
                                   'Cerv_Lim'       : 0,
                                   'Thor_Lim'       : 0

                                 }):
        
        self.settings = settings
        self.ip = self.settings['ip']
        self.port = self.settings['port']
        self.useSpanish = self.settings['UseSpanish']
        self.patient = None

        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        
        except RuntimeError:
                logging.debug("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                              "Please check your script arguments. Run with -h option for help.")
                sys.exit(1)
        
        self.robotName = self.settings['name']
        self.HR_lim = self.settings['HeartRate_Lim']
        self.Cer_lim = self.settings['Cerv_Lim']
        self.Thor_lim = self.settings['Thor_Lim']
        self.dialogs = dialogs.Dialogs()

        self.go_on = True
        self.soun_ON = None
        

        
        
        # Updating the services of the robot

        #Load memory services to recognize events
        self.memory = self.session.service("ALMemory")

        #Load AlTextToSpeech
        self.tts = self.session.service("ALTextToSpeech")
        self.setLanguage('Spanish')
        # Load animated speech service
        self.animatedSpeechProxy = self.session.service("ALAnimatedSpeech")
        # Load motion service
        self.motion = self.session.service("ALMotion")
        #Load posture service
        self.posture = self.session.service("ALRobotPosture")
        #Load tracker service 
        self.tracker = self.session.service("ALTracker") 

        # Create the sound tracker of the robot
        self.soundTracker=soundTracker.Sound_Detector()

        # Load behaviors services
        self.behavior_mng_service = self.session.service("ALBehaviorManager")

        #names = self.behavior_mng_service.getInstalledBehaviors()
        #print "Behaviors on the robot:"
        #print names
        #Call launchDialogs function
        self.flag_Sound = True

        
        self.launchDialogs()


    def setLanguage(self, value):
        self.tts.setLanguage(value)

    def setVolume(self, value):
        curr_Vol = self.tts.getVolume()
        print(curr_Vol)
        self.tts.setVolume(value)


    def launchDialogs(self):
        #loading dialogs
        self.dialogs.load_dialogs()

    def start_Introduction(self):
        # Function to start the introduction with NAO

        self.motion.wakeUp()
        self.animatedSpeechProxy.say(self.dialogs.WelcomeSentence)
        
    def launch_SoundTracker(self):

        print('launching Sound tracker')
        self.soundTracker.on_Start()
        self.soundTracker.launch_thread()
        time.sleep(2)
        self.cont = 0
        while self.flag_Sound == True:
            time.sleep(1)
            self.sound = self.soundTracker.got_sound
            print(self.sound)
            self.say_Hello(self.sound)


    def tracking_faces(self):
        targetName = "Face"
        faceWidth = 0.1
        self.tracker.registerTarget(targetName, faceWidth)
        # start tracker.
        self.tracker.track(targetName)


    def say_Hello(self, value):    


        if value == True:
            print("Say Hello to the patient")
            time.sleep(2)
            s = self.dialogs.get_welcome_sentence()
            s = s.replace('XX', self.patient['name'])
            self.animatedSpeechProxy.say(s)
            self.soundTracker.shutdown()
            self.flag_Sound = False
            
        elif (value == False):
            self.cont = self.cont + 1
            print(self.cont)
            if (self.cont == 1):
                self.tts.say(self.dialogs.noListeningSentence)
            if self.cont == 10:
                self.cont = 0 

    def load_selfPresentation(self):
        # Set the robot self presentation
        self.behavior_mng_service.runBehavior('robot_intro-f8648f/behavior_1')

    def load_patientPresentation(self):

        #Set the behavior to introduce patient presentation
        self.behavior_mng_service.runBehavior('intro_yourself-883ef7/behavior_1')


    def load_ElephantBehavior(self):
        #Set the behavior to make an elephant
        self.behavior_mng_service.runBehavior('elephant-7550d5/behavior_1')

    def load_MouseBehavior(self):
        #Set the behavior to make an elephant
        self.behavior_mng_service.runBehavior('mouse-286ea0/behavior_1')

    def load_gorillaBehavior(self):
        # set the behavior to make a gorilla
        self.behavior_mng_service.runBehavior('gorilla-b5bbf5/behavior_1')

    def load_butterflyBehavior(self):
        # ser the behavior to make a butterfly
        self.behavior_mng_service.runBehavior('butterfly-fe943b/behavior_1')

    def load_HeadExplanation(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('cabeza-882689/behavior_1')

    def load_ArmLExplanation(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('nao1_brazoiz-329b85/behavior_1')

    def load_ArmRExplanation(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('brazodr-ef940c/behavior_1')

    def load_LegLExplanation(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('piernaiz-2a44ea/behavior_1')

    def load_LegRExplanation(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('piernadr-9c8dca/behavior_1')

    def load_name(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('nombre-e64e27/behavior_1')

    def load_age(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('edad-37b6a6/behavior_1')

    def load_activity(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('actividad-0b56b7/behavior_1')

    def load_bye(self):
        # ser the behavior to make move the robot's head
        self.behavior_mng_service.runBehavior('adios-65b195/behavior_1')


    def load_Speech(self, speech):
        s = speech
        self.animatedSpeechProxy.say(s)

    def load_Right(self):
        
        behaviors = ['check_1-dc0fc5/behavior_1','check_2-2f6680/behavior_1','check_3-5a98d4/behavior_1']
        i = random.randint(0, len(behaviors) - 1)
        self.behavior_mng_service.runBehavior(behaviors[i])

    def load_Wrong(self):
        
        behaviors = ['no-0ef1d3/behavior_1','no_1-53de65/behavior_1','no_2-8f9f45/behavior_1']
        i = random.randint(0, len(behaviors) - 1)
        self.behavior_mng_service.runBehavior(behaviors[i])


    def start_session(self):
        print('Start_session')
        self.motion.wakeUp()
        #self.tts.say(self.welcomeSentence)
        #self.posture.goToPosture("StandZero", 1.0)
        self.animatedSpeechProxy.say(self.dialogs.TherapyWelcomeSentence)
        #print('Aqui')
        time.sleep(3)


    def setData(self, data):

        self.ecg = data['ecg']
        self.emg = data['ecg']

        if self.ecg['hr'] > 160:
            self.say(self.dialogs.hrIsUpSentence)

        if((self.emg['MuscleName'] == "RigthGluteus") and (self.emg['Contractions'] == 0)):

            print('No hay contracion del Gluteo derecho')

        if((self.emg['MuscleName'] == "LeftGluteus") and (self.emg['Contractions'] == 0)):

            print('No hay contracion del Gluteo izquierdo')




    def shutdown(self):
        self.animatedSpeechProxy.say(self.dialogs.ByeSentence)
        if self.motion.robotIsWakeUp():
            self.tracker.stopTracker()
            self.motion.rest()
            self.tracker.unregisterAllTargets()
        if (self.behavior_mng_service.isBehaviorRunning('robot_intro-f8648f/behavior_1')):
            self.behavior_mng_service.stopBehavior('robot_intro-f8648f/behavior_1')

        if (self.behavior_mng_service.isBehaviorRunning('intro_yourself-883ef7/behavior_1')):
            self.behavior_mng_service.stopBehavior('intro_yourself-883ef7/behavior_1')
            #self.sound_suscriber.unsubscribe("SoundDetected")



def Test():

    nao = RobotController()
    nao.tracking_faces()
    nao.start_Introduction()
    nao.launch_SoundTracker()
    nao.shutdown()


#if __name__ == '__main__':
    #nao = RobotController()





    