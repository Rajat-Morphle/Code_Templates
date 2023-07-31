from tkinter import *

root = Tk()
root.geometry("240x240")
root.title("SWITCH GUI")

SWITCH_STATE = StringVar()
SWITCH_STATE.set("ON")

global sw_state
sw_state = True

def switcher():
    global sw_state
    print("callback funcf. called.")
    if (sw_state == True):
        sw_state = False
        SWITCH_STATE.set("ON")
        print(" state is OFF")
    else:
        sw_state = True
        SWITCH_STATE.set("OFF")
        print(" state is ON")

SWITCH = Button(root, textvariable=SWITCH_STATE, padx=32, command=switcher).pack(pady=20)

root.mainloop()