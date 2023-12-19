import paho.mqtt.client as mqtt
import time
import random

broker="broker.hivemq.com"
topic="esekku/643040666-2/temperature1"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883)

data=24

while(True):
    client.publish(topic,data)
    time.sleep(10)

