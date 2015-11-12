#!/usr/bin/env python

# exemple treeviewbasique.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleTreeViewBasique:

    # fermeture de la fenetre et sortie du programme
    def evnmt_delete(self, widget, evnmt, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Creation d'une nouvelle fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.set_title("Exemple TreeView simple")

        self.fenetre.set_size_request(200, 200)

        self.fenetre.connect("delete_event", self.evnmt_delete)

        # Creation d'un TreeStore avec une colonne de type chaine, pour servir
        # de modele
        self.treestore = gtk.TreeStore(str)

        # A present ajoutons des donnees : 4 lignes ayant 3 lignes filles
        # chacune
        for mere in range(4):
            m_iter = self.treestore.append(None, ['ligne mere %i' % mere])
            for fille in range(3):
                self.treestore.append(m_iter, ['ligne fille %i de la ligne %i'
                                                  % (fille, mere)])

        # creation du TreeView en utilisant notre TreeStore
        self.treeview = gtk.TreeView(self.treestore)

        # creation du TreeViewColumn pour afficher les donnees
        self.tvcolumn = gtk.TreeViewColumn('Colonne 0')

        # on place tvcolumn dans notre TreeView
        self.treeview.append_column(self.tvcolumn)

        # creation d'un CellRendererText pour afficher les donnees
        self.cell = gtk.CellRendererText()

        # on place cell dans le TreeViewColumn et on lui permet de s'etirer
        self.tvcolumn.pack_start(self.cell, True)

        # reglage de l'attribut "text" de cell sur la colonne 0 - recupere le
        # texte dans cette colonne du TreeStore
        self.tvcolumn.add_attribute(self.cell, 'text', 0)

        # on autorise la recherche
        self.treeview.set_search_column(0)

        # on autorise la classement de la colonne
        self.tvcolumn.set_sort_column_id(0)

        # on autorise le classement des lignes par glisser-deposer
        self.treeview.set_reorderable(True)

        self.fenetre.add(self.treeview)

        self.fenetre.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    exempletv = ExempleTreeViewBasique()
    main()
