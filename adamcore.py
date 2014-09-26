"""
provides access to adaption data and files
"""
from grammar import Grammar

class AdamCore():
    """
    adam core activities
    - reading grammar
    - reading adaption data files
    - saving adaption data files
    """
    def __init__(self):
        self.closeAdaption()

    def openAdaption(self, filename):
        """
        open adaption file
        """


    def closeAdaption(self):
        """
        close adaption data file and clean up core
        """
        self.grammar = None


    def saveAdaption(self,filename):
        """
        save adaption data file
        """


    def openGrammar(self, filename):
        """
        open grammar file
        """
        self.grammar = Grammar(filename)

