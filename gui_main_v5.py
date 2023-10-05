# -*- coding: utf-8 -*-
# C:\Users\hirof\Anaconda3\Library\bin\pyuic5 -o gui_ui.pygui_main1.ui
import sys
import os

import numpy as np
from NIDAQ_plt3 import AI as NI
from PyQt5 import QtWidgets, QtCore
from ui_v5 import Ui_MainWindow
from matplotlibwidget import MatplotlibWidget
import pyvisa as visa
import serial, time

class wavefunc():
    def wf1974(voltage, pulse_1, period_b, period_t, num_cycl, offset):
        rm = visa.ResourceManager()
        # wv = rm.get_instrument("USB0::0x0D4A::0x000E::9137840::INSTR")
        wv = rm.open_resource("USB0::0x0D4A::0x000E::9334150::INSTR")
        
        # Set parameters to Ch1
        wv.write(':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude '+ str(voltage) +'; OFFSet '+ str(offset))
        wv.write(':SOURce1:BURSt:TRIGger:NCYCles '+ str(1))
        wv.write(':SOURce1:FUNCtion:SHAPe PULSe')
        wv.write(':TRIGger1:BURSt:SOURce EXT')
        wv.write(':SOURce1:PULSe:PERiod '+str(period_b)+'ms')
        wv.write(':SOURce1:PULSe:WIDTh '+str(pulse_1)+'ms')
        wv.write(':SOURce1:BURSt:TGATe:OSTop CYCLe')
        wv.write(':SOURce1:BURSt:SLEVel:STATe ON')
        # Calculate stop level
        stoplev = -200*(offset/voltage)
        print("Stop Level: {:.4f}".format(stoplev))
        wv.write(':SOURce1:BURSt:SLEVel {:.4f}PCT'.format(stoplev))
        # wv.write(':SOURce2:PHAse:ADJust -180DEG')
        wv.write(':SOURce1:BURSt:TDELay 0ms')
        # wv.write(':SOURce2:BURSt:TDELay '+str(delay)+'ms')
        wv.write('OUTPut1:STATe ON')
        
        # Set parameters to Ch2
        wv.write(':SOURce2:VOLTage:LEVel:IMMediate:AMPLitude '+ str(5) +'; OFFSet '+ str(2.5))
        wv.write(':SOURce2:BURSt:TRIGger:NCYCles '+ str(num_cycl))#number of cycles output one
        wv.write(':SOURce2:FUNCtion:SHAPe PULSe')
        wv.write(':TRIGger2:BURSt:SOURce EXT')
        wv.write(':SOURce2:PULSe:PERiod '+str(period_t)+'ms')
        wv.write(':SOURce2:PULSe:WIDTh 1ms')
        wv.write(':SOURce2:BURSt:TGATe:OSTop CYCLe')
        wv.write(':SOURce2:BURSt:SLEVel:STATe ON')
        wv.write(':SOURce2:BURSt:SLEVel -100PCT')
        wv.write(':SOURce2:BURSt:TDELay 400ms')
        wv.write('OUTPut2:STATe ON')
        
        wv.close()
        ui.Bottom_message.setPlainText('Vp-p = {:.2f}, offset = {:+.2f}, x20: [{:.1f}, {:.1f}]'.format(voltage, offset, 20*(offset-0.5*voltage), 20*(offset+0.5*voltage)))
        
