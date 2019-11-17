'''
Created on Nov 5, 2019
@author: mgazzola
Find all files in the resource of indicated type
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

class Search(object):

    __environment = "DEV"

    def __init__(self):
        pass
    
    def performSearch(self,criteria):

        #initial configuration
        logger = Logger.getInstance()
        logger.logDebug('performing search with criteria: ' + criteria)    
        props = Properties.getInstance()
        index_path = props.get(self.__environment,'index_path')
        
        # define schema and get a writer for it
        ix = open_dir(index_path)
        
        # perform search
        searchResults = []
        i = 0
        with ix.searcher() as searcher:
            query = QueryParser("content", ix.schema).parse(criteria)
            results = searcher.search(query,limit=10)
            for result in results:
                 
                order = result['orderno']
                path = result['path']
                title = result['title']
                searchResult = SearchResult(title,path,order,criteria)
                searchResults.append(searchResult)
                i = i + 1
           
        logger.logDebug("results found: " + str(i))
        return searchResults