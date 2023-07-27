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
    bus.send(can_msg)
    print("home sent\n")

    while(1):
        response = bus.recv()
        if(response.data[2] == 2):
            break
        else:
            print("Running...")
    print("Homing Done!\n")
    time.sleep(0.1)

def moveto(id, pos):
    # POS
    CAN_ID = (int(id) + 756)
    POS = float(pos)
    byte_arr = bytearray(struct.pack("f", float(POS)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF5, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    bus.send(can_msg)

    time.sleep(0.1)

def sync(check_id):
    can_msg = can.Message(arbitration_id     = 0x001,
                            data             = [0x00, 0x00, 0X00, 0x0F],
                            is_extended_id   = False)
    bus.send(can_msg)
    bus.send(can_msg)
    print("sync sent")
    # print(f"moving to {POS}\n")
    
    while(1):
        response = bus.recv()
        if(response.data[2] == 2 and response.arbitration_id == (check_id + 1268 )):
            break
        else:
            print("Running...")
    print("Reached!\n")
    time.sleep(0.1)

def open_gates():
    # opening all the gates
    moveto(1,130)
    moveto(2,0)
    moveto(3,0)
    moveto(8,130)
    sync(8)

def close_gates():
    # closing all gates
    moveto(1,0)
    moveto(2,130)
    moveto(3,130)
    moveto(8,0)
    sync(8)

def home_all():
    print("motor_1 Homing.")
    home(1)
    
    print("motor_2 homing.")
    home(2)
    
    print("motor_3 homing.")
    home(3)
    
    print("motor_4 homing.")
    home(4)
    moveto(4,40)
    sync(4)
    
    print("motor_5 homing.")
    home(5)
    moveto(5,40)
    sync(5)

    print("motor_7 homing.")
    home(7)
    moveto(7,40)
    sync(7)
    
    print("motor_8 homing.")
    home(8)
    
    print("motor_9 homing.")
    home(9)

    print("moving cam...")
    moveto(9,80)
    sync(9)

    print("motor_10 Homing.")
    home(10)
    
    print("opening all the gates.")
    open_gates()

    print("homing the Hanger gantry...")
    home(6)
    moveto(6,190)
    sync(6)

    # close_gates()

def position_hanger1():
    
    moveto(9,80)
    sync(9)
    home(10)
    open_gates()
    moveto(6,425)
    sync(6)
    close_gates()
    moveto(10,-18)
    sync(10)
    moveto(9,160)
    moveto(10,-25)
    sync(10)

def position_hanger2():
    
    moveto(9,80)
    sync(9)
    home(10)
    open_gates()
    moveto(6,895)
    sync(6)
    close_gates()
    moveto(10,-15)
    sync(10)
    moveto(9,160)
    moveto(10,-25)
    sync(10)

def teardown():
    moveto(9,200)
    moveto(10,-20)
    sync(10)
    moveto(9,80)
    sync(9)

def transport():
    moveto(9,80)
    sync(9)
    home(10)
    open_gates()
    moveto(6,-280)
    sync(6)
    close_gates()
# ///////////////////////////////////////////////////////////////////////

def main():
    # SEQUENCE

    while(1):

        # home_all()
        position_hanger1()
        y = input()
        teardown()
        x = input()
        transport()
        # position_hanger2()
        # teardown()

        break


if __name__ == "__main__":
    main()