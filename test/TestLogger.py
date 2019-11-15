'''
Created on Nov 4, 2019

@author: mgazzola
'''
import unittest
import sys
sys.path.insert(1, '/home/mgazzola/eclipse-workspace/lonix_prototype/src/util')
from Logger import Logger


class Test(unittest.TestCase):


    def testInstance(self):
        l = Logger.getInstance()
        print(l)
        a = Logger.getInstance()
        print(a)
        self.assertTrue(str(l)==str(a))
        
    def testLogMethods(self):
        l = Logger.getInstance()
        print(l)
        l.logDebug("jerousia")
        l.logError("chatuma")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()