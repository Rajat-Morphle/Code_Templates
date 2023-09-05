import can
import struct
import time

bus = can.interface.Bus(channel='can0', bustype='socketcan')

def EMCY():
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [EMCY]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SYNC():
    CAN_ID = 1
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SYNC]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

# def TIMESTAMP():
#     CAN_ID = 2
#     can_msg = can.Message(arbitration_id     = CAN_ID,
#                             data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
#                             is_extended_id   = False)
#     bus.send(can_msg)
#     print("sent: [TIMESTAMP]\n")

#     while(1):
#         print("waiting for response...")
#         response = bus.recv()
#         if(response.data[2] == 1):
#             print("Response recieved.")
#             break
#     time.sleep(0.1)

def CANBOOT():
    CAN_ID = 251
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [CANBOOT]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

# def CAN_SILENT_MODE():
#     CAN_ID = 252
#     can_msg = can.Message(arbitration_id     = CAN_ID,
#                             data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
#                             is_extended_id   = False)
#     bus.send(can_msg)
#     print("sent: [CAN_SILENT_MODE]\n")

#     while(1):
#         print("waiting for response...")
#         response = bus.recv()
#         if(response.data[2] == 1):
#             print("Response recieved.")
#             break
#     time.sleep(0.1)

def CHIP_RESTART():
    CAN_ID = 253
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [CHIP_RESTART]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

# def CHIP_ID_HASH():
#     CAN_ID = 254
#     can_msg = can.Message(arbitration_id     = CAN_ID,
#                             data             = [0x00, 0x00, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
#                             is_extended_id   = False)
#     bus.send(can_msg)
#     print("sent: [CHIP_RESTART]\n")

#     while(1):
#         print("waiting for response...")
#         response = bus.recv()
#         if(response.data[2] == 1):
#             print("Response recieved.")
#             break
#     time.sleep(0.1)

# /////////////////////////////////////////////////////////////////////////////////

def HOME():
    CAN_ID = (756 + 0) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF4, 0x01, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [HOME]\n")

    while(1):
        print("waiting for completion...")
        response = bus.recv()
        if(response.data[2] == 2):
            break
        else:
            print("Running...")
    print("Homing Done!\n")
    time.sleep(0.1)

def MOVETO(pos):
    CAN_ID = (756 + 0)
    POS = float(pos)
    byte_arr = bytearray(struct.pack("f", float(POS)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF5, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [MOVETO]\n")

    while(1):
        print("waiting for completion...")
        response = bus.recv()
        if(response.data[2] == 2):
            break
        else:
            print("Running...")
    print("Motion Done!\n")

    time.sleep(0.1)

def MOVETO_NOSYNC(pos):
    CAN_ID = (756 + 0)
    POS = float(pos)
    byte_arr = bytearray(struct.pack("f", float(POS)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x01, 0x02, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [MOVETO_NOSYNC]\n")

    while(1):
        print("waiting for completion...")
        response = bus.recv()
        if(response.data[2] == 2):
            break
        else:
            print("Running...")
    print("Motion Done!\n")

    time.sleep(0.1)

def SPEED(speed):
    CAN_ID = (756 + 0)
    SPEED = float(speed)
    byte_arr = bytearray(struct.pack("f", float(SPEED)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF6, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SPEED]\n")


    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

def ACCEL(accel):
    CAN_ID = (756 + 0)
    ACCEL = float(accel)
    byte_arr = bytearray(struct.pack("f", float(accel)))
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xF7, 0x01, 0X00, 0x00, byte_arr[0], byte_arr[1], byte_arr[2], byte_arr[3]],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [ACCEL]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

def RESET_ERROR_FLAG():
    CAN_ID = (756 + 0) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xFC, 0x01, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [RESET_ERROR_FLAG]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

def EMCY_SHUTDOWN():
    CAN_ID = (756 + 0) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xFD, 0x01, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [EMCY_SHUTDOWN]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

def START_SENDING_CURRENT_POSITION():
    CAN_ID = (756 + 0) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xFF, 0x01, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [START_SENDING_CURRENT_POSITION]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

def STOP_SENDING_CURRENT_POSITION():
    CAN_ID = (756 + 0) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x00, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [STOP_SENDING_CURRENT_POSITION]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

def READ_CURRENT_POSITION():
    CAN_ID = (756 + 0) 
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0xFE, 0x01, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [READ_CURRENT_POSITION]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break

    time.sleep(0.1)

# def SEEK():
#     CAN_ID = (756 + 0) 
#     can_msg = can.Message(arbitration_id     = CAN_ID,
#                             data             = [0xF8, 0x01, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
#                             is_extended_id   = False)
#     bus.send(can_msg)
#     print("sent: [SEEK]\n")

#     while(1):
#         print("waiting for response...")
#         response = bus.recv()
#         if(response.data[2] == 1):
#             print("Response recieved.")
#             break

#     time.sleep(0.1)

# ////////////////////////////////////////////////////////////////////////////////////
# FLASH DATA UPDATE COMMANDS

def WRITE_TO_FLASH():
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x58, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [WRITE_TO_FLASH]\n")

    #  NO RESPONSE
    # while(1):
    #     print("waiting for response...")
    #     response = bus.recv()
    #     if(response.data[2] == 1):
    #         print("Response recieved.")
    #         break
    time.sleep(0.1)

def WRITE_DEFAULT_DATA():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x59, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [WRITE_DEFAULT_DATA]\n")

    #  NO RESPONSE
    # while(1):
    #     print("waiting for response...")
    #     response = bus.recv()
    #     if(response.data[2] == 1):
    #         print("Response recieved.")
    #         break
    time.sleep(0.1)

def SET_CAN_ID():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5A, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_CAN_ID]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_AXIS_TYPE():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5B, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_AXIS_TYPE]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_AXIS_TYPE():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5B, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_AXIS_TYPE]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_MAX_POS():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5C, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_MAX_POS]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_HOMING_DIRECTION():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5D, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_HOMING_DIRECTION]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_MOTOR_ORIENTATION():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5E, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_MOTOR_ORIENTATION]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_HOMING_BUMP():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x5F, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_HOMING_BUMP]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_POST_HOMING_OFFSET():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x60, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_POST_HOMING_OFFSET]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_MAX_ACCEL():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x61, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_MAX_ACCEL]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_MAX_DECEL():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x62, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_MAX_DECEL]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_CLOSELOOP_MIN_ERROR():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x63, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_CLOSELOOP_MIN_ERROR]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_CLOSELOOP_MAX_ERROR():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x64, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg) 
    print("sent: [SET_CLOSELOOP_MAX_ERROR]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_LEADSCREW_PITCH():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x65, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_LEADSCREW_PITCH]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

def SET_MAX_RPM():  # LOAD DEFAULT FLASH DATA
    CAN_ID = 0
    can_msg = can.Message(arbitration_id     = CAN_ID,
                            data             = [0x66bdd, 0x02, 0X00, 0x00, 0x00, 0x00, 0x00, 0x00 ],
                            is_extended_id   = False)
    bus.send(can_msg)
    print("sent: [SET_MAX_RPM]\n")

    while(1):
        print("waiting for response...")
        response = bus.recv()
        if(response.data[2] == 1):
            print("Response recieved.")
            break
    time.sleep(0.1)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def main():
    pass

if __name__ == "__main__":
    main()