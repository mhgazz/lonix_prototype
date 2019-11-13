'''
Created on Nov 4, 2019
@author: mgazzola
application properties central
'''


import configparser

class Properties(object):

    __instance = None
    __propertiesUtil = None
    
    
    @staticmethod   
    def getInstance():
        if Properties.__instance == None:
            Properties()
        return Properties.__instance

    def __init__(self):
        if Properties.__instance == None:
            Properties.__instance = self        
            config = configparser.ConfigParser()
            config.read('/home/mgazzola/eclipse-workspace/loinx prototype/src/config/application.ini')
            Properties.__propertiesUtil = config
            
    def get(self,env,property):
        return Properties.__propertiesUtil[env][property]
        