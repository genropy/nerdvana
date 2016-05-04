#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    auto = root.branch(u"auto")
    auto.thpage(u"!!Brand", table="game.brand")
    auto.thpage(u"!!Console", table="game.console")
    auto.thpage(u"!!Country", table="game.country")
    auto.thpage(u"!!Genre", table="game.genre")
    auto.thpage(u"!!Game", table="game.game")
    auto.webpage(u"!!Hello", filepath="/game/helloworld")

