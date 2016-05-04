#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('brand', pkey='id', name_long='!!Brand', 
                        name_plural='!!Brand',caption_field='name')
        self.sysFields(tbl) #id,__ins_ts,__mod_ts
        tbl.column('name',name_long='!!Name')
        tbl.column('country' ,size=':3',name_long='!!Country'
                    ).relation('country.code',relation_name='brands',
                                mode='foreignkey')
        tbl.column('start_year',dtype='I',name_long='!!Start year')