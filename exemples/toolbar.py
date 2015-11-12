#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example barre_outils.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBarreOutils:
    # Cette méthode est connectée au bouton Fermer ou à la fermeture
    # de la fenêtre depuis le gestionnaire de fenêtre
    def delete_event(self, widget, event=None):
        gtk.main_quit()
        return False

    # Ceci est simple... quand l'un de ces boutons est commuté, 
    # on cherche lequel est actif et on régle le style de la
    # barre d'outils en conséquence.
    def change_radio(self, widget, barre_outils):
        if self.bouton_texte.get_active(): 
            barre_outils.set_style(gtk.TOOLBAR_TEXT)
        elif self.bouton_icone.get_active():
            barre_outils.set_style(gtk.TOOLBAR_ICONS)
        elif self.bouton_deux.get_active():
            barre_outils.set_style(gtk.TOOLBAR_BOTH)

    # Encore plus simple, on vérifie le bouton à bascule et on
    # autorise / interdit les infobulles
    def change_bascule(self, widget, barre_outils):
        barre_outils.set_tooltips(widget.get_active())

    def __init__(self):
        # Ici, la fenêtre principale (un dialogueue) et la boîte à poignée
        # Bon, on a besoin d'une barre d'outils, d'une icône avec un masque
        # (un pour tous les boutons) et un widget icône dans lequel la placer
        # (on crée un widget pour chaque bouton)
        # On crée une nouvelle fenêtre avec son titre, d'une taille adaptée
        dialogue = gtk.Dialog()
        dialogue.set_title("Exemple GTKToolbar")
        dialogue.set_size_request(450, 250)
        dialogue.set_resizable(True)

        # En général, on quitte quand quelqu'un essaie de nous fermer
        dialogue.connect("delete_event", self.delete_event)

        # Pour faire les chose bien, nous plaçons la barre d'outils dans une
        # boîte à poignée, ainsi elle peut être détachée de la fenêtre principale. 
        boite_poing = gtk.HandleBox()
        dialogue.vbox.pack_start(boite_poing, False, False, 5)

        # La barre d'outils sera horizontale, avec à la fois des icônes 
        # et du texte et un espace de 5 pixels entre les items. Enfin, 
        # nous la mettons dans notre boite à poignée. 
        barre_outils = gtk.Toolbar()
        barre_outils.set_orientation(gtk.ORIENTATION_HORIZONTAL)
        barre_outils.set_style(gtk.TOOLBAR_BOTH)
        barre_outils.set_border_width(5)
        boite_poing.add(barre_outils)

        # le premier item est le bouton "Fermer"
        img_icone = gtk.Image() # widget icône
        img_icone.set_from_file("gtk.xpm")
        bouton_fermer = barre_outils.append_item(
            "Fermer",               # étiquette du bouton
            "Fermer l'application", # infobulle du bouton
            "Privé",                # info privée du bouton
            img_icone,              # widget icône
            self.delete_event)      # un signal
        barre_outils.append_space() # espace après l'item

        # maintenant, on crée le groupe de boutons radio
        img_icone = gtk.Image() # widget icône
        img_icone.set_from_file("gtk.xpm")
        bouton_icone = barre_outils.append_element(
            gtk.TOOLBAR_CHILD_RADIOBUTTON, # type d'élément
            None,                          # widget
            "Icônes",                      # étiquette
            "Barre d'outils avec icônes uniquement",       # infobulle
            "Privé",                       # info privée du bouton
            img_icone,                     # icône
            self.change_radio,             # signal
            barre_outils)                  # donnée pour le signal
        barre_outils.append_space()
        self.bouton_icone = bouton_icone

        # les boutons radio suivants renvoient aux précédents
        img_icone = gtk.Image() # widget icône
        img_icone.set_from_file("gtk.xpm")
        bouton_texte = barre_outils.append_element(
            gtk.TOOLBAR_CHILD_RADIOBUTTON,
            bouton_icone,
            "Texte",
            "Barre d'outils avec texte uniquement",
            "Privé",
            img_icone,
            self.change_radio,
            barre_outils)
        barre_outils.append_space()
        self.bouton_texte = bouton_texte

        img_icone = gtk.Image() # widget icône
        img_icone.set_from_file("gtk.xpm")
        bouton_deux = barre_outils.append_element(
            gtk.TOOLBAR_CHILD_RADIOBUTTON,
            bouton_texte,
            "Les deux",
            "Barre d'outils avec icônes et texte",
            "Privé",
            img_icone,
            self.change_radio,
            barre_outils)
        barre_outils.append_space()
        self.bouton_deux = bouton_deux
        bouton_deux.set_active(True)

        # Ici un simple bouton à bascule
        img_icone = gtk.Image() # widget icône
        img_icone.set_from_file("gtk.xpm")
        bouton_info = barre_outils.append_element(
            gtk.TOOLBAR_CHILD_TOGGLEBUTTON,
            None,
            "Infobulles",
            "Barre d'outils avec/sans infobulles",
            "Privé",
            img_icone,
            self.change_bascule,
            barre_outils)
        barre_outils.append_space()
        bouton_info.set_active(True)

        # pour placer un élément dans la barre d'outils, il faut
        # seulement le créer et l'ajouter avec une infobulle adéquate
        zone_saisie = gtk.Entry()
        barre_outils.append_widget(zone_saisie,  "Juste une zone de saisie", "Privé")

        # il n'est pas créé dans la barre d'outils, il faut l'afficher
        zone_saisie.show()

        # C'est fait ! Affichons tout.
        barre_outils.show()
        boite_poing.show()
        dialogue.show()

def main():
    # On reste dans gtk_main et on attend que la fête commence !
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleBarreOutils()
    main()
