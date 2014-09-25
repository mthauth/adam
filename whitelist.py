import os
import StringIO
import ConfigParser


class Whitelist():
    def __init__(self, filename):
        print "Whitelist()"
        self.openWhitelist(filename)
        
    def openWhitelist(self, filename):
        print "openWhitelist()"
        
        ##apply a dummy section
        config = StringIO.StringIO()
        #config.write( '[dummysection]\n' )
        config.write( open( filename, 'r' ).read() )
        config.seek(0, os.SEEK_SET)

        ## read the sections in file        
        cp = ConfigParser.ConfigParser()
        cp.readfp( config )
        self.sections=cp.sections()

        ## and append them to a itemlist
        self.items = {}
        for section in self.sections:
            self.items[section] = WhitelistItem(section, cp)
      
    def getMandatoryChilds(self,parent):
        print "getMandatoryChilds()"
        print ":"+parent+":"
        parent = unicode(parent)
        return self.items[parent].childs_mandatory
        
    def getOptionalChilds(self,parent):
        print "getOptionalChilds()"
        parent = unicode(parent)
        return self.items[parent].childs_optional
        
    def getItem(self,type_):
        print "getItem()"
        type_ = unicode(type_)
        return self.items[type_]
        
        
        
class WhitelistItem():
    def __init__(self, type_, config):
        print "WhitelistItem()"
        
        # type of item
        self.type = type_
        

        # mandatory childs for item
        try:
            self.childs_mandatory=config.get(self.type,'childs_mandatory').split(',')
            if self.childs_mandatory[0] == "":
                self.childs_mandatory=None
        except:
            self.childs_mandatory=None
            
            
        # optional childs for item
        try:
            self.childs_optional=config.get(self.type,'childs_optional').split(',')
            if self.childs_optional[0] == "":
                self.childs_optional=None
        except:
            self.childs_optional=None       
                 
        
        # human-readable (default) name
        try:
            self.name=config.get(self.type,'name')
        except:
            self.name=None
            

        # allowed human-readable name variants
        try:
            name_check=config.get(self.type,'name_check')
            
            if name_check[0:5] == "regex":
                i=name_check[6:]
                self.name_check=[ "regex", i ]
                
            elif name_check[0:6] == "select":
                i=name_check[7:]
                self.name_check=[ "select", i ]
                
            else:
                self.name_check=["readonly",self.name]
                
        except:
            self.name_check=["readonly",self.name]
            
        
        # human-readable (default) value
        try:
            self.value=config.get(self.type,'value')
        except:
            self.value=''
            

        # allowed human-readable value variants 
        try:
            value_check=config.get(self.type,'value_check')
            
            if value_check[0:5] == "regex":
                i=value_check[6:]
                self.value_check=[ "regex", i ]
                
            elif value_check[0:6] == "select":
                i=value_check[7:]
                self.value_check=[ "select", i ]
                
            else:
                self.value_check=["readonly",""]
                
        except:
            self.value_check=["readonly",""]
            

        # allowed quantity of type
        try:
            self.quantity=config.get(self.type,'quantity')
        except:
            self.quantity="multiple"

        self.print_()


    def print_(self):
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
        
