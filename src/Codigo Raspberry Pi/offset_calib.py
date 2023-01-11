from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servo_x = Servo(13, pin_factory=factory)
servo_y = Servo(12, pin_factory=factory)

offset_x = 0.05
offset_y = -0.05

servo_x.value = offset_x
servo_y.value = offset_y
