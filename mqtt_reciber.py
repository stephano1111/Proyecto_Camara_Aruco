import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("huber/2")

def on_message(client, userdata, msg):
  print(msg.topic + " " + str(msg.payload))
    
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

