from PyQt4 import QtGui
from PyQt4 import QtCore
import re

class Delegate(QtGui.QStyledItemDelegate):
    def __init__(self, parent, core):
        QtGui.QStyledItemDelegate.__init__(self,parent)
        self.core = core


    def editItem(self, item, col):
        print "editItem()"
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

        
    def sizeHint(self, option, index):
        print "sizeHint()"
        default = QtGui.QStyledItemDelegate.sizeHint(self, option, index)
        return QtCore.QSize(default.width(), default.height() + 6)


    def createEditor(self, parent, option, index):
        print "createEditor()"

        if self.data_check == None or self.data_check[0] == "readonly":
            return
        
        elif self.data_check[0] == "regex":
            editor = QtGui.QLineEdit(parent)
        
        elif self.data_check[0] == "select":
            editor = QtGui.QComboBox(parent)
                        
        return editor


    def setEditorData(self, editor, index):
        print "setEditorData()"
        
        if self.data_check == None or self.data_check[0] == "readonly":
            return
        
        elif self.data_check[0] == "regex":
            text = index.model().data(index, QtCore.Qt.DisplayRole).toString()
            editor.setText(text)
            
        elif self.data_check[0] == "select":
            for item in self.data.split(','):
                editor.addItem(QtCore.QString(item))
            

    def setModelData(self, editor, model, index):
        print "setModelData()"
        
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
        
        
#        if self.coll == 0:
#            is_option = False
#            section_name = self.item.get_section()
#            for condition in self.whitelist.conditions:
#                cond = condition.get_section()
#                if cond == section_name:
#                    is_option = True
#            if not is_option:
#                regex = self.check_node_name(editor.text())
#                self.item.setText(1, "")
#            else:
#                regex = None
#        else:
#            regex = self.check_text(editor.text())
#            if regex != None:
#                regex = True
#        if regex:
#            model.setData(index, QtCore.QVariant(editor.text()))
#        self.item = None
 
#    def check_node_name(self, text):
#        truth = False
#        self.path += text
#        for option in self.whitelist.options:
#                opt = option.get_parameter()
#                regex = re.match(opt, self.path, re.IGNORECASE)
#                if regex != None:
#                    truth = True
#        return truth

#    def check_text(self, text):
#        item_name = self.item.text(0)
#        for cond in self.whitelist.conditions:
#            cond_name = cond.get_name()
#            if item_name == cond_name:
#                condition = cond.get_value()
#                regex = re.match( condition, text, re.IGNORECASE )
#                return regex
#        return None

