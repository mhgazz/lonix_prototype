'''
Created on Nov 5, 2019

@author: mgazzola
'''
import unittest
from Search import Search

class TestSearch(unittest.TestCase):


    def testInitial(self):
        search = Search()
        results = search.performSearch('terrible')
        self.assertTrue(len(results)>0)
        self.assertTrue(len(results)==1)
        for result in results:
            print(result.get_title())
        
        results = search.performSearch('parrafa')
        self.assertTrue(len(results)>0)
        self.assertTrue(len(results)==4)
        for result in results:
            print(result.get_title())
        
        
    def testComplex(self):
        search = Search()
        results = search.performSearch('WAS iSeries')
        print(len(results))
        #self.assertTrue(len(results)>0)
        #self.assertTrue(len(results)==1)
        for result in results:
            print(result.get_title())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()