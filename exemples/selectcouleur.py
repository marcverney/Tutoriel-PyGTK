#!/usr/bin/env python

# exemple selectcouleur.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleSelecteurCouleur:
    # Gestionnaire du signal "color_changed"
    def rappel_color_changed(self, widget):
        # On recupere la table des couleurs de la zone de dessin
        tablecouleurs = self.zonedessin.get_colormap()

        # On recupere la couleur courante
        couleur = self.dialselectcouleur.colorsel.get_current_color()

        # On definit la couleur d'arriere plan de la fenetre
        self.zonedessin.modify_bg(gtk.STATE_NORMAL, couleur)

    # Gestionnaire d'evenement de la zone de dessin
    def evnmt_zone(self, widget, evnmt):
        prisencharge = False

        # On verifie si on a recu un evenement "button-press"
        if evnmt.type == gtk.gdk.BUTTON_PRESS:
            prisencharge = True

            # Creation de la boite de dialogue du selecteur de couleur
            if self.dialselectcouleur == None:
                self.dialselectcouleur = gtk.ColorSelectionDialog(
                    "Selection de la couleur d'arriere-plan")

            # On recupere le selecteur de couleur
            selectcouleur = self.dialselectcouleur.colorsel

            selectcouleur.set_previous_color(self.couleur)
            selectcouleur.set_current_color(self.couleur)
            selectcouleur.set_has_palette(True)

            # Connexion au signal "color_changed"
            selectcouleur.connect("color_changed", self.rappel_color_changed)
            # Affichage de la boite de dialogue
            reponse = self.dialselectcouleur.run()

            if reponse -- gtk.RESPONSE_OK:
                self.couleur = selectcouleur.get_current_color()
            else:
                self.zonedessin.modify_bg(gtk.STATE_NORMAL, self.couleur)

            self.dialselectcouleur.hide()

        return prisencharge

    # Fermeture et sortie du gestionnaire
    def destruct_fenetre(self, widget, evnmt):
        gtk.main_quit()
        return True

    def __init__(self):
        self.dialselectcouleur = None
        # Creation d'une fenetre racine + titre + modes
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Test de selection de couleur")
        fenetre.set_resizable(True)

        # Connexion aux evenements "delete" et "destroy" pour pouvoir sortir
        fenetre.connect("delete_event", self.destruct_fenetre)
  
        # Creation de la zone de dessin + taille + recup evnmts des boutons
        self.zonedessin = gtk.DrawingArea()

        self.couleur = self.zonedessin.get_colormap().alloc_color(0, 65535, 0)

        self.zonedessin.set_size_request(200, 200)
        self.zonedessin.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.zonedessin.connect("event", self.evnmt_zone)
  
        # Ajout de la zone de dessin a la fenetre, puis affichage des deux
        fenetre.add(self.zonedessin)
        self.zonedessin.show()
        fenetre.show()
  
def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleSelecteurCouleur()
    main()
