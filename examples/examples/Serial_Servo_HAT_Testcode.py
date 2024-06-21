''' Serial Servo HAT Testcode '''
import os
import sys
sys.path.append("examples/lib")

from PIL import Image, ImageDraw, ImageFont
from time import sleep
from lib import display_1inch14
from lib.serial_comm import SerialComm
from lib.command import Commands
from lib.servo_instruction import SBSServo
import RPi.GPIO as GPIO

# Set GPIOs for BCM mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define Button connections
BT1 = 5 
BT2 = 6
BT3 = 13 
BT4 = 19

# configure button for input
GPIO.setup(BT1,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(BT2,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(BT3,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(BT4,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up

# Set up the font paths
font1 = ImageFont.truetype("font/Font00.ttf", 25)
font2 = ImageFont.truetype("font/Font00.ttf", 16)
font3 = ImageFont.truetype("font/Font02.ttf", 25)

# Initialize the LCD display
disp = display_1inch14.lcd_display()
disp.Init()

def display_text(text1, text2):
    # Create a new image with white background
    image = Image.new("RGB", (disp.width, disp.height), "BLACK")

    # Draw some text on the image
    draw = ImageDraw.Draw(image)
    draw.text((10, 5), text1, font=font1, fill="YELLOW")
    draw.text((10, 50), text2, font=font1, fill="BLUE")
    
    # Display the image on the LCD
    disp.ShowImage(image)

def rotate_servo(ID):
    servo.writeAngleLimit(ID, angleMin=0, angleMax=0)
    servo.motor_mode(ID, speed=500, direction=0) #clockwise direction
    sleep(2)
    servo.motor_mode(ID, speed=0, direction=0)   #Stop
    sleep(2)

display_text("Hello..!", "")
sleep(1)
disp.clear()

if __name__ == "__main__":
    servo=SBSServo()
    servo.connect(port="/dev/ttyS0", baudrate=115200) #Serial port used
    ServoID=servo.readID() #Read ID of connected servo motor
    print(ServoID)
    
    try :
        while 1:
            if GPIO.input(BT1)==0:
                print ("BT1 Pressed")
                display_text("BT1 Pressed", "Rotate ServoID: " + str(ServoID[0]))
                rotate_servo(ServoID[0])
                # Clear the display
                disp.clear()
                sleep(0.2)
                
            if GPIO.input(BT2)==0: 
                print ("BT2 Pressed")
                display_text("BT2 Pressed", "Rotate ServoID: " + str(ServoID[1]))
                rotate_servo(ServoID[1])
                # Clear the display
                disp.clear()
                sleep(0.2)
                
            if GPIO.input(BT3)==0: 
                print ("BT3 Pressed")
                display_text("BT3 Pressed", "Rotate ServoID: " + str(ServoID[2]))
                rotate_servo(ServoID[2])
                # Clear the display
                disp.clear()
                sleep(0.2)
                
            if GPIO.input(BT4)==0: 
                print ("BT4 Pressed")
                display_text("BT4 Pressed", "Rotate ServoID: " + str(ServoID[3]))
                rotate_servo(ServoID[3])
                # Clear the display
                disp.clear()
                sleep(0.2)

            display_text("Press Any Button", "")   
            sleep(0.1)    
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        
            
            

