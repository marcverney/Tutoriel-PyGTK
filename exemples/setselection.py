#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple setselection.py

import pygtk
pygtk.require('2.0')
import gtk
import time

class SetSelectionExample:
    # Fonction de rappel quand l'utilisateur modifie la sélection.
    def selection_toggled(self, widget, window):
        if widget.get_active():
            self.have_selection = window.selection_owner_set("PRIMARY")
            # si réclamer la sélection échoue, on remet le bouton
            # dans l'état inactif.
            if not self.have_selection:
                widget.set_active(False)
        else:
            if self.have_selection:
                # Impossible de libérer la sélection en PyGTK,
                # on indique juste que l'on ne la possède pas.
                self.have_selection = False
        return

    # Appelé lorsqu'une autre application réclame la sélection.
    def selection_clear(self, widget, event):
        self.have_selection = False
        widget.set_active(False)
        return True

    # Fournit le temps actuel comme sélection.
    def selection_handle(self, widget, selection_data, info, time_stamp):
        current_time = time.time()
        timestr = time.asctime(time.localtime(current_time))

        # Quand on renvoie une chaîne unique, elle ne doit se terminer 
        # par une valeur nulle. Ceci le fait pour nous.
        selection_data.set_text(timestr, len(timestr))
        return

    def __init__(self):
        self.have_selection = False
        # Création de la fenêtre de niveau supérieur
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Set Selection")
        window.set_border_width(10)
        window.connect("destroy", lambda w: gtk.main_quit())
        self.window = window
        # Création d'une boîte évènement pour contenir le bouton 
        # car il n'a pas sa propre GdkWindow.
        eventbox = gtk.EventBox()
        eventbox.show()
        window.add(eventbox)
        
        # Création d'un bouton interrupteur pour agir avec la sélection
        selection_button = gtk.ToggleButton("Réclamer sélection")
        eventbox.add(selection_button)

        selection_button.connect("toggled", self.selection_toggled, eventbox)
        eventbox.connect_object("selection_clear_event", self.selection_clear,
                                selection_button)

        eventbox.selection_add_target("PRIMARY", "STRING", 1)
        eventbox.selection_add_target("PRIMARY", "COMPOUND_TEXT", 1)
        eventbox.connect("selection_get", self.selection_handle)
        selection_button.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    SetSelectionExample()
    main()
