
# imports
from gpiozero import MotionSensor
import time
import datetime

def get_time():
    """ returns the current time with format """
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return time_str

# assign the sensor
sensor = MotionSensor(26)
sleep_time = 2
counter = 0

# log
print("starting motion sensor checking")

# infinite loop to keep sensor going
while True:
    # log sleep
    print("sleeping for {}".format(sleep_time))

    # sleep
    time.sleep(sleep_time)
    counter = counter + 1

    # log
    print("{} - sensor awake".format(counter))
    
    # trigger the sensor
    sensor.wait_for_motion()

    # print when triggered
    print("{} - got motion\n".format(get_time()))

