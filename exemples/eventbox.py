#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple eventbox.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoiteEvenement:
    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Boîte à évènement")
        fenetre.connect("destroy", lambda w: gtk.main_quit())
        fenetre.set_border_width(10)

        # On crée une boite à évènement et on l'ajoute à la fenêtre principale
        boite_evenement = gtk.EventBox()
        fenetre.add(boite_evenement)
        boite_evenement.show()

        # On crée un label long
        label = gtk.Label("Cliquer ici pour quitter, finir, terminer, sortir...")
        boite_evenement.add(label)
        label.show()

        # On fixe sa taille de départ (largeur, hauteur).
        label.set_size_request(110, 30)

        # On relie une action à la boîte
        boite_evenement.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        boite_evenement.connect("button_press_event", lambda w,e: gtk.main_quit())

        # D'autres choses pour lesquelles il faut une fenêtre X...
        boite_evenement.realize()
        boite_evenement.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))

        # Un arrière-plan en vert
        boite_evenement.modify_bg(gtk.STATE_NORMAL,
                            boite_evenement.get_colormap().alloc_color("green"))

        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleBoiteEvenement()
    main()
