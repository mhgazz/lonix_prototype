'''
Created on Oct 28, 2019

@author: mgazzola
represents a fragment of a file
'''

class Fragment(object):


    text=''
    sourceFile=''
    order=0
    tags=''

    def __init__(self,text,sourceFile,order,tags):
        self.text=text
        self.sourceFile=sourceFile
        self.order=order
        self.tags=tags

    def get_text(self):
        return self.text


    def get_source_file(self):
        return self.sourceFile


    def get_order(self):
        return self.order


    def get_tags(self):
        return self.tags


    def set_text(self, value):
        self.text = value


    def set_source_file(self, value):
        self.sourceFile = value


    def set_order(self, value):
        self.order = value


    def set_tags(self, value):
        self.tags = value


    def del_text(self):
        del self.text


    def del_source_file(self):
        del self.sourceFile


    def del_order(self):
        del self.order


    def del_tags(self):
        del self.tags
    
    
    
    
    
        