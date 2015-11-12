#!/usr/bin/env python

# exemple treemodelsort.py

import pygtk
pygtk.require('2.0')
import gtk
import random

class ExempleTreeModelSort:

    # ferme la fenetre et quitte
    def delete_event(self, widget, event, donnees=None):
        gtk.main_quit()
        return False

    def ajout_ligne(self, b):
        alea = self.alea
        # ajoute une ligne aleatoire d'entiers
        i0 = self.fenetre[0].sm.get_model().append([alea.randint(0, 1000),
                                              alea.randint(0, 1000000),
                                              alea.randint(-10000, 10000)])
        # selectionne la nouvelle ligne dans chaque vue
        for n in range(3):
            sel = self.fenetre[n].tv.get_selection()
            i1 = self.fenetre[n].sm.convert_child_iter_to_iter(None, i0)
            sel.select_iter(i1)

    def __init__(self):
        # cree un liststore avec trois colonnes d'entiers
        self.liststore = gtk.ListStore(int, int, int)

        # cree un generateur de nombres aleatoires
        self.alea = random.Random()

        # Cree les nouvelles fenetres
        self.fenetre = [None] * 3
        
        for n in range(3):
            self.fenetre[n] = gtk.Window(gtk.WINDOW_TOPLEVEL)
            fen = self.fenetre[n]
            fen.set_title("Exemple TreeModelSort %i" % n)
            fen.set_size_request(220, 200)
            fen.connect("delete_event", self.delete_event)
            fen.vbox = gtk.VBox()
            fen.add(fen.vbox)
            fen.sw = gtk.ScrolledWindow()
            fen.sm = gtk.TreeModelSort(self.liststore)
            # Installe le classement de colonne
            fen.sm.set_sort_column_id(n, gtk.SORT_ASCENDING)
            fen.tv = gtk.TreeView(fen.sm)
            fen.vbox.pack_start(fen.sw)
            fen.b = gtk.Button('Ajout ligne')
            fen.b.connect('clicked', self.ajout_ligne)
            fen.vbox.pack_start(fen.b, False)
            fen.sw.add(fen.tv)
            fen.tv.colonne = [None]*3
            fen.tv.colonne[0] = gtk.TreeViewColumn('0-1000')
            fen.tv.colonne[1] = gtk.TreeViewColumn('0-1000000')
            fen.tv.colonne[2] = gtk.TreeViewColumn('-10000-10000')
            fen.tv.cell = [None]*3
            for i in range(3):
                fen.tv.cell[i] = gtk.CellRendererText()
                fen.tv.append_column(fen.tv.colonne[i])
                fen.tv.colonne[i].set_sort_column_id(i)
                fen.tv.colonne[i].pack_start(fen.tv.cell[i], True)
                fen.tv.colonne[i].set_attributes(fen.tv.cell[i], text=i)
            fen.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    exempletms = ExempleTreeModelSort()
    main()
