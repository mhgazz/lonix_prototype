'''
Created on Oct 28, 2019

@author: root
'''
import unittest
from DocxFileReader import DocxFileReader

class TestTextFileReader(unittest.TestCase):

    def test(self):
        f = DocxFileReader()
        p = f.openFile('/home/mgazzola/Documents/instructivos/Archivos_Configuracion_y_Log.docx')
        fr = f.readFile(p)
        self.assertTrue(fr==14)
        i = 0
        while i<fr:
            text = f.readNextSegment(p)
            self.assertFalse(text is None)
            i=i+1
        
        
        
        #print(text)
        

if __name__ == '__main__':
    unittest.main()