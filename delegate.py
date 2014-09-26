"""
"""
from PyQt4 import QtGui
from PyQt4 import QtCore
import re

class Delegate(QtGui.QStyledItemDelegate):
    """
    """
    def __init__(self, parent, core):
        QtGui.QStyledItemDelegate.__init__(self,parent)
        self.core = core


    def editItem(self, item, col):
        """
        """
        self.item=item
        self.col=col
        
        if col == 2: #type column
            self.data_check=None
            self.data=None
            
        elif col == 0: #name column
            self.data_check=item.wl.name_check
            self.data=item.wl.name
            
        elif col == 1: #value column
            self.data_check=item.wl.value_check
            self.data=item.wl.value
            
        else: #other cases
            self.data_check=None
            self.data=None
            

    def createEditor(self, parent, option, index):
        """
        """
        if self.data_check == None or self.data_check[0] == "readonly":
            return
        
        elif self.data_check[0] == "regex":
            editor = QtGui.QLineEdit(parent)
        
        elif self.data_check[0] == "select":
            editor = QtGui.QComboBox(parent)
                        
        return editor


    def setEditorData(self, editor, index):
        """
        """
        if self.data_check == None or self.data_check[0] == "readonly":
            return
        
        elif self.data_check[0] == "regex":
            text = index.model().data(index, QtCore.Qt.DisplayRole).toString()
            editor.setText(text)
            
        elif self.data_check[0] == "select":
            for item in self.data.split(','):
                editor.addItem(QtCore.QString(item))
            

    def setModelData(self, editor, model, index):
        """
        """
        dataok=False
        if self.data_check == None or self.data_check[0] == "readonly":
            return
        
        elif self.data_check[0] == "regex":
            text=editor.text()
            if re.match(self.data_check[1],text,re.IGNORECASE) != None:
                dataok=True
            
        elif self.data_check[0] == "select":
            text=editor.currentText()
            dataok=True

        if dataok == True:
            model.setData(index,QtCore.QVariant(text))


    def sizeHint(self, option, index):
        """
        """
        default = QtGui.QStyledItemDelegate.sizeHint(self, option, index)
        return QtCore.QSize(default.width(), default.height() + 6)
