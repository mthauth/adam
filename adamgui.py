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
    - setup gui
    - provides slots for main menu
    - setup signals and slots for main menu
    """
    def __init__(self):
        self.core = AdamCore()
        QtGui.QMainWindow.__init__(self)
        AdamWindow.__init__(self)
        self.setupAdamGui()


    def setupAdamGui(self):
        """
        setup adam gui
        - setups adams mainwindow ui
        - add tree widget to mainwindow
        """
        self.setupUi(self)
        self.treeWidget = TreeWidget(self.core, self.centralwidget)
        self.gridLayout.addWidget(self.treeWidget,0,0,1,1)
        self.setupSignalsSlots()


    def openAdaptionDataFile(self):
        """
        slot for opening existing adaption data file
        - ask for file
        - close current open adapation
        - open requested file
        """
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.closeAdaptionDataFile()
        self.core.openAdaption(self.filename)


    def newAdaptionDataFile(self):
        """
        slot for creating new adaption data file
        - ask for grammar file for new adaption data
        - setup tree widget
        """
        grammarfilename = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        self.core.openGrammar(grammarfilename)
        self.treeWidget.setupTree()


    def closeAdaptionDataFile(self):
        """
        slot for closing currently opened adaption data file
        """
        self.core.closeAdaption()


    def saveAdaptionDataFile(self):
        """
        slot for saving adaption data file
        - if filename is not defined, saveAs will be called
        """
        try:
            self.filename
            self.core.saveAdaption(self.filename)
        except:
            self.saveAsAdaptionDataFile()


    def saveAsAdaptionDataFile(self):
        """
        slot for saving adaption data file (ask for destination before saving)
        - ask for file to save into
        """
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Save file as')
        self.core.saveAdaption(self.filename)


    def exportAdaptionDataAs(self):
        """
        slot for exporting adaption data
        """


    def setupSignalsSlots(self):
        """
        setup signal and slots
        """
        self.actionNew.triggered.connect(lambda: self.newAdaptionDataFile())
        self.actionOpen.triggered.connect(lambda: self.openAdaptionDataFile())
        self.actionClose.triggered.connect(lambda: self.closeAdaptionDataFile())
        self.actionSave.triggered.connect(lambda: self.saveAdaptionDataFile())
        self.actionSaveAs.triggered.connect(lambda: self.saveAsAdaptionDataFile())
        self.actionExport.triggered.connect(lambda: self.exportAdaptionDataAs())
        self.actionExit.triggered.connect(lambda: self.close())

