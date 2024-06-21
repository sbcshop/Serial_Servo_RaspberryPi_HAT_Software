import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
BT1 = 5 
BT2 = 6
BT3 = 13 
BT4 = 19

GPIO.setup(BT1,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(BT2,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(BT3,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(BT4,  GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up


try :
    while 1:
        if GPIO.input(BT1)==0:
            print ("BT1 Pressed")
            sleep(0.2)
            
        if GPIO.input(BT2)==0: 
            print ("BT2 Pressed")
            sleep(0.2)
            
        if GPIO.input(BT3)==0: 
            print ("BT3 Pressed")
            sleep(0.2)
            
        if GPIO.input(BT4)==0: 
            print ("BT4 Pressed")
            sleep(0.2)
            
        sleep(0.1)    
        
except KeyboardInterrupt:
    GPIO.cleanup()
