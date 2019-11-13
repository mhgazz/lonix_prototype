'''
Created on Nov 1, 2019

@author: mgazzola
'''
import unittest
import logging
import logging.config

class TestLogging(unittest.TestCase):


    def test(self):
        logging.config.fileConfig(fname='logger.conf', disable_existing_loggers=False)
        
        # Get the logger specified in the file
        logger = logging.getLogger()
        logger.debug('This is a debug message')
        logger.error('This is a debug message')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()