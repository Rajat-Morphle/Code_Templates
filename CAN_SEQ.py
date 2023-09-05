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
        print("waiting for can message")
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

    time.sleep(0.1)

def sync(check_id):
    can_msg = can.Message(arbitration_id     = 0x001,
                            data             = [0x00, 0x00, 0X00, 0x0F],
                            is_extended_id   = False)
    bus.send(can_msg)
    print(f"Start time: {str(time.time())}")
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

def speed(id, speed):
    CAN_ID = (int(id) + 756)
    SPEED = float(speed)
    byte_arr = bytearray(struct.pack("f", float(SPEED)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF6, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    bus.send(can_msg)

    time.sleep(0.1)

def accel(id, accel):
    CAN_ID = (int(id) + 756)
    ACCEL = float(accel)
    byte_arr = bytearray(struct.pack("f", float(accel)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF7, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    # bus.send(can_msg)

    time.sleep(0.1)
def open_gates():
    # opening all the gates
    moveto(1,130)
    moveto(2,0)
    moveto(3,0)
    moveto(8,180)
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
    
    # print("motor_4 homing.")
    # home(4)
    # moveto(4,40)
    # sync(4)
    
    # print("motor_5 homing.")
    # home(5)
    # moveto(5,20)
    # sync(5)

    print("motor_7 homing.")
    home(7)
    # moveto(7,26)
    # sync(7)
    
    print("motor_8 homing.")
    home(8)
    
    print("motor_9 homing.")
    home(9)

    print("moving cam...")
    speed(9,180)
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
    moveto(6,893)
    sync(6)
    close_gates()
    moveto(10,-18)
    sync(10)
    moveto(9,160)
    moveto(10,-28)
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
    moveto(10,-6)
    sync(10)
    open_gates()
    moveto(6,185)
    sync(6)
    close_gates()
# ///////////////////////////////////////////////////////////////////////

def main():
    # i = 14
    # home(i)
    # accel(i, 10000)
    # # speed(i, 50)
    # for j in range (650, 1000000, 10):
    #     print("current acc.: ", j)
    #     speed(i, j)
    #     time.sleep(0.1)
        
    #     moveto(i, 150)
    #     sync(i)
    #     moveto(i, 60)
    #     sync(i)

    accel(11, 100)
    accel(12, 3000)
    accel(13, 3000)
    accel(14, 10000)
    accel(15, 10000)
    # time.sleep(0.2)

    speed(11, 60)
    speed(12, 80)
    speed(13, 150)
    speed(14, 800)
    speed(15, 700)
    time.sleep(0.2)

    home(11)
    home(12)
    home(13)
    home(14)
    home(15)
    input()

# ready for pickup
    print("ready for pickup.")
    moveto(11,130)
    moveto(12,60)
    moveto(13,30)
    moveto(15,60)
    sync(11)

# dip 1
    input()
    speed(12, 25)
    print("dip")
    moveto(12, 40)
    moveto(11, 170)
    sync(12)

# # pick 1
#     input()
#     speed(12, 60)
#     speed(13, 15)
#     accel(13, 10000)
#     print("pick")
    
#     moveto(11, 150)
#     moveto(12, 20)
#     moveto(13, 20)
#     sync(12)

# # pull-out 1

#     moveto(11,110)
#     moveto(12,35)
#     sync(11)
    

    # for i in range(2000, 100000, 5000):
    #     accel(5, i)
    #     print(f"{i}\n")
        
    #     moveto(5, 130)
    #     sync(5)
    #     print(f"End time: {str(time.time())}")
    #     moveto(5, 90)
    #     sync(5)        


if __name__ == "__main__":
    main()
