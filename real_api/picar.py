import sys
from real_api.front_wheels import *
from real_api.back_wheels import *
from real_api.helper_files.Servo import *
from real_api.helper_files.PCF8591 import *
from real_api.helper_files.PCA9685 import *

class picar:
    def setup():
        pwm=PCA9685.PWM(bus_number=1)
        pwm.setup()
        pwm.frequency = 60
