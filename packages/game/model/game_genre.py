#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('game_genre', pkey='id', name_long='!!Game genre', name_plural='!!Game genre')
        self.sysFields(tbl)
        tbl.column('game_id',size='22' ,
                    group='_',name_long='!!Game'
                    ).relation('game.id',relation_name='genres',mode='foreignkey',onDelete='raise')
        tbl.column('genre_id',size='22' ,group='_',name_long='!!Genre').relation('genre.id',relation_name='games',mode='foreignkey',onDelete='raise')