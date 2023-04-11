
# import string
# import paho.mqtt.client as mqtt #import the client1
# import time
# import logging

# class MQTTClientController():
#     def __init__(self, _clientName: string):
#         self.client = mqtt.Client(_clientName)

#         self.client.connect('192.168.0.121')
#         self.client.on_connect = self.on_connect
#         self.client.on_disconnect = self.on_disconnect
#         self.client.on_connect_fail = self.on_connect_fail
#         self.client.on_message = self.on_message

#     # def Block4CheckConnection(self, waitingTime: int):
#     #     pre = time.time()
#     #     while (time.time() - pre < waitingTime):
#     #         pass
#     #     if (not self.mqttComp.connectStatus):
#     #         return False
#     #     return True

#     # The callback for when the client receives a CONNACK response from the server.
#     def on_connect(self, client, userdata, flags, rc):
#         logging.info("Connected with result code "+str(rc))
#         # print("Connected with result code "+str(rc))
#         # reconnect then subscriptions will be renewed.
#         client.subscribe("/Multiple_Machine/#")

#     def on_disconnect(self, client, userdata, rc):
#         print("Dis-Connect")
#     def on_connect_fail(self, client, userdata, rc):
#         print("Faild")

#     # The callback for when a PUBLISH message is received from the server.
#     def on_message(self, client, userdata, msg):
#         print(msg.topic+" "+str(msg.payload))


# mqttClient = MQTTClientController("ABC")

# mqttClient.client.loop_start()
# time.sleep(100)
# mqttClient.client.loop_stop()
import time
from Script.MqttController.MQTTController import MQTTClientController
from Script.Component.MQTTComp import MQTTComp
from Script.Utils import PareSystemConfig

global mqttComp
def SetupConfig(config:PareSystemConfig):
    global mqttComp
    mqttComp = MQTTComp(
        config.mqttCfg.brokerIP,
        config.mqttCfg.brokerPort,
        config.mqttCfg.mqttTopic,
        config.mqttCfg.controlTopic,
        config.mqttCfg.dataTopic,
        config.mqttCfg.timestampTopic,
        config.mqttCfg.timestampProcessTopic,
        0,
        0,
        False,
        False,
        config.mqttCfg.isTimeStamp
    )
def main():
    global mqttComp
    config = PareSystemConfig('config.cfg')
    if (not config.isHaveConfig):
        print("[MasterController]: Pareconfig error")
        exit()

    # tracemalloc.start()
    # gc.enable()
    SetupConfig(config)
    mqttController = MQTTClientController(mqttComp, 'Seg')
    mqttController.client.loop_start()
    time.sleep(1000)
    mqttController.client.loop_stop()

if __name__ == "__main__":
    main()