#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple aspectframe.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleAspectFrame:
    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL);
        fenetre.set_title("Cadre_proportionnel")
        fenetre.connect("destroy", lambda x: gtk.main_quit())
        fenetre.set_border_width(10)

        # Créer un cadre proportionnel - l'ajouter à la fenêtre principale
        cadre_prop = gtk.AspectFrame("2x1", # étiquette
                                       0.5, # x centré dans la fenêtre à
                                       0.5, # y centré dans la fenêtre à
                                       2, # rapport x/y = 2
                                       False) # ignorer taille des widgets enfant
        fenetre.add(cadre_prop)
        cadre_prop.show()

        # Ajouter un widget enfant dans le cadre proportionnel
        zone_dessin = gtk.DrawingArea()

        # Déclarer une fenêtre de 200x200 mais le cadre proportionnel
        # avec un rapport de 2x1 affiche une zone de 200x100
        zone_dessin.set_size_request(200, 200)
        cadre_prop.add(zone_dessin)
        zone_dessin.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleAspectFrame()
    main()
