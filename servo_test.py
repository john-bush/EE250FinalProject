from gpiozero import Servo
from time import sleep

servo = Servo(18)

while True:
    servo.min()
    sleep(2)
    servo.mid()
    sleep(.1)