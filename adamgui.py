"""
module to handle the gui mainwindow of ADaM
"""

from PyQt4 import QtGui
from adamwindow import Ui_AdamWindow as AdamWindow
from adamcore import AdamCore
from treewidget import TreeWidget

class AdamGui(QtGui.QMainWindow, AdamWindow):
    """
    class represents a QMainWindow based on Ui_AdamWindow
    """
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        AdamWindow.__init__(self)
        self.core = AdamCore()
        self.setupAdamGui()
        self.setupSignalsSlots()


    def setupAdamGui(self):
        """
        """
        self.setupUi(self)
        self.treeWidget = TreeWidget(self.core, self.centralwidget)
        self.gridLayout.addWidget(self.treeWidget,0,0,1,1)


    def newAdaptionDataFile(self):
        """
        """
        self.closeAdaptionDataFile()
        self.openGrammarFile()


    def openAdaptionDataFile(self):
        """
        """
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.closeAdaptionDataFile()
        self.core.openAdaption(self.filename)
        self.setTreeWidget()


    def openGrammarFile(self):
        """
        """
        grammarfilename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.core.openGrammar(grammarfilename)
        self.treeWidget.setupTree()


    def closeAdaptionDataFile(self):
        """
        """
        self.core.closeAdaption()


    def saveAdaptionDataFile(self):
        """
        """
        try:
            self.filename
            self.core.saveAdaption(self.filename)
        except:
            self.filename = self.saveAsAdaptionDataFile()


    def saveAsAdaptionDataFile(self):
        """
        """
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Save file as')            
        self.core.saveAdaption(self.filename)


    def exportAdaptionDataAs(self):
        """
        """


    def setupSignalsSlots(self):
        """
        """
        self.actionExit.triggered.connect(lambda: self.close())
        self.actionNew.triggered.connect(lambda: self.newAdaptionDataFile())
        self.actionOpenGrammar.triggered.connect(lambda: self.openGrammarFile())
        self.actionClose.triggered.connect(lambda: self.closeAdaptionDataFile())
        self.actionSave.triggered.connect(lambda: self.saveAdaptionDataFile())
        self.actionSaveAs.triggered.connect(lambda: self.saveAsAdaptionDataFile())
        self.actionExport.triggered.connect(lambda: self.exportAdaptionDataAs())


    def setTreeWidget(self):
        """
        """
        tree = self.core.getTree()
        self.treeWidget.addTopLevelItem(tree)
