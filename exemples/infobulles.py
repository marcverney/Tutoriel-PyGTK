#!/usr/bin/env python

# exemple infobulles.py

import pygtk
pygtk.require('2.0')
import gtk

# On cree une fleche avec les parametres specifies
# et on la place dans un bouton
def cree_fleche_bouton(type, ombre):
    bouton = gtk.Button();
    fleche = gtk.Arrow(type, ombre);
    bouton.add(fleche)
    bouton.show()
    fleche.show()
    return bouton

class Infobulles:
    def __init__(self):
        # Creation d'une fenetre
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        fenetre.set_title("Infobulles")

        # C'est une bonne idee de faire ceci pour chaque fenetre
        fenetre.connect("destroy", gtk.main_quit)

        # On fixe la largeur des bordures de la fenetre
        fenetre.set_border_width(10)

        # On cree une boite pour contenir les boutons/fleches
        boite = gtk.HBox(False, 0)
        boite.set_border_width(2)
        fenetre.add(boite)

        # Creation d'un objet Tooltips
        self.infobulles = gtk.Tooltips()

        # On place et on affiche tous nos widgets
        boite.show()

        bouton = cree_fleche_bouton(gtk.ARROW_UP, gtk.SHADOW_IN)
        boite.pack_start(bouton, False, False, 3)
        self.infobulles.set_tip(bouton, "SHADOW_IN")

        bouton = cree_fleche_bouton(gtk.ARROW_DOWN, gtk.SHADOW_OUT)
        boite.pack_start(bouton, False, False, 3)
        self.infobulles.set_tip(bouton, "SHADOW_OUT")
  
        bouton = cree_fleche_bouton(gtk.ARROW_LEFT, gtk.SHADOW_ETCHED_IN)
        boite.pack_start(bouton, False, False, 3)
        self.infobulles.set_tip(bouton, "SHADOW_ETCHED_IN")
  
        bouton = cree_fleche_bouton(gtk.ARROW_RIGHT, gtk.SHADOW_ETCHED_OUT)
        boite.pack_start(bouton, False, False, 3)
        self.infobulles.set_tip(bouton, "SHADOW_ETCHED_OUT")
  
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    infob = Infobulles()
    main()
