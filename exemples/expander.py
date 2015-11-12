#!/usr/bin/env python
# coding: utf8
import time
import pygtk
pygtk.require('2.0')
import gtk

class ExempleExpanseur:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        expanseur = gtk.Expander(None)
        fenetre.add(expanseur)
        boitehor = gtk.HBox()
        image = gtk.Image()
        image.set_from_stock(gtk.STOCK_OPEN, gtk.ICON_SIZE_BUTTON)
        label = gtk.Label(' Dossier Temps')
        boitehor.pack_start(image)
        boitehor.pack_start(label)
        expanseur.set_label_widget(boitehor)
        expanseur.connect('notify::expanded', self.fct_rappel_expanse)
        fenetre.show_all()
        return

    def fct_rappel_expanse(self, expanseur, params):
        if expanseur.get_expanded():
            #label = gtk.Label(time.ctime()) ### original
            label = gtk.Label(time.strftime('%a %d %b %Y %H:%M:%S', time.localtime())) ### modif traducteur
            label.show()
            expanseur.add(label)
        else:
            expanseur.remove(expanseur.child)
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ee = ExempleExpanseur()
    main()
