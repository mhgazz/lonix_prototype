'''
Created on Oct 28, 2019

@author: root
'''
import unittest
from TextFileReader import TextFileReader

class TestTextFileReader(unittest.TestCase):

    def test(self):
        f = TextFileReader()
        p = f.openFile('/home/mgazzola/Documents/instructivos/TIPS-BROKER-MQ.txt')
        fr = f.readFile(p)
        text = f.readNextSegment(p)
        i=0
        while(i<fr):
            text = f.readNextSegment(p)
            i=i+1
        self.assertTrue(fr==546)
        self.assertTrue(text!="")
        #print(text)
        

if __name__ == '__main__':
    unittest.main()