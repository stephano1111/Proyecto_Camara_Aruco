from paho.mqtt import client as mqtt_client
import random


broker = 'broker.hivemq.com'
port = 1883
topic = "huber/1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
msg = "44444"

#conectar
client = mqtt_client.Client(client_id)
client.connect(broker, port)
client.loop_start()

#publicar
client.publish(topic, msg)

print("queeeee)")
