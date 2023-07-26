import can
import struct
import time

bus = can.interface.Bus(channel='can0', bustype='socketcan')

# ==================================================== FUNCTION DEFINITIONS ================================================


def home(id):
    CAN_ID = (int(id) + 756) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF4, 0x01, 0X01, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("home sent\n")

    while(1):
        response = bus.recv()
        if(response.data[2]==2):
            break
        else:
            print("Running...")
    print("Homing Done!\n")
    time.sleep(0.5)

def moveto(id, pos):
    # POS
    CAN_ID = (int(id) + 756)
    POS = float(pos)
    byte_arr = bytearray(struct.pack("f", float(POS)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF5, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    time.sleep(0.1)

    # SYNC
    can_msg = can.Message(arbitration_id     = 0x001,
                            data             = [0x00, 0x00, 0X00, 0x0F],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sync sent")
    print(f"moving to {POS}\n")
    
    while(1):
        response = bus.recv()
        if(response.data[2]==2):
            break
        else:
            print("Running...")
    print("Reached!\n")
    # time.sleep(0.5)


def main():
    # SEQUENCE

    while(1):
        home(2)
        home(3)
        home(5)
        home(9)
        moveto(9,80)
        home(8)
        home(9)
        moveto(9,30)
        moveto(8,150)
        moveto(8,120)
        moveto(5,90)
        moveto(5,50)
        moveto(9,0)
        moveto(9,90)
        moveto(8,0)


if __name__ == "__main__":
    main()





# response = bus.recv()