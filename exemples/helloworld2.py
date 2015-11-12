#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple helloworld2.py

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld2:

    # Notre fonction de rappel ameliorée. Les données
    # qui lui sont transmises sont affichées sur stdout.
    def salut(self, widget, donnees):
        print "Re-salut ! - Clic sur le %s" % donnees

    # Une autre fonction de rappel
    def evnmt_delete(self, widget, evenement, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Création d'une nouvelle fenêtre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Nouvel appel, qui donne le titre "Salut les boutons !"
        # à notre nouvelle fenêtre
        self.fenetre.set_title("Salut les boutons !")

        # Ici on définit juste un gestionnaire pour le signal
        # delete_event (qui quittera GTK immédiatement)
        self.fenetre.connect("delete_event", self.evnmt_delete)

        # On fixe la largeur des bordures de la fenêtre.
        self.fenetre.set_border_width(10)

        # On crée une boîte pour y placer des widgets. Nous y reviendrons
        # en détail dans la section "placement". La boîte n'est pas visible,
        # c'est juste un outil pour disposer des widgets.
        self.boite1 = gtk.HBox(False, 0)

        # On place la boîte dans la fenêtre principale.
        self.fenetre.add(self.boite1)

        # Création d'un nouveau bouton avec l'étiquette "Bouton 1".
        self.bouton1 = gtk.Button("Bouton 1")

        # Lorsqu'on cliquera sur le bouton, la ligne suivante appellera la
        # méthode "salut" avec la chaîne "bouton 1" comme argument.
        self.bouton1.connect("clicked", self.salut, "bouton 1")

        # Plutôt que add(), on utilise pack_start() afin de placer le bouton 
        # dans la boîte invisible (qui a elle-même été placée dans la fenêtre).
        self.boite1.pack_start(self.bouton1, True, True, 0)

        # N'oubliez pas cette étape, elle fait savoir à GTK que la préparation
        # de ce bouton est terminée et qu'il peut maintenant être affiché
        self.bouton1.show()

        # On répète les mêmes étapes pour créer un second bouton
        self.bouton2 = gtk.Button("Bouton 2")

        # On appelle la même fonction de rappel, mais avec un argument
        # différent : la chaîne de caractères "bouton 2".
        self.bouton2.connect("clicked", self.salut, "bouton 2")

        self.boite1.pack_start(self.bouton2, True, True, 0)

        # L'ordre d'affichage des boutons n'est pas trés important, mais je conseille
        # d'afficher la fenêtre en dernier pour que tout s'affiche d'un seul coup.
        self.bouton2.show()
        self.boite1.show()
        self.fenetre.show()

def boucle():
    gtk.main()

if __name__ == "__main__":
    salut = HelloWorld2()
    boucle()
