"""
"""
from PyQt4 import QtGui,QtCore


class TreeItem(QtGui.QTreeWidgetItem):
    """
    represents a single treewidget item 
    """
    def __init__(self, parent, grammardata):
        self.grammar = grammardata
        it0=str(self.grammar.name)
        it1=str(self.grammar.value)
        it2=str(self.grammar.type)
        
        cols=[it0,it1,it2]
        
        QtGui.QTreeWidgetItem.__init__(self, parent, cols)
        self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)
