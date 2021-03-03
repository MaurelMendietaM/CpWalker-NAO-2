from __future__ import division
import binascii
import sys,getopt
import socket
import numpy as np
import time
import struct
import os
import threading
import scipy.signal as signal
import resources.variablesEMG as variablesEMG
import CpWalker_index as cp
import Queue
# Importing the statistics module 
import statistics

#object to aquire and analyze the EMG delsys data

class EMG_Sensor(object):

    def __init__(self, settings = {'MuscletoUse': None}):

        #load settings
        self.settings = settings
        self.MuscletoUse = self.settings['MuscletoUse']
        print(self.MuscletoUse)

        self.variablesEMG = variablesEMG.EMG_Variables()
        self.variablesEMG.load_variables()
        self.phase_Gait = 0
        self.cp = cp.CpWalkerAquisition()

        #Create the sockets to initiate the communication with EMG delsys system
        #creates general connection with EMG Delsys
        self.s1 = socket.socket()
        self.s1.connect(('localhost', 50040))
        #Opening the specific port to get EMG signal 
        self.s = socket.socket()
        self.s.connect(('localhost',50041))
        #Command to start, always ends with \r\n\r\n

        self.start_command="START\r\n\r\n"
        self.s1.sendall(self.start_command)


        self.go_ON = False
        self.feedback_Data =  {'MuscleName': None, 'Phase': None, 'contractions': None }

        


    def process(self):
        #print('hereeeeeeeeeeeeeee')

        counter = 0
        iR = 0
        iL = 0
        p = 0
        k = 1
        im=0
        init=0
        init_phase=0
        init1=0

        #self.s1.send(bytes(self.start_command))
        #print("start")
        while self.go_ON == True:

        #for i in range(1000000):
            #Receiving info in packages of 4 BYTES so each package is an emg
            self.variablesEMG.answer = self.s.recv(4)
            a = struct.unpack('f', self.variablesEMG.answer)
            self.variablesEMG.emg0.append(a)
            p += 1
            #print(self.variablesEMG.emg0)
            if(p > 1) :

                #print(self.variablesEMG.emg0)
                
                if(len(self.variablesEMG.emg0) % 16 == 1) :

                    k = self.getIndexCpWalker()
                    #print('getIndexCpWalker')
                    kleft = k + 100

                    self.variablesEMG.Index.append(self.decidePhase(k))
                    self.variablesEMG.IndexLeft.append(self.decidePhase(kleft))
                    #print(self.variablesEMG.Index)

                    '''    
                    print('Index cpWalker_Data')
                    print(self.variablesEMG.IndexLeft)
                    print(kleft)
                    '''
                    self.phase_Gait = self.decidePhase(k)

                    

                    self.variablesEMG.RightGluteus.append(self.variablesEMG.emg0[counter][0])
                    self.variablesEMG.RightQuadriceps.append(self.variablesEMG.emg0[counter+1][0])
                    self.variablesEMG.RightTriceps.append(self.variablesEMG.emg0[counter+2][0])
                    self.variablesEMG.RightHamstrings.append(self.variablesEMG.emg0[counter+3][0])
                
                    self.variablesEMG.LeftGluteus.append(self.variablesEMG.emg0[counter+4][0])
                    self.variablesEMG.LeftQuadriceps.append(self.variablesEMG.emg0[counter+5][0])
                    self.variablesEMG.LeftTriceps.append(self.variablesEMG.emg0[counter+6][0])
                    self.variablesEMG.LeftHamstrings.append(self.variablesEMG.emg0[counter+7][0])
                    k += 1
                    #print(self.variablesEMG.LeftQuadriceps)
                    #print('------------------')
                    

                    if k == 200:


                        p_0 = len(self.variablesEMG.RightGluteus)
                       # print('---------------------------')
                        
                        #print(p_0)
                        #print(len(self.variablesEMG.RightQuadriceps))
                        #print('---------------------------')
                        if (self.MuscletoUse == "1"):
                            self.Muscle(self.variablesEMG.RightGluteus[init:p_0],"RightGluteus",self.variablesEMG.Index[init:p_0])
                        if (self.MuscletoUse == "2"):
                            self.Muscle(self.variablesEMG.RightQuadriceps[init:p_0],"RightQuadriceps",self.variablesEMG.Index[init:p_0])
                        #self.Muscle(self.variablesEMG.RightTriceps[init:p_0],"RightTriceps",self.variablesEMG.Index[init:p_0])
                        #self.Muscle(RightHamstrings[iR:p],"RightHamstrings",Index[iR:p])
                        init = p_0
                        iR = p
                    
                    if kleft == 200:
                        #print('here')
                        p_1 = len(self.variablesEMG.LeftGluteus)
                        #print(p_1)
                        #print(len(self.variablesEMG.LeftQuadriceps))

                        if (self.MuscletoUse == "1"):
                            self.Muscle(self.variablesEMG.LeftGluteus[init1:p_1],"LeftGluteus",self.variablesEMG.IndexLeft[init1:p_1])
                        if (self.MuscletoUse == "2"):
                            self.Muscle(self.variablesEMG.LeftQuadriceps[init1:p_1],"LeftQuadriceps", self.variablesEMG.IndexLeft[init1:p_1])
                        #self.Muscle(LeftTriceps[iL:p],"LeftTriceps",IndexLeft[iL:p])
                        #self.Muscle(LeftHamstrings[iL:p],"LeftHamstrings",IndexLeft[iL:p])

                        init1 =p_1

                    counter += 16

                #if len(self.variablesEMG.emg0) == 5000000:
                   # print("ya")
                    #break
  


    
        #print(self.variablesEMG.RightGluteus)


    def getIndexCpWalker(self):

        m =self.cp.cpWalker_Data()

        return(m)

    def start(self):

        self.cp.start()
        self.go_ON = True

    def stop(self):
        self.cp.stop()
        self.go_ON = False

    def decidePhase(self,index):

        phase = -1
        if 0<=index<40:
            phase = 1
        if 40<=index<90:
            phase = 2
        if 90<=index<140:
            phase = 3
        if 140<=index<=200:
            phase = 4
        
        return phase


    def launch_EMGsensor(self):


        self.cp.launch_CPthread()
        self.p = threading.Thread(target = self.process)
        self.p.start()
        time.sleep(0.1)



    def Muscle(self,emg,MuscleName, CpWalkerIndex):
        #print('Muscle')
        #print(len(CpWalkerIndex))
        window = signal.get_window('hann',80)
        RMSemg, time = self.rollapply(emg,window, by=1, fs=1.)

        #print(len(RMSemg))
        fs = 2000 
        fc = 10/(fs/2)
        b = signal.firwin(100,fc)
        self.emg_filtered = signal.lfilter(b,1,RMSemg)
        #print(self.emg_filtered)
        contraction = self.apply_threshold(self.emg_filtered*10000)
        #print(contraction)
        self.ApplyCpWalkerIndex(CpWalkerIndex,MuscleName,contraction)




    def rollapply(self,x, window, by=1, fs=1.):


    #    """
    #    Applies a function to a signal in a moving window.
    #    :param x: The input signal.
    #    :param fun: The function to be applied in each of the windows. It should take an input signal as argument.
    #    :param window: A window function as returned by scipy.signal.get_window
    #    :param by: calculate 'fun' at every 'by'-th time point
    #    :param fs: sampling frequency of 'x'
    #    :return: a tuple consisting of time, result
    #    """
        result = []
        time = []
        for j in range(0, len(x)-len(window)-1,by):
            a = x[j:(j+len(window))]*window
            b = self.RMS(a)
            result.append(b)
            
            c = (j+j+len(window))/2
            time.append(c)
            
        return (result,time)



        

    def RMS(self,x):

        M = len(x)
        suma = np.sum(x*x)
        return np.sqrt(suma/M)

    def threshold_from_data(self,emg):
  
        mean = 0
        for k in range(0 ,len(emg)-1):
            mean+=emg[k]
        th = (mean/len(emg)) *1.5
        return th

    def apply_threshold(self,emg):

        th = self.threshold_from_data(emg)
        contraction = []
        for k in range(0,len(emg)-1):
            if (((emg[k]>th) and (emg[k+1]<th)) or (((emg[k]<th) and (emg[k+1]>th)))):
                contraction.append(1) 
                #print("CONTRACTION")
                self.contraction = 1
            else : 
                contraction.append(0) 
                self.contraction = 0
         
        return contraction


    def countContractions(self,contractionlist):
        contadorContraction = 0
        for i in range (0,len(contractionlist)-1):
            if(contractionlist[i] != 0):
                contadorContraction+= 1
        contadorContraction = contadorContraction/2
        #print(contadorContraction)
        return contadorContraction

    def ApplyCpWalkerIndex(self, phase, MuscleName, contractionList):
        print('ApplyCpWalkerIndex Enter')

        changeOfPhase, numberofChanges = self.knowPhaseChange(phase)
        #print("number of changes :")
        #print(numberofChanges)
        #print("changeOfPhase")
        #print(changeOfPhase)
        #if len(changeOfPhase)>3:
           #print(phase[changeOfPhase[2]:changeOfPhase[3]])
        number_phase = 0
        contraction_phase = 0
      
        
        #if (len(changeOfPhase)>2):
        #print(phase[changeOfPhase[2]:len(phase)-1])

        if(len(changeOfPhase)>2):

            #PHASE 1
            mean1 = statistics.mean(phase[0:changeOfPhase[0]-1])
            mean2 = statistics.mean(phase[changeOfPhase[0]:changeOfPhase[1]-1])
            mean3 = statistics.mean(phase[changeOfPhase[1]:changeOfPhase[2]-1])
            mean4 = statistics.mean(phase[changeOfPhase[2]:len(phase)-1])

            '''
            print('mean1'+str(mean1))
            print('mean2'+str(mean2))
            print('mean3'+str(mean3))
            print('mean4'+str(mean4))

            '''


        

        if(MuscleName == 'RightGluteus' or MuscleName == 'LeftGluteus' or MuscleName == 'RightHamstrings'  or MuscleName == 'LeftHamstrings'):
            #print('AQUIIII')
            contraction_phase = self.countContractions(contractionList[0:changeOfPhase[0]-1])
            number_phase = "1"

        #PHASE 2
        elif(MuscleName == 'RightQuadriceps' or MuscleName == 'LeftQuadriceps'):
            if(len(changeOfPhase) == 2):
                #print('Aqui')
                contraction_phase = self.countContractions(contractionList[changeOfPhase[0]:changeOfPhase[1]-1])
                number_phase = "2"
            if(len(changeOfPhase) == 3) :
                contraction_phase = self.countContractions(contractionList[changeOfPhase[2]:len(phase)-1])
                number_phase = "4"

        #PHASE 3 and PHASE 4
        elif(MuscleName == 'RightTriceps' or MuscleName == 'LeftTriceps'):
            if(len(changeOfPhase) >2) :
                contraction_phase = self.countContractions(contractionList[changeOfPhase[1]:changeOfPhase[2]-1])
                number_phase = "3"
            
        else:
            contraction_phase = None
            number_phase = None



        self.feedback_Data =  {'MuscleName':MuscleName, 'Phase': number_phase, 'contractions': contraction_phase }
        #print(self.feedback_Data)  


    def knowPhaseChange(self,phases):
        p = 0
        change = []
        for i in range( 0, len(phases)-2):
            if phases[i] != phases[i+1]:
                change.append(i+1)
                #print(i)
                p+=1
        if p == 0: 
            change.append(-1)
            p = -1

        return change,p

   
    def getData(self):
        
        value = self.feedback_Data

        return(value)




# This is the example tu run the code in an external object the EMG Sensor
# Data
    
def main():
    emg = EMG_Sensor(settings = {'MuscletoUse': "1"})
    emg.start()
    emg.launch_EMGsensor()
    time.sleep(4)
    for i in range(1000):
        m = emg.getData()
        print(m)
        time.sleep(0.5)
    emg.stop()
#A= main()



        

    


            




        




#if __name__ == '__main__':
    #main()
