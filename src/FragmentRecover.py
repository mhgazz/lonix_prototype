'''
Created on Nov 5, 2019
@author: mgazzola
retrieve a certain fragment of a document on demand
'''

import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
sys.path.insert(1, '/home/mgazzola/eclipse-workspace/lonix_prototype/src/util')
from Logger import Logger
from Properties import Properties
from whoosh.index import open_dir
from SearchResult import SearchResult

from Fragment import Fragment
from ParserProvider import ParserProvider



class FragmentRecover(object):

    def __init__(self):
        pass
    
    def recover(self,filepath,order):
        curFrag = self.retrieve(filepath,order)
        text = curFrag.get_text()
        i = 1
        while (len(text)<=100):
            if(int(order)-i>=0):
                curFrag = self.retrieve(filepath,int(order)-i)
                text = curFrag.get_text() + " " + text
            curFrag = self.retrieve(filepath,int(order)+i)
            text = text + " " + curFrag.get_text()
        curFrag.set_text(text)
        return curFrag
    
    def retrieve(self,filepath,order):
        #initial configs
        logger = Logger.getInstance()
        
        order = int(order)        
        tokens = filepath.split('/');
        filetitle = tokens[len(tokens)-1]
        logger.logInfo('Indexing file: ' + filetitle)
        reader = ParserProvider.getParser(filetitle)
        filepointer = reader.openFile(filepath)
        fr = reader.readFile(filepointer)
        i = 0
        fragment = Fragment('',filepath,order,'')
        while i<fr:
            text = reader.readNextSegment(filepointer)
            if(text!=''):
                if (i==order):
                    fragment.set_text(text)
            i=i+1
        return fragment