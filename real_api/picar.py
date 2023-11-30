import sys
from real_api.helper_files import PCA9685

class picar:
    def setup():
        pwm=PCA9685.PWM(bus_number=1)
        pwm.setup()
        pwm.frequency = 60
