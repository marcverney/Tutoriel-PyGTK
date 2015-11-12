#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple scrolledwin.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleScrolledWindow:
    def destroy(self, widget):
        gtk.main_quit()

    def __init__(self):
        # Créer une boîte de dialogue pour y placer 
        # la fenêtre à défilement 
        fenetre = gtk.Dialog()
        fenetre.connect("destroy", self.destroy)
        fenetre.set_title("Fenêtre à défilement")
        fenetre.set_border_width(0)
        fenetre.set_size_request(300, 300)

        # Créer une fenêtre à défilement.
        fenetre_defil = gtk.ScrolledWindow()
        fenetre_defil.set_border_width(10)

        # La gestion des barres est soit POLICY AUTOMATIC, soit  POLICY_ALWAYS.
        # POLICY_AUTOMATIC décide automatiquement s'il faut ou non des barres,
        # POLICY_ALWAYS met toujours des barres
        # Le premier paramètre correspond à la barre horizontale,
        # le second à la barre verticale. 
        fenetre_defil.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)

        # Créer une boîte de dialogue avec une boîte verticale.
        fenetre.vbox.pack_start(fenetre_defil, True, True, 0)
        fenetre_defil.show()
    
        # Créer une table de 10x10 cases.
        table = gtk.Table(10, 10, False)

        # Définir l'espacement des lignes et colonnes à 10 pixels.
        table.set_row_spacings(10)
        table.set_col_spacings(10)

        # Placer la table dans la fenêtre à défilement.
        fenetre_defil.add_with_viewport(table)
        table.show()

        # Créer une grille de boutons commutateurs dans la table
        # pour la démonstration de la fenêtre à défilement
        for i in range(10):
            for j in range(10):
                buffer = "bouton (%d,%d)" % (i, j)
                bouton = gtk.ToggleButton(buffer)
                table.attach(bouton, i, i+1, j, j+1)
                bouton.show()

        # Ajouter un bouton « Fermer » en bas de la boîte de dialogue.
        bouton = gtk.Button("Fermer")
        bouton.connect_object("clicked", self.destroy, fenetre)

        # Définir ce bouton en « bouton par défaut ».
        bouton.set_flags(gtk.CAN_DEFAULT)
        fenetre.action_area.pack_start(bouton, True, True, 0)

        # Récupèrer le bouton par défaut. Presser
        # la touche « Entrée » activera le bouton.
        bouton.grab_default()
        bouton.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleScrolledWindow()
    main()
