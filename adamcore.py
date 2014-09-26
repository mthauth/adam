"""
"""
from PyQt4 import QtGui
from whitelist import Whitelist
 
class AdamCore():
    """
    """
    def __init__(self):
        """
        """
        self.whitelist = None

   
    def openAdaption(self, filename):
        """
        """
        
        
    def closeAdaption(self):
        print "closeAdapation()"
        self.tree=QtGui.QTreeWidgetItem([])


    def saveAdaption(self,filename):
        print "saveAdaption()"    

 
    def openWhitelist(self, filename):
        """
        """
        self.whitelist = Whitelist(filename)

