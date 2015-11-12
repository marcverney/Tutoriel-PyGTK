#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoutonPolice:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        boitever = gtk.VBox()
        fenetre.add(boitever)
        boitehor = gtk.HBox()
        boitever.pack_start(boitehor, False)
        label = gtk.Label('Police actuelle : ')
        boitehor.pack_start(label, False)
        boutonpolice = gtk.FontButton('Monospace Italic 14')
        boutonpolice.set_use_font(True)
        boutonpolice.set_title('Choisir une police')
        boutonpolice.connect('font-set', self.fct_rappel_choixpolice)
        boitehor.pack_start(boutonpolice)
        self.boutonpolice = boutonpolice
        boitebouton = gtk.HButtonBox()
        boitever.pack_start(boitebouton, False)
        b = gtk.ToggleButton('le "use_font"', False)
        b.connect('toggled', self.fct_rappel_visupolice)
        b.set_active(True)
        boitebouton.pack_start(b)
        b = gtk.ToggleButton('le "use_size"', False)
        b.connect('toggled', self.fct_rappel_visutaille)
        b.set_active(False)
        boitebouton.pack_start(b)
        b = gtk.ToggleButton('le "show_style"', False)
        b.connect('toggled', self.fct_rappel_affichstyle)
        b.set_active(True)
        boitebouton.pack_start(b)
        b = gtk.ToggleButton('le "show_size"', False)
        b.connect('toggled', self.fct_rappel_affichtaille)
        b.set_active(True)
        boitebouton.pack_start(b)
        fenetre.show_all()
        return
    def fct_rappel_visupolice(self, togglebutton):
        self.boutonpolice.set_use_font(togglebutton.get_active())
        return
    def fct_rappel_visutaille(self, togglebutton):
        self.boutonpolice.set_use_size(togglebutton.get_active())
        return
    def fct_rappel_affichstyle(self, togglebutton):
        self.boutonpolice.set_show_style(togglebutton.get_active())
        return
    def fct_rappel_affichtaille(self, togglebutton):
        self.boutonpolice.set_show_size(togglebutton.get_active())
        return
    def fct_rappel_choixpolice(self, boutonpolice):
        police = boutonpolice.get_font_name()
        print 'Vous avez choisi la police : ', police
        return

def main():
    gtk.main()


if __name__ == '__main__':
    cbe = ExempleBoutonPolice()
    main()
