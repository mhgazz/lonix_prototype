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
            if (w.startswith("\n\n")):
                w = w.lstrip("\n\n")
                w = "\n\r" + w
            if (w.endswith("\n\n")):
                w = w.rstrip("\n\n")
                w = w + "\n\r"
            output = output + w + " "
        return output

    def formatText(self,text,criteria):
        spttext = text.split(" ")
        sptcriteria = criteria.lower().split(" ")
        output = ""
        l = 0
        for w in spttext:
            l = l + len(w + " ")
            if (w.lower() in sptcriteria):
                w = colored(w, 'red', attrs=['reverse', 'blink'])
            output = output + " " + w
        return output