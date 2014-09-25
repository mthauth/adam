from PyQt4 import QtGui,QtCore


class TreeItem(QtGui.QTreeWidgetItem):
    def __init__(self, parent, whitelistdata):

        self.wl = whitelistdata
        it0=str(self.wl.name)
        it1=str(self.wl.value)
        it2=str(self.wl.type)
        
        cols=[it0,it1,it2]
        
        QtGui.QTreeWidgetItem.__init__(self, parent, cols)
        self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)
        
