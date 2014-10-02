"""
provides access to adaption data and files
"""
from grammar import Grammar
from adaption import Adaption

class AdamCore(object):
    """
    adam core activities
    - reading grammar
    - reading adaption data files
    - saving adaption data files
    """
    def __init__(self):
        self.adaption = None
        self.grammar = None
        self.closeAdaption()

    def openAdaption(self, filename):
        """
        open adaption file
        """
        self.adaption = Adaption(filename)
        self.openGrammar(self.adaption.getGrammarfile())


    def closeAdaption(self):
        """
        close adaption data file and clean up core
        """
        self.grammar = None
        self.adaption = None


    def saveAdaption(self, filename, treewidget):
        """
        save adaption data file
        """
        self.adaption = Adaption(filename)
        self.adaption.saveAdaption(filename, treewidget)


    def openGrammar(self, filename):
        """
        open grammar file
        """
        self.grammar = Grammar(filename)

