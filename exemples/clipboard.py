#!/usr/bin/env python
# -*- coding:utf8 -*-
import pygtk
pygtk.require('2.0')
import gtk, gobject

class ClipboardInfo:
    pass

class ExempleClipboard:
    # met à jour le texte du bouton et l'infobulle
    def metajour_boutons(self):
        for i in range(len(self.clipboard_historique)):
            info = self.clipboard_historique[i]
            if info:
                bouton = self.boutons[i]
                if info.text:
                    bouton.set_label(' '.join(info.text[:16].split('\n')))
                if info.cibles:
                    # écrit l'info de cible dans l'infobulle
                    self.bulle_bouton.set_tip(bouton, info.cibles)
        return

    # gestionnaire de signal appelé quand le presse-papier renvoie la cible
    def clipboard_cibles_acceptees(self, clipboard, cibles, info):
        if cibles:
            # on doit supprimer les doublons à cause de Netscape
            cibl = {}
            for t in cibles:
                cibl[str(t)] = 0
            cibl = cibl.keys()
            cibl.sort()
            info.cibles = '\n'.join(cibl)
        else:
            info.cibles = None
            print 'Pas de cible pour :', info.text
        self.metajour_boutons()
        return

    def clipboard_texte_accepte(self, clipboard, texte, donnees):
        if not texte or texte == '':
            return
        cbi = ClipboardInfo()
        cbi.text = texte
        # insère en début et supprime doublons
        self.clipboard_historique = ([cbi]
                                  + [info for info in self.clipboard_historique
                                     if info and info.text<>texte])[:10]
        self.clipboard.request_targets(self.clipboard_cibles_acceptees, cbi)
        return

    # affiche le texte associé au bouton dans l'historique du presse-papier
    def bouton_clique(self, bouton):
        i = self.boutons.index(bouton)
        if self.clipboard_historique[i]:
            self.textbuffer.set_text(self.clipboard_historique[i].text)
        else:
            self.textbuffer.set_text('')
        return

    # recherche le texte du presse-papier
    def cherche_info_clipboard(self):
        self.clipboard.request_text(self.clipboard_texte_accepte)
        return True

    def installe_clipboard(self, bouton):
        texte = self.textbuffer.get_text(*self.textbuffer.get_bounds())
        self.clipboard.set_text(texte)
        return

    def __init__(self):
        nb_boutons = 10
        self.boutons = nb_boutons * [None]
        self.clipboard_historique = nb_boutons * [None]
        self.fenetre = gtk.Window()
        self.fenetre.set_title("Exemple de Clipboard")
        self.fenetre.connect("destroy", lambda w: gtk.main_quit())
        self.fenetre.set_border_width(0)
        boiteboutonV = gtk.VButtonBox()
        boiteboutonV.show()
        boiteboutonV.set_layout(gtk.BUTTONBOX_START)
        boiteH = gtk.HBox()
        boiteH.pack_start(boiteboutonV, False)
        boiteH.show()
        self.bulle_bouton = gtk.Tooltips()
        for i in range(nb_boutons):
            self.boutons[i] = gtk.Button(str(i)+"---")
            self.boutons[i].set_use_underline(False)
            boiteboutonV.pack_start(self.boutons[i])
            self.boutons[i].show()
            self.boutons[i].connect("clicked", self.bouton_clique)
        boiteV = gtk.VBox()
        boiteV.show()
        fenetredefil = gtk.ScrolledWindow()
        fenetredefil.show()
        self.vuetexte = gtk.TextView()
        self.vuetexte.show()
        self.vuetexte.set_size_request(200,100)
        self.vuetexte.set_wrap_mode(gtk.WRAP_CHAR)
        self.textbuffer = self.vuetexte.get_buffer()
        fenetredefil.add(self.vuetexte)
        boiteV.pack_start(fenetredefil)
        bouton = gtk.Button('Copy to Clipboard')
        bouton.show()
        bouton.connect('clicked', self.installe_clipboard)
        boiteV.pack_start(bouton, False)
        boiteH.pack_start(boiteV)
        self.fenetre.add(boiteH)
        self.fenetre.show()
        self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
        self.clipboard.request_text(self.clipboard_texte_accepte)
        gobject.timeout_add(1500, self.cherche_info_clipboard)
        return

def main():
  gtk.main()
  return 0

if __name__ == '__main__':
    cbe = ExempleClipboard()
    main()
