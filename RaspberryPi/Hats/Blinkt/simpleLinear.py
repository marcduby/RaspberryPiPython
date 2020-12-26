# imports
from blinkt import set_pixel, set_brightness, show, clear
import time

def side_to_side(blink_number, sleep_time):
    for i in range(blink_number):
        # set the pixel
        pixel_number = i % 8

        # set the colors
        red = i * 10
        blue = 255 - red
        green = 0

        # clear the old pixel
        clear()

        # set the new pixel
        set_pixel(pixel_number, red, green, blue)
        show() 

        # sleep
        time.sleep(sleep_time)

    # clear at the end of the loop
    clear()
    show()

# call the function
side_to_side(50, 0.2)
