'''
Created on Oct 28, 2019

@author: root
'''
from AbstractFileReader import AbstractFileReader

class TextFileReader(AbstractFileReader):
    '''
    implementation for txt plain file
    '''
    paragraphs = []
    i = 0
    t = 0

    def __init__(self):
        '''
        Constructor
        '''
    
    def openFile(self, curFile):
        fp = open(curFile,'r', encoding="latin-1")
        text = fp.readline()
        self.t = 0
        while (text):
            self.paragraphs.append(text)
            self.t = self.t + 1
            text = fp.readline()
        return fp
        
    def readNextSegment(self, fp):
        text = self.paragraphs[self.i]
        self.i = self.i + 1
        return text

    def readCertSegment(self, fp, order):
        text = self.paragraphs[order]
        return text    
    
    def closeFile(self,curFile):
        curFile.close()
        
    def readFile(self,curFile):
        return self.t-1
        