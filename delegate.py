"""
provides display and editing facility for ADaM tree item
"""
from PyQt4 import QtGui,QtCore
import re

class Delegate(QtGui.QStyledItemDelegate):
    """
    delegation class for editing facility on TreeItem based on QtGui.QStyledItemDelegate
    """
    def __init__(self, parent):
        QtGui.QStyledItemDelegate.__init__(self,parent)
        self.core = parent.core


    def editItem(self, item, col):
        """
        slot for editing a given column on a given tree item
        - set data to be edited depending on item and column
        """

        if col == 2: #type column
            self.data_check=None
            self.data=None

        elif col == 0: #name column
            self.data_check=item.grammar.name_check
            self.data=item.grammar.name

        elif col == 1: #value column
            self.data_check=item.grammar.value_check
            self.data=item.grammar.value

        else: #other cases
            self.data_check=None
            self.data=None


    def createEditor(self, parent, option, index):
        """
        setup editor depending on data check
        - in case of data_check, says
          - regex: QLineEdit
          - select: QComboBox
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
        setting the editor data depending on data check
        - in case of data_check, says
          - regex: write current text to editor
          - select: split string to array and attach each element to list
        """
        if self.data_check == None or self.data_check[0] == "readonly":
            return

        elif self.data_check[0] == "regex":
            text = index.model().data(index, QtCore.Qt.DisplayRole).toString()
            editor.setText(text)

        elif self.data_check[0] == "select":
            for item in self.data_check[1].split(','):
                editor.addItem(QtCore.QString(item))


    def setModelData(self, editor, model, index):
        """
        check edited data and set it to item col
        in case of data_check
        - regex: verify content vs given regular expression
        - select: take content and set it
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
        optimize column size to new content
        """
        default = QtGui.QStyledItemDelegate.sizeHint(self, option, index)
        return QtCore.QSize(default.width(), default.height() + 6)
