# imports
from blinkt import set_pixel, set_brightness, show, clear
import time

# set the brightness
set_brightness(0.05)

class Point():
    """ class to encapsulate the moving pixel """
    def __init__(self, red, green, blue, position=0, direction=1):
        self.direction = direction
        self.red = red 
        self.green = green 
        self.blue = blue 
        self.position = position 

    def click(self):
        # if at end, reverse direction
        if self.position == 0 or self.position == 7:
            self.direction = self.direction * -1
        
        # increment position
        self.position = self.position + self.direction

        # set the pixel
        set_pixel(self.position, self.red, self.green, self.blue)


class Click():
    """ class to encapsulate the countdown """
    def __init__(self, epochs=10, sleep_time=0.1):
        self.listeners = []
        self.epochs = epochs
        self.sleep_time = sleep_time

    def register(self, listener):
        self.listeners.append(listener)

    def start(self):
        for i in range(self.epochs):
            # clear the old pixels
            clear()

            # increment the listening points
            for point in self.listeners:
                point.click()

            # show the pixels
            show()

            # sleep
            time.sleep(self.sleep_time)

        # clear at end of loop
        clear()
        show()

if __name__ == "__main__":
    # initialize
    click = Click(epochs=100, sleep_time=0.05)
    click.register(Point(0, 0, 255, 4, 1))
    click.register(Point(255, 0, 0, 3, -1))

    # start
    click.start()
