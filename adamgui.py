#!/usr/bin/python

from PyQt4 import QtGui
from adamwindow import Ui_AdamWindow as AdamWindow
from adamcore import AdamCore
from treewidget import TreeWidget

class AdamGui(QtGui.QMainWindow, AdamWindow): 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        AdamWindow.__init__(self)
        self.core = AdamCore()
        self.setupAdamGui()
        self.setupSignalsSlots()
        
    def setupAdamGui(self):
        print "setupAdamGui()"
        self.setupUi(self)
        self.treeWidget = TreeWidget(self.core, self.centralwidget)
        self.gridLayout.addWidget(self.treeWidget,0,0,1,1)
        
    def newAdaptionDataFile(self):
        print "newAdaptionDataFile()"
        self.closeAdaptionDataFile()
        self.openWhitelistFile()
        
    def openAdaptionDataFile(self):
        print "openAdaptionDataFile()"
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.closeAdaptionDataFile()
        self.core.openAdaption(self.filename)
        self.setTreeWidget()
        
    def openWhitelistFile(self):
        print "openWhitelistFile()"
        whitelistfilename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.core.openWhitelist(whitelistfilename)
        self.treeWidget.setupTree()
        
    def closeAdaptionDataFile(self):
        print "closeAdaptionDataFile()"
        self.core.closeAdaption()

    def saveAdaptionDataFile(self):
        print "saveAdaptionDataFile()"
        try:
            self.filename
            self.core.saveAdaption(self.filename)
        except:
            self.filename = self.saveAsAdaptionDataFile()

    def saveAsAdaptionDataFile(self):
        print "saveAsAdaptionDataFile()"
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Save file as')            
        self.core.saveAdaption(self.filename)

    def exportAdaptionDataAs(self):
        print "exportAdaptionDataAs()"

    def setupSignalsSlots(self):
        print "setupSignalsSlots()"
        self.actionExit.triggered.connect(lambda: self.close())
        self.actionOpen.triggered.connect(lambda: self.newAdaptionDataFile())
        self.actionOpenWhitelist.triggered.connect(lambda: self.openWhitelistFile())
        self.actionClose.triggered.connect(lambda: self.closeAdaptionDataFile())
        self.actionSave.triggered.connect(lambda: self.saveAdaptionDataFile())
        self.actionSaveAs.triggered.connect(lambda: self.saveAsAdaptionDataFile())
        self.actionExport.triggered.connect(lambda: self.exportAdaptionDataAs())

    def setTreeWidget(self):
        tree = self.core.getTree()
        self.treeWidget.addTopLevelItem(tree)

