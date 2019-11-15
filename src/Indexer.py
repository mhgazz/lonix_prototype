'''
@author: mgazzola
main class for indexing process
'''

import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from FileDiscover import FileDiscover
from ParserProvider import ParserProvider
sys.path.insert(1, '/home/mgazzola/eclipse-workspace/lonix_prototype/src/util')
from Logger import Logger
from Properties import Properties


class Indexer(object):
    
    #change form different environments DEV | QA | PROD
    __environment = 'DEV'
    
    def __init__(self):
        pass
    
    def run(self):
        
        logger = Logger.getInstance()
        logger.logInfo('------------------------------------------')
        logger.logInfo('-- Starting indexing process      --------')
        
        props = Properties.getInstance()
        files_path = props.get(self.__environment,'files_path')
        index_path = props.get(self.__environment,'index_path')
        
        logger.logInfo('-- files path: '+ files_path )
        logger.logInfo('------------------------------------------')
        
        #discover files
        filesList = None
        files = FileDiscover()
        files.add_extension('docx')
        files.add_extension('txt')
        files.add_localtion(files_path)
        filesList = files.explore()
        
        # create an index subdir in case it not exists
        if not os.path.exists(index_path):
            os.mkdir(index_path)
        
        # define schema and get a writer for it
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True), orderno=ID(stored=True), content=TEXT)
        ix = create_in(index_path, schema)
        writer = ix.writer()
        
        # index the content
        for curfile in filesList:
            tokens = curfile.split('/');
            filetitle = tokens[len(tokens)-1]
            logger.logInfo('Indexing file: ' + filetitle)
            reader = ParserProvider.getParser(filetitle)
            filepointer = reader.openFile(curfile)
            fr = reader.readFile(filepointer)
            i = 0
            while i<fr:
                text = reader.readNextSegment(filepointer)
                if(text!=''):
                    logger.logDebug('---' + text)
                    writer.add_document(title=filetitle, path=curfile, orderno=str(i), content=text)
                i=i+1
            reader.closeFile(filepointer)
        writer.commit()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    indexer = Indexer()
    indexer.run()