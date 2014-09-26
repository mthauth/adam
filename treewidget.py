"""
provides classes for visualize and interact a treewidget
- show widget
- control and show context menu
- interactive add / edit tree widget items
- expands / collaps items
"""

from PyQt4 import QtGui,QtCore
from delegate import Delegate
from contextmenu import ContextMenu
import functools

class TreeWidget(QtGui.QTreeWidget):
    """
    provides tree widget derived from QtGui.QTreeWidget
    """
    def __init__(self, core, parent=None):
        QtGui.QTreeWidget.__init__(self, parent)
        self.core = core

        self.setupUi()


    def setupUi(self):
        """
        setup the ui of widget
        - three columns (two visible, one invisible)
        - connect double-click event with edit item function
        """

        self.ready=False
        self.header().setHidden(True)
        self.setColumnCount(3)
        self.headerItem().setText(0, "name")
        self.headerItem().setText(1, "value")
        self.headerItem().setText(2, "type")
        self.setColumnHidden(2,True)
        self.setExpandsOnDoubleClick(False)

        self.delegate = Delegate(self)
        self.setItemDelegate(self.delegate)
        self.itemDoubleClicked.connect(functools.partial(self.delegate.editItem))


    def setupTree(self):
        """
        setting up the root of tree
        - add root childs to tree
        - set widget readiness flag to true
        """
        self.addItems(self,self.core.grammar.getMandatoryChilds('root'))
        self.ready=True


    def addItem(self, parent, type_):
        """
        add a single tree item type (child) (and its mandatory childs) to selected tree item (parent)
        - create new tree item of one type (child)
        - append it to tree item (parent)
        - get mandatory item types of child
        - recursivly append mandatory childs
        - expand new items and resize column to fit them all
        """
        grammaritem=self.core.grammar.getItem(type_)
        item=TreeItem(parent, grammaritem)
        self.expandItem(item)

        mandatory=self.core.grammar.getMandatoryChilds(type_)
        if mandatory != None:
            self.addItems(item,mandatory)

        self.resizeColumnToContents(0)


    def addItems(self,parent,types_):
        """
        add a number of tree items, like addItem (for tree setup and automatic)
        - add multiple number of new items of item types (siblings) to tree one item (parent)
        - mostly for coded adding
        """
        for type_ in types_:
            self.addItem(parent,type_)


    def contextMenuEvent(self, event):
        """
        show ContextMenu and let it handle the event
        - create new context menu
        - direct event to context menu
        """
        ContextMenu(self,self.core).handleEvent(event)


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
