'''
Created on Oct 29, 2019

@author: root
Find all files in the resource of indicated type
'''


import os

class FileDiscover(object):

    locations = []
    extensions = []

    def __init__(self):
        '''
        Constructor
        '''
    
    def explore(self):
        files = []
        # r=root, d=directories, f = files
        for path in self.locations:
            for r, d, f in os.walk(path):
                for file in f:
                    curExtension = file.split('.')[-1] 
                    if curExtension in self.extensions:
                        files.append(os.path.join(r, file))
        
        return files
        
    
    def add_localtion(self,location):
        self.locations.append(location)
        
    def add_extension(self,extension):
        self.extensions.append(extension)
        
    