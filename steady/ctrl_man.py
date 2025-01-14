#Daniel Asadi
#Eng Sci 2T3
#FCET Lab, UTIAS

import serial
import time

def controlValve(ser, status1):
    if status1 == 0:
        ser.write(b'A') #high
        status1 = 1
        print('VALVE OPEN')
    else:
        ser.write(b'B') #low
        status1 = 0
        print('VALVE CLOSED')
    return status1

def controlCam(ser):
    ser.write(b'C') #high
    time.sleep(0.2)
    ser.write(b'D') #low
    print('CAM RECORD')
    time.sleep(0.1)
    ser.write(b'C') #high
    time.sleep(0.2)
    ser.write(b'D') #low
    print('CAM READY')

def controlWire(ser, status3):
    if status3 == 0:
        ser.write(b'E') #high
        status3 = 1
        print('WIRE ON')
    else:
        ser.write(b'F') #low
        status3 = 0
        print('WIRE OFF')
    return status3

def controlCap(ser, status4):
    if status4 == 0:
        ser.write(b'G') #high
        status4 = 1
        print('CAP DISCHARGED')
    else:
        ser.write(b'H') #low
        status4 = 0
        print('CAP CHARGING')
    return status4

def readEnc(loops):
    for i in range(loops):
        line = ser.readline() #read a byte
        if line:
            try:
                string = line.decode() #convert the byte string to a unicode string
                pos = int(string) #convert the unicode string to an int
                print(pos)
            except ValueError:
                print('ERROR')
    ser.close()

def emergencyStop(ser):
    ser.write(b'B') #low
    print('VALVE CLOSED')
    ser.write(b'D') #low
    print('CAM OFF')
    ser.write(b'F') #low
    print('WIRE OFF')
    ser.write(b'H') #low
    print('CAP CHARGING')
    ser.close()
    quit()

if __name__ == "__main__":
    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM7', 115200, timeout=1)
    #ser.close() #temporary
    time.sleep(2)
    status1 = 0
    status2 = 0
    status3 = 0
    status4 = 0
    setting = 5

    print('Valve control (LEDY): TOGGLE [1]')
    print('Camera control (LEDR): TOGGLE [2]')
    print('Wire control (LEDG): TOGGLE [3]')
    print('Capacitor control (LEDB): TOGGLE [4]')
    print('Exit: [0]')

    while True:
        try:
            setting = int(input())
        except ValueError:
                print('ERROR')
                continue
        if setting == 1:
            status1 = controlValve(ser, status1)
        elif setting == 2:
            controlCam(ser)
        elif setting == 3:
            status3 = controlWire(ser, status3)
        elif setting == 4:
            status4 = controlCap(ser, status4)
        elif setting == 0:
            emergencyStop(ser)
        else:
            print('ERROR')