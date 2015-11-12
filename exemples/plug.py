#!/usr/bin/python
# -*- coding:utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk,sys

Wid = 0L
if len(sys.argv) == 2:
    Wid = long(sys.argv[1])

plug = gtk.Plug(Wid)
print "Id de Plug=", plug.get_id()

def embed_event(widget):
    print "Je (", widget, ") viens juste d'être inséré !"

plug.connect("embedded", embed_event)

entry = gtk.Entry()
entry.set_text("salut")
def entry_point(widget):
    print "Vous avez modifié mon texte en '%s'" % widget.get_text()

entry.connect("changed", entry_point)
plug.connect("destroy", lambda w: gtk.main_quit())

plug.add(entry)
plug.show_all()


gtk.main()
