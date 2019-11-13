'''
Created on Nov 5, 2019

@author: mgazzola
'''
import unittest
from FragmentRecover import FragmentRecover


class TestFragmentRecover(unittest.TestCase):


    def testName(self):
        
        fr = FragmentRecover()
        fgm = fr.retrieve('/home/mgazzola/Documents/instructivos/was/aprovisionamiento.proxy.prod/Creacion Websphere Proxy Server.docx', 110)
        self.assertTrue(fgm.get_text())
        print(fgm.get_source_file())
        print(fgm.get_order())
        print(fgm.get_text())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()