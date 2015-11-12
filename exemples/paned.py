#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example paned.py

import pygtk
pygtk.require('2.0')
import gtk, gobject

class ExempleVolets:
    # Crée la liste des "messages"
    def create_list(self):
        # Crée une nouvelle fenêtre à défilement avec ascenseurs si nécessaire
        fenetre_defil = gtk.ScrolledWindow()
        fenetre_defil.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        modele = gtk.ListStore(gobject.TYPE_STRING)
        tree_view = gtk.TreeView(modele)
        fenetre_defil.add_with_viewport (tree_view)
        tree_view.show()

        # Ajoute quelques messages dans la fenêtre
        for i in range(10):
            msg = "Message #%d" % i
            iter = modele.append()
            modele.set(iter, 0, msg)

        cellule = gtk.CellRendererText()
        colonne = gtk.TreeViewColumn("Messages", cellule, text=0)
        tree_view.append_column(colonne)

        return fenetre_defil
   
    # Ajoute du texte au widget texte - ceci est un rappel qui est invoqué
    # quand la fenêtre est réalisée. On pourrait forcer aussi la fenêtre à être
    # réalisée avec gtk.Widget.realize(), mais elle devrait appartenir 
    # d'abord à une hiérarchie.
    def insert_text(self, buffer):
        iter = buffer.get_iter_at_offset(0)
        buffer.insert(iter,
                      "From: pathfinder@nasa.gov\n"
                      "To: mom@nasa.gov\n"
                      "Subject: Faites le !\n"
                      "\n"
                      "Nous sommes arrivés juste ce matin. \n"
                      "Le temps a été superbe, clair mais froid\n"
                      "et il y a plein de vues amusantes.\n"
                      "Sojourner vous dit bonjour. À bientôt.\n"
                      " -Path\n")
   
    # Crée une zone de texte avec ascenseurs qui affiche un "message"
    def create_text(self):
        vuetexte = gtk.TextView()
        buffer = vuetexte.get_buffer()
        fenetre_defil = gtk.ScrolledWindow()
        fenetre_defil.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        fenetre_defil.add(vuetexte)
        self.insert_text(buffer)
        fenetre_defil.show_all()
        return fenetre_defil
   
    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Fenêtre à volets")
        fenetre.connect("destroy", lambda w: gtk.main_quit())
        fenetre.set_border_width(10)
        fenetre.set_size_request(450, 400)

        # Crée une fenêtre à volets verticale et l'ajoute à la fenêtre principale
        vpaned = gtk.VPaned()
        fenetre.add(vpaned)
        vpaned.show()

        # Crée le contenu des deux moitiés de la fenêtre
        liste = self.create_list()
        vpaned.add1(liste)
        liste.show()

        texte = self.create_text()
        vpaned.add2(texte)
        texte.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleVolets()
    main()
