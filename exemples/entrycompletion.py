#!/usr/bin/env python
# coding: utf8
import time
import pygtk
pygtk.require('2.0')
import gtk

class ExempleCompletementEntree:
    def __init__(self):
        fenetre = gtk.Window()
        fenetre.connect('destroy', lambda w: gtk.main_quit())
        boitever = gtk.VBox()
        label = gtk.Label('Taper a, b, c ou d\npour compléter')
        boitever.pack_start(label)
        saisie = gtk.Entry()
        boitever.pack_start(saisie)
        fenetre.add(boitever)
        completement = gtk.EntryCompletion()
        self.liststore = gtk.ListStore(str)
        for s in ['ananas', 'banane', 'capri', 'comte', 'couleur',
                  'défi', 'défaut']:
            self.liststore.append([s])
        completement.set_model(self.liststore)
        saisie.set_completion(completement)
        completement.set_text_column(0)
        completement.connect('match-selected', self.match_cb)
        saisie.connect('activate', self.activate_cb)
        fenetre.show_all()
        return

    def match_cb(self, completement, model, iter):
        print model[iter][0], 'était sélectionné'
        return

    def activate_cb(self, saisie):
        texte = saisie.get_text()
        if texte:
            if text not in [ligne[0] for ligne in self.liststore]:
                self.liststore.append([texte])
                saisie.set_text('')
        return

def main():
    gtk.main()
    return

if __name__ == "__main__":
    ece = ExempleCompletementEntree()
    main()
