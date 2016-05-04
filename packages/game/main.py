#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='game package',sqlschema='game',sqlprefix=True,
                    name_short='Game', name_long='Game', name_full='Game')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
