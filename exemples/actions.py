#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class ActionExemple:
    def __init__(self):
        # Créer la fenêtre de premier niveau
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        window.set_size_request(300, -1)
        vbox = gtk.VBox()
        window.add(vbox)

        # Créer un groupe de raccourcis
        groupe_rapide = gtk.AccelGroup()
        # Ajouter le groupe à la fenêtre de premier niveau
        window.add_accel_group(groupe_rapide)

        # Créer un ActionGroup appelé  ExempleAction
        groupe_actions = gtk.ActionGroup('ExempleAction')

        # Créer une action_quitte pour quitter le programme avec un élément de Stock
        action_quitte = gtk.Action('Quitter', '_Quitter moi !', 'Quitter le programme',
                            gtk.STOCK_QUIT)
        action_quitte.set_property('short-label', '_Quitter')
        # Connecter une fonction de rappel à l'action
        action_quitte.connect('activate', self.quit_cb)

        # Ajouter l'action à groupe_actions avec un raccourci clavier
    	# "None" signifie utiliser le raccourci de l'élément Stock
        groupe_actions.add_action_with_accel(action_quitte, None)

        # Lier l'action au groupe_rapide
        action_quitte.set_accel_group(groupe_rapide)

        # Connecter l'accélérateur à l'action
        action_quitte.connect_accelerator()

        # Créer un ToggleAction, etc.
        muteaction = gtk.ToggleAction('Volume', '_Volume', 'Niveau de son', None)
        groupe_actions.add_action_with_accel(muteaction, '<Control>v')
        muteaction.set_accel_group(groupe_rapide)
        muteaction.connect_accelerator()
        muteaction.connect('toggled', self.mute_cb)

        # Créer quelques RadioActions
        amaction = gtk.RadioAction('MA', 'M_A',"Modulation d'amplitude", None, 0)
        groupe_actions.add_action_with_accel(amaction, '<Control>a')
        amaction.set_accel_group(groupe_rapide)
        amaction.connect_accelerator()
        amaction.set_active(True)

        fmaction = gtk.RadioAction('MF', 'M_F', 'Modulation de fréquence', None, 1)
        groupe_actions.add_action_with_accel(fmaction, '<Control>f')
        fmaction.set_accel_group(groupe_rapide)
        fmaction.connect_accelerator()
        fmaction.set_group(amaction)

        ssbaction = gtk.RadioAction('BLU', '_BLU', 'Bande latérale unique',
                                    None, 2)
        groupe_actions.add_action_with_accel(ssbaction, '<Control>b')
        ssbaction.set_accel_group(groupe_rapide)
        ssbaction.connect_accelerator()
        ssbaction.connect('changed', self.radioband_cb)
        ssbaction.set_group(amaction)

        # Créer une barre de menus
        menubar = gtk.MenuBar()
        vbox.pack_start(menubar, False)

        # Créer l'Action Fichier et l'élément de menu
        file_action = gtk.Action('Fichier', '_Fichier', None, None)
        groupe_actions.add_action(file_action)
        file_menuitem = file_action.create_menu_item()
        menubar.append(file_menuitem)

        # Créer le menu Fichier
        file_menu = gtk.Menu()
        file_menuitem.set_submenu(file_menu)

        # Créer un élément de menu délégué
        quititem = action_quitte.create_menu_item()
        file_menu.append(quititem)

        # Créer et remplir le menu Son avec un élément de menu Volume
        sound_action = gtk.Action('Son', '_Son', None, None)
        groupe_actions.add_action(sound_action)
        sound_menuitem = sound_action.create_menu_item()
        menubar.append(sound_menuitem)
        sound_menu = gtk.Menu()
        sound_menuitem.set_submenu(sound_menu)
        muteitem = muteaction.create_menu_item()
        sound_menu.append(muteitem)

        # Créer et remplir le menu Modulation
        radioband_action = gtk.Action('Modulation', '_Modulation', None, None)
        groupe_actions.add_action(radioband_action)
        radioband_menuitem = radioband_action.create_menu_item()
        menubar.append(radioband_menuitem)
        radioband_menu = gtk.Menu()
        radioband_menuitem.set_submenu(radioband_menu)
        amitem = amaction.create_menu_item()
        radioband_menu.append(amitem)
        fmitem = fmaction.create_menu_item()
        radioband_menu.append(fmitem)
        ssbitem = ssbaction.create_menu_item()
        radioband_menu.append(ssbitem)

        # Créer une barre d'outils
        toolbar = gtk.Toolbar()
        vbox.pack_start(toolbar, False)
        toolbar.set_style(gtk.TOOLBAR_BOTH) # ajout traducteur

        # Créer un élément de barre d'outils délégué
        quittoolitem = action_quitte.create_tool_item()
        toolbar.insert(quittoolitem, 0)

        # Créer un séparateur
        separator = gtk.SeparatorToolItem()
        toolbar.insert(separator, -1)

        # Créer les éléments toggle et radio et les ajouter à la barre d'outils
        mutetoolitem = muteaction.create_tool_item()
        toolbar.insert(mutetoolitem, -1)
        separator = gtk.SeparatorToolItem()
        toolbar.insert(separator, -1)
        amtoolitem = amaction.create_tool_item()
        toolbar.insert(amtoolitem, -1)
        fmtoolitem = fmaction.create_tool_item()
        toolbar.insert(fmtoolitem, -1)
        ssbtoolitem = ssbaction.create_tool_item()
        toolbar.insert(ssbtoolitem, -1)

        # Créer et placer deux étiquettes
        label = gtk.Label('Son non établi')
        vbox.pack_start(label)
        self.mutelabel = label
        label = gtk.Label('Mode MA')
        vbox.pack_start(label)
        self.bandlabel = label

        # Créer un bouton pour l'utiliser comme autre widget délégué
        
        quitbutton = gtk.Button()
        # l'ajouter à la fenêtre
        vbox.pack_start(quitbutton, False)

        # Lier l'action à son widget délégué
        action_quitte.connect_proxy(quitbutton)
        # On doit placer l'infobulle après l'ajout de l'élément à la barre d'outils
        for action in groupe_actions.list_actions():
            action.set_property('tooltip', action.get_property('tooltip'))
        tooltips = gtk.Tooltips()
        tooltips.set_tip(quitbutton, action_quitte.get_property('tooltip'))

        window.show_all()
        return

    def mute_cb(self, action):
        # action n'est pas encore réalisée
        text = ('établi', 'non établi')[action.get_active()==False]
        self.mutelabel.set_text('Son %s' % text)
        return

    def radioband_cb(self, action, current):
        text = ('MA', 'MF', 'BLU')[action.get_current_value()]
        self.bandlabel.set_text('Mode %s' % text)
        return

    def quit_cb(self, b):
        print 'Quitter programme'
        gtk.main_quit()

if __name__ == '__main__':
    ba = ActionExemple()
    gtk.main()
