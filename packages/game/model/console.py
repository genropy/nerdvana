#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('console',pkey='id',name_long='Console',name_plural='Console',caption_field='name')
        self.sysFields(tbl)
        tbl.column('code',size=':10',name_long='Code',unique=True,indexed=True)
        tbl.column('name',name_long='Name')
        tbl.column('brand_id',size='22',name_long='Brand',group='_').relation('brand.id',relation_name='consoles', mode='foreignkey', onDelete='raise')
        tbl.column('launch_date',dtype='D',name_long='Launch date')
        tbl.column('cpu',name_long='Cpu')
        tbl.column('support',size=':5',name_long='Support',
                    values='CD:CD,DVD:DVD,CART:Cartridge')
