#!/usr/bin/env python

# exemple boutons.py

import pygtk
pygtk.require('2.0')
import gtk

# On cree une boite verticale, on y place une image 
# et une etiquette, et on renvoie la boite.

def boite_xpm_etiquette(parent, fichier_xpm, texte_etiquette):
    # On cree une boite pour la pixmap et l'etiquette
    boite1 = gtk.HBox(False, 0)
    boite1.set_border_width(2)

    # A present l'image.
    image = gtk.Image()
    image.set_from_file(fichier_xpm)

    # On cree une etiquette pour le bouton.
    etiquette = gtk.Label(texte_etiquette)

    # On place la pixmap et l'etiquette dans la boite.
    boite1.pack_start(image, False, False, 3)
    boite1.pack_start(etiquette, False, False, 3)

    image.show()
    etiquette.show()
    return boite1

class Bouton:
    # Notre methode de rappel habituelle.
    def salut(self, widget, donnees=None):
        print "Salut ! - Clic sur le %s." % donnees

    def __init__(self):
        # Creation d'une nouvelle fenetre.
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.set_title("Bouton et image")

        # C'est une bonne idee de faire ceci pour chaque fenetre.
        self.fenetre.connect("destroy", lambda wid: gtk.main_quit())
        self.fenetre.connect("delete_event", lambda a1,a2: gtk.main_quit())

        # On fixe la largeur des bordures de la fenetre.
        self.fenetre.set_border_width(10)

        # Creation d'un nouveau bouton.
        bouton = gtk.Button()

        # On connecte le signal "clicked" du bouton a la fonction de rappel
        bouton.connect("clicked", self.salut, "bouton cool")

        # Ceci appelle notre fonction de creation de boites.
        boite1= boite_xpm_etiquette(self.fenetre, "info.xpm", "bouton cool")

        # On place et on affiche tous nos widgets.
        bouton.add(boite1)

        boite1.show()
        bouton.show()

        self.fenetre.add(bouton)
        self.fenetre.show()

def main():
    gtk.main()
    return 0     

if __name__ == "__main__":
    Bouton()
    main()
