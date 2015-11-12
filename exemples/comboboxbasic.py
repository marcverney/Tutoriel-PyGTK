#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoiteDeroul:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        boitderoul = gtk.combo_box_new_text()
        fenetre.add(boitderoul)
        boitderoul.append_text('Choisir une tarte :')
        boitderoul.append_text('Pommes')
        boitderoul.append_text('Cerises')
        boitderoul.append_text('Myrtilles')
        boitderoul.append_text('Raisin')
        boitderoul.append_text('Peches')
        boitderoul.append_text('Noix')
        boitderoul.connect('changed', self.fct_rappel_change)
        boitderoul.set_active(0)
        fenetre.show_all()
        return

    def fct_rappel_change(self, boitderoul):
        modele = boitderoul.get_model()
        index = boitderoul.get_active()
        if index:
            print "J'aime les tartes aux ", modele[index][0]
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ebd = ExempleBoiteDeroul()
    main()
