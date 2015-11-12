#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

class ExempleUIGestion:
    ui = '''<ui>
    <menubar name="BarreMenu">
      <menu action="Fichier">
        <menuitem action="Quitter"/>
      </menu>
      <menu action="Son">
        <menuitem action="Volume"/>
      </menu>
      <menu action="Modulation">
        <menuitem action="MA"/>
        <menuitem action="MF"/>
        <menuitem action="BLU"/>
      </menu>
    </menubar>
    <toolbar name="BarreOutils">
      <toolitem action="Quitter"/>
      <separator/>
      <toolitem action="Volume"/>
      <separator/>
      <placeholder name="ElementsMod">
        <toolitem action="MA"/>
        <toolitem action="MF"/>
        <toolitem action="BLU"/>
      </placeholder>
    </toolbar>
    </ui>'''
      
    def __init__(self):
        # Créer la fenêtre de premier niveau
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        fenetre.set_size_request(300, -1)
        vbox = gtk.VBox()
        fenetre.add(vbox)

        # Créer une instance du UIManager
        gestionui = gtk.UIManager()

        # Ajouter le groupe de raccourcis à la fenêtre de premier niveau
        grouperacc = gestionui.get_accel_group()
        fenetre.add_accel_group(grouperacc)

        # Créer un ActionGroup
        groupeactions = gtk.ActionGroup('ExempleUIGestion')
        self.groupeactions = groupeactions

        # Créer une ToggleAction, etc.
        groupeactions.add_toggle_actions([('Volume', None, '_Volume', '<Control>v',
                                         'Niveau de son', self.rappel_volume)])

        # Créer les actions
        groupeactions.add_actions([('Quitter', gtk.STOCK_QUIT, '_Quitter moi !', None,
                                  'Quitter le programme', self.rappel_quitte),
                                 ('Fichier', None, '_Fichier'),
                                 ('Son', None, '_Son'),
                                 ('Modulation', None, '_Modulation')])
        groupeactions.get_action('Quitter').set_property('short-label', '_Quitter')

        # Créer quelques RadioActions
        groupeactions.add_radio_actions([('MA', None, '_MA', '<Control>m',
                                        "Modulation d'amplitude", 0),
                                       ('MF', None, 'M_F', '<Control>f',
                                        'Modulation de fréquence', 1),
                                       ('BLU', None, '_BLU', '<Control>b',
                                        'Bande latérale unique', 2),
                                       ], 0, self.rappel_modulation)

        # Ajouter le groupe d'action au gestionnaire d'interface
        gestionui.insert_action_group(groupeactions, 0)

        # Ajouter une description d'Interface Utilisateur
        gestionui.add_ui_from_string(self.ui)

        # Créer la barre de menus
        barremenus = gestionui.get_widget('/BarreMenu')
        vbox.pack_start(barremenus, False)

        # Créer la barre d'outils
        barreoutils = gestionui.get_widget('/BarreOutils')
        vbox.pack_start(barreoutils, False)

        # Créer et placer deux étiquettes
        label = gtk.Label('Son non établi')
        vbox.pack_start(label)
        self.textevolume = label
        label = gtk.Label('Modulation MA')
        vbox.pack_start(label)
        self.bandlabel = label

        # Créer les boutons pour contrôler la sensibilité et la visibilité des actions
        buttonbox = gtk.HButtonBox()
        boutonsensible = gtk.CheckButton('Sensible')
        boutonsensible.set_active(True)
        boutonsensible.connect('toggled', self.change_sensible)
        boutonvisible = gtk.CheckButton('Visible')
        boutonvisible.set_active(True)
        boutonvisible.connect('toggled', self.change_visible)
        # les ajouter à la boîte à boutons
        buttonbox.pack_start(boutonsensible, False)
        buttonbox.pack_start(boutonvisible, False)
        vbox.pack_start(buttonbox)

        fenetre.show_all()
        return

    def rappel_volume(self, action):
        # action n'est pas encore réalisée
        texte = ('établi', 'non établi')[action.get_active()==False]
        self.textevolume.set_text('Son %s' % texte)
        return

    def rappel_modulation(self, action, current):
        text = ('MA', 'MF', 'BLU')[action.get_current_value()]
        self.bandlabel.set_text('Mode %s' % text)
        return

    def rappel_quitte(self, b):
        print 'Quitter le programme'
        gtk.main_quit()

    def change_sensible(self, b):
        self.groupeactions.set_sensitive(b.get_active())
        return

    def change_visible(self, b):
        self.groupeactions.set_visible(b.get_active())
        return

if __name__ == '__main__':
    ba = ExempleUIGestion()
    gtk.main()
