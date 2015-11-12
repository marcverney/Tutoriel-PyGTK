#!/usr/bin/env python

# exemple casesacocher.py

import pygtk
pygtk.require('2.0')
import gtk
 
class Casesacocher:
    # Notre fonction de rappel. Le parametre "donnees"
    # transmis a cette methode est affiche sur stdout
    def fct_rappel(self, widget, donnees=None):
        print "La %s a ete %s." % (donnees, ("desactivee", "activee")[widget.get_active()])

    # Cette fonction de rappel quitte le programme
    def evnmt_delete(self, widget, evenement, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Creation d'une nouvelle fenetre.
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # On definit le titre de la fenetre.
        self.fenetre.set_title("Cases a cocher")

        # On definit un gestionnaire de signal pour "delete_event",
        # qui quitte GTK immediatement.
        self.fenetre.connect("delete_event", self.evnmt_delete)

        # On fixe la largeur des bordures de la fenetre.
        self.fenetre.set_border_width(20)

        # Creation d'une boite verticale.
        boite_v = gtk.VBox(True, 2)

        # On place la VBox dans la fenetre principale.
        self.fenetre.add(boite_v)

        # Creation du premier bouton.
        bouton = gtk.CheckButton("case a cocher 1")

        # Lorsque l'on change l'etat du bouton, la methode fct_rappel() est
        # appelee, avec un pointeur sur "case a cocher 1" comme argument.
        bouton.connect("toggled", self.fct_rappel, "case a cocher 1")


        # Insertion du bouton 1 dans le quart superieur gauche du tableau.
        boite_v.pack_start(bouton, True, True, 2)

        bouton.show()

        # Creation du deuxieme bouton.

        bouton = gtk.CheckButton("case a cocher 2")

        # Lorsque l'on change l'etat du bouton, la methode fct_rappel() est
        # appelee, avec un pointeur sur "case a cocher 2" comme argument.
        bouton.connect("toggled", self.fct_rappel, "case a cocher 2")
        # Insertion du bouton 2 dans le quart superieur droit du tableau.
        boite_v.pack_start(bouton, True, True, 2)

        bouton.show()

        # Creation du bouton "Quitter".
        bouton = gtk.Button("Quitter")

        # Lorsque l'on clique sur le bouton, la fonction mainquit() est
        # appelee et le programme se termine.
        bouton.connect("clicked", lambda wid: gtk.main_quit())

        # Insertion du bouton "Quitter" dans les deux quarts inferieurs du tableau.
        boite_v.pack_start(bouton, True, True, 2)

        bouton.show()
        boite_v.show()
        self.fenetre.show()

def main():
    gtk.main()
    return 0       
 
if __name__ == "__main__":
    Casesacocher()
    main()
