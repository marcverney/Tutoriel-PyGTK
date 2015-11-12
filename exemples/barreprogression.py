#!/usr/bin/env python
  
# exemple barreprogression.py

import pygtk
pygtk.require('2.0')
import gtk

# Fonction qui actualise la valeur de la barre de progression
# pour qu'on ait un petit peu de mouvement
def tempo_progression(objetbarre):
    if objetbarre.case_activite.get_active():
        objetbarre.barreprogression.pulse()
    else:
        # On calcule la valeur de la barre de progression en prenant
        # en compte l'intervalle defini dans l'ajustement
        nouv_val = objetbarre.barreprogression.get_fraction() + 0.01
        if nouv_val > 1.0:
            nouv_val = 0.0
        # On fixe la nouvelle valeur
        objetbarre.barreprogression.set_fraction(nouv_val)

    # Cette fonction etant une fonction de temporisation, on
    # renvoie TRUE afin qu'elle puisse encore etre appelee
    return True

class BarreProgression:
    # Fonction de rappel qui active ou desactive l'affichage du texte
    # dans la coulisse de la barre de progression
    def modif_affich_texte(self, widget, data=None):
        if widget.get_active():
            self.barreprogression.set_text("exemple de texte")
        else:
            self.barreprogression.set_text("")

    # Fonction de rappel qui active ou desactive le mode "activite" de
    # la barre de progression
    def modif_mode(self, widget, data=None):
        if widget.get_active():
            self.barreprogression.pulse()
        else:
            self.barreprogression.set_fraction(0.0)

    # Fonction de rappel qui modifie l'orientation de la barre de progression
    def modif_orientation(self, widget, data=None):
        if self.barreprogression.get_orientation() == gtk.PROGRESS_LEFT_TO_RIGHT:
            self.barreprogression.set_orientation(gtk.PROGRESS_RIGHT_TO_LEFT)
        elif self.barreprogression.get_orientation() == gtk.PROGRESS_RIGHT_TO_LEFT:
            self.barreprogression.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)

    # Liberation de la memoire reservee et retrait de la temporisation
    def sortie(self, widget, data=None):
        gtk.timeout_remove(self.tempo)
        self.tempo = 0
        gtk.main_quit()

    def __init__(self):
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.fenetre.set_resizable(True)

        self.fenetre.connect("destroy", self.sortie)
        self.fenetre.set_title("Barre de progression")
        self.fenetre.set_border_width(0)

        boite_v = gtk.VBox(False, 5)
        boite_v.set_border_width(10)
        self.fenetre.add(boite_v)
        boite_v.show()
  
        # Creation d'un objet alignement au centre
        align = gtk.Alignment(0.5, 0.5, 0, 0)
        boite_v.pack_start(align, False, False, 5)
        align.show()

        # Creation de la barre de progression en utilisant l'ajustement
        self.barreprogression = gtk.ProgressBar()

        align.add(self.barreprogression)
        self.barreprogression.show()

        # On ajoute une fonction de rappel temporisee, qui actualisera
        # la valeur de la barre de progression
        self.tempo = gtk.timeout_add (100, tempo_progression, self)

        separateur = gtk.HSeparator()
        boite_v.pack_start(separateur, False, False, 0)
        separateur.show()

        # lignes, colonnes, homogene
        tableau = gtk.Table(2, 2, False)
        boite_v.pack_start(tableau, False, True, 0)
        tableau.show()

        # Ajout d'une case a cocher pour l'affichage du texte dans la coulisse
        case = gtk.CheckButton("Afficher le texte")
        tableau.attach(case, 0, 1, 0, 1,
                       gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL,
                       5, 5)
        case.connect("clicked", self.modif_affich_texte)
        case.show()

        # Ajout d'une case a cocher pour activer ou desactiver le mode "activite"
        self.case_activite = case = gtk.CheckButton("Mode activite")
        tableau.attach(case, 0, 1, 1, 2,
                       gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL,
                       5, 5)
        case.connect("clicked", self.modif_mode)
        case.show()

        # Ajout d'une case a cocher pour modifier l'orientation
        case = gtk.CheckButton("De droite a gauche")
        tableau.attach(case, 0, 1, 2, 3,
                       gtk.EXPAND | gtk.FILL, gtk.EXPAND | gtk.FILL,
                       5, 5)
        case.connect("clicked", self.modif_orientation)
        case.show()

        # Ajout d'un bouton pour quitter le programme
        bouton = gtk.Button("Fermer")
        bouton.connect("clicked", self.sortie)
        boite_v.pack_start(bouton, False, False, 0)

        # Ceci fait en sorte que le bouton puisse etre le widget par defaut
        bouton.set_flags(gtk.CAN_DEFAULT)

        # Ceci fait du bouton le bouton par defaut. Le simple fait d'appuyer
        # sur la touche "Enter" l'activera
        bouton.grab_default ()
        bouton.show()

        self.fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    BarreProgression()
    main()
