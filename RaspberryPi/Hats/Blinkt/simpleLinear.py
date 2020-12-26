# imports
from blinkt import set_pixel, set_brightness, show, clear
import time

# set the brightness
set_brightness(0.1)

# methods
def side_to_side_motion(blink_number, sleep_time, pixel_number=4):
    """ will rotate light in circular motion """
    # set direction
    direction = 1

    # loop
    for i in range(blink_number):
        # set the pixel
        if pixel_number == 7 or pixel_number == 0:
            direction = direction * -1
            pixel_number = pixel_number + direction

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

def circular_motion(blink_number, sleep_time):
    """ will rotate light in circular motion """
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
side_to_side_motion(50, 0.4)
