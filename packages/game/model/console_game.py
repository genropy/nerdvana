#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('console_game', pkey='id', name_long='!!Console game', name_plural='!!Console games')
        self.sysFields(tbl)
        tbl.column('game_id',size='22',
                    group='_',
                    name_long='!!Game').relation('game.id',
                                                    relation_name='consoles',
                                                    mode='foreignkey',onDelete='raise')
        tbl.column('console_id',size='22' ,group='_',name_long='!!Console').relation('console.id',
                                                relation_name='games',mode='foreignkey',onDelete='raise')