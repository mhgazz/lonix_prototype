'''
Created on Nov 4, 2019

@author: mgazzola
'''
import unittest
import sys
sys.path.insert(1, '/home/mgazzola/eclipse-workspace/loinx prototype/src/util')
from Properties import Properties

class TestProperties(unittest.TestCase):


    def test(self):
        props = Properties.getInstance()
        host2 = props.get('QA','host')
        print(host2)
        host1 = props.get('DEV','host')
        print(host1)
        self.assertEqual(host1, host2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()