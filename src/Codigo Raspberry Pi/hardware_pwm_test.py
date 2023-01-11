"""import pigpio

pi = pigpio.pi()


pi.hardware_PWM(12, 50, 50000)
pi.hardware_PWM(13, 50, 100000)"""

from servo_control import Servo
import numpy as np
import time

servo_x = Servo(12)
servo_y = Servo(13)

servo_x.value(-0.15)
servo_y.value(0.1)


"""
arr = np.linspace(-1.0, 1.0, 201)

servo_x.value(-0.15)

while True:
    
    for it in arr:
        servo_y.value(it)
        time.sleep(0.005)
        
    for it in arr[::-1]:
        servo_y.value(it)
        time.sleep(0.02)
"""
