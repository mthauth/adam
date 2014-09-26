"""
provides classes for visualize and interact a Context Menu
- show menu widget
- control and show context menu
- offering allowed adding options
"""

from PyQt4 import QtGui
import functools

class ContextMenu(QtGui.QMenu):
    """
    provides context menu derived from QtGui.QMenu
    - setup context menu 
    - setup actions depending on context
    - submenu "add" actions in context to depending tree item type 
    """
    def __init__(self, parent, core):
        QtGui.QMenu.__init__(self, parent)
        self.parent=parent
        self.core=core
        self.pos=None
        self.addmenu=None
        

    def handleEvent(self, event):
        """
        handles the context menu event
        - consider widget is in an ready state
        - identify item of calling tree widget
        - setups menu
        - show menu
        """        
        self.pos=None
        if self.parent.ready == False:
            return
        elif event.reason() == event.Mouse:
            self.pos = event.globalPos()
            item = self.parent.itemAt(event.pos())
        else:
            selection = self.parent.selectedItems()
            if selection:
                item = selection[0]
            else:
                item = self.parent.currentItem()
                if item is None:
                    item = self.parent.invisibleRootItem().child(0)
            if item is not None:
                parent = item.parent()
                while parent is not None:
                    parent.setExpanded(True)
                    parent = parent.parent()
                itemrect = self.parent.visualItemRect(item)
                portrect = self.parent.viewport().rect()
                if not portrect.contains(itemrect.topLeft()):
                    self.parent.scrollToItem(item, QtGui.QTreeWidget.PositionAtCenter)
                    itemrect = self.parent.visualItemRect(item)
                itemrect.setLeft(portrect.left())
                itemrect.setWidth(portrect.width())
                self.pos = self.parent.mapToGlobal(itemrect.center())

        if self.pos is not None:
            self.setupMenu(item)
            self.popup(self.pos)
            
        event.accept()

        
    def setupMenu(self,item):
        """
        setup the menu ready for display
        - get mandatory and optional childs of item and 
        - attach submenu add with them
        """
        try:
            type_=item.text(2)
        except:
            type_="root"

        self.contextMenuActionsAdd(item,self.core.grammar.getMandatoryChilds(type_))
        self.contextMenuActionsAdd(item,self.core.grammar.getOptionalChilds(type_))
                

    def contextMenuActionsAdd(self,item,actions):
        """
        attach contexted sub menu add actions of item
        - attach the submenu add
        - and append item type contexted childs as possible add actions
        """
        if actions == None:
            return
        
        if self.addmenu == None:
            self.addmenu=self.addMenu("add")
            
        menuactions = {}
        for action in actions:
            text=self.core.grammar.items[action].name
            menuactions[action] = QtGui.QAction(self)
            menuactions[action].setText(text)
            menuactions[action].triggered.connect(functools.partial(self.execContextMenuAction,item,"add",action))
            self.addmenu.addAction(menuactions[action])


    def execContextMenuAction(self,parent,action,type_):
        """
        slot for triggered context menu action
        """
        if action == 'add':
            self.parent.addItem(parent,type_)
