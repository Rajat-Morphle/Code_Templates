import serial
import time

cam_port = "/dev/ttyACM0"
ring_port = "/dev/ttyACM1"

motor = serial.Serial(port = cam_port, timeout=0.5)
time.sleep(1)
# motor.flush()
# motor.flushInput()
# motor.write("<I0>\n".encode("utf-8")) #list down the connected dynamixel.
# print("sent: I0")
# time.sleep(1)

# motor.flush()
# motor.flushInput()
# motor.write("<I1,D>\n".encode("utf-8")) #turn the position torque mode on.
# print("sent: I1,D")
# time.sleep(1)

# motor.flush()
# motor.flushInput()
# motor.write("<I1,v=20>\n".encode("utf-8")) # sets the velocity of the dynamixel.
# print("sent: I1,v=20")
# time.sleep(1)

# motor.flush()
# motor.flushInput()
# motor.write("<I1,P=1000>\n".encode("utf-8")) # sets the postion to 0.
# print("sent: I1,P=1000")
# time.sleep(1)

# print("Dynamixel initialised.")
# time.sleep(1)

motor.flush()
motor.flushInput()
motor.write("<hx>\n".encode("utf-8"))
print("sent: hx")
time.sleep(3)

print("cam motor initialised.")

# motor.close()
# print("serial port closed")

# ////////////////////////////////////////////////////////////////////////////

motor = serial.Serial(port = ring_port, timeout=0.5)

time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<hx>\n".encode("utf-8"))
print("sent: hx")
time.sleep(5)

print("ring motor iitialised.")

# motor.close()
# print("serial port closed")

# /////////////////////////////////////////////////////////////////////////////
                                # Sequence #
# /////////////////////////////////////////////////////////////////////////////

motor = serial.Serial(port = cam_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<av165>\n".encode("utf-8")) #cam's new home
print("sent: av165")
time.sleep(3)

# motor.close()
# print("serial port closed")

motor = serial.Serial(port = ring_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<av655>\n".encode("utf-8")) #ring's pickup position
print("sent: av655")
time.sleep(15)

# motor.close()
# print("serial port closed")

motor = serial.Serial(port = cam_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<av125>\n".encode("utf-8")) #cam's new home
print("sent: av125")
time.sleep(3)

motor = serial.Serial(port = cam_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<I1,P=630>\n".encode("utf-8")) #cam's new home
print("sent: I1,P=630")
time.sleep(10)

motor = serial.Serial(port = cam_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<I1,P=1000>\n".encode("utf-8")) #cam's new home
print("sent: I1,P=1000")
time.sleep(5)

motor = serial.Serial(port = cam_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<av165>\n".encode("utf-8")) #cam's new home
print("sent: av165")
time.sleep(3)

# motor.close()
# print("serial port closed")

motor = serial.Serial(port = ring_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<av86>\n".encode("utf-8")) #ring's pickup position
print("sent: av86")
time.sleep(15)

motor = serial.Serial(port = ring_port, timeout=0.5)
time.sleep(1)
motor.flush()
motor.flushInput()
motor.write("<av10>\n".encode("utf-8")) #ring's pickup position
print("sent: av10")
time.sleep(5)

# motor.close()
# print("serial port closed")


# /////////////////////////////////////////////////////////////////////////////