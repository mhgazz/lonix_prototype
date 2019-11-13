'''
Created on Nov 6, 2019

@author: mgazzola
'''
import unittest
from Indexer import Indexer
from FragmentRecover import FragmentRecover
from Search import Search

class TestIntegration(unittest.TestCase):


    def test(self):
        # run indexing process
        #indexer = Indexer()
        #indexer.run()
        #print("index completed")
        
        #perform search
        search = Search()
        results = search.performSearch('WAS iSeries')
        print('hists: ' + str(len(results)))
        self.assertTrue(len(results))

        #recover fragments
        fr = FragmentRecover()
        for result in results:
            print(result)
            fgm = fr.retrieve(result.get_path(), result.get_order() )
            print(fgm.get_source_file())
            print(fgm.get_order())
            print(fgm.get_text())
            self.assertTrue(fgm.get_text())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()