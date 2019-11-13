'''
Created on Oct 28, 2019

@author: root
'''
from ansible.module_utils.common import file

class AbstractFileReader(object):
    '''
    abstract class for file reader, needs to be implemented
    '''


    def __init__(self):
        raise NotImplementedError
        
    def openFile(self, curFile):
        '''
        implements file open
        returns file pointer
        '''
        raise NotImplementedError
        
    def readNextSegment(self, curFilePointer):
        '''
        brings the next fragment of the file
        returns a frangment object
        '''
        raise NotImplementedError
        
    def closeFile(self,curFile):
        '''
        close the file if needed
        '''
        raise NotImplementedError
    
    def readFile(self,curFile):
        '''
        red the file contents
        returns amount of fragments
        '''
        raise NotImplementedError