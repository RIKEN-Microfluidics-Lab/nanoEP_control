# -*- coding: utf-8 -*-
# C:\Users\hirof\Anaconda3\Library\bin\pyuic5 -o gui_ui.pygui_main1.ui
import sys
import os

import numpy as np
from NIDAQ_plt3 import AI as NI
from PyQt5 import QtWidgets, QtCore
from ui_v2 import Ui_MainWindow
from matplotlibwidget import MatplotlibWidget
import pyvisa as visa

class wavefunc():
    def wf1974(voltage, pulse,period,num_cycl):
#        import visa
#        float exposure
#        float width1; float width2
        rm = visa.ResourceManager()
        # wv = rm.get_instrument("USB0::0x0D4A::0x000E::9137840::INSTR")
        wv = rm.open_resource("USB0::0x0D4A::0x000E::9334150::INSTR")
        #print(wv.query('*IDN?'))
        wv.write(':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude '+ str(voltage) +'; OFFSet '+ str(voltage/2))
        # wv.write(':SOURce2:VOLTage:LEVel:IMMediate:AMPLitude 5.0; OFFSet 2.5')
        wv.write(':SOURce1:BURSt:TRIGger:NCYCles '+ str(num_cycl))#number of cycles output onw
        # wv.write(':SOURce2:BURSt:TRIGger:NCYCles '+ numofpulse)#number of cycles output two
        wv.write(':SOURce1:FUNCtion:SHAPe PULSe')
        # wv.write(':SOURce2:FUNCtion:SHAPe PULSe')
        wv.write(':TRIGger1:BURSt:SOURce EXT')
        # wv.write(':TRIGger2:BURSt:SOURce EXT')
        
        wv.write(':SOURce1:PULSe:PERiod '+str(period)+'ms')#control the pulse period of output1
        # wv.write(':SOURce2:PULSe:PERiod '+str(dt)+'ms')#control the pulse period of output2
        wv.write(':SOURce1:PULSe:WIDTh '+str(pulse)+'ms')#control the pulse width of output one
        # wv.write(':SOURce2:PULSe:WIDTh '+str(width2)+'ms')#control the pulse width of output two
        wv.write(':SOURce1:BURSt:TGATe:OSTop CYCLe')
        # wv.write(':SOURce2:BURSt:TGATe:OSTop CYCLe')
        wv.write(':SOURce1:BURSt:SLEVel:STATe ON')
        wv.write(':SOURce1:BURSt:SLEVel -100PCT')
        # wv.write(':SOURce2:PHAse:ADJust -180DEG')
        wv.write(':SOURce1:BURSt:TDELay 400ms')
        # wv.write(':SOURce2:BURSt:TDELay '+str(delay)+'ms')
        wv.write('OUTPut1:STATe ON')
        # wv.write('OUTPut2:STATe ON')
        
