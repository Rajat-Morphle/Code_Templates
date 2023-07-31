from tkinter import *
import can
import struct

root = Tk()
root.geometry("330x360")
root.title("CAN_TRX GUI")

CAN_ID = IntVar()
COMMAND_ID = IntVar()
VALUE = StringVar()
FLAG = IntVar()

RESPONSE_ID = StringVar()
RESPONSE_DATA = StringVar()

def B1_callback():

    can_id = (CAN_ID.get() + 256)

    comm_id = COMMAND_ID.get()
    value = float(VALUE.get())
    flag = FLAG.get()
    print(f"-------------------------------------------------------\n\ncan_id: {can_id}")
    print(f"type of can_id: {type(can_id)}\n")
    byte_arr = bytearray(struct.pack("f", float(value)))

    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    can_msg = can.Message(arbitration_id = can_id,
                          data           = [comm_id, 0, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3], 0, flag],
                          is_extended_id = False)
    bus.send(can_msg)

    response = bus.recv()

    response_id = str(response.arbitration_id)
    response_data = str(response.data)

    RESPONSE_ID.set(f"RESPONSE_ID:  {response_id}")
    RESPONSE_DATA.set(f"RESPONSE_DATA\n{response_data}")

    print(f"response_id: {response_id}")
    print(response_data)
    bus.shutdown()


L0 = Label(root, text = "CAN FRAME COMPOSER", padx = 86, pady = 2, bg="grey", fg="white").grid(row = 0, columnspan= 2)
L1 = Label(root, text = "CAN_ID", padx = 8, pady = 2).grid(row = 1, column = 0)
L2 = Label(root, text = "Command_ID", padx = 8, pady = 2).grid(row = 2, column = 0)
L3 = Label(root, text = "Value", padx = 8, pady = 2).grid(row = 3, column = 0)
L4 = Label(root, text = "Flag", padx = 8, pady = 2).grid(row = 4, column = 0)

E1 = Entry(root, textvariable = CAN_ID).grid(row = 1, column = 1, pady=4)
E2 = Entry(root, textvariable = COMMAND_ID).grid(row = 2, column = 1, pady=4)
E3 = Entry(root, textvariable = VALUE).grid(row = 3, column = 1, pady=4)
E4 = Entry(root, textvariable = FLAG).grid(row = 4, column = 1, pady=4)

VALUE.set("0")

B1 = Button(root, text="SEND", command = B1_callback, padx=30, border = 2).grid(row=5, column=1, pady=8)

G1 = Label(root, text="", pady=8).grid(row=6)
L5 = Label(root, textvariable=RESPONSE_ID).grid(row=7, columnspan=2)
L6 = Label(root, textvariable=RESPONSE_DATA).grid(row=8, columnspan=2)

RESPONSE_ID.set("RESPONSE_ID")
RESPONSE_DATA.set("RESPONSE_DATA")


root.mainloop()
