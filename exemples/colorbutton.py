#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoutonCouleur:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        boitehor = gtk.HBox()
        fenetre.add(boitehor)
        label = gtk.Label('Couleur premier plan : ')
        boitehor.pack_start(label, False)
        boutoncouleur = gtk.ColorButton(gtk.gdk.color_parse('red'))
        boutoncouleur.set_use_alpha(True)
        boutoncouleur.set_title('Choisir une couleur')
        boutoncouleur.set_alpha(32767)
        boutoncouleur.connect('color-set', self.color_set_cb)
        boitehor.pack_start(boutoncouleur)
        fenetre.show_all()
        return

    def color_set_cb(self, boutoncouleur):
        color = boutoncouleur.get_color()
        alpha = boutoncouleur.get_alpha()
        print 'Vous avez choisi la couleur :', \
              color.red, color.green, color.blue, 'avec alpha:', alpha
        return

def main():
    gtk.main()


if __name__ == '__main__':
    ecb = ExempleBoutonCouleur()
    main()
