#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoiteDeroulSaisie:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        boitderoulsaisie = gtk.combo_box_entry_new_text()
        fenetre.add(boitderoulsaisie)
        boitderoulsaisie.append_text('Pommes')
        boitderoulsaisie.append_text('Cerises')
        boitderoulsaisie.append_text('Myrtilles')
        boitderoulsaisie.append_text('Raisin')
        boitderoulsaisie.append_text('Peches')
        boitderoulsaisie.append_text('Noix')
        boitderoulsaisie.child.connect('changed', self.fct_rappel_change)
        boitderoulsaisie.set_active(0)
        fenetre.show_all()
        return

    def fct_rappel_change(self, saisie):
        print "J'aime les tartes aux ", saisie.get_text()
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ebds = ExempleBoiteDeroulSaisie()
    main()
