# -*- coding: utf-8 -*-
import time
import random

class EMG_Variables(object):
    def __init__(self):
        self.initTime = time.time()

    def load_variables(self):
        #Creating the variables needed for the analysis
        self.answer = []
        self.emg0 = []
        self.calibrationSignal = []
        self.RightGluteus = [] #IMPORTANT INITIALIZE IT TO 0
        self.RightQuadriceps = []
        self.RightTriceps = []
        self.RightHamstrings = []
        self.LeftGluteus = []
        self.LeftQuadriceps = []
        self.LeftTriceps = []
        self.LeftHamstrings = []
        self.emg9 = []
        self.Index = []
        self.IndexLeft = []
        self.EMGlength = 2500
        self.CPWalkerIndex = 0 #from cpwalker
        self.j = 0 
        self.counterEMG1 = [0]
        self.counterEMG2 = [0]
        self.counterEMG3 = [0]
        self.counterEMG4 = [0]
        self.cyclestowait = 4
        self.phase = 0
        
if __name__ == '__main__':
    s = EMG_Variables()
    s.load_variables()