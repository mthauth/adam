"""
module for working with adaption and adaption file
adaption has a section named "[adaption]", containing
- grammar: adaption based grammarfile
- separator: separator between types in adaption file
"""
import os
import StringIO
import ConfigParser


class Adaption(object):
    """
    represents an adaption stored in file
    - sets file to load from and save in adaption
    """
    def __init__(self, filename):
        self.filename = filename
        self.sections = None
        self.openAdaption(self.filename)


    def openAdaption(self, filename):
        """
        open adaption file and set config parser
        """
        ##raw file open and read operation
        config = StringIO.StringIO()
        config.write(open(filename, 'r').read())
        config.seek(0, os.SEEK_SET)

        ## read the sections from file content
        configparser = ConfigParser.ConfigParser()
        configparser.readfp(config)
        self.sections = configparser.sections()


    def getGrammarfile(self):
        """
        get filename of adaption file from adaption file and return it
        """
        return self.filename


    def saveAdaption(self, filename, treewidget):
        """
        reads the tree and write it to file
        """
        if treewidget is None:
            return

        #print treewidget.invisibleRootItem().child(0).text(0)
        self.getChilds(treewidget.invisibleRootItem(), "root")


    def getChilds(self, item, path):
        """
        return the tree in config style
        """
        #if item.grammar.value == '' and item.grammar.value_check == 'readonly':
        #    print item.text(2)
        #    return
        #else:
        #    print path
        print path

        for childindex in range(item.childCount()):
            child = item.child(childindex)
            self.getChilds(child, path+"/"+child.text(2))

