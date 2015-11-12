#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple scribblesimple.py

 # GTK - The GIMP Toolkit
 # Copyright (C) 1995-1997 Peter Mattis, Spencer Kimball and Josh MacDonald
 # Copyright (C) 2001-2004 John Finlay
 #
 # This library is free software; you can redistribute it and/or
 # modify it under the terms of the GNU Library General Public
 # License as published by the Free Software Foundation; either
 # version 2 of the License, or (at your option) any later version.
 #
 # This library is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 # Library General Public License for more details.
 #
 # You should have received a copy of the GNU Library General Public
 # License along with this library; if not, write to the
 # Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 # Boston, MA 02111-1307, USA.


import pygtk
pygtk.require('2.0')
import gtk

# Pixmap d'arrière-plan pour la zone de dessin
pixmap = None

# Création d'un nouveau pixmap d'arrière-plan de la taille voulue
def configure_event(widget, event):
    global pixmap

    x, y, largeur, hauteur = widget.get_allocation()
    pixmap = gtk.gdk.Pixmap(widget.window, largeur, hauteur)
    pixmap.draw_rectangle(widget.get_style().white_gc,
                          True, 0, 0, largeur, hauteur)

    return True

# Redessine l'écran à partir du pixmap d'arrière-plan
def expose_event(widget, event):
    x , y, largeur, hauteur = event.area
    widget.window.draw_drawable(widget.get_style().fg_gc[gtk.STATE_NORMAL],
                                pixmap, x, y, x, y, largeur, hauteur)
    return False

# Dessine un rectangle sur l'écran
def brosse_dessin(widget, x, y):
    rect = (int(x-5), int(y-5), 10, 10)
    pixmap.draw_rectangle(widget.get_style().black_gc, True,
                          rect[0], rect[1], rect[2], rect[3])
    widget.queue_draw_area(rect[0], rect[1], rect[2], rect[3])

def bouton_press_event(widget, event):
    if event.button == 1 and pixmap != None:
        brosse_dessin(widget, event.x, event.y)
    return True

def motion_notify_event(widget, event):
    if event.is_hint:
        x, y, etat = event.window.get_pointer()
    else:
        x = event.x
        y = event.y
        etat = event.state
    
    if etat & gtk.gdk.BUTTON1_MASK and pixmap != None:
        brosse_dessin(widget, x, y)
  
    return True

def main():
    fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
    fenetre.set_name ("Test Input")

    boitev = gtk.VBox(False, 0)
    fenetre.add(boitev)
    boitev.show()

    fenetre.connect("destroy", lambda w: gtk.main_quit())

    # Création de la zone de dessin
    zone_dessin = gtk.DrawingArea()
    zone_dessin.set_size_request(200, 200)
    boitev.pack_start(zone_dessin, True, True, 0)

    zone_dessin.show()

    # Signaux utilisés pour gérer le pixmap hors écran
    zone_dessin.connect("expose_event", expose_event)
    zone_dessin.connect("configure_event", configure_event)

    # Signaux d'événements
    zone_dessin.connect("motion_notify_event", motion_notify_event)
    zone_dessin.connect("button_press_event", bouton_press_event)

    zone_dessin.set_events(gtk.gdk.EXPOSURE_MASK
                            | gtk.gdk.LEAVE_NOTIFY_MASK
                            | gtk.gdk.BUTTON_PRESS_MASK
                            | gtk.gdk.POINTER_MOTION_MASK
                            | gtk.gdk.POINTER_MOTION_HINT_MASK)

    # .. Et un bouton quitter
    bouton = gtk.Button("Quit")
    boitev.pack_start(bouton, False, False, 0)

    bouton.connect_object("clicked", lambda w: w.destroy(), fenetre)
    bouton.show()

    fenetre.show()

    gtk.main()

    return 0

if __name__ == "__main__":
    main()
