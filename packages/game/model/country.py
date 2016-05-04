#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('country', pkey='code', name_long='!!Country', 
                        name_plural='!!Countries',caption_field='name',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size=':3',name_long='!!Code')
        tbl.column('name',name_long='!!Name')