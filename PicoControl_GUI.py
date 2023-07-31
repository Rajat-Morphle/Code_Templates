from tkinter import *
import can
import struct

root = Tk()
root.geometry("1080x240")
root.title("PicoControl GUI")

CAN_ID = IntVar()
COMMAND_ID = IntVar()
VALUE = IntVar()
FLAG = IntVar()

def B1_callback():
    pass


L0 = Label(root, text = "", padx = 8, pady = 2).grid(row = 0, column = 0)
L1 = Label(root, text = "CAN_ID", padx = 72, pady = 2).grid(row = 1, column = 0)
L2 = Label(root, text = "Command_ID", padx = 8, pady = 2).grid(row = 1, column = 1)
L3 = Label(root, text = "Value", padx = 82, pady = 2).grid(row = 1, column = 2)
L4 = Label(root, text = "Flag", padx = 8, pady = 2).grid(row = 1, column = 3)

E1 = Entry(root, textvariable = CAN_ID).grid(row = 2, column = 0)
E2 = Entry(root, textvariable = COMMAND_ID).grid(row = 2, column = 1)
E3 = Entry(root, textvariable = VALUE).grid(row = 2, column = 2)
E4 = Entry(root, textvariable = FLAG).grid(row = 2, column = 3)

B1 = Button(root, text="SEND", command = B1_callback, padx=30, border = 2).grid(row=2, column=4, padx = 32)


root.mainloop()
