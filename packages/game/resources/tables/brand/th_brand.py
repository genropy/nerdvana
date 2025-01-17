#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name')
        r.fieldcell('country')
        r.fieldcell('start_year')

    def th_order(self):
        return 'name'

    def th_query(self):
        return dict(column='name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('name')
        fb.field('country',auxColumns='$code,$name')
        fb.field('start_year')
        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@consoles')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')


