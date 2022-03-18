import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url
    @staticmethod
    def getName():
        name = config.get('common info', 'username')
        return name

    @staticmethod
    def getUseremail():
        useremail = config.get('common info', 'useremail')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
