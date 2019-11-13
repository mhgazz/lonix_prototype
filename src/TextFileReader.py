'''
Created on Oct 28, 2019

@author: root
'''
from AbstractFileReader import AbstractFileReader

class TextFileReader(AbstractFileReader):
    '''
    implementation for txt plain file
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def openFile(self, curFile):
        fp = open(curFile,'r', encoding="latin-1")
        return fp
        
    def readNextSegment(self, fp):
        text = fp.read()
        return text
    
    def closeFile(self,curFile):
        ''' # '''
        pass
        
    def readFile(self,curFile):
        return 1
        