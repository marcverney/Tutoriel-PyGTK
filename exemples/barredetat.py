#!/usr/bin/env python

# exemple barredetat.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBarreEtat:
    def empiler(self, widget, donnees):
        tampon = " Element %d" % self.compteur
        self.compteur = self.compteur + 1
        self.barredetat.push(donnees, tampon)
        return

    def depiler(self, widget, donnees):
        self.barredetat.pop(donnees)
        return

    def __init__(self):
        self.compteur = 1
        # Creation d'une fenetre
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_size_request(200, 100)
        fenetre.set_title("Exemple de barre d'etat PyGTK")
        fenetre.connect("delete_event", gtk.main_quit)
 
        boite_v = gtk.VBox(False, 1)
        fenetre.add(boite_v)
        boite_v.show()
          
        self.barredetat = gtk.Statusbar()      
        boite_v.pack_start(self.barredetat, True, True, 0)
        self.barredetat.show()

        context_id = self.barredetat.get_context_id("Exemple barredetat")
        
        bouton = gtk.Button("empiler un element")
        bouton.connect("clicked", self.empiler, context_id)
        boite_v.pack_start(bouton, True, True, 2)
        bouton.show()              

        bouton = gtk.Button("depiler le dernier element")
        bouton.connect("clicked", self.depiler, context_id)
        boite_v.pack_start(bouton, True, True, 2)
        bouton.show()              

        # On affichera toujours la fenetre a la derniere etape, de sorte que
        # tout apparaisse a l'ecran en un bloc.
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleBarreEtat()
    main()
