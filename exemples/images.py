#!/usr/bin/env python

# exemple images.py

import pygtk
pygtk.require('2.0')
import gtk

class ImagesExemple:
    # Si elle est invoquee (via le "delete_event"), cette fonction ferme l'application
    def fermer_application(self, widget, evnmt, data=None):
        gtk.main_quit()
        return False

    # Cette fonction est invoquee quand on clique sur le bouton. Elle affiche un message.
    def clic_bouton(self, widget, data=None):
        print "Clic sur le bouton %s" % data

    def __init__(self):
        # creation de la fenetre principale, et connexion du signal
        # delete_event a la fermeture de l'application
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.connect("delete_event", self.fermer_application)
        fenetre.set_border_width(10)
        fenetre.show()

        # Une boite horizontale pour contenir les boutons
        boite_h = gtk.HBox()
        boite_h.show()
        fenetre.add(boite_h)

        animpixbuf = gtk.gdk.PixbufAnimation("goal.gif")
        image = gtk.Image()
        image.set_from_animation(animpixbuf)
        image.show()
        # un bouton pour contenir le widget image
        bouton = gtk.Button()
        bouton.add(image)
        bouton.show()
        boite_h.pack_start(bouton)
        bouton.connect("clicked", self.clic_bouton, "1")
        
        # creation de plusieurs gtk.Image a partir de donnees de
        # fichiers, et chargement dans des boutons
        image = gtk.Image()
        image.set_from_file("pomme-rouge.png")
        image.show()
        # un bouton pour contenir le widget image
        bouton = gtk.Button()
        bouton.add(image)
        bouton.show()
        boite_h.pack_start(bouton)
        bouton.connect("clicked", self.clic_bouton, "2")

        image = gtk.Image()
        image.set_from_file("chaos.jpg")
        image.show()
        # un bouton pour contenir le widget image
        bouton = gtk.Button()
        bouton.add(image)
        bouton.show()
        boite_h.pack_start(bouton)
        bouton.connect("clicked", self.clic_bouton, "3")

        image = gtk.Image()
        image.set_from_file("important.tif")
        image.show()
        # un bouton pour contenir le widget image
        bouton = gtk.Button()
        bouton.add(image)
        bouton.show()
        boite_h.pack_start(bouton)
        bouton.connect("clicked", self.clic_bouton, "4")

        image = gtk.Image()
        image.set_from_file("ballonfoot.gif")
        image.show()
        # un bouton pour contenir le widget image
        bouton = gtk.Button()
        bouton.add(image)
        bouton.show()
        boite_h.pack_start(bouton)
        bouton.connect("clicked", self.clic_bouton, "5")


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ImagesExemple()
    main()
