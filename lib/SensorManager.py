
import EMG_sensor as Emg
#import src.Ecg as Ecg
import ecg_sensor as Ecg
import threading
import time
import random

class SensorManager(object):
    def __init__(self, ecg   = {"port":'COM4', "sample":1},
                       EMG   = {"MuscletoUse": None}
                ):
        #sensor control variable
        self.settings_emg = EMG

        self.settings_ecg = ecg
        print(self.settings_ecg)
        #control variables
        self.EMG =False
        self.ECG =False
        #data variable
        self.data = {
                     "ecg": 0,
                     "emg": {"MuscleName": 0.0, "Phase": 0.0, "Contractions":0.0},
                    }

    #activate sensors
        #self.emg = Emg.EMG_Sensor(self.settings_emg)


    def set_sensors(self, ecg =True, emg = True):
        self.EMG = emg
        self.ECG = ecg
        if self.EMG:
            self.emg = Emg.EMG_Sensor(self.settings_emg)

        if self.ECG:
            #self.ecg = Ecg.Ecg(settings = self.settings_ecg)
            self.ecg = Ecg.EcgSensor(port=self.settings_ecg['port'], sample = self.settings_ecg['sample'])


    def launch_Sensors(self):

        if self.EMG:
            self.emg.start()
            self.emg.launch_EMGsensor()
            #time.sleep(4)

        if self.ECG:
            self.ecg.start()
            self.ecg.play()

    #read sensor data and update data variable
    def update_data(self):
        print("Update data from SensorManager")
        if self.EMG:
            print('yes')
            emg_data = self.emg.getData()
        else:
            emg_data = None
        

        if self.ECG:
            #ecg_data = self.ecg.read_data()
            ecg_data = self.ecg.get_data()
            #print('Data ecg from Manager')
            #print(ecg_data)
            if not ecg_data:
                ecg_data = 0

            #ecg_data = float(ecg_data)
            if len(str(ecg_data))> 1:
                ecg_data = ecg_data[5]
                #ecg_data = float(ecg_data)
        else:
            ecg_data = 110 + random.randint(0,30)

        

        self.data['emg'] = emg_data
        self.data['ecg'] = ecg_data

        #self.data = str(self.data)
        

    def print_data(self):
        print("DATA FROM MANAGER: " + str(self.data)) 

    def get_Data(self):

        return(self.data)

    def shutdown(self):

        if self.EMG:
            self.emg.stop()
        if self.ECG:
            self.ecg.shutdown()



def main():
    sm = SensorManager(ecg   = {"port":'COM4', "sample":1}, EMG = {'MuscletoUse': "1"})
    sm.set_sensors(ecg = True, emg = True)
    sm.launch_Sensors()
    time.sleep(5)
    for i in range(10000):
        sm.update_data()
        sm.print_data()
        time.sleep(0.5)
    emg.stop()
#A = main()


   