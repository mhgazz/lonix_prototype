'''
Created on Oct 28, 2019

@author: root
'''
import unittest
from Fragment import Fragment

class TestFragment(unittest.TestCase):

    def test(self):
        f = Fragment("test", "/home/mgazzola/test.txt", 1, "test")
        self.assertEqual("test", f.get_text(), "OK")
        

if __name__ == '__main__':
    unittest.main()