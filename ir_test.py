import RPi.GPIO as IO
from time import sleep

IO.setup(14,IO.IN)

while (1):
    sleep(2)

    if (IO.input(14) == True):
        print("Far.")
    
    if (IO.input(14) == False):
        print ("Close.")

