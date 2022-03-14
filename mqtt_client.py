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
        prom=0
        prom1=0
        prom2=0
        prom3=0
        for info in list:

            #Info viene de camara aruco
            for i in range (1000):
                prom+=info["coordenadas"][0][0]
                prom1+=info["coordenadas"][0][1]
                prom2+=info["coordenadas"][1][0]
                prom3+=info["coordenadas"][1][1]

            prom=prom/1000
            prom1=prom/1000
            prom2=prom/1000
            prom3=prom/1000
           
            prom= round(prom,2)
            prom1= round(prom1,2)
            prom2= round(prom2,2)
            prom3= round(prom3,2)

            client.publish(self.get_topic(),"Coordenada x1: " + str(prom) + " Coordenada y1: " + str(prom1) + "Coordenada x2: " + str(prom2) + "Coordenada y2: " + str(prom3))

            #client.publish(self.get_topic(),"hola")
        client.loop_stop()
