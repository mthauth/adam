"""
"""
from PyQt4 import QtGui
from grammar import Grammar
 
class AdamCore():
    """
    """
    def __init__(self):
        """
        """
        self.grammar = None

   
    def openAdaption(self, filename):
        """
        """
        
        
    def closeAdaption(self):
        print "closeAdapation()"
        self.tree=QtGui.QTreeWidgetItem([])


    def saveAdaption(self,filename):
        print "saveAdaption()"    

 
    def openGrammar(self, filename):
        """
        """
        self.grammar = Grammar(filename)

