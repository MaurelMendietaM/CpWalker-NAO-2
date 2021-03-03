
# -*- coding: cp1252 -*-
import sys
import qi
from naoqi import ALModule
from naoqi import ALBroker
#import almath
import logging
import time
import random
import threading
import functools

class RobotController(object):

    def __init__(self,settings = { 'name'           : "NAO",
                                   'ip'             : '192.168.1.75',
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

        self.session = qi.Session()
        self.robotName = self.settings['name']
        self.HR_lim = self.settings['HeartRate_Lim']
        self.Cer_lim = self.settings['Cerv_Lim']
        self.Thor_lim = self.settings['Thor_Lim']

        self.go_on = True
        
        print('b')
        #myBroker = ALBroker("myBroker", "0.0.0.0", 0, self.ip, self.port)
        #self.module = RobotModule( name = 'module')

        self.session.connect("tcp://" + self.ip + ":" + str(self.port))

        #print('vv')

        self.tts = self.session.service("ALTextToSpeech")
        self.setLanguage('Spanish')
        self.animatedSpeechProxy = self.session.service("ALAnimatedSpeech")
        self.motion = self.session.service("ALMotion")
        self.posture = self.session.service("ALRobotPosture")
        '''
        self.motion = self.session.service("ALMotion")
        self.motion.wakeUp()
        self.motion.setBreathConfig([["Bpm", 6], ["Amplitude", 0.9]])
        self.motion.setBreathEnabled("Body", True)
        self.motion.setStiffnesses('Head', 1.0)
        '''
        #self.behavior_mng_service = self.session.service("ALBehaviorManager")
        #names = self.behavior_mng_service.getInstalledBehaviors()
        #print "Behaviors on the robot:"
        #print names

        #names = self.behavior_mng_service.getRunningBehaviors()
        #print "Running behaviors:"
        #print names


        self.configuration = {"bodyLanguageMode":"contextual"}

    def setLanguage(self, value):
        self.tts.setLanguage(value)

    def setVolume(self, value):
        self.tts.setVolume(value)

    def say(self, textToSay):
        self.tts.say(textToSay)


    def lookAtPatient(self): 
        names = ["HeadYaw", "HeadPitch"]
        #angleLists = [ 30.0*almath.TO_RAD, -30.0*almath.TO_RAD]
        #timeLists  = [1.0, 1.2]
        #isAbsolute = True
        #self.motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)


    def set_limits(self):
        self.hr = self.HR_lim

    def set_sentences(self):
        print('set_sentences')
        self.welcomeSentence = " ^startTag(animations/Stand, hello) Hola, \\pau=400\\ ^waitTag(animations/Stand, hello). ^startTag(me)  Mi nombre es Nao ^waitTag(me). ^startTag(affirmative_context) ^startTag(affirmative_context)  Te estare acompaniando en la sesion . Como te llamas?"
        self.sayGoodBye = "^startTag(bow) Alecsandra , Fue un placer acompaniarte durante la sesion  ^waitTag(bow).\\pau=400\\ ^startTag(hello) Nos vemos la proxima ocasion. ^waitTag(hello) "
        self.hrIsUpSentence = 'Parece que estas empezando a estar cansado,\\pau=300\\ todo esta bien?'
        self.headPostureCorrectionSentence = "Mejora la posicion de tu cabeza "
        self.torsePostureCorrectionSentence = 'Trata de enderezarte,\\pau=300\\ pon la espalda recta'
        self.askBorgScale = '^startTag(indicate) Que tan cansado te sientes? \\pau=200\\ responde segun la escala ^waitTag(indicate)'
        self.borgAlertSentence   =  "Al parecer estás muy cansado,\\pau=200\\ voy a llamar al doctor!."
        self.borgRecievedSentence   = "Gracias"
        self.torsehorizontalcorrectiondere="^startTag(indicate) Te estas inclinando hacia el lado derecho, \\pau=200\\ trata de enderezarte ^waitTag(indicate)"
        self.torsehorizontalcorrectionizq="^startTag(indicate) Te estas inclinando hacia el lado izkierdo, \\pau=200\\ trata de enderezarte ^waitTag(indicate)"
        self.headhorizontalcorrectiondere="^startTag(indicate) Tu cabeza esta inclinada hacia el lado derecho, \\pau=200\\ trata de enderezarla^waitTag(indicate)"
        self.headhorizontalcorrectionizq="^startTag(indicate) Tu cabeza esta inclinada hacia el lado izkierdo, \\pau=200\\ trata de enderezarla^waitTag(indicate)"
        self.motivationSentence = ["^startTag(happy)Puedes hacerlo! ^waitTag(happy)","^startTag(happy) Que bien lo haces!^waitTag(happy)","^startTag(enthusiastic)Te felicito!^waitTag(enthusiastic)","^startTag(enthusiastic)Sigue asi!^waitTag(enthusiastic)"]

    def connect_to_robot(self):

        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))

        except RuntimeError:
            logging.debug("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                          "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

    def set_routines(self):
        sayMotivation = functools.partial(self.get_motivation)
        self.sayMotivationTask = qi.PeriodicTask()
        self.sayMotivationTask.setCallback(sayMotivation)
        self.sayMotivationTask.setUsPeriod(self.settings['MotivationTime'])
        self.sayMotivationTask.start(True)

        getBorg = functools.partial(self.get_borg_scale)
        self.askBorgTask = qi.PeriodicTask()
        self.askBorgTask.setCallback(getBorg)
        self.askBorgTask.setUsPeriod(100000000)
        self.askBorgTask.start(True)

    def stop_routines(self):
        self.sayMotivationTask.stop()
        self.askBorgTask.stop()

    #binding functions to the interface

    def start_session(self):
        print('Start_session')
        self.motion.wakeUp()
        #self.tts.say(self.welcomeSentence)
        #self.posture.goToPosture("StandZero", 1.0)
        self.animatedSpeechProxy.say(self.welcomeSentence,self.configuration)
        #print('Aqui')
        time.sleep(10)
        
        

        #if d > 120:
            #self.tts.say(self.borgAlertSentence)
        #else:
            #self.tts.say(self.borgRecievedSentence)

    def ask_hr_high(self):
        self.tts.say(self.hrIsUpSentence)


    def get_motivation(self):

        i = random.randint(0, len(self.motivationSentence) - 1)
        
        self.animatedSpeechProxy.say(self.motivationSentence[i])

    def get_borg_scale(self):
        #self.tts.say(self.askBorgScale)
        self.animatedSpeechProxy.say(self.askBorgScale)


    def correct_torse_posture(self):
        #self.tts.say(self.torsePostureCorrectionSentence)
        self.animatedSpeechProxy.say(self.torsePostureCorrectionSentence)

    def correct_head_posture(self):
        #self.tts.say(self.headPostureCorrectionSentence)
        self.animatedSpeechProxy.say(self.headPostureCorrectionSentence)

    def correct_torsehorizontal_postureder(self):
        #self.tts.say(self.torsehorizontalcorrection)
        self.animatedSpeechProxy.say(self.torsehorizontalcorrectiondere)

    def correct_headhorizontal_postureder(self):
        #self.tts.say(self.torsehorizontalcorrection)
        self.animatedSpeechProxy.say(self.headhorizontalcorrectiondere)

    def correct_torsehorizontal_postureizq(self):
        #self.tts.say(self.torsehorizontalcorrection)
        self.animatedSpeechProxy.say(self.torsehorizontalcorrectionizq)

    def correct_headhorizontal_postureizq(self):
        #self.tts.say(self.torsehorizontalcorrection)
        self.animatedSpeechProxy.say(self.headhorizontalcorrectionizq)

    def set_data(self, data):
        self.ecg = data['ecg']
        self.angles1 = data['imu1']
        self.angles2 = data['imu2']
        

        print('Data from RobotController')
        print (self.angles2['pitch'])
        #print(self.hr)
        print(self.Thor_lim)

        if self.ecg['hr'] > 160:
            self.say(self.hrIsUpSentence)

        if ((float(self.angles2['yaw']) > 10)):
##        
            #self.animatedSpeechProxy.say(self.torsehorizontalcorrection)
           # print("correct torse")
            print(self.angles2['yaw'])
            print ("Hubo correccion en inclinacion HACIA UN LADO izquierdo")
            #print(self.Thor_lim)    
            self.correct_torsehorizontal_postureizq()
            time.sleep(0.1)
            #self.bad_posture_behavior()


        if (float(self.angles2['yaw'])< -10):
##        
            #self.animatedSpeechProxy.say(self.torsehorizontalcorrection)
           # print("correct torse")
            print(self.angles2['yaw'])
            print ("Hubo correccion en inclinacion HACIA UN LADO derecho")
            #print(self.Thor_lim)    
            self.correct_torsehorizontal_postureder()
            time.sleep(0.1)
            #self.bad_posture_behavior()

        if (float(self.angles2['pitch'])  > 10):
            
            #self.animatedSpeechProxy.say(self.torsePostureCorrectionSentence)
            #print("correct torse")
            print(self.angles2['pitch'])
            print ("Hubo correccion en inclinacion hacia delante")
            #pnt(self.Thor_lim)
            self.correct_torse_posture()
            time.sleep(0.1)
            #self.bad_posture_behavior()

        

        if (float(self.angles1['yaw']) > 10):
##        
            #self.animatedSpeechProxy.say(self.torsehorizontalcorrection)
           # print("correct torse")
            print(self.angles2['yaw'])
            print ("Hubo correccion en inclinacion CABEZA HACIA UN LADO derecho")
            #print(self.Thor_lim)    
            self.correct_headhorizontal_postureder()
            time.sleep(0.1)
            #self.bad_posture_behavior()
        
        if (float(self.angles1['yaw']) < -10):
##        
            #self.animatedSpeechProxy.say(self.torsehorizontalcorrection)
           # print("correct torse")
            print(self.angles2['yaw'])
            print ("Hubo correccion en inclinacion CABEZA HACIA UN LADO izqqq")
            #print(self.Thor_lim)    
            self.correct_headhorizontal_postureizq()
            time.sleep(0.1)
            #self.bad_posture_behavior()        
        if (float(self.angles1['pitch']) < -10):
        #
            #self.animatedSpeechProxy.say(self.headPostureCorrectionSentence)
            #print("correct cervical")
            print(self.angles1['pitch'])
            print ("Hubo correccion en CABEZA HACIA DELANTE")
            #print(self.Cer_lim)
            
            self.correct_head_posture()
            time.sleep(0.1)
            #self.bad_cervical_behavior()
        

    #BEHAVIOR
    #posture correction
    def bad_posture_behavior(self):
        threading.Thread(target = self.load_bad_posture_behavior).start()
        
    def bad_cervical_behavior(self):
        threading.Thread(target = self.load_bad_cervical_behavior).start()

    def load_bad_posture_behavior(self):
        self.behavior_mng_service.runBehavior('correct_posture-385681')
        #self.behavior_mng_service.runBehavior('correct_posture-385681/correct_posture')

    def load_bad_cervical_behavior(self):
        self.behavior_mng_service.runBehavior('behavior_1-938fab')
        #self.behavior_mng_service.runBehavior('behavior_1-938fab/behavior_1')

    def load_bad_horizontal_behavior(self):
        self.behavior_mng_service.runBehavior('horizontal-ac4f87/behavior_1')
        #self.behavior_mng_service.runBehavior('behavior_1-938fab/behavior_1')
    
    def shutdown(self):
        self.animatedSpeechProxy.say(self.sayGoodBye)
        if self.motion.robotIsWakeUp():
            self.motion.rest()
        if (self.behavior_mng_service.isBehaviorRunning('correct_posture-385681')):
            self.behavior_mng_service.stopBehavior('correct_posture-385681')
        if(self.behavior_mng_service.isBehaviorRunning('behavior_1-938fab')):
            self.behavior_mng_service.stopBehavior('behavior_1-938fab')
        if(self.behavior_mng_service.isBehaviorRunning('horizontal-ac4f87/behavior_1')):
            self.behavior_mng_service.stopBehavior('horizontal-ac4f87/behavior_1')


def main():


    nao = RobotController()
    
    
    nao.set_sentences()
    nao.set_limits()


    #t =threading.Thread(target = nao.correct_torse_posture)

    nao.start_session()

    #nao.correct_head_posture()
    #nao.set_routines()
    #t.start()
    time.sleep(25)
    #nao.load_bad_posture_behavior()
    #nao.correct_torse_posture()
    #nao.stop_routines()
    nao.shutdown()



    print('x')

M = main()
#    nao.connect_to_robot()

    #global module
#    module = nao.module

     
'''
    def process(nao):
        go_on = True
        while go_on:
            print('.....')
            a = random.random()
            cont = 10 * a
            data = {'ecg': 100*cont, 'imu': [cont, cont, cont] }
            print (data)
            nao.get_data(data)
            time.sleep(5)

    print('a')  
    threading.Thread(target  = process , args =(nao,)).start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        nao.go_on = False

'''
if __name__ == '__main__':
    main()

