#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple layout.py

import pygtk
pygtk.require('2.0')
import gtk
import random

class ExempleAffiche:
    def WindowDeleteEvent(self, widget, event):
        # retourne False pour que la fenêtre soit détruite
        return False

    def WindowDestroy(self, widget, *data):
        # quitte la boucle principale
        gtk.main_quit()

    def ButtonClicked(self, bouton):
        # déplace le bouton
        self.affiche.move(bouton, random.randint(0,500),
                         random.randint(0,500))

    def __init__(self):
        # crée la fenêtre de niveau supérieur
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Exemple conteneur Layout")
        fenetre.set_default_size(300, 300)
        fenetre.connect("delete-event", self.WindowDeleteEvent)
        fenetre.connect("destroy", self.WindowDestroy)
        # crée une table et la place dans la fenêtre
        table = gtk.Table(2, 2, False)
        fenetre.add(table)
        # crée le conteneur affiche affiche et le place dans la table
        self.affiche = gtk.Layout(None, None)
        self.affiche.set_size(600, 600)
        table.attach(self.affiche, 0, 1, 0, 1, gtk.FILL|gtk.EXPAND,
                     gtk.FILL|gtk.EXPAND, 0, 0)
        # crée les barres de défilement et les place dans la table
        vert_defil = gtk.VScrollbar(None)
        table.attach(vert_defil, 1, 2, 0, 1, gtk.FILL|gtk.SHRINK,
                     gtk.FILL|gtk.SHRINK, 0, 0)
        horiz_defil = gtk.HScrollbar(None)
        table.attach(horiz_defil, 0, 1, 1, 2, gtk.FILL|gtk.SHRINK,
                     gtk.FILL|gtk.SHRINK, 0, 0)	
        # les barres de défilement utilisent les ajustements du conteneur
        vAdjust = self.affiche.get_vadjustment()
        vert_defil.set_adjustment(vAdjust)
        hAdjust = self.affiche.get_hadjustment()
        horiz_defil.set_adjustment(hAdjust)
        # crée 3 boutons et les place dans le conteneur 
        bouton = gtk.Button("Clic !")
        bouton.connect("clicked", self.ButtonClicked)
        self.affiche.put(bouton, 0, 0)
        bouton = gtk.Button("Clic !")
        bouton.connect("clicked", self.ButtonClicked)
        self.affiche.put(bouton, 100, 0)
        bouton = gtk.Button("Clic !")
        bouton.connect("clicked", self.ButtonClicked)
        self.affiche.put(bouton, 200, 0)
        # Montre tous les widgets
        fenetre.show_all()

def main():
    # on entre dans la boucle principale
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleAffiche()
    main()
