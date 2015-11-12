#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple getselection.py

import pygtk
pygtk.require('2.0')
import gtk

class GetSelectionExample:
    # Gestionnaire de signal invoqué quand l'utilisateur
    # clique sur le bouton "Get String Target"
    def get_stringtarget(self, widget):
        # Et demande la cible "STRING" pour la sélection primaire
        ret = widget.selection_convert("PRIMARY", "STRING")
        return

    # Gestionnaire de signal invoqué quand l'utilisateur clique sur le bouton "Get Targets"
    def get_targets(self, widget):
        # Et demande la cible "TARGETS" pour la sélection primaire
        ret = widget.selection_convert("PRIMARY", "TARGETS")
        return

    # Gestionnaire de signal appelé quand le propriétaire de la sélection retourne les données
    def selection_received(self, widget, selection_data, data):
        # On s'assure que les données sont au bon format
        if str(selection_data.type) == "STRING":
            # On affiche la chaîne reçue
            print "STRING TARGET: %s" % selection_data.get_text()

        elif str(selection_data.type) == "ATOM":
            # On affiche la liste des cibles que l'on reçoit
            targets = selection_data.get_targets()
            for target in targets:
                name = str(target)
                if name != None:
                    print "%s" % name
                else:
                    print "(mauvaise cible)"
        else:
            print "La sélection n'est pas un \"STRING\" ou un \"ATOM\"!"

        return False
  

    def __init__(self):
        # Création de la fenêtre de niveau supérieur
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Get Selection")
        window.set_border_width(10)
        window.connect("destroy", lambda w: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        # Création du bouton pour obtenir la chaîne de la cible (de la sélection)
        button = gtk.Button("Contenu de la cible")
        eventbox = gtk.EventBox()
        eventbox.add(button)
        button.connect_object("clicked", self.get_stringtarget, eventbox)
        eventbox.connect("selection_received", self.selection_received)
        vbox.pack_start(eventbox)
        eventbox.show()
        button.show()

        # Création du bouton pour obtenir les formats de cibles acceptés
        button = gtk.Button("Liste des cibles")
        eventbox = gtk.EventBox()
        eventbox.add(button)
        button.connect_object("clicked", self.get_targets, eventbox)
        eventbox.connect("selection_received", self.selection_received)
        vbox.pack_start(eventbox)
        eventbox.show()
        button.show()

        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    GetSelectionExample()
    main()
