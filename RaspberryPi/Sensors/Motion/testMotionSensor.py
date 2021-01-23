
# imports
from pgiozero import MotionSensor
import time

# assign the sensor
sensor = MotionSensor(26)

# infinite loop to keep sensor going
while True:
    # log
    print("starting motion sensor checking")

    # sleep
    time.sleep(5)

    # trigger the sensor
    sensor.wait_for_motion()

    # print when triggered
    print("got motion\n")

