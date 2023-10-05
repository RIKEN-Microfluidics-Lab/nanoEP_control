# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:22:41 2021

@author: lab
"""

import serial, time


class dsp21func():
    def MotorON():
        dsp21 = serial.Serial('COM12', 9600, timeout=0.1)
        dsp21.write(b'4MN\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
    def TellPosi():
        dsp21 = serial.Serial('COM12', 9600, timeout=0.1)
        dsp21.write(b'4TP\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
    def MoveRel(NumRot):
        dsp21 = serial.Serial('COM12', 9600, timeout=0.1)
        masse = '4MR' + str(NumRot) +'\r\n'
        dsp21.write(masse.encode())
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
    def MoveAbs(Position):
        dsp21 = serial.Serial('COM12', 9600, timeout=0.1)
        masse = '4MA' + str(Position) +'\r\n'
        dsp21.write(masse.encode())
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()
    def GoHome():
        dsp21 = serial.Serial('COM12', 9600, timeout=0.1)
        dsp21.write(b'4GH\r\n')
        time.sleep(0.1)
        line = dsp21.read_all()
        print(line.decode())
        dsp21.close()



