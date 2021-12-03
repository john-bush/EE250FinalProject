import RPi.GPIO as IO
from time import sleep

P_IR = 11

IO.setmode(IO.BOARD)
IO.setup(P_IR,IO.IN)

while (1):
    sleep(2)

    if (IO.input(P_IR) == True):
        print(str(IO.input(P_IR)))
    
    if (IO.input(P_IR) == False):
        print (str(IO.input(P_IR)))

