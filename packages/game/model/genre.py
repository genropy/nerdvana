#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('genre', pkey='id', name_long='!!Genre', 
                        name_plural='!!Genre',caption_field='name')
        self.sysFields(tbl,hierarchical='name')
        tbl.column('name',name_long='!!Name')