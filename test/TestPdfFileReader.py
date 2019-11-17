'''
Created on Oct 28, 2019

@author: root
'''
import unittest
from PdfFileReader import PdfFileReader

class TestPdfFileReader(unittest.TestCase):

    def test(self):
        f = PdfFileReader()
        p = f.openFile('/home/mgazzola/Documents/instructivos/WebSphere MQ Primer.pdf')
        fr = f.readFile(p)
        print(fr)
        self.assertTrue(fr==64)
        i = 0
        text = ""
        while i<fr:
            text = f.readNextSegment(p)
            self.assertFalse(text is None)
            i=i+1
            print(text)
        

if __name__ == '__main__':
    unittest.main()