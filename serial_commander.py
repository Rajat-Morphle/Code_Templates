import serial
import time

port = "/dev/ttyACM0"

motor = serial.Serial(port = port, timeout=0.5)
time.sleep(1)

# while True:
motor.flush()
motor.flushInput()
motor.write("g28y\n".encode("utf-8"))
print("CAM HOME")
time.sleep(3)

motor.flush()
motor.flushInput()
motor.write("g0y80\n".encode("utf-8"))
print("CAM READY")
time.sleep(2)

motor.flush()
motor.flushInput()
motor.write("g28z\n".encode("utf-8"))
print("DIPPER HOME")
time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("g0z0\n".encode("utf-8"))
print("DIPPER READY")
time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("g28x\n".encode("utf-8"))
print("HANGER HOME")
time.sleep(4)

motor.flush()
motor.flushInput()
motor.write("g0x349f6000\n".encode("utf-8"))
print("hANGER READY")
time.sleep(5)

motor.flush()
motor.flushInput()
motor.write("g0z14\n".encode("utf-8"))
print("ROLLER DOWM")
time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("g0z18\n".encode("utf-8"))
print("DIPPER DOWN")
time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("g0y160z14\n".encode("utf-8"))
print("TEARDOWN")
time.sleep(2)

motor.flush()
motor.flushInput()
motor.write("g0z0\n".encode("utf-8"))
print("ROLLER LIFT")
time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("g0y80\n".encode("utf-8"))
print("CAM RETRACT")
time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("g0x74f5000\n".encode("utf-8"))
print("TRANSPORT")
time.sleep(6)


# motor.close()
# print("serial port closed")


# /////////////////////////////////////////////////////////////////////////////