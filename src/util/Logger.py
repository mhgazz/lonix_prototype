'''
Created on Nov 4, 2019

@author: mgazzola
'''

import logging
import logging.config
from Properties import Properties
from telnetlib import DEBUGLEVEL

class Logger(object):
    '''
    wrapper for logger utility using Logging Module
        
    '''
    __instance = None
    __loggerUtil = None
    __environment = "DEV"
    
    @staticmethod   
    def getInstance():
        if Logger.__instance == None:
            Logger()
        return Logger.__instance
        
    
    def __init__(self):
        if Logger.__instance == None:
            #get configuration
            props = Properties.getInstance()
            glevel = props.get(self.__environment,'log_level')
            logpath = props.get(self.__environment,'log_file')
            logOutput = props.get(self.__environment,'log_output')
            lformat = '%(asctime)s - %(levelname)s - %(message)s'
            Logger.__instance = self
            logger = logging.getLogger()
            
            #file logger configuration
            logging.basicConfig(format=lformat,filename=logpath,level=glevel)
            
            #console logger config
            if (logOutput=='2'):
                ch = logging.StreamHandler()
                ch.setLevel(glevel)
                chformatter = logging.Formatter(lformat)
                ch.setFormatter(chformatter)
                logger.addHandler(ch)

            #asign instance
            Logger.__loggerUtil = logger 

            
    def logDebug(self,message):
        Logger.__loggerUtil.debug(message)
    
    def logWarning(self,message):
        Logger.__loggerUtil.warning(message)

    def logInfo(self,message):
        Logger.__loggerUtil.info(message)

    def logError(self,message):
        Logger.__loggerUtil.error(message)
    
    def logCritical(self,message):
        Logger.__loggerUtil.critial(message)