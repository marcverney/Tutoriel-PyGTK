#!/usr/bin/env python

# exemple boutonsradio.py

import pygtk
pygtk.require('2.0')
import gtk

class BoutonsRadio:
    def fct_rappel(self, widget, donnees=None):
        print "Le %s a ete %s." % (donnees, ("desactive", "active")[widget.get_active()])

    def quitter_pgm(self, widget, evenement, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.connect("delete_event", self.quitter_pgm)

        self.fenetre.set_title("Boutons radio")
        self.fenetre.set_border_width(0)

        boite1 = gtk.VBox(False, 0)
        self.fenetre.add(boite1)
        boite1.show()

        boite2 = gtk.VBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        bouton = gtk.RadioButton(None, "bouton radio 1")
        bouton.connect("toggled", self.fct_rappel, "bouton radio 1")
        boite2.pack_start(bouton, True, True, 0)
        bouton.show()

        bouton = gtk.RadioButton(bouton, "bouton radio 2")
        bouton.connect("toggled", self.fct_rappel, "bouton radio 2")
        bouton.set_active(True)
        boite2.pack_start(bouton, True, True, 0)
        bouton.show()

        bouton = gtk.RadioButton(bouton, "bouton radio 3")
        bouton.connect("toggled", self.fct_rappel, "bouton radio 3")
        boite2.pack_start(bouton, True, True, 0)
        bouton.show()

        separateur = gtk.HSeparator()
        boite1.pack_start(separateur, False, True, 0)
        separateur.show()

        boite2 = gtk.VBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, False, True, 0)
        boite2.show()

        bouton = gtk.Button("fermer")
        bouton.connect_object("clicked", self.quitter_pgm, 
                              self.fenetre, None)
        boite2.pack_start(bouton, True, True, 0)
        bouton.set_flags(gtk.CAN_DEFAULT)
        bouton.grab_default()
        bouton.show()
        self.fenetre.show()

def main():
    gtk.main()
    return 0        

if __name__ == "__main__":
    BoutonsRadio()
    main()
