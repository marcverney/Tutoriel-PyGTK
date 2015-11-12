#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ExempleComboBoxColonnes:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        boitderoul = gtk.ComboBox()
        liststore = gtk.ListStore(str)
        case = gtk.CellRendererText()
        boitderoul.pack_start(case)
        boitderoul.add_attribute(case, 'text', 0)
        fenetre.add(boitderoul)
        boitderoul.set_wrap_width(5)
        for n in range(50):
            liststore.append(['Item %d'%n])
        boitderoul.set_model(liststore)
        boitderoul.connect('changed', self.fct_rappel_change)
        boitderoul.set_active(0)
        fenetre.show_all()
        return

    def fct_rappel_change(self, boitderoul):
        modele = boitderoul.get_model()
        index = boitderoul.get_active()
        if index > -1:
            print modele[index][0], 'choisi'
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ecc = ExempleComboBoxColonnes()
    main()
