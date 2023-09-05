from tkinter import *
import can
import struct
import subprocess

root = Tk()
# root.geometry("1300x720")
root.title("PicoControl GUI")

CAN_ID = IntVar()
COMMAND_ID = IntVar()
VALUE = IntVar()
FLAG = IntVar()

def B1_callback():
    subprocess.run('sudo openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000" -c "program /home/morphle/PicoControl/bootloader/deployer.elf verify reset exit')
    
def B2_callback():
    subprocess.run('sudo openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000" -c "program /home/morphle/PicoControl/bootloader/katapult.elf verify reset exit')

def B3_callback():
    subprocess.run('sudo ip link set can0 down')
    subprocess.run('sudo ip link set can0 up type can bitrate 1000000')
    # print(os.system('python3 /home/morphle/PicoControl/bootloader/flash_can.py -i can0 -q'))
    subprocess.run('python3 /home/morphle/PicoControl/bootloader/flash_can.py -i can0 -q')
    # uuid = 'xxxxxxxxxxxx'
    # flash_command = 'python3 flash_can.py -i can0 -f ../cmake-build-debug/src/picocontrol.bin -u ' + uuid

    # print(flash_command)
    # print(os.system(flash_command))

def B4_callback():
    pass

def B5_callback():
    pass

def B6_callback():
    pass

def B7_callback():
    pass

def B8_callback():
    pass


L0 = Label(root, text = "PROGRAM WINDOW", bg = "white",fg="grey", padx = 200, pady = 4, border = 2,  font=(" ", 18, "bold")) .grid(row=0, columnspan=5)

L1 = Label(root, text = "Flash Deployer", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=1, columnspan=2)
B1 = Button(root, text="FLASH", command = B1_callback, padx=30, pady=12) .grid(row=1, column=3, columnspan=2)

L2 = Label(root, text = "Flash Katapult", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=2, columnspan=2)
B2 = Button(root, text="FLASH", command = B2_callback, padx=30, pady=12) .grid(row=2, column=3, columnspan=2)

L3 = Label(root, text = "Flash Firmware", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=3, columnspan=2)
B3 = Button(root, text="FLASH", command = B3_callback, padx=30, pady=12) .grid(row=3, column=3, columnspan=2)

L4 = Label(root, text = "Save Default Data", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=4, columnspan=2)
B4 = Button(root, text="SAVE", command = B4_callback, padx=30, pady=12) .grid(row=4, column=3, columnspan=2)

L5 = Label(root, text = "BOARD QC", bg = "white",fg="grey", padx = 200, pady = 4, border = 2,  font=(" ", 18, "bold")) .grid(row=5, columnspan=2)

L6 = Label(root, text = "Home Motor", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=6, columnspan=2)
B5 = Button(root, text="HOME", command = B5_callback, padx=30, pady=12) .grid(row=6, column=3, columnspan=2)

L7 = Label(root, text = "Move Motor", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=7, columnspan=2)
B6 = Button(root, text="MOVE", command = B6_callback, padx=30, pady=12) .grid(row=7, column=3, columnspan=2)

L8 = Label(root, text = "Brake", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=8, columnspan=2)
B7 = Button(root, text="BRAKE", command = B7_callback, padx=30, pady=12) .grid(row=8, column=3, columnspan=2)



L9 = Label(root, text = "SETUP WINDOW", bg = "white",fg="grey", padx = 100, pady = 4, border = 2,  font=(" ", 18, "bold")) .grid(row=0, column=4, columnspan=2)

L10 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=1, column=5)
E1   = Entry(root, text = "CAN ID") .grid(row=1, column=6)

L11 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=2, column=5)
E2   = Entry(root, text = "CAN ID") .grid(row=2, column=6)

L12 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=3, column=5)
E3   = Entry(root, text = "CAN ID") .grid(row=3, column=6)

L13 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=4, column=5)
E4   = Entry(root, text = "CAN ID") .grid(row=4, column=6)

L14 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=5, column=5)
E5   = Entry(root, text = "CAN ID") .grid(row=5, column=6)

L15 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=6, column=5)
E6   = Entry(root, text = "CAN ID") .grid(row=6, column=6)

L16 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=7, column=5)
E7   = Entry(root, text = "CAN ID") .grid(row=7, column=6)

L17 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=8, column=5)
E8   = Entry(root, text = "CAN ID") .grid(row=8, column=6)

L18 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=9, column=5)
E9   = Entry(root, text = "CAN ID") .grid(row=9, column=6)

L19 = Label(root, text = "CAN ID", fg="grey", padx = 4, pady = 4, border = 2,  font=(" ", 12, "bold")) .grid(row=10, column=5)
E10   = Entry(root, text = "CAN ID") .grid(row=10, column=6)

B8 = Button(root, text="SAVE", command = B8_callback, padx=30, pady=12) .grid(row=11, column=5, columnspan=2)

root.mainloop()
