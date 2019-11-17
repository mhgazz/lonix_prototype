'''
Created on Nov 6, 2019

@author: mgazzola
command line client
'''


import unittest
import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser

sys.path.insert(1, '/home/mgazzola/eclipse-workspace/lonix_prototype/src/util')
sys.path.insert(1, '/home/mgazzola/eclipse-workspace/lonix_prototype/src/')
from FragmentRecover import FragmentRecover
from Search import Search
from Logger import Logger
from Properties import Properties
from termcolor import colored, cprint


class LoinxCLI(unittest.TestCase):


    @staticmethod
    def run():

        logger=Logger.getInstance()
        logger.logInfo(' --------- Initiating CLI ----------')
        
        print('============================Local Indexer===============================')
        print('\r\n')
        ac = 'n'
        while(ac.upper()=='N'):
            print('\r\n')
            criteria = input("ingrese criterio de busqueda :")
            logger.logInfo('criteria: ' + criteria)
            
            #perform search
            search = Search()
            results = search.performSearch(criteria)
            ac='o'
            
            while(ac.upper()=='O'):
                print('hists: ' + str(len(results)))
                print('criterio: ' + criteria)
                logger.logInfo('hists: ' + str(len(results)))
        
                #recover fragments
                fr = FragmentRecover()
                i = 0
                for result in results:
                    print(str(i) + " | " + result.get_title())
                    i = i + 1 
                if (i==0):
                    print("No se hallaron resultados")
                    ac="N"
                    break
                print("-----------------")
        
        
                print("\n\r")
                print("\n\r")
                
                #result input and validation
                fg=""
                while (fg=="" or int(fg)>=i):
                    fg = input("seleccione resultado: ")
                    try:
                        int(fg)
                    except ValueError:
                        fg=""
       
                print("\n\r")
                print("\n\r")
                print('========================================================================')
                fgm = fr.recover(results[int(fg)].get_path(), results[int(fg)].get_order())
                print(fg + " | " + results[int(fg)].get_title())
                print('fragmento ' + str(fgm.get_order()) + '   extension chars: ' + str(len(fgm.get_text())))
                print('------------------------------------------------------------------------')
                print(LoinxCLI.format_text(fgm.get_text(),criteria))
                print('------------------------------------------------------------------------')
                print('ver (o)tro resultado  (t)exto completo  (n)ueva busqueda  (f)inalizar ')
                print('========================================================================')

                ac=""
                while(ac.upper() not in ['O','T','N','F']):
                    ac = input()
                
                if (ac.upper()=='T'):
                    LoinxCLI.openFile(results[int(fg)].get_path())
                    ac='o'

    
    # give format for the output, carriage return, color
    @staticmethod
    def format_text(text,criteria):
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
    
    
    @staticmethod
    def openFile(curfile):
        tokens = curfile.split('/');
        filename = tokens[-1]
        tokens = filename.split('.');
        filext = tokens[-1]
        
        if (filext.upper()=="DOCX"):
            os.system('soffice \"' + curfile + '\" &')
        elif (filext.upper()=="TXT"):
            os.system('gedit \"' + curfile + '\" &')
        elif (filext.upper()=="PDF"):
            os.system('evince \"' + curfile + '\" &')
        else:
            Exception('spam', 'eggs')




if __name__ == "__main__":
    print('\r\n')
    print('\r\n')
    LoinxCLI.run()