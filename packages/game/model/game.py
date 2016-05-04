#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('game', pkey='id', name_long='!!Game', 
                        name_plural='!!Games',caption_field='title')
        self.sysFields(tbl)
        tbl.column('title',name_long='!!Title')
        tbl.column('description',name_long='!!Description')
        tbl.column('start_date','D',name_long='!!Start date')
