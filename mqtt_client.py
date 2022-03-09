from paho.mqtt import client as mqtt_client
import random
import time

#clase que tiene metodos para conectar al broker publico y mandar la informacion que se desee
class cliente:
    def __init__(self,broker='broker.hivemq.com',port=1883,topic="huber/1",client_id=f'python-mqtt-{random.randint(0, 1000)}'):
        self.broker=broker
        self.port=port
        self.topic=topic
        self.client_id=client_id
    def get_broker(self):
        return self.broker
    def get_port(self):
        return self.port
    def get_topic(self):
        return self.topic
    def get_id(self):
        return self.client_id
    def set_msg(self,msg):
        self.msg=msg
    def get_msg(self):
        return self.msg
    def connect_client(self, list):
        #msg = "prueba"
        #conectar
        client = mqtt_client.Client(self.get_id())
        client.connect(self.get_broker(), self.get_port())
        client.loop_start()
        #publicar
        for info in list:
            client.publish(self.get_topic(),str(info["coordenadas"][0][0]))
        client.loop_stop()