class dsp21func():
    def MotorON():
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        dsp21.write(b'4MN\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
        
    def TellPosi():
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        dsp21.write(b'4TP\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
        
    def MoveRel(NumRot):
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        messe = '4MR' + str(NumRot) +'\r\n'
        dsp21.write(messe.encode())
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
        
    def MoveAbs(Position):
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        messe = '4MA' + str(Position) +'\r\n'
        dsp21.write(messe.encode())
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
        
    def GoHome():
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        dsp21.write(b'4GH\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
    
    def DefHome():
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        dsp21.write(b'4DH\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
    
    def SentCommand(dsp_command):
        dsp21 = serial.Serial('COM4', 9600, timeout=0.1)
        dsp_cmd_sent = str(dsp_command) + '\r\n'
        print(dsp_cmd_sent)
        dsp21.write(dsp_cmd_sent.encode())
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
        return line.decode()
        
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
        ui.timer = QtCore.QTimer(self)
        ui.timer.timeout.connect(self.update_figure)
        ui.timer.start(100)
        ui.x=[]
        ui.y=[]
        ui.c=[]
        ui.save=False
        ui.monitor = True
        
        # Wave generator
        voltage_low = 1.75   # [V]
        voltage_high = -0.75  # [V]
        pulse_1=2.5     # [ms]
        pulse_2=50     # [ms]
        pulse_3=50
        period_b=pulse_1 + pulse_2       # [ms]
        period_t=pulse_1 + pulse_2 + pulse_3 # [ms]
        num_cycl=200
        offset = (voltage_high+voltage_low)/2
        voltage_pp = abs(voltage_high-voltage_low)
        ui.WG_Vol1_Edit.setPlainText(str(voltage_low))
        ui.WG_Vol2_Edit.setPlainText(str(voltage_high))
        ui.WG_t1_Edit.setPlainText(str(pulse_1))
        ui.WG_t2_Edit.setPlainText(str(pulse_2))
        ui.WG_t3_Edit.setPlainText(str(pulse_3))
        ui.WG_Cyc_Edit.setPlainText(str(num_cycl))
        wavefunc.wf1974(voltage_pp, pulse_1, period_b, period_t, num_cycl, offset)
        
        # DAQ (monitor)
        ui.DAQ_NumCh_Edit.setPlainText('2')     # Number of channel
        ui.DAQ_Rate_Edit.setPlainText('1000')   # Sampling rate, [ms]
        ui.DAQ_NumSmpl_Edit.setPlainText('1000')    # Number of sample
        ui.ch_num=int(ui.DAQ_NumCh_Edit.toPlainText())
        ui.rate=int(ui.DAQ_Rate_Edit.toPlainText())
        ui.smpl=int(ui.DAQ_NumSmpl_Edit.toPlainText())
        
        # Motor
        ui.MA_Edit.setPlainText('0')    # Move absolute
        ui.MR_Edit.setPlainText('0')    # Move relative
        ui.mv_abs = int(ui.MA_Edit.toPlainText())
        ui.mv_rel = int(ui.MR_Edit.toPlainText())
        
        # Recode
        ui.Filepath_Edit.setPlainText('./data')
        ui.Filename_Edit.setPlainText('data')
        

    def update_figure(self):
        import time
        smpltime=time.time()
        data=NI.NIDAQ_Stream(ui.ch_num,ui.smpl,ui.rate)    
        
        if ui.monitor == True:
            ui.graphwidget.axes.clear()
            ui.graphwidget.x  = np.arange(0,ui.smpl,1)
            for counter2 in range(0,ui.ch_num):
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
            if ui.monitor == False:
                self.slot7()
            filepath = ui.Filepath_Edit.toPlainText()
            filename_user = ui.Filename_Edit.toPlainText()
            ui.Filename = NI.DefFile(filepath, filename_user)
            print(ui.Filename)
            ui.label_16.setText("ON")
            ui.label_16.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"    color: #ff0000;\n"
"}")
        else:
            ui.label_16.setText("OFF")
            ui.label_16.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"    color: blue;\n"
"}")
            

    def slot4(self):    # Set parameter to wf1974
        voltage_1=float(ui.WG_Vol1_Edit.toPlainText())
        voltage_2=float(ui.WG_Vol2_Edit.toPlainText())
        pulse_1=float(ui.WG_t1_Edit.toPlainText())
        pulse_2=float(ui.WG_t2_Edit.toPlainText())
        pulse_3=float(ui.WG_t3_Edit.toPlainText())
        num_cycl=float(ui.WG_Cyc_Edit.toPlainText())
        
        period_b=pulse_1 + pulse_2       # [ms]
        period_t=pulse_1 + pulse_2 + pulse_3 # [ms]
        offset = (voltage_1+voltage_2)/2
        voltage_pp = abs(voltage_2-voltage_1)
        wavefunc.wf1974(voltage_pp, pulse_1, period_b, period_t, num_cycl, offset)
        
    def slot5(self):    # Sent trigger to wf1974
        rm = visa.ResourceManager()
        wv = rm.open_resource("USB0::0x0D4A::0x000E::9334150::INSTR")
        wv.write(":TRIGger2:SEQuence:IMMediate")
        # wv.write("*TRG")
        wv.close()
        
        print("Triggered")
        
    def slot6(self):    # Set parameters to DAQ
        ui.ch_num=int(ui.DAQ_NumCh_Edit.toPlainText())
        ui.rate=int(ui.DAQ_Rate_Edit.toPlainText())
        ui.smpl=int(ui.DAQ_NumSmpl_Edit.toPlainText())
        print("Parameters of monitor are updated")
        
    def slot7(self):    # Monitor ON/OFF
        ui.monitor = not ui.monitor
        if ui.monitor == False:
            ui.timer.stop()
            print("Monitor OFF")
            ui.label_14.setText("OFF")
            ui.label_14.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"    color: blue;\n"
"}")
        else:
            ui.timer.start(100)
            print("Monitor ON")
            ui.label_14.setText("ON")
            ui.label_14.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"    color: #ff0000;\n"
"}")
            
    def slot8(self):    # Set filename
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directry", './')
        ui.Filepath_Edit.setPlainText(filepath)
        print(filepath)
        
    def slot9(self):    # Move absolute
        ui.mv_abs = int(ui.MA_Edit.toPlainText())
        line = dsp21func.MoveAbs(ui.mv_abs)
        ui.Motor_message.setPlainText(line)
        
    def slot10(self):   # Move relative
        ui.mv_rel = int(ui.MR_Edit.toPlainText())
        line = dsp21func.MoveRel(ui.mv_rel)
        ui.Motor_message.setPlainText(line)
        
    def slot11(self):   # Define home
        line = dsp21func.DefHome()
        ui.Motor_message.setPlainText(line)
        
    def slot12(self):   # Go home
        line = dsp21func.GoHome()
        ui.Motor_message.setPlainText(line)
        
    def slot13(self):   # Motor ON
        line = dsp21func.MotorON()
        ui.Motor_message.setPlainText(line)
        
    def slot14(self):   # Tell position
        line = dsp21func.TellPosi()
        ui.Motor_message.setPlainText(line)
        
    def slot15(self):   # Sent command
        ui.dsp21Command=ui.SentCommand_Edit.toPlainText()
        line = dsp21func.SentCommand(ui.dsp21Command)
        ui.Motor_message.setPlainText(line)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    
    