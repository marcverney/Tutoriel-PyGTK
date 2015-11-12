#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example boutonbox.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoiteBouton:
    # Créer une boite à boutons avec les paramètres indiqués
    def create_boite_bout(self, horizontal, title, spacing, layout):
        cadre = gtk.Frame(title)

        if horizontal:
            boite_bout = gtk.HButtonBox()
        else:
            boite_bout = gtk.VButtonBox()

        boite_bout.set_border_width(5)
        cadre.add(boite_bout)

        # Définir l'apparence de la boite à bouton
        boite_bout.set_layout(layout)
        boite_bout.set_spacing(spacing)

        bouton = gtk.Button(stock=gtk.STOCK_OK)
        boite_bout.add(bouton)

        bouton = gtk.Button(stock=gtk.STOCK_CANCEL)
        boite_bout.add(bouton)

        bouton = gtk.Button(stock=gtk.STOCK_HELP)
        boite_bout.add(bouton)

        return cadre

    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Boîtes à boutons")

        fenetre.connect("destroy", lambda x: gtk.main_quit())

        fenetre.set_border_width(10)

        boitev_princ = gtk.VBox(False, 0)
        fenetre.add(boitev_princ)

        cadre_horz = gtk.Frame("Boîtes à boutons horizontales")
        boitev_princ.pack_start(cadre_horz, True, True, 10)

        boitev = gtk.VBox(False, 0)
        boitev.set_border_width(10)
        cadre_horz.add(boitev)

        boitev.pack_start(self.create_boite_bout(True, "Spread (spacing 40)",
                                         40, gtk.BUTTONBOX_SPREAD),
                        True, True, 0)

        boitev.pack_start(self.create_boite_bout(True, "Edge (spacing 30)",
                                         30, gtk.BUTTONBOX_EDGE),
                        True, True, 5)

        boitev.pack_start(self.create_boite_bout(True, "Start (spacing 20)",
                                         20, gtk.BUTTONBOX_START),
                        True, True, 5)

        boitev.pack_start(self.create_boite_bout(True, "End (spacing 10)",
                                         10, gtk.BUTTONBOX_END),
                        True, True, 5)

        cadre_vert = gtk.Frame("Boîtes à boutons verticales")
        boitev_princ.pack_start(cadre_vert, True, True, 10)

        boiteh = gtk.HBox(False, 0)
        boiteh.set_border_width(10)
        cadre_vert.add(boiteh)

        boiteh.pack_start(self.create_boite_bout(False, "Spread (spacing 5)",
                                         5, gtk.BUTTONBOX_SPREAD),
                        True, True, 0)

        boiteh.pack_start(self.create_boite_bout(False, "Edge (spacing 30)",
                                         30, gtk.BUTTONBOX_EDGE),
                        True, True, 5)

        boiteh.pack_start(self.create_boite_bout(False, "Start (spacing 20)",
                                         20, gtk.BUTTONBOX_START),
                        True, True, 5)

        boiteh.pack_start(self.create_boite_bout(False, "End (spacing 20)",
                                         20, gtk.BUTTONBOX_END),
                        True, True, 5)

        fenetre.show_all()

def main():
    # Entrer dans la boucle principale
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleBoiteBouton()
    main()
