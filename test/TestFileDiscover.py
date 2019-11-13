'''
Created on Oct 28, 2019

@author: root
'''
import unittest
from FileDiscover import FileDiscover

class TestFileDiscover(unittest.TestCase):

    def test(self):
        f = FileDiscover()
        f.add_extension('docx')
        f.add_extension('txt')
        f.add_localtion('/home/mgazzola/Documents/instructivos')
        files = f.explore()
        self.assertFalse(files is None)
        print(files)

if __name__ == '__main__':
    unittest.main()