from paho.mqtt import client as mqtt_client
import random

broker = 'broker.hivemq.com'
port = 1883
topic = "steph/1"

client_id = f'python-mqtt-{random.randint(0, 1000)}'

client = mqtt_client.Client(client_id)
client.connect(broker, port)