class MainWindow(QtWidgets.QMainWindow):    
    def __init__(self, parent=None):
        global ui
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.graphwidget= MatplotlibWidget(ui.centralwidget,title='', xlabel='Time', ylabel='',
                 xscale='linear', yscale='linear',
                 width=13, height=3, dpi=100)
        #ui.graphwidget= MatplotlibWidget(ui.centralwidget,height=3)

        #ui.graphwidget.axes1 = ui.graphwidget.figure.add_subplot(121)  
        #ui.graphwidget.axes = ui.graphwidget.figure.add_subplot(121)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(100)
        ui.x=[]
        ui.y=[]
        ui.c=[]
        ui.save=False
        ui.Filename="./test.txt"
        ui.value=0
        ui.monitor = True
        
        # Wave generator
        voltage=5   # [V]
        pulse=5     # [ms]
        frequency=20    # [Hz]
        period=1000/frequency       # [ms]
        num_cycl=100
        ui.WG_Vol_Edit.setPlainText(str(voltage))
        ui.WG_Pul_Edit.setPlainText(str(pulse))
        ui.WG_Frq_Edit.setPlainText(str(frequency))
        ui.WG_Cyc_Edit.setPlainText(str(num_cycl))
        wavefunc.wf1974(voltage, pulse, period,num_cycl)
        
        # DAQ (monitor)
        ui.DAQ_NumCh_Edit.setPlainText('2')     # Number of channel
        ui.DAQ_Rate_Edit.setPlainText('1000')   # Sampling rate, [ms]
        ui.DAQ_NumSmpl_Edit.setPlainText('1000')    # Number of sample
        ui.ch_num=int(ui.DAQ_NumCh_Edit.toPlainText())
        ui.rate=int(ui.DAQ_Rate_Edit.toPlainText())
        ui.smpl=int(ui.DAQ_NumSmpl_Edit.toPlainText())
        
        
        
    def update_figure(self):
        import time
        smpltime=time.time()
        data=NI.NIDAQ_Stream(ui.ch_num,ui.smpl,ui.rate)    
        
        if ui.monitor == True:
            ui.graphwidget.axes.clear()
            ui.graphwidget.x  = np.arange(0,ui.smpl,1)
            # plot ch0,1,2
            for counter2 in range(0,ui.ch_num-1):
                ui.graphwidget.y  = data[counter2]
                ui.graphwidget.axes.plot(ui.graphwidget.x,ui.graphwidget.y)
            ui.graphwidget.draw()
        
        if ui.save == True:  
            if ui.count != 0:
                smpltime=smpltime-ui.stime
                duration=float(ui.smpl)/float(ui.rate) #second
                stamp=np.linspace(smpltime,smpltime+duration,ui.smpl)
                data=np.vstack([stamp,data])
                with open(ui.Filename,'a') as f_handle:
                    np.savetxt(f_handle,data.T,delimiter=',')
            else:
                ui.stime=smpltime
                smpltime=smpltime-ui.stime
                duration=float(ui.smpl)/float(ui.rate) #second
                stamp=np.linspace(smpltime,smpltime+duration,ui.smpl)
                data=np.vstack([stamp,data])
                np.savetxt(ui.Filename,data.T,delimiter=',')
            ui.count = ui.count + 1
        else:
            ui.count = 0


        
    def slot1(self):
        ui.save = not ui.save
        if ui.save == True:
            ui.Filename = NI.DefFile(filepath, filename_user)
            filename_user = ui.plainTextEdit_9.toPlainText()
    
    def slot2(self):# valve on off
#        NI.NIDAQ_Stream()
        ui.valve = not ui.valve
        NI.ArduinoDO(ui.valve)
        #I.ArduinoAO(ui.valve, ui.value)
#    def slot3(self):
#        NI.NIDAQ_DO()       

    def slot4(self):
        voltage=float(ui.plainTextEdit_1.toPlainText())
        pulse=float(ui.plainTextEdit_2.toPlainText())
        frequency=float(ui.plainTextEdit_3.toPlainText())
        num_cycl=float(ui.plainTextEdit.toPlainText())#interval
        period=1000/frequency
        wavefunc.wf1974(voltage,pulse,period,num_cycl)

        
    def slot5(self):
        rm = visa.ResourceManager()
        wv = rm.open_resource("USB0::0x0D4A::0x000D::9148960::INSTR")
        wv.write("*TRG")
        
        # NI.ArduinoDP(4,interval,1,number)
        
    def slot6(self):
        print("slot6 is pushed")
        ui.ch_num=int(ui.plainTextEdit_4.toPlainText())
        ui.rate=int(ui.plainTextEdit_5.toPlainText())
        ui.smpl=int(ui.plainTextEdit_6.toPlainText())
        
    def slot7(self):
        print("slot7 is pushed")
        ui.monitor = not ui.monitor
        
    def slot8(self):
        print("slot8 is pushed")
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directry", 'C:/Users/Lab/Documents/python/git_electroporation')
        ui.plainTextEdit_8.setPlainText(filepath)
        print(filepath)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
    
    