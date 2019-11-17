'''
Created on Nov 4, 2019

@author: mgazzola
'''
from AbstractFileReader import AbstractFileReader
from DocxFileReader import DocxFileReader
from TextFileReader import TextFileReader
from PdfFileReader import PdfFileReader


class ParserProvider(object):

    def __init__(self, params):
        pass 

        
    @staticmethod
    def getParser(curfile):
        afr = None
        tokens = curfile.split('/');
        filename = tokens[-1]
        tokens = filename.split('.');
        filext = tokens[-1]
        
        
        if (filext.upper()=="DOCX"):
            afr = DocxFileReader()
        elif (filext.upper()=="TXT"):
            afr = TextFileReader()
        elif (filext.upper()=="PDF"):
            afr = PdfFileReader()
        else:
            Exception('spam', 'eggs')
        
        return afr