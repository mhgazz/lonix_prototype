'''
Created on Nov 4, 2019

@author: mgazzola
'''
import unittest
from Indexer import Indexer

class TestIndexer(unittest.TestCase):


    def testName(self):
        indexer = Indexer()
        indexer.run()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()