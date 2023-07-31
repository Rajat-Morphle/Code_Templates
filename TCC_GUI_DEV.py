from tkinter import *
import can
import struct
import serial
import time

root = Tk()

root.geometry("1280x720") # ("width x height").
# root.minsize(1280,720) # (width, height)
# root.maxsize(1280, 720)
# root.attributes('-fullscreen', True)

# root.configure(bg="white")

root.title("TEMP CONTROL CARD GUI")

SETPOINT  =  IntVar()
TEMP      =  StringVar()
STATE     =  StringVar()
SWITCH_STATE = StringVar()
SWITCH_STATE.set("STATE IS OFF!")

SETPOINT_R  =  IntVar()
STATE_R     =  IntVar()
TEMP_R      =  StringVar()
STATE_R     =  StringVar()

port = serial.Serial(port='/dev/ttyACM0')

global SW_STATE
SW_STATE = False

# ///////////////////////////////////////////////////////////////////////////////////////////////

def read_temp_callback():  # currently it is printing the data that is in the stack of the serial buffer not the latest one..

    data_serial = port.readline().decode().rstrip()  # Read a line of data from the serial port and decode it
    # print(data_serial)
    if "TEMP:" in data_serial:
        data_array = data_serial.split(" ")
        # print(data_array[1])
        TEMP_R.set(f"Temperature: {data_array[1]}")
     
        # print(data_array[4])
        STATE_R.set(f"State: {data_array[4]}")

        # print(data_array[7])
        SETPOINT_R.set(F"Setpoint: {data_array[7]}")

    root.after(10, read_temp_callback)
    # break 



# ////////////////////////////////////////////////////////////////////////////////////////////////

def setpoint_button_callback():
    # sending the setpoint
    # print(STATE.get())
    T = float(SETPOINT.get())
    # print(type(T))
    # print(T)
    byte_arr = bytearray(struct.pack("f", float(T)))

    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    can_msg = can.Message(arbitration_id = 0x110,
                          data           = [0, 0, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3], 0, 0],
                          is_extended_id = False)
    bus.send(can_msg)
    bus.shutdown()


def state_button_callback():
    # print(SETPOINT.get())

    global SW_STATE
    print("callback funcf. called.")
    if (SW_STATE == True):
        SW_STATE = False
        SWITCH_STATE.set("STATE IS OFF!")
        # print(" state is OFF")
    else:
        SW_STATE = True
        SWITCH_STATE.set("STATE IS ON! ")
        # print(" state is ON")

    if(SW_STATE == True):
        bus = can.interface.Bus(channel='can0', bustype='socketcan')
        can_msg = can.Message(arbitration_id = 0x104,
                              data           = [1, 0, 0, 0, 0, 0, 0, 0],
                              is_extended_id = False)
        bus.send(can_msg)
        bus.shutdown()

    if(SW_STATE == False):
        bus = can.interface.Bus(channel='can0', bustype='socketcan')
        can_msg = can.Message(arbitration_id = 0x104,
                              data           = [0, 0, 0, 0, 0, 0, 0, 0],
                              is_extended_id = False)
        bus.send(can_msg)
        bus.shutdown()
    
def setpoint_up_callback():
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    can_msg = can.Message(arbitration_id = 0x106,
                            data           = [0, 0, 0, 0, 0, 0, 0, 0],
                            is_extended_id = False)
    bus.send(can_msg)
    bus.shutdown()

def setpoint_down_callback():
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    can_msg = can.Message(arbitration_id = 0x108,
                            data           = [0, 0, 0, 0, 0, 0, 0, 0],
                            is_extended_id = False)
    bus.send(can_msg)
    bus.shutdown()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

label1 = Label(text = "Morphle", bg = "purple", fg = "white", padx= 603, pady = 4, font = ("calibri", 12, "bold")).grid(columnspan=3)

STATE_LABEL      = Label    (root, text="STATE",      padx = 16,    pady = 8, border = 10, font=(" ", 14, "bold")) .grid(row=1, column=0, pady=8)
STATE_BUTTON     = Button   (root, textvariable=SWITCH_STATE, command = state_button_callback, padx=322, pady=16, border=2, bg="dim gray", fg="white", font=(" ", 14, "bold")) .grid(row=1, column=1, columnspan=2, pady=8)

SETPOINT_LABEL   = Label    (root, text="SETPOINT",   padx = 16,    pady = 8, border = 10) .grid(row=2, column=0, pady=8)
SETPOINT_ENTRY   = Entry    (root, textvariable = SETPOINT, width=40) .grid(row=2, column=1, pady=8)
SETPOINT_BUTTON  = Button   (root, text="SET", command = setpoint_button_callback, padx=126, pady=16, border=2, bg="dim gray", fg="white", font=(" ", 14, "bold")) .grid(row=2, column=2, pady=8)

SETPOINT_UP_BUTTON = Button   (root, text="SETPOINT UP", command = setpoint_up_callback, padx=480, pady=16, border=2, bg="dim gray", fg="white", font=(" ", 14, "bold")) .grid(row=3, columnspan=3, pady=8)
SETPOINT_DOWN_BUTTON = Button   (root, text="SETPOINT DOWN", command = setpoint_down_callback, padx=460, pady=16, border=2, bg="dim gray", fg="white", font=(" ", 14, "bold")) .grid(row=4, columnspan=3, pady=8)

GAP1             = Label    (root, text="", pady=0) .grid(row=5, columnspan=3)
TEMP_STATUS_TITLE     = Label    (root, text="TEMPERATURE", bg = "grey", padx = 502, pady = 16) .grid(row=6, columnspan=3)
TEMP_STATUS_BAR       = Label    (root, textvariable = TEMP_R, bg = "white",fg="grey", padx = 418, pady = 16, border = 2,  font=(" ", 14, "bold")) .grid(row=7, columnspan=3)

GAP2             = Label    (root, text="", pady=0) .grid(row=8, columnspan=3)
STATE_STATUS_TITLE     = Label    (root, text="CURRENT STATE", bg = "grey", padx = 500, pady = 16) .grid(row=9, columnspan=3)
STATE_STATUS_BAR       = Label    (root, textvariable = STATE_R, bg = "white", fg="grey", padx = 510, pady = 16, border = 2, font=(" ", 14, "bold")) .grid(row=10, columnspan=3)

GAP3             = Label    (root, text="", pady=0) .grid(row=11, columnspan=3)
SETPOINT_STATUS_TITLE     = Label    (root, text="CURRENT SETPOINT", bg = "grey", padx = 488, pady = 16) .grid(row=12, columnspan=3)
SETPOINT_STATUS_BAR       = Label    (root, textvariable = SETPOINT_R, bg = "white", fg="grey", padx = 488, pady = 16, border = 2, font=(" ", 14, "bold")) .grid(row=13, columnspan=3)

root.after(1000, read_temp_callback)
 
root.mainloop()


# References

# Label
#     text: adds the text 
#     bg/background: define the background
#     fg: for foreground
#     font: sets the font: [font = ("comicsansms", 20, "bold")]
#     padx = 23
#     pady: Y padding
#     borderwidth = 2 (in pixels)
#     relief = border styling (SUNKEN, RAISED, GROOVE, RIDGE)

# IMG1 = PhotoImage(file = "/home/morphle/Documents/codes/Python/images/img1.png")
# IMG_LABEL1 = Label(image = IMG1).grid(row=0, column=0)
