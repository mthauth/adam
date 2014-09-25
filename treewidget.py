from PyQt4 import QtGui
from treeitem import TreeItem
from delegate import Delegate
import functools


class TreeWidget(QtGui.QTreeWidget):
    def __init__(self, core, parent=None):
        QtGui.QTreeWidget.__init__(self, parent)
        self.core = core
        self.pos=None
        self.delegate = Delegate(self,core)
        self.setItemDelegate(self.delegate)
        self.header().setHidden(True)
        self.setColumnCount(3)
        self.headerItem().setText(0, "name")
        self.headerItem().setText(1, "value")
        self.headerItem().setText(2, "type")
        self.setColumnHidden(2,True)
        self.ready=False
        self.itemDoubleClicked.connect(functools.partial(self.editItem))
        self.setExpandsOnDoubleClick(False)
        

    def setupTree(self):
        self.addItems(self,self.core.whitelist.getMandatoryChilds('root'))
        self.ready=True
        
        
    def execContextMenuAction(self,parent,action,type_):
        print "execContextMenuAction( " + action + "," + type_ + " )"
        if action == 'add':
            self.addItem(parent,type_)
            
        
    def editItem(self,item,col):
        print "editItem()"
        print item.text(2)
        self.delegate.editItem(item,col)
              
        
    def addItems(self,parent,types_):
        for type_ in types_:
            self.addItem(parent,type_)
            
            
    def addItem(self, parent, type_):
        wlitem=self.core.whitelist.getItem(type_)
        item=TreeItem(parent, wlitem)
        self.expandItem(item)
        mandatory=self.core.whitelist.getMandatoryChilds(type_)

        if mandatory != None:
            self.addItems(item,mandatory)
            
        self.resizeColumnToContents(0)
        

    def contextMenuEvent(self, event):
        print "contextMenuEvent()"
        if self.ready == False:
            return
        
        self.pos=None
        if event.reason() == event.Mouse:
            self.pos = event.globalPos()
            item = self.itemAt(event.pos())
        else:
            selection = self.selectedItems()
            if selection:
                item = selection[0]
            else:
                item = self.currentItem()
                if item is None:
                    item = self.invisibleRootItem().child(0)
            if item is not None:
                parent = item.parent()
                while parent is not None:
                    parent.setExpanded(True)
                    parent = parent.parent()
                itemrect = self.visualItemRect(item)
                portrect = self.viewport().rect()
                if not portrect.contains(itemrect.topLeft()):
                    self.scrollToItem(item, QtGui.QTreeWidget.PositionAtCenter)
                    itemrect = self.visualItemRect(item)
                itemrect.setLeft(portrect.left())
                itemrect.setWidth(portrect.width())
                self.pos = self.mapToGlobal(itemrect.center())

        if self.pos is not None:
            self.openMenu(item)
            
        event.accept()
        

    def openMenu(self,item):
        print "openMenu()"
        
        try:
            type_=item.text(2)
        except:
            type_="root"

        menu = QtGui.QMenu(self)
        addmenu=menu.addMenu("add")
        
        self.addContextMenuActions(addmenu,item,self.core.whitelist.getMandatoryChilds(type_))
        self.addContextMenuActions(addmenu,item,self.core.whitelist.getOptionalChilds(type_))
        
        menu.popup(self.pos)
        

    def addContextMenuActions(self,menu,item,actions):                
        if actions == None:
            return
        menuactions = {}
        for action in actions:
            text=self.core.whitelist.items[action].name
            menuactions[action] = QtGui.QAction(self)
            menuactions[action].setText(text)
            menuactions[action].triggered.connect(functools.partial(self.execContextMenuAction,item,"add",action))
            menu.addAction(menuactions[action])




