#!/usr/bin/env python

# exemple tableau.py

import pygtk
pygtk.require('2.0')
import gtk

class Tableau:
    # Notre fonction de rappel. Le parametre "donnees"
    # transmis a cette methode est affiche sur stdout
    def salut(self, widget, donnees=None):
        print "Salut ! - Clic sur le %s." % donnees

    # Cette fonction de rappel quitte le programme
    def evnmt_delete(self, widget, evenement, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Creation d'une nouvelle fenetre.
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # On definit le titre de la fenetre.
        self.fenetre.set_title("Tableau")

        # On definit un gestionnaire de signal pour "delete_event",
        # qui quitte GTK immediatement.
        self.fenetre.connect("delete_event", self.evnmt_delete)

        # On fixe la largeur des bordures de la fenetre.
        self.fenetre.set_border_width(20)

        # Creation d'un tableau de 2x2.
        tableau = gtk.Table(2, 2, True)

        # On place le tableau dans la fenetre principale.
        self.fenetre.add(tableau)

        # Creation du premier bouton.
        bouton = gtk.Button("bouton 1")

        # Lorsque l'on clique sur le bouton, la methode salut() est
        # appelee, avec un pointeur sur "bouton 1" comme argument.
        bouton.connect("clicked", self.salut, "bouton 1")


        # Insertion du bouton 1 dans le quart superieur gauche du tableau.
        tableau.attach(bouton, 0, 1, 0, 1)

        bouton.show()

        # Creation du second bouton.

        bouton = gtk.Button("bouton 2")

        # Lorsque l'on clique sur le bouton, la methode "salut" est
        # appelee, avec un pointeur sur "bouton 2" comme argument.
        bouton.connect("clicked", self.salut, "bouton 2")
        # Insertion du bouton 2 dans le quart superieur droit du tableau.
        tableau.attach(bouton, 1, 2, 0, 1)

        bouton.show()

        # Creation du bouton "Quitter".
        bouton = gtk.Button("Quitter")

        # Lorsque l'on clique sur le bouton, la fonction mainquit est
        # appelee et le programme se termine.
        bouton.connect("clicked", gtk.main_quit)

        # Insertion du bouton "Quitter" dans les deux quarts inferieurs du tableau.
        tableau.attach(bouton, 0, 2, 1, 2)

        bouton.show()

        tableau.show()
        self.fenetre.show()

def main():
    gtk.main()
    return 0       

if __name__ =="__main__":
    Tableau()
    main()
