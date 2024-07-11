import os
import sys
sys.path.append("examples/lib")

from lib.serial_comm import SerialComm
from lib.command import Commands
from lib.servo_instruction import SBSServo
from time import sleep


if __name__ == "__main__":
        servo=SBSServo()
        servo.connect(port="/dev/ttyS0", baudrate=115200)
        '''
        ServoID=servo.readID()	# Uncomment to Read IDs of connected Serial Servo Motors
        print(ServoID)
        '''
        ServoID1 = 3  # using Serial Servo with ID 3, change as per your motor
        servo.writeAngleLimit(ID=ServoID1, angleMin=0, angleMax=1000) #set min max angle
        
        while 1:
            servo.servoWrite(ID=ServoID1, position=0, r_time=0, r_speed=900) #Set to 0 position
            sleep(3)
            servo.servoWrite(ID=ServoID1, position=999, r_time=0, r_speed=900) #Set to 999 position
            sleep(3)
