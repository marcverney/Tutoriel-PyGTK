#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example bloc_notes.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBlocNotes:
    # Cette méthode fait circuler la position des étiquettes
    def circule_bloc(self, bouton, bloc_notes):
        bloc_notes.set_tab_pos((bloc_notes.get_tab_pos()+1) %4)

    # Ajoute/supprime les onglets et bordures des pages
    def style_bloc(self, bouton, bloc_notes):
        val_onglet = False
        val_bord = False
        if self.show_tabs == False:
	    val_onglet = True 
        if self.show_border == False:
	    val_bord = True

        bloc_notes.set_show_tabs(val_onglet)
        self.show_tabs = val_onglet
        bloc_notes.set_show_border(val_bord)
        self.show_border = val_bord

    # Supprime une page du bloc-notes
    def supprime_bloc(self, bouton, bloc_notes):
        page = bloc_notes.get_current_page()
        bloc_notes.remove_page(page)
        # Il faut rafraîchir l'affichage du widget
        # Ceci oblige le widget à se redessiner
        bloc_notes.queue_draw_area(0,0,-1,-1)

    def delete(self, widget, event=None):
        gtk.main_quit()
        return False

    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.connect("delete_event", self.delete)
        fenetre.set_border_width(10)

        table = gtk.Table(3,6,False)
        fenetre.add(table)

        # Créer un nouveau bloc-notes, définir la position des onglets
        bloc_notes = gtk.Notebook()
        bloc_notes.set_tab_pos(gtk.POS_TOP)
        table.attach(bloc_notes, 0,6,0,1)
        bloc_notes.show()
        self.show_tabs = True
        self.show_border = True

        # On ajoute quelques pages au bloc-notes
        for i in range(5):
            bufferf = "Ajout après cadre %d" % (i+1)
            bufferl = "PostPage %d" % (i+1)

            cadre = gtk.Frame(bufferf)
            cadre.set_border_width(10)
            cadre.set_size_request(100, 75)
            cadre.show()

            label = gtk.Label(bufferf)
            cadre.add(label)
            label.show()

            label = gtk.Label(bufferl)
            bloc_notes.append_page(cadre, label)
      
        # Ajout d'une page à un endroit précis
        checkbouton = gtk.CheckButton("Cliquez moi svp !")
        checkbouton.set_size_request(100, 75)
        checkbouton.show ()

        label = gtk.Label("Ajout page")
        bloc_notes.insert_page(checkbouton, label, 2)

        # Enfin, ajout de page au début du bloc-notes
        for i in range(5):
            bufferf = "Ajout avant cadre %d" % (i+1)
            bufferl = "PréPage %d" % (i+1)

            cadre = gtk.Frame(bufferf)
            cadre.set_border_width(10)
            cadre.set_size_request(100, 75)
            cadre.show()

            label = gtk.Label(bufferf)
            cadre.add(label)
            label.show()

            label = gtk.Label(bufferl)
            bloc_notes.prepend_page(cadre, label)
    
        # Définir la page d'ouverture (page 4)
        bloc_notes.set_current_page(3)

        # Créer quelques boutons
        bouton = gtk.Button("fermer")
        bouton.connect("clicked", self.delete)
        table.attach(bouton, 0,1,1,2)
        bouton.show()

        bouton = gtk.Button("page suiv.")
        bouton.connect("clicked", lambda w: bloc_notes.next_page())
        table.attach(bouton, 1,2,1,2)
        bouton.show()

        bouton = gtk.Button("page préc.")
        bouton.connect("clicked", lambda w: bloc_notes.prev_page())
        table.attach(bouton, 2,3,1,2)
        bouton.show()

        bouton = gtk.Button("pos. onglet")
        bouton.connect("clicked", self.circule_bloc, bloc_notes)
        table.attach(bouton, 3,4,1,2)
        bouton.show()

        bouton = gtk.Button("onglet/bords")
        bouton.connect("clicked", self.style_bloc, bloc_notes)
        table.attach(bouton, 4,5,1,2)
        bouton.show()

        bouton = gtk.Button("supp. page")
        bouton.connect("clicked", self.supprime_bloc, bloc_notes)
        table.attach(bouton, 5,6,1,2)
        bouton.show()

        table.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleBlocNotes()
    main()
