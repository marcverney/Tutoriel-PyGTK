#!/usr/bin/env python

# exemple treeviewcolumn.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleTreeViewColumn:

    # ferme la fenetre et quitte
    def delete_event(self, widget, evemnt, donnees=None):
        gtk.main_quit()
        return False

    def fait_pb(self, tvcolumn, cell, modele, iter):
        stock = modele.get_value(iter, 1)
        pb = self.treeview.render_icon(stock, gtk.ICON_SIZE_MENU, None)
        cell.set_property('pixbuf', pb)
        return

    def __init__(self):
        # Creation d'une nouvelle fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.set_title("Exemple TreeViewColumn")

        #self.window.set_size_request(200, 200)

        self.fenetre.connect("delete_event", self.delete_event)

        # creation d'une liststore avec des colonnes chaine comme modele
        self.liststore = gtk.ListStore(str, str, str, 'gboolean')

        # creation d'une vue utilisant le liststore
        self.treeview = gtk.TreeView(self.liststore)

        # creation des colonnes pour afficher les donnees
        self.tvcolumn = gtk.TreeViewColumn('Pixbuf et Texte')
        self.tvcolumn1 = gtk.TreeViewColumn('Texte seul')

        # ajout d'une ligne avec texte et image stock item
        # couleurs (en format chaine) pour le fond
        self.liststore.append(['Ouvrir', gtk.STOCK_OPEN, 'Ouvrir un fichier', True])
        self.liststore.append(['Nouveau', gtk.STOCK_NEW, 'Nouveau fichier', True])
        self.liststore.append(['Imprimer', gtk.STOCK_PRINT, 'Imprimer fichier', False])

        # ajout des colonnes au treeview
        self.treeview.append_column(self.tvcolumn)
        self.treeview.append_column(self.tvcolumn1)

        # creation d'un CellRenderer pour le rendu des donnees
        self.cellpb = gtk.CellRendererPixbuf()
        self.cell = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()

        # definition de la couleur de fond
        self.cellpb.set_property('cell-background', 'yellow')
        self.cell.set_property('cell-background', 'cyan')
        self.cell1.set_property('cell-background', 'pink')


        # ajout des cells aux colonnes - la 2 en premier
        self.tvcolumn.pack_start(self.cellpb, False)
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn1.pack_start(self.cell1, True)

        # fixe les attributs du cell a la colonne idoine du liststore
        # GTK+ 2.0 ne comprend pas la propriete "stock_id"
        if gtk.gtk_version[1] < 2:
            self.tvcolumn.set_cell_data_func(self.cellpb, self.fait_pb)
        else:
            self.tvcolumn.set_attributes(self.cellpb, stock_id=1)
        self.tvcolumn.set_attributes(self.cell, text=0)
        self.tvcolumn1.set_attributes(self.cell1, text=2,
                                      cell_background_set=3)

        # autorise la recherche dans le treeview
        self.treeview.set_search_column(0)

        # autorise le classement dans la colonne
        self.tvcolumn.set_sort_column_id(0)

        # autorise le rearrangement par glisser-deposer
        self.treeview.set_reorderable(True)

        self.fenetre.add(self.treeview)

        self.fenetre.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    exempletvc = ExempleTreeViewColumn()
    main()
