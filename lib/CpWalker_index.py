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
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style


#object to aquire and analyze the EMG delsys data

class CpWalkerAquisition(object):

    def __init__(self):

        # Here goes the code to initializate the communication with the cpWalker
        # FOR EXAMPLE:
        '''
        sCPW = socket.socket()
        sCPW.connect(('localhost',9998))
        '''

        self.go_ON = False
        self.index = 0

        
    def process(self):

        ''' 
        If the cpWalker is connected then the code should see something like this:

        c = sCPW.recv(4)
        index = int.from_bytes( c, "big" )
        #print(index)
        return index
        '''

        # Here is the code to SIMULATE the data
        self.index = 0;

        while self.go_ON == True:
            #Cyclic patron generation
            self.index = self.index + 1
            if (self.index > 200):
                self.index = 0
            time.sleep(0.015)


    def cpWalker_Data(self):

        data = self.index
        return(data)

    def launch_CPthread(self):

        self.p = threading.Thread(target = self.process)
        self.p.start()

    def start(self):

        self.go_ON = True

    def stop(self):

        self.go_ON = False

#How to use the code in another object:
def main():
    cp = CpWalkerAquisition()
    cp.start()
    cp.launch_CPthread()
    time.sleep(0.1)
    for i in range(1000):
        m = cp.cpWalker_Data()
        print(m)
    cp.stop()
    

#A= main()








        