# Team: Pilar Luiz & John Bush 
# GitHub repo: https://github.com/john-bush/EE250FinalProject

import paho.mqtt.client as mqtt
from gpiozero import Servo
import time
import sys
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
#sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi

servo = Servo(21)


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("dreamteam/motor")
    client.message_callback_add("dreamteam/motor", on_motor)


#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_motor(client, userdata, message):
    print("Motor activated")
    s = str(message.payload, 'utf-8')
    if s == "OPEN":
        
        servo.mid()
        time.sleep(.2)
        servo.min()

        client.publish("dreamteam/motor", "CLOSE")


if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="lab.ee250io.tk", port=1883, keepalive=60)
    client.loop_start()

    while True:
        # if the read values, publish
        distance = grovepi.ultrasonicRead(7)
        client.publish("dreamteam/ultrasonicRanger", distance)
        time.sleep(1)
            

