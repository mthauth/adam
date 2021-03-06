"""
provides classes to handle and hold the formal grammar
"""
import os
import StringIO
import ConfigParser


class Grammar(object):
    """
    class to open and parse grammar file to store content as list of grammar items
    """
    def __init__(self, filename):
        self.openGrammar(filename)
        self.items = None
        self.sections = None


    def openGrammar(self, filename):
        """
        open grammar file, generate grammar item and store to list
        """
        ##raw file open and read operation
        config = StringIO.StringIO()
        config.write(open(filename, 'r').read())
        config.seek(0, os.SEEK_SET)

        ## read the sections from file content
        configparser = ConfigParser.ConfigParser()
        configparser.readfp(config)
        self.sections = configparser.sections()

        ## and append them to a itemlist
        self.items = {}
        for section in self.sections:
            self.items[section] = GrammarItem(section, configparser)


    def getMandatoryChilds(self, parent):
        """
        return mandatory childs of a type item (parent)
        """
        parent = unicode(parent)
        return self.items[parent].childs_mandatory


    def getOptionalChilds(self, parent):
        """
        return optional childs of a type item (parent)
        """
        parent = unicode(parent)
        return self.items[parent].childs_optional


    def getItem(self, type_):
        """
        return a single type item
        """
        type_ = unicode(type_)
        return self.items[type_]



class GrammarItem(object):
    """
    single grammar item representing a type, stores
    - type: config section name, identifies an item
    - childs_mandatory: comma-separated list of mandatory type's
    - childs_optional: comma-separated list of optional types
    - quantity: string multiple or single, defines how-many sibling types can be defined at once
    - name / value: default human-readable string to be displayed
    - name_check / value_check: valid string for name/value
      - regex: regular-expression with prepended "regex:" string
      - select: comma-separated list-string with prepended "select:" string
    """
    def __init__(self, type_, config):
        # type of item
        self.type = type_
        self.config = config
        self.setData()
        self.items = None
        self.sections = None
        self.name = None
        self.name_check = None
        self.value = None
        self.value_check = None
        self.childs_mandatory = None
        self.childs_optional = None
        self.quantity = None

    def setData(self):
        """
        set the data from config to current instance of GrammarItem
        """
        # mandatory childs for item
        try:
            self.childs_mandatory = self.config.get(self.type, 'childs_mandatory').split(',')
            if self.childs_mandatory[0] == "":
                self.childs_mandatory = None
        except:
            self.childs_mandatory = None


        # optional childs for item
        try:
            self.childs_optional = self.config.get(self.type, 'childs_optional').split(',')
            if self.childs_optional[0] == "":
                self.childs_optional = None
        except:
            self.childs_optional = None


        # human-readable (default) name
        try:
            self.name = self.config.get(self.type, 'name')
        except:
            self.name = None


        # allowed human-readable name variants
        try:
            name_check = self.config.get(self.type, 'name_check')

            if name_check[0:5] == "regex":
                i = name_check[6:]
                self.name_check = ["regex", i]

            elif name_check[0:6] == "select":
                i = name_check[7:]
                self.name_check = ["select", i]

            else:
                self.name_check = ["readonly", self.name]

        except:
            self.name_check = ["readonly", self.name]


        # human-readable (default) value
        try:
            self.value = self.config.get(self.type, 'value')
        except:
            self.value = ''


        # allowed human-readable value variants
        try:
            value_check = self.config.get(self.type, 'value_check')

            if value_check[0:5] == "regex":
                i = value_check[6:]
                self.value_check = ["regex", i]

            elif value_check[0:6] == "select":
                i = value_check[7:]
                self.value_check = ["select", i]

            else:
                self.value_check = ["readonly", ""]

        except:
            self.value_check = ["readonly", ""]


        # allowed quantity of type
        try:
            self.quantity = self.config.get(self.type, 'quantity')
        except:
            self.quantity = "multiple"

        self.dump()


    def dump(self):
        """
        print item data to std out
        """
        print "========================================"
        print "new Item:"
        print self.type
        print "Name:"
        print self.name
        print "Name check:"
        print self.name_check
        print "Value:"
        print self.value
        print "Value check:"
        print self.value_check
        print "Mandatory Childs:"
        print self.childs_mandatory
        print "Optional Childs:"
        print self.childs_optional
        print "Quantity:"
        print self.quantity
        print "========================================"

