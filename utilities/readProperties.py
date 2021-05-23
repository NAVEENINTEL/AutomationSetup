import configparser

config=configparser.RawConfigParser()
configFilePath=r'config.ini'
config.read(configFilePath)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        url = config.get('common info', 'username')
        return url

    @staticmethod
    def getPassword():
        url = config.get('common info', 'password')
        return url

