import configparser

class MQTTConfig():
    def __init__(self, configSession):
        self.error = False
        try:
            if 'brokerIP' in configSession:
                self.brokerIP = configSession['brokerIP']
            if 'brokerPort' in configSession:
                self.brokerPort = configSession['brokerPort']
            if 'mqttTopic' in configSession:
                self.mqttTopic = configSession['mqttTopic']
            if 'controlTopic' in configSession:
                self.controlTopic = configSession['controlTopic']
            if 'dataTopic' in configSession:
                self.dataTopic = configSession['dataTopic']
            if 'timestampTopic' in configSession:
                self.timestampTopic = configSession['timestampTopic']
            if 'timestampProcessTopic' in configSession:
                self.timestampProcessTopic = configSession['timestampProcessTopic']
            if 'isTimeStamp' in configSession:
                if (int(configSession['isTimeStamp']) == 1):
                    self.isTimeStamp = True
                else:
                    self.isTimeStamp = False
            if 'processTime' in configSession:
                if (int(configSession['processTime']) == 1):
                    self.processTime = True
                else:
                    self.processTime = False

        except Exception as e:
            self.error = True
            print("[MQTTConfig] Error")


class PareSystemConfig():
    def __init__(self, configPath):
        self._config = configparser.ConfigParser()
        self._config.read(configPath)
        self.isHaveConfig = True
        self.mqttCfg = []
        
        if (self._config == []):
            self.isHaveConfig = False
        
        try:
            self.mqttCfg = MQTTConfig(self._config['mqtt'])
            if (
                self.mqttCfg.error
                ):
                self.isHaveConfig = False
        except Exception as e:
            self.isHaveConfig = False
            print("[Config] Error when pare config")
