from tkinter import *
import can
import struct
import subprocess
import time

root = Tk()
# root.geometry("1300x720")
root.title("PicoControl GUI")

bus = can.interface.Bus(channel='can0', bustype='socketcan')

# MOTOR TESTING FIELD VARIABLES:
device_id               = IntVar()
pos_val                 = DoubleVar()
speed_val               = IntVar()
accel_val               = IntVar()

# FLASH DATA ENTRY FIELD VARIABLES:
new_device_id           = IntVar()
axis_type               = IntVar()
max_position            = DoubleVar()
homing_direction        = IntVar()
motor_orientation       = IntVar()
homing_bump             = DoubleVar()
post_homing_offset      = DoubleVar()
max_acceleration        = IntVar()
max_deceleration        = IntVar()
close_loop_min_error    = DoubleVar()
close_loop_max_error    = DoubleVar()
leadscrew_pitch         = IntVar()
max_rpm                 = IntVar()
homing_speed            = IntVar()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

def home():
    id = device_id.get()
    CAN_ID = (id + 756) 
    print(CAN_ID)
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF4, 0x01, 0X01, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("home sent\n")
    time.sleep(0.1)

    while(1):
        print("waiting for can message")
        response = bus.recv()
        if(response.data[2] == 2):
            break
        else:
            print("Running...")
    print("Homing Done!\n")
    time.sleep(0.1)

def brake():
    pass

