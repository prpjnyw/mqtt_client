import paho.mqtt.client as mqtt


broker="broker.hivemq.com"
topic="esekku/643040666-2/temperature"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)



# Keep the script running
while(True):
    client.publish(topic, 11)
