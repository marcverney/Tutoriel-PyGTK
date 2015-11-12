#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class BasicAction:
    def __init__(self):
        # Créer la fenêtre de premier niveau
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        vbox = gtk.VBox()
        vbox.show()
        window.add(vbox)

        # Créer un groupe de raccourcis
        groupe_rapide = gtk.AccelGroup()
        # Ajouter le groupe à la fenêtre de premier niveau
        window.add_accel_group(groupe_rapide)

        # Créer une action_quitte pour quitter le programme avec un élément de Stock
        action_quitte = gtk.Action('Quitter', '_Quittez moi ! ', 'Quitter le programme',
                            gtk.STOCK_QUIT)
        action_quitte.set_property('short-label', '_Quitter')
        # Connecter une fonction de rappel à l'action
        action_quitte.connect('activate', self.fonct_quitte)

        # Créer un ActionGroup appelé ActionBasic
        groupe_actions = gtk.ActionGroup('ActionBasic')
        # Ajouter l'action à groupe_actions avec un raccourci clavier
        # "None" signifie utiliser le raccourci de l'élément Stock
        groupe_actions.add_action_with_accel(action_quitte, None)

        # Lier l'action au groupe_rapide
        action_quitte.set_accel_group(groupe_rapide)

        # Créer une barre de menu
        barremenu = gtk.MenuBar()
        barremenu.show()
        vbox.pack_start(barremenu, False)

        # Créer une action "Fichier" et l'élément de menu correspondant
        action_fichier = gtk.Action('Fichier', '_Fichier', None, None)
        groupe_actions.add_action(action_fichier)
        elmenu_fichier = action_fichier.create_menu_item()
        barremenu.append(elmenu_fichier)

        # Créer le menu Fichier
        menu_fichier = gtk.Menu()
        elmenu_fichier.set_submenu(menu_fichier)

        # Créer  un élément de menu délégué
        menuitem = action_quitte.create_menu_item()
        menu_fichier.append(menuitem)

        # Créer une barre d'outils
        barreoutils = gtk.Toolbar()
        barreoutils.show()
        barreoutils.set_style(gtk.TOOLBAR_BOTH) # ajout traducteur
        vbox.pack_start(barreoutils, False)

        # Créer un élément de barre d'outils délégué
        elbarre1 = action_quitte.create_tool_item()
        barreoutils.insert(elbarre1, 0)

        # Créer et placer l'étiquette
        label = gtk.Label('''
Choisir Fichier->Quittez moi ! ou
cliquer sur le bouton Quitter de la barre d'outils ou
cliquer sur le bouton Quitter du bas ou
taper Control+q
pour sortir.
''')
        label.show()
        vbox.pack_start(label)

        # Créer un bouton pour l'utiliser comme autre widget délégué
        bouton_quitter = gtk.Button()
        # l'ajouter à la fenêtre
        vbox.pack_start(bouton_quitter, False)

        # Lier l'action à son widget délégué
        action_quitte.connect_proxy(bouton_quitter)
        # On doit placer l'infobulle après l'ajout de l'élément à la barre d'outils
        action_quitte.set_property('tooltip', action_quitte.get_property('tooltip'))
        les_infobulles = gtk.Tooltips()
        les_infobulles.set_tip(bouton_quitter, action_quitte.get_property('tooltip'))

        window.show()
        return

    def fonct_quitte(self, b):
        print 'On quitte le programme'
        gtk.main_quit()

if __name__ == '__main__':
    ba = BasicAction()
    gtk.main()
