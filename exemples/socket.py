#!/usr/bin/python
# -*- coding:utf-8 -*-
import string

import pygtk
pygtk.require('2.0')
import gtk,sys

window = gtk.Window()
window.show()

socket = gtk.Socket()
socket.show()
window.add(socket)

print "ID du Socket = ", socket.get_id()
window.connect("destroy", lambda w: gtk.main_quit())

def plugged_event(widget):
    print "Je (", widget, ") viens juste d'avoir un plug inséré !"

socket.connect("plug-added", plugged_event)

if len(sys.argv) == 2:
    socket.add_id(long(sys.argv[1]))

gtk.main()
