'''
Created on Nov 16, 2019

@author: mgazzola
'''

class AbstractOutputFormater(object):
    '''
    abstract class cleaning text coming from files
    '''


    def __init__(self, params):
        ''' Constructor '''
    
    def cleanText(self,text):
        ''' remove disturbing characters '''
        raise NotImplementedError

    def formatText(self,text):
        ''' remove disturbing characters '''
        raise NotImplementedError