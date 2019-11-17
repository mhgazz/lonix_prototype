'''
Created on Nov 15, 2019

@author: mgazzola
'''
from AbstractFileReader import AbstractFileReader
import PyPDF2

class PdfFileReader(AbstractFileReader):
    '''
    implementation for PDF files
    '''

    i = 0

    def __init__(self):
        '''
        Constructor
        '''
    
    def openFile(self, curFile):
        pdfFileObj = open(curFile, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        return pdfReader
        
    def readNextSegment(self, fp):
        pageObj = fp.getPage(self.i)
        self.i = self.i + 1
        return pageObj.extractText()
    
    def readCertSegment(self, fp, order):
        pageObj = fp.getPage(order)
        return pageObj.extractText()
    
    def closeFile(self,curFile):
        curFile = None
        
    def readFile(self,fp):
        return fp.numPages
        