import string
import paho.mqtt.client as mqtt #import the client1
import time
import logging
from Script.Component.MQTTComp import MQTTComp
from enum import Enum
import json
class PublishType(Enum):
    CONTROL = 1,

class MQTTClientController():
    def __init__(self, _mqttComp: MQTTComp, _clientName: string):
        self.mqttComp = _mqttComp
        self.client = mqtt.Client(_clientName)
        self.client.connect(self.mqttComp.brokerIP)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_connect_fail = self.on_connect_fail
        self.client.on_message = self.on_message

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        # logging.info("Connected with result code "+str(rc))
        print("Connected with result code "+str(rc))
        self.mqttComp.connectStatus = True
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.mqttComp.commandTopic)
        if (self.mqttComp.dataTopic):
            client.subscribe(self.mqttComp.dataTopic)

    def on_disconnect(self, client, userdata, msg):
        self.mqttComp.connectStatus = False
    
    def on_connect_fail(self, client, userdata, msg):
        self.mqttComp.connectStatus = False

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        msgContent = msg.payload.decode("utf-8")
        print(msg.topic+" "+str(msgContent))
        signalControl = {
            "steer": 10,
            "speed": 30
        }
        signalControl_J = json.dumps(signalControl, indent=4)
        self.publish_message(PublishType.CONTROL, signalControl_J)

        # if (msg.topic == self.mqttComp.timestampTopic):
        #     self.mqttComp.timestampValue = float(msgContent)

    def publish_message(self, type : PublishType, message):
        topic = "NULL"
        if (type == PublishType.CONTROL):
            topic = self.mqttComp.controlTopic
        self.client.publish(topic, message)
