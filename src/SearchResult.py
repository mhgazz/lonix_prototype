'''
Created on Nov 5, 2019
@author: mgazzola

Represents an atomic result of a search 
'''

class SearchResult(object):

    title=''
    path=''
    order=''
    query=''

    def get_title(self):
        return self.__title


    def get_path(self):
        return self.__path


    def get_order(self):
        return self.__order


    def get_query(self):
        return self.__query


    def set_title(self, value):
        self.__title = value


    def set_path(self, value):
        self.__path = value


    def set_order(self, value):
        self.__order = value


    def set_query(self, value):
        self.__query = value


    def del_title(self):
        del self.__title


    def del_path(self):
        del self.__path


    def del_order(self):
        del self.__order


    def del_query(self):
        del self.__query


    def __init__(self, title, path, order, query):
        self.title = title
        self.path = path
        self.order = order
        self.query = query
    
    title = property(get_title, set_title, del_title, "title's docstring")
    path = property(get_path, set_path, del_path, "path's docstring")
    order = property(get_order, set_order, del_order, "order's docstring")
    query = property(get_query, set_query, del_query, "query's docstring")

        