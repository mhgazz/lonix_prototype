'''
Created on Nov 16, 2019

@author: mgazzola
'''

from AbstractOutputFormater import AbstractOutputFormater

class ConsoleOutputFormater(AbstractOutputFormater):
    '''
    text console format utils
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
 
    def cleanText(self,text,criteria):
        spttext = text.split(" ")
        sptcriteria = criteria.lower().split(" ")
        l = 0
        for w in spttext:
            if (w.startswith("\n\n")):
                w = w.lstrip("\n\n")
                w = "\n\r" + w
            if (w.endswith("\n\n")):
                w = w.rstrip("\n\n")
                w = w + "\n\r"
            l = l + len(w + " ")
            if (w.lower() in sptcriteria):
                w = colored(w, 'red', attrs=['reverse', 'blink'])
            sys.stdout.write(w)
            sys.stdout.write(" ")
            sys.stdout.flush()
        

    def formatText(self,text):
        ''' remove disturbing characters '''
        raise NotImplementedError