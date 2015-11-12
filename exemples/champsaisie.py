#!/usr/bin/env python

# exemple champsaisie.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleSaisieTexte:
    def fct_rappel_entree(self, widget, champsaisie):
        textesaisi = champsaisie.get_text()
        print "Contenu de la champ de saisie : %s\n" % textesaisi

    def champsaisie_editable(self, casecocher, champsaisie):
        champsaisie.set_editable(casecocher.get_active())

    def champsaisie_visible(self, casecocher, champsaisie):
        champsaisie.set_visibility(casecocher.get_active())

    def __init__(self):
        # Creation d'une nouvelle fenetre
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_size_request(200, 100)
        fenetre.set_title("Saisie de texte GTK")
        fenetre.connect("delete_event", gtk.main_quit)

        boite_v = gtk.VBox(False, 0)
        fenetre.add(boite_v)
        boite_v.show()

        champsaisie = gtk.Entry()
        champsaisie.set_max_length(50)
        champsaisie.connect("activate", self.fct_rappel_entree, champsaisie)
        champsaisie.set_text("salut")
        champsaisie.insert_text(" tout le monde", len(champsaisie.get_text()))
        champsaisie.select_region(0, len(champsaisie.get_text()))
        boite_v.pack_start(champsaisie, True, True, 0)
        champsaisie.show()

        boite_h = gtk.HBox(False, 0)
        boite_v.add(boite_h)
        boite_h.show()
                                  
        casecocher = gtk.CheckButton("Editable")
        boite_h.pack_start(casecocher, True, True, 0)
        casecocher.connect("toggled", self.champsaisie_editable, champsaisie)
        casecocher.set_active(True)
        casecocher.show()
    
        casecocher = gtk.CheckButton("Visible")
        boite_h.pack_start(casecocher, True, True, 0)
        casecocher.connect("toggled", self.champsaisie_visible, champsaisie)
        casecocher.set_active(True)
        casecocher.show()
                                   
        bouton = gtk.Button(stock=gtk.STOCK_CLOSE)
        bouton.connect_object("clicked", gtk.main_quit, fenetre)
        boite_v.pack_start(bouton, True, True, 0)
        bouton.set_flags(gtk.CAN_DEFAULT)
        bouton.grab_default()
        bouton.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleSaisieTexte()
    main()
