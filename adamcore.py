from PyQt4 import QtGui
from whitelist import Whitelist
 
class AdamCore(): 
    def __init__(self):
        print "AdamCore()"
        self.tree = QtGui.QTreeWidgetItem()

    def openAdaption(self, filename):
        print "openAdapation()"
        
    def closeAdaption(self):
        print "closeAdapation()"
        self.tree=QtGui.QTreeWidgetItem([])

    def saveAdaption(self,filename):
        print "saveAdaption()"

    def getTree(self):
        #self.tree.addChild()
        #self.tree = QtGui.QTreeWidgetItem(["root"])
        #A = QtGui.QTreeWidgetItem(self.tree, ["A"])
        #QtGui.QTreeWidgetItem(A, ["bar"])
        #bazA = QtGui.QTreeWidgetItem(A, ["baz", "a", "b"])
        #QtGui.QTreeWidgetItem(bazA, ["blub"])
        
        self.tree = QtGui.QTreeWidgetItem(["root"])
        
        for mandatory in enumerate(self.whitelist.getMandatoryChilds("root")):
            print mandatory
            QtGui.QTreeWidgetItem(self.tree,mandatory)
            
        for optional in enumerate(self.whitelist.getOptionalChilds("root")):
            print optional
            QtGui.QTreeWidgetItem(self.tree,optional)
        
        return self.tree
    
 
    def openWhitelist(self, filename):
        self.whitelist = Whitelist(filename)