import serial
import time

port = "/dev/ttyACM0"

motor = serial.Serial(port = port, timeout=0.5)
time.sleep(0.5)

motor.flush()
motor.flushInput()
print("start time [command]: ", time.time())
# motor.write("<speed,1>\n".encode("utf-8"))
motor.write("<speed,10>\n".encode("utf-8"))
print("start time [command]: ", time.time())
time.sleep(0.5)
motor.flush()
motor.flushInput()
# motor.write("<accel,1000>\n".encode("utf-8"))
motor.write("<accel,100>\n".encode("utf-8"))
time.sleep(0.5)

while 1:
    # print("starting loop"
    motor.flush()
    motor.flushInput()
    motor.write("<openmoveto,0>\n".encode("utf-8")) #list down the connected dynamixel.
    print("start time: ", time.time())
    while 1:
        line = motor.readline().decode('utf-8')
        # print("[print]: ", line)
        if "REACHED" in line:
            print("end time: ", time.time())
            break
        else:
            continue

    motor.flush()
    motor.flushInput()
    motor.write("<openmoveto,100>\n".encode("utf-8")) #list down the connected dynamixel.
    print("start time: ", time.time())
    while 1:
        line = motor.readline().decode('utf-8')
        # print("[print]: ", line)
        if "REACHED" in line:
            print("end time: ", time.time())
            break
        else:
            continue


# /////////////////////////////////////////////////////////////////////////////