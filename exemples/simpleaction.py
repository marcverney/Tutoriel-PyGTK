#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class SimpleAction:
    def __init__(self):
        # Créer la fenêtre de premier niveau
        window = gtk.Window()
        window.set_size_request(70, 30)
        window.connect('destroy', lambda w: gtk.main_quit())

        # Créer un groupe de raccourcis
        groupe_rapide = gtk.AccelGroup()
        # Ajouter le groupe à la fenêtre de premier niveau
        window.add_accel_group(groupe_rapide)

        # Créer une action_quitte pour quitter le programme avec un élément de Stock
        action_quitte = gtk.Action('Quitter', None, None, gtk.STOCK_QUIT)
        # Connecter une fonction de rappel à l'action
        action_quitte.connect('activate', self.fonct_quitte)

        # Créer un ActionGroup appelé ActionSimple
        groupe_actions = gtk.ActionGroup('ActionSimple')
        # Ajouter l'action à groupe_actions avec un raccourci clavier
        # "None" signifie utiliser l'accélérateur de l'élément Stock
        groupe_actions.add_action_with_accel(action_quitte, None)

        ## Lier l'action au groupe_rapide
        action_quitte.set_accel_group(groupe_rapide)

        # Connecter l'accélérateur à l'action
        action_quitte.connect_accelerator()

        # Créer un bouton pour l'utiliser comme autre widget délégué
        bouton_quitter = gtk.Button()
        # l'ajouter à la fenêtre
        window.add(bouton_quitter)

        # Lier l'action à son widget délégué
        action_quitte.connect_proxy(bouton_quitter)

        window.show_all()
        return

    def fonct_quitte(self, b):
        print 'Quitter le programme'
        gtk.main_quit()

if __name__ == '__main__':
    sa = SimpleAction()
    gtk.main()
