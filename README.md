# Serial_Servo_RaspberryPi_HAT_Software

<img src= "https://cdn.shopify.com/s/files/1/1217/2104/files/Artboard_1_2.png?v=1718787431"/>

The Serial Servo Raspberry Pi HAT is equipped with a range of versatile features. It offers multiple powering options, including a Type C power input for breakout use, as well as two alternative power sources through screw terminals and a DC jack, providing flexibility to suit your specific requirements.

Additionally, it boasts four Serial Servo connectors, each accompanied by four programmable buttons, enhancing its functionality. For added safety and convenience, an on/off switch is incorporated into the design. Furthermore, the HAT features a 1.14” TFT Display to provide clear status indicators, ensuring a user-friendly experience.

This Github provides getting started guide for Serial Servo RaspberryPi HAT.

## Features:
- Pi HAT with standard 40 pin Headers to connect various Raspberry Pi boards and compatible SBC’s
- TFT 1.14” display for user interactions
- Four slot to connect Serial Servo Motors, and easily cascade servo to connect more number of motor*
- Four Programmable Buttons to add additional control features to your project 
- Screw terminal and DC jack options to connect 6-8.4V adapter with onboard regulator 
- Power status LED to indicate board power
- Type C interface for direct use with PC/laptop using standalone GUI software
- Compatible Servo Motors =>
    - [SB-SS023](https://shop.sb-components.co.uk/products/sb-serial-servo-sb-ss023-powerful-multi-purpose-digital-servo-motor?_pos=1&_sid=5cba75e00&_ss=r) - For Lightweight Projects
    - [SB-SS15](https://shop.sb-components.co.uk/products/sb-serial-servo-sb-ss15-powerful-multi-purpose-digital-servo-motor?_pos=2&_sid=5cba75e00&_ss=r) - For Heavier Applications
    - Servo Motor Key Features:
      - Real-Time Position, Load, Temperature, Speed, and Voltage feedback.
      - Servo/Motor Mode Switchable
      - High Precision And Large Torque
      - ID Range 1~253
      - 38400 bps ~ 1Mbps (1Mbps by default)

***NOTE:  Avoid Connecting More Than 6 Servos At A Time, Not Recommended Due To High Current Demand By Servos.**

For more details about Serial Servo Motor checkout [Manual](https://github.com/sbcshop/Serial_Servo_Breakout_Software/blob/main/Documents/SB_Servo_User_Manual.pdf).

## Specification:
- Microcontroller: Raspberry Pi boards and compatible SBC’s
- Board Supply Voltage: 5V 
- Operating Pin Voltage: 3.3V
- Operating Servo voltage: 6~8.4V 
- Display Size: 1.14” 
- Display Resolution : 240x320 pixels
- Display Driver: ST7789 
- Display Appearance: RGB, 65K/262K
- Temperature Range: -20°C ~ +70°C

## Getting Started with Serial Servo Raspberry Pi HAT 
### Pinout
<img src= "https://cdn.shopify.com/s/files/1/1217/2104/files/Artboard_1_copy_2.png?v=1718788207" />

- (1), (3), (9), (11) Programmable Buttons
- (2) Serial Servo connector
- (4) ON/OFF Motor Supply 
- (5) DC Jack Input (6~8.4V DC)
- (6) Screw Terminal input (6~8.4V)
- (7) Type C
- (8) Power Status LED
- (10) TFT 1.14” Display
- (12) Standard 40 pin Raspberry Pi Header

### Interfacing Details 
**Pins Mapping of RPi and HAT**
  
  <img src="https://github.com/sbcshop/Serial_Servo_RaspberryPi_HAT_Software/blob/main/images/Serial_Servo_RPi_HAT_Interfacing.jpg" width="586" height="361">
  
  _Display Pins:_
  | Symbol | Description |
  |---|---|
  | CS | Display control Chip select pin for SPI bus interfacing |
  | CLK | Display SPI Clock Pin |
  | DC | Data/Command pin of Display |
  | DIN  | Data In (MOSI) pin of Display SPI interfacing |
  | RESET | Display Reset pin |
  | BL | BackLight for Display panel |
  
   _Actuator Pins:_
  | Symbol | Description | 
  |---|---|
  | BT1 | Programmable Button 1 |
  | BT2 | Programmable Button 2 |
  | BT3 | Programmable Button 3 |
  | BT4 | Programmable Button 4 |
  
   _Serial Servo Bus Pins:_
   
  * Servo connector having +ve[6~8.4VDC], -ve[GND] and Signal pin. 
  * Serial Servo Signal pins breakout into UART RXD and TXD to connect with RPi UART pins,
    
  | Symbol | Description | 
  |---|---|
  | Servo Bus RXD | UART communication pin |
  | Servo Bus TXD | UART communication pin |
  
### Download and install Raspberry OS to Pi
  - Follow the Getting Started [Link](https://www.raspberrypi.com/documentation/computers/getting-started.html) to perform OS install 
  - Now you can either use Screen and Keyboard to access Pi or Setup to use [remotely with VNC viewer](https://projects.raspberrypi.org/en/projects/infrared-bird-box/13).

## Resources 
  * [Schematic](https://github.com/sbcshop/Serial_Servo_RaspberryPi_HAT_Hardware/blob/main/Design%20Data/SCH_Serial_Servo_RaspberryPi_HAT.pdf)
  * [Step File](https://github.com/sbcshop/Serial_Servo_RaspberryPi_HAT_Hardware/blob/main/Mechanical%20Data/Serial_Servo_RaspberryPi_HAT.step)
  * [Hardware Files](https://github.com/sbcshop/Serial_Servo_RaspberryPi_HAT_Hardware)
    
**Other Related :**
  * [Getting Started With Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
  * [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)


## Related Products  

  * [Serial Servo Pico HAT](https://shop.sb-components.co.uk/products/serial-servo-pico-hat?_pos=5&_sid=1178c9361&_ss=r)

    ![Serial_Servo_Pico_HAT](https://shop.sb-components.co.uk/cdn/shop/files/Artboard2_1.png?v=1718781807&width=150)
    
  * [Serial Servo Arduino Shield](https://shop.sb-components.co.uk/products/serial-servo-arduino-shield-1?_pos=4&_sid=1178c9361&_ss=r)

    ![Serial_Servo_Arduino_Shield](https://shop.sb-components.co.uk/cdn/shop/files/Artboard2_3.png?v=1718793718&width=150)

  * [Serial Servo ESP32](https://shop.sb-components.co.uk/products/serial-servo-based-on-esp32-1?_pos=1&_sid=c593a9981&_ss=r)

    ![Serial_Servo_ESP32](https://shop.sb-components.co.uk/cdn/shop/files/esp322.png?v=1718797495&width=150)
  
  * [Serial Servo Breakout](https://shop.sb-components.co.uk/products/serial-servo-breakout-1?_pos=3&_sid=5d47c0d83&_ss=r)

    ![Serial_Servo_Breakout](https://shop.sb-components.co.uk/cdn/shop/files/Artboard2.png?v=1718780131&width=150)



## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
