#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class ExempleActionGroup:
    def __init__(self):
        # Créer la fenêtre de premier niveau
        window = gtk.Window()
        window.connect('destroy', lambda w: gtk.main_quit())
        window.set_size_request(300, -1)
        vbox = gtk.VBox()
        window.add(vbox)

        # Créer un groupe d'accélérateurs
        accelgroup = gtk.AccelGroup()
        # Ajouter le groupe à la fenêtre de premier niveau
        window.add_accel_group(accelgroup)

        # Créer un ActionGroup appelé  ExempleActionGroup
        actiongroup = gtk.ActionGroup('ExempleActionGroup')
        self.actiongroup = actiongroup

        # Créer un ToggleAction, etc.
        actiongroup.add_toggle_actions([('Volume', None, '_Volume', '<Control>v',
                                         'Niveau de son', self.mute_cb)])

        # Créer les actions
        actiongroup.add_actions([('Quitter', gtk.STOCK_QUIT, '_Quitter', None,
                                  'Quitter le programme', self.quit_cb),
                                 ('Fichier', None, '_Fichier'),
                                 ('Son', None, '_Son'),
                                 ('Modulation', None, '_Modulation')])
        actiongroup.get_action('Quitter').set_property('short-label', '_Quitte')

        # Créer quelques RadioActions
        actiongroup.add_radio_actions([('MA', None, 'M_A', '<Control>a',
                                        "Modulation d'amplitude", 0),
                                       ('MF', None, 'M_F', '<Control>f',
                                        'Modulation de fréquence', 1),
                                       ('BLU', None, '_BLU', '<Control>b',
                                        'Bande latérale unique', 2),
                                       ], 0, self.radioband_cb)
        for action in actiongroup.list_actions():
            action.set_accel_group(accelgroup)

        # Créer une barre de menus
        menubar = gtk.MenuBar()
        vbox.pack_start(menubar, False)

        # Créer l'élément de menu action Fichier
        file_menuitem = actiongroup.get_action('Fichier').create_menu_item()
        menubar.append(file_menuitem)

        # Créer le menu Fichier
        file_menu = gtk.Menu()
        file_menuitem.set_submenu(file_menu)

        # Créer l'élément de menu Quitter
        quitaction = actiongroup.get_action('Quitter')
        quititem = quitaction.create_menu_item()
        file_menu.append(quititem)

        # Créer et remplir le menu Son avec un élément de menu Volume
        sound_menuitem = actiongroup.get_action('Son').create_menu_item()
        menubar.append(sound_menuitem)
        sound_menu = gtk.Menu()
        sound_menuitem.set_submenu(sound_menu)
        muteaction = actiongroup.get_action('Volume')
        muteitem = muteaction.create_menu_item()
        sound_menu.append(muteitem)

        # Créer et remplir le menu Modulation
        radiobanditem = actiongroup.get_action('Modulation').create_menu_item()
        menubar.append(radiobanditem)
        radiobandmenu = gtk.Menu()
        radiobanditem.set_submenu(radiobandmenu)
        amaction = actiongroup.get_action('MA')
        amitem = amaction.create_menu_item()
        radiobandmenu.append(amitem)
        fmaction = actiongroup.get_action('MF')
        fmitem = fmaction.create_menu_item()
        radiobandmenu.append(fmitem)
        ssbaction = actiongroup.get_action('BLU')
        ssbitem = ssbaction.create_menu_item()
        radiobandmenu.append(ssbitem)

        # Créer une barre d'outils
        toolbar = gtk.Toolbar()
        toolbar.set_style(gtk.TOOLBAR_BOTH) # ajout traducteur
        vbox.pack_start(toolbar, False)

        # Créer un élément de barre d'outils délégué
        quittoolitem = quitaction.create_tool_item()
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

        # Créer les boutons pour contrôler la visibilité et sensitivité des actions
        buttonbox = gtk.HButtonBox()
        sensitivebutton = gtk.CheckButton('Sensitif')
        sensitivebutton.set_active(True)
        sensitivebutton.connect('toggled', self.toggle_sensitivity)
        visiblebutton = gtk.CheckButton('Visible')
        visiblebutton.set_active(True)
        visiblebutton.connect('toggled', self.toggle_visibility)
        # les ajouter à la boîte de bouton
        buttonbox.pack_start(sensitivebutton, False)
        buttonbox.pack_start(visiblebutton, False)
        vbox.pack_start(buttonbox)

        # On doit placer les infobulles après l'ajout de l'élément à la barre d'outils
        for action in actiongroup.list_actions():
            action.set_property('tooltip', action.get_property('tooltip'))

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
        print 'Programme terminé'
        gtk.main_quit()

    def toggle_sensitivity(self, b):
        self.actiongroup.set_sensitive(b.get_active())
        return

    def toggle_visibility(self, b):
        self.actiongroup.set_visible(b.get_active())
        return

if __name__ == '__main__':
    ba = ExempleActionGroup()
    gtk.main()
