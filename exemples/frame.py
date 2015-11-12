#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple frame.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleCadre:
    def __init__(self):
        # Créer une nouvelle fenêtre
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Exemple de cadre")

        # On connecte l'évènement "destroy" au gestionnaire de signal 
        fenetre.connect("destroy", lambda w: gtk.main_quit())
        fenetre.set_size_request(300, 300)

        # On définit la largeur de bordure de la fenêtre
        fenetre.set_border_width(10)

        # On crée un cadre
        cadre = gtk.Frame()
        fenetre.add(cadre)

        # On indique l'étiquette du cadre
        cadre.set_label("Widget GTK Cadre")

        # On aligne l'étiquette sur la droite du cadre
        cadre.set_label_align(1.0, 0.5)

        # On précise le style du cadre
        #cadre.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
        cadre.set_shadow_type(gtk.SHADOW_OUT)
        cadre.show()
  
        # On affiche la fenêtre
        fenetre.show()

def main():
    # Enter the event loop
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleCadre()
    main()
