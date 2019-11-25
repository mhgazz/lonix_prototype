'''
Created on Nov 16, 2019
@author: mgazzola
'''

from AbstractOutputFormater import AbstractOutputFormater
import unittest
import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
sys.path.insert(1, '/home/mgazzola/eclipse-workspace/lonix_prototype/src/util')
from Search import Search
from Logger import Logger
from termcolor import colored, cprint


class ConsoleOutputFormater(AbstractOutputFormater):
    '''
    text console format utils
    '''

    def __init__(self):
        pass
 
    def cleanText(self,text):
        spttext = text.split(" ")
        output = ""
        for w in spttext:
            if (w.endswith("\n")):
                if (len(w)>1 and w[-2]!="."):
                    w = w[0:len(w)-1]
            if (w.startswith("\n")):
                w = w[1:len(w)]
            if (w.startswith("\n\n")):
                w = w.lstrip("\n\n")
                w = "\n\r" + w
            if (w.endswith("\n\n")):
                w = w.rstrip("\n\n")
                w = w + "\n\r"
            n = w.find("\n\n")
            if (n > 0):
                w = w.replace("\n"," ")
            n = w.find("\n")
            if (n > 0 and w[n-1]!="."):
                w = w.replace("\n","")
            output = output + w + " "
        return output

    def formatText(self,text,criteria):
        spttext = text.split(" ")
        sptcriteria = criteria.lower().split(" ")
        output = ""
        l = 0
        for w in spttext:
            l = l + len(w + " ")
            
            #remark criteria word in text
            wcriteria = w.lower()
            wcriteria = wcriteria.replace(";","")
            wcriteria = wcriteria.replace(",","")
            wcriteria = wcriteria.replace(".","")
            wcriteria = wcriteria.replace(":","")
            wcriteria = wcriteria.replace("\"","")
            wcriteria = wcriteria.replace("'","")
            wcriteria = wcriteria.replace("(","")
            wcriteria = wcriteria.replace(")","")
            wcriteria = wcriteria.replace("[","")
            wcriteria = wcriteria.replace("]","")
            wcriteria = wcriteria.replace("{","")
            wcriteria = wcriteria.replace("}","")
            if (wcriteria in sptcriteria):
                w = colored(w, 'red', attrs=['reverse', 'blink'])
            
            #line length
            if (w.find("\n")>-1):
                l = 0
            if (l>75):
                w = w + "\n\r"
                l = 0
            output = output + " " + w
        return output