def speed():
    id = device_id.get()
    speed = float(speed_val.get())
    CAN_ID = (id + 756)
    byte_arr = bytearray(struct.pack("f", float(speed)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF6, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)
    print("speed set successfully.")  

def acceleration():
    id = device_id.get()
    accel = float(accel_val.get())
    CAN_ID = (id + 756)
    byte_arr = bytearray(struct.pack("f", float(accel)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF7, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)
    print("acceleration set successfully.")

def move():
    id = device_id.get()
    pos = float(pos_val.get())
    CAN_ID = (id + 756)
    byte_arr = bytearray(struct.pack("f", float(pos)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF5, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("position sent.")
    time.sleep(0.1)
    
    can_msg = can.Message(arbitration_id     = 0x001,
                            data             = [0x00, 0x00, 0X00, 0x0F],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sync sent")
    time.sleep(0.1)
    
    while(1):
        response = bus.recv()
        if(response.data[2] == 2 and response.arbitration_id == (id + 1268 )):
            break
        else:
            print("Running...")
    print("Reached!\n")

    time.sleep(0.1)

def canboot():
    id = device_id.get()
    byte_arr = bytearray(struct.pack("i", id+500))

    can_msg = can.Message(arbitration_id     = 0xFB,
                            data             = [byte_arr[0], byte_arr[1], 0X00, 0x00, 0X00, 0x00, 0X00, 0x00],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)
    print("canboot initialised.")

def flash():
    pass

def reset():
    id = device_id.get()
    byte_arr = bytearray(struct.pack("i", id+500))

    can_msg = can.Message(arbitration_id     = 0xFD,
                            data             = [byte_arr[0], byte_arr[1], 0X00, 0x00, 0X00, 0x00, 0X00, 0x00],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)


# FLASH DATA EDITING FUNCTIONS:

def write_to_flash():
    id = device_id.get()
    CAN_ID = (id + 756)

    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x58, 0x02, 0X00, 0x00, 0X00, 0x00, 0X00, 0x00],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.2)
    print("writing data to flash successful.")

    print("initialising reset")
    reset()


def set_device_id():
    id = device_id.get()
    CAN_ID = (id + 756)

    new_id = new_device_id.get() + 500
    if new_id >= 500 and new_id < 600:
        byte_arr = bytearray(struct.pack("f", float(new_id)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x5A, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid device ID.")

def set_axis_type():
    id = device_id.get()
    CAN_ID = (id + 756)

    axis = axis_type.get()
    if axis != 0 and axis !=1:
        print("invalid axis type")
        return
    byte_arr = bytearray(struct.pack("f", float(axis)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5B, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)

def set_max_position():
    id = device_id.get()
    CAN_ID = (id + 756)

    max_pos = max_position.get()
    if max_pos >= 0 and max_pos < 1000:
        byte_arr = bytearray(struct.pack("f", float(max_pos)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x5C, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid max position.")

def set_homing_direction():
    id = device_id.get()
    CAN_ID = (id + 756)

    homing_dir = homing_direction.get()
    if homing_dir != 0 and homing_dir !=1:
        print("invalid homing direction")
        return
    byte_arr = bytearray(struct.pack("f", float(homing_dir)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5D, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)

def set_motor_orientation():
    id = device_id.get()
    CAN_ID = (id + 756)

    motor_dir = motor_orientation.get()
    if motor_dir != 0 and motor_dir !=1:
        print("invalid motor orientation")
        return
    byte_arr = bytearray(struct.pack("f", float(motor_dir)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5E, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)

def set_homing_bump():
    id = device_id.get()
    CAN_ID = (id + 756)

    home_bump = homing_bump.get()
    if home_bump >= 0 and home_bump < 50:
        byte_arr = bytearray(struct.pack("f", float(home_bump)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x5F, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid homing bump.")

def set_post_homing_offset():
    id = device_id.get()
    CAN_ID = (id + 756)

    post_home_offset = post_homing_offset.get()
    if post_home_offset >= 0 and post_home_offset < 50:
        byte_arr = bytearray(struct.pack("f", float(post_home_offset)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x60, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid homing offset.")

def set_max_acceleration():
    id = device_id.get()
    CAN_ID = (id + 756)

    max_accel = max_acceleration.get()
    if max_accel >= 0 and max_accel < 1000000:
        byte_arr = bytearray(struct.pack("f", float(max_accel)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x61, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid max accel.")

def set_max_deceleration():
    id = device_id.get()
    CAN_ID = (id + 756)

    max_decel = max_deceleration.get()
    if max_decel >= 0 and max_decel < 1000000:
        byte_arr = bytearray(struct.pack("f", float(max_decel)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x62, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid max decel.")

def set_close_loop_min_error():
    id = device_id.get()
    CAN_ID = (id + 756)

    min_error = close_loop_min_error.get()
    if min_error >= 0 and min_error < 2:
        byte_arr = bytearray(struct.pack("f", float(min_error)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x63, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid set close loop min error.")

def set_close_loop_max_error():
    id = device_id.get()
    CAN_ID = (id + 756)

    max_error = close_loop_max_error.get()
    if max_error >= 0 and max_error < 2:
        byte_arr = bytearray(struct.pack("f", float(max_error)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x64, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid set close loop max error.")

def set_leadscrew_pitch():
    id = device_id.get()
    CAN_ID = (id + 756)

    pitch = leadscrew_pitch.get()
    if pitch >= 0 and pitch < 15:
        byte_arr = bytearray(struct.pack("f", float(pitch)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x65, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid leadscrew pitch.")

def set_max_rpm():
    id = device_id.get()
    CAN_ID = (id + 756)

    rpm_max = max_rpm.get()
    if rpm_max >= 0 and rpm_max < 1000:
        byte_arr = bytearray(struct.pack("f", float(rpm_max)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x66, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid max RPM.")

def set_homing_speed():
    id = device_id.get()
    CAN_ID = (id + 756)

    home_speed = homing_speed.get()
    if home_speed >= 0 and home_speed < 1000:
        byte_arr = bytearray(struct.pack("f", float(home_speed)))
        can_msg = can.Message(arbitration_id     = CAN_ID,
                                data             = [0x67, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                                is_extended_id   = False)
        bus.send(can_msg)
        time.sleep(0.1)

    else:
        print("invalid homing speed.")
        

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////


FLASH_DATA_EDITOR = Label(root, text = "FLASH DATA EDITOR", bg = "white",fg="black", padx = 190, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=0, columnspan=2)
HEADER = Label(root, text = "", fg="black", padx = 620, pady = 4, border = 2,  font=(" ", 2, "bold")) .grid(row=1, column=0, columnspan=5)

# NEW_DEVICE_ID = Label(root, text = "NEW DEVICE ID", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=2, column=0)
B_NEW_DEVICE_ID = Button(root, text="NEW DEVICE ID", command = set_device_id, padx=103, pady=8) .grid(row=2, column=1)
E_NEW_DEVICE_ID   = Entry(root, textvariable = new_device_id) .grid(row=2, column=0)

# AXIS_TYPE = Label(root, text = "AXIS TYPE", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=3, column=0)
B_AXIS_TYPE = Button(root, text="AXIS_TYPE", command = set_axis_type, padx=119, pady=8) .grid(row=3, column=1)
E_AXIS_TYPE   = Entry(root, textvariable = axis_type) .grid(row=3, column=0)

# MAX_POSITION = Label(root, text = "MAX POSITION", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=4, column=0)
B_MAX_POSITION = Button(root, text="MAX_POSITION", command = set_max_position, padx=104, pady=8) .grid(row=4, column=1)
E_MAX_POSITION   = Entry(root, textvariable = max_position) .grid(row=4, column=0)

# HOMING_DIRECTION = Label(root, text = "HOMING DIRECTION", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=5, column=0)
B_HOMING_DIRECTION = Button(root, text="HOMING_DIRECTION", command = set_homing_direction, padx=86, pady=8) .grid(row=5, column=1)
E_HOMING_DIRECTION   = Entry(root, textvariable = homing_direction) .grid(row=5, column=0)

# MOTOR_ORIENTATION = Label(root, text = "MOTOR ORIENTATION", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=6, column=0)
B_MOTOR_ORIENTATION = Button(root, text="MOTOR_ORIENTATION", command = set_motor_orientation, padx=80, pady=8) .grid(row=6, column=1)
E_MOTOR_ORIENTATION   = Entry(root, textvariable = motor_orientation) .grid(row=6, column=0)

# HOMING_BUMP = Label(root, text = "HOMING BUMP", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=7, column=0)
B_HOMING_BUMP = Button(root, text="HOMING_BUMP", command = set_homing_bump, padx=102, pady=8) .grid(row=7, column=1)
E_HOMING_BUMP   = Entry(root, textvariable = homing_bump) .grid(row=7, column=0)

# POST_HOMING_OFFSET = Label(root, text = "POST HOMING OFFSET", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=8, column=0)
B_POST_HOMING_OFFSET = Button(root, text="POST_HOMING_OFFSET", command = set_post_homing_offset, padx=76, pady=8) .grid(row=8, column=1)
E_POST_HOMING_OFFSET   = Entry(root, textvariable = post_homing_offset) .grid(row=8, column=0)

# MAX_ACCELERATION = Label(root, text = "MAX_ACCELERATION", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=9, column=0)
B_MAX_ACCELERATION = Button(root, text="MAX_ACCELERATION", command = set_max_acceleration, padx=85, pady=8) .grid(row=9, column=1)
E_MAX_ACCELERATION   = Entry(root, textvariable = max_acceleration) .grid(row=9, column=0)

# MAX_DECELERATION = Label(root, text = "MAX DECELERATION", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=10, column=0)
B_MAX_DECELERATION = Button(root, text="MAX_DECELERATION", command = set_max_deceleration, padx=85, pady=8) .grid(row=10, column=1)
E_MAX_DECELERATION   = Entry(root, textvariable = max_deceleration) .grid(row=10, column=0)

# CLOSE_LOOP_MIN_ERROR = Label(root, text = "CLOSE LOOP MIN ERROR", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=11, column=0)
B_CLOSE_LOOP_MIN_ERROR = Button(root, text="CLOSE_LOOP_MIN_ERROR", command = set_close_loop_min_error, padx=69, pady=8) .grid(row=11, column=1)
E_CLOSE_LOOP_MIN_ERROR   = Entry(root, textvariable = close_loop_min_error) .grid(row=11, column=0)

# CLOSE_LOOP_MAX_ERROR = Label(root, text = "CLOSE LOOP MAX ERROR", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=12, column=0)
B_CLOSE_LOOP_MAX_ERROR = Button(root, text="CLOSE_LOOP_MAX_ERROR", command = set_close_loop_max_error, padx=67, pady=8) .grid(row=12, column=1)
E_CLOSE_LOOP_MAX_ERROR   = Entry(root, textvariable = close_loop_max_error) .grid(row=12, column=0)

# LEADSCREW_PITCH = Label(root, text = "LEADSCREW PITCH", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=13, column=0)
B_LEADSCREW_PITCH = Button(root, text="LEADSCREW_PITCH", command = set_leadscrew_pitch, padx=90, pady=8) .grid(row=13, column=1)
E_LEADSCREW_PITCH   = Entry(root, textvariable = leadscrew_pitch) .grid(row=13, column=0)

# MAX_RPM = Label(root, text = "MAX RPM", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=14, column=0)
B_MAX_RPM = Button(root, text="MAX_RPM", command = set_max_rpm, padx=120, pady=8) .grid(row=14, column=1)
E_MAX_RPM   = Entry(root, textvariable = max_rpm) .grid(row=14, column=0)

# HOMING_SPEED = Label(root, text = "HOMING SPEED", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=15, column=0)
B_HOMING_SPEED = Button(root, text="HOMING_SPEED", command = set_homing_speed, padx=101, pady=8) .grid(row=15, column=1)
E_HOMING_SPEED   = Entry(root, textvariable = homing_speed) .grid(row=15, column=0)

PRE_FOOTER = Label(root, text = "", fg="black", padx = 620, pady = 4, border = 2,  font=(" ", 2, "bold")) .grid(row=16, column=0, columnspan=5)

B_WRITE_TO_FLASH = Button(root, text="WRITE TO FLASH", command = write_to_flash, padx=208, pady=8) .grid(row=17, column=0, columnspan=2)

MOTOR_TESTER = Label(root, text = "MOTOR TESTER", bg = "white",fg="black", padx = 250, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=0, column=2 ,columnspan=3)

HOME = Label(root, text = "HOME", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=2, column=2)
B_HOME = Button(root, text="HOME", command = home, padx=174, pady=8) .grid(row=2, column=3, columnspan=3)

BRAKE = Label(root, text = "BRAKE", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=3, column=2)
B_BRAKE = Button(root, text="BRAKE", command = brake, padx=172, pady=8) .grid(row=3, column=3, columnspan=3)

SPEED = Label(root, text = "SPEED", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=4, column=2)
E_SPEED   = Entry(root, textvariable = speed_val) .grid(row=4, column=3)
B_SPEED = Button(root, text = "SPEED", command = speed, padx=66, pady=8) .grid(row=4, column=4)

ACCELERATION = Label(root, text = "ACCEL", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=5, column=2)
E_ACCELERATION = Entry(root, textvariable = accel_val) .grid(row=5, column=3)
B_ACCELERATION = Button(root, text="ACCELERATION", command = acceleration, padx=37, pady=8) .grid(row=5, column=4)

MOVE = Label(root, text = "MOVE", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=6, column=2)
E_MOVE   = Entry(root, textvariable = pos_val) .grid(row=6, column=3)
B_MOVE = Button(root, text="MOVE", command = move, padx=67, pady=8) .grid(row=6, column=4)

FLASH_WINDOW = Label(root, text = "FLASH WINDOW", bg="white", fg="black", padx = 210, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=9, column=2, columnspan=3)

DEVICE_ID = Label(root, text = "DEVICE_ID", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=11, column=2)
E_DEVICE_ID = Entry(root, textvariable = device_id) .grid(row=11, column=3, columnspan=2)
# PRE_CANBOOT = Label(root, text = "", bg="RED", fg="black", padx = 200, pady = 4, border = 2,  font=(" ", 2, "bold")) .grid(row=12, column=2, columnspan=3)
B_CANBOOT = Button(root, text="CANBOOT", command = canboot, padx=250, pady=8) .grid(row=12, column=2, columnspan=3)

UUID = Label(root, text = "UUID", fg="black", padx = 20, pady = 4, border = 2,  font=(" ", 13, "bold")) .grid(row=14, column=2)
E_UUID = Entry(root, text = "UUID") .grid(row=14, column=3, columnspan=2)
# PRE_FLASH = Label(root, text = "", bg="RED", fg="black", padx = 200, pady = 4, border = 2,  font=(" ", 2, "bold")) .grid(row=15, column=2, columnspan=3)
B_FLASH = Button(root, text="FLASH", command = flash, padx=260, pady=8) .grid(row=15, column=2, columnspan=3)

B_RESET = Button(root, text="RESET BOARD", command = reset, padx=235, pady=8) .grid(row=17, column=2, columnspan=3)

FOOTER = Label(root, text = "", fg="black", padx = 620, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=18, column=0, columnspan=5)

root.mainloop()



# Buttons to be added:
    # set default data button








# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def B1_callback():
#     subprocess.run('sudo openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000" -c "program /home/morphle/PicoControl/bootloader/deployer.elf verify reset exit')
    
# def B2_callback():
#     subprocess.run('sudo openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000" -c "program /home/morphle/PicoControl/bootloader/katapult.elf verify reset exit')

# def B3_callback():
#     subprocess.run('sudo ip link set can0 down')
#     subprocess.run('sudo ip link set can0 up type can bitrate 1000000')
#     # print(os.system('python3 /home/morphle/PicoControl/bootloader/flash_can.py -i can0 -q'))
#     subprocess.run('python3 /home/morphle/PicoControl/bootloader/flash_can.py -i can0 -q')
#     # uuid = 'xxxxxxxxxxxx'
#     # flash_command = 'python3 flash_can.py -i can0 -f ../cmake-build-debug/src/picocontrol.bin -u ' + uuid

#     # print(flash_command)
#     # print(os.system(flash_command))



