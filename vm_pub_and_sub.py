# Team: Pilar Luiz & John Bush
# GitHub repo: https://github.com/john-bush/EE250FinalProject

from sys import pycache_prefix
import paho.mqtt.client as mqtt
import time

# Variable to keep track of if the bird has left not is remaining in range of sensor. 
# Don't want to continuously distirbute food to a bird until it leaves and returns. 
bird_waiting = False

# Detection Distance
threshold = 10

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("dreamteam/ultrasonicRanger")
    client.message_callback_add("dreamteam/ultrasonicRanger", on_ultrasonic)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_ultrasonic(client, userdata, message):
    print("VM: " + str(message.payload, 'utf-8') + "cm")
    print("Distance: " + int(message.payload))
    global bird_waiting
    if int(message.payload) < threshold and bird_waiting is False:
        # Feed the bird
        bird_waiting = True
        client.publish("dreamteam/motor", "OPEN")
    elif int(message.payload) >= threshold:
        bird_waiting = False


if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="lab.ee250io.tk", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
            

