import os
import sys
sys.path.append("examples/lib")

from PIL import Image, ImageDraw, ImageFont
from lib import display_1inch14
import time

# Set up the font paths
font1 = ImageFont.truetype("font/Font00.ttf", 25)
font2 = ImageFont.truetype("font/Font00.ttf", 16)
font3 = ImageFont.truetype("font/Font02.ttf", 25)

# Initialize the LCD display
disp = display_1inch14.lcd_display()
disp.Init()

# Create a new image with white background
image = Image.new("RGB", (disp.width, disp.height), "BLACK")

# Draw some text on the image
draw = ImageDraw.Draw(image)
draw.text((10, 5), "Hello, World!", font=font1, fill="BLUE")
draw.text((10, 60), "Serial Servo HAT", font=font1, fill="YELLOW")

# Display the image on the LCD
disp.ShowImage(image)

# Wait for a while to keep the message on the screen
time.sleep(5)

# Clear the display
disp.clear()
