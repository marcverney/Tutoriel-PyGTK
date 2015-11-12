#!/usr/bin/env python

# exemple treeviewdnd.py

import pygtk
pygtk.require('2.0')
import gtk

class TreeViewDnDExemple:

    CIBLES = [
        ('MY_TREE_MODEL_ROW', gtk.TARGET_SAME_WIDGET, 0),
        ('text/plain', 0, 1),
        ('TEXT', 0, 2),
        ('STRING', 0, 3),
        ]
    # fermer la fenetre et quitter
    def ferme_event(self, widget, event, donnees=None):
        gtk.main_quit()
        return False

    def efface_selection(self, bouton):
        selection = self.treeview.get_selection()
        modele, iter = selection.get_selected()
        if iter:
            modele.remove(iter)
        return

    def __init__(self):
        # Creer une nouvelle fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.set_title("Cache URL")

        self.fenetre.set_size_request(250, 200)

        self.fenetre.connect("delete_event", self.ferme_event)

        self.fen_deroule = gtk.ScrolledWindow()
        self.vboite = gtk.VBox()
        self.hboite = gtk.HButtonBox()
        self.vboite.pack_start(self.fen_deroule, True)
        self.vboite.pack_start(self.hboite, False)
        self.b0 = gtk.Button('Effacer tout')
        self.b1 = gtk.Button('Effacer selection')
        self.hboite.pack_start(self.b0)
        self.hboite.pack_start(self.b1)

        # pour modele, creer une liste avec une colonne contenant une chaine
        self.modeleliste = gtk.ListStore(str)

        # creer la vue arborescente utilisant le modeleliste
        self.treeview = gtk.TreeView(self.modeleliste)

        # creer un CellRenderer pour preparer les donnees
        self.cell = gtk.CellRendererText()

        # creer unTreeViewColumn pour afficher les donnees
        self.colonneTV = gtk.TreeViewColumn('URL', self.cell, text=0)

        # ajouter la colonne au treeview
        self.treeview.append_column(self.colonneTV)
        self.b0.connect_object('clicked', gtk.ListStore.clear, self.modeleliste)
        self.b1.connect('clicked', self.efface_selection)
        # autoriser la recherche dans le treeview
        self.treeview.set_search_column(0)

        # autoriser le tri pour la colonne
        self.colonneTV.set_sort_column_id(0)

        # Autoriser le glisser-deposer y compris interne a la colonne
        self.treeview.enable_model_drag_source( gtk.gdk.BUTTON1_MASK,
                                                self.CIBLES,
                                                gtk.gdk.ACTION_DEFAULT|
                                                gtk.gdk.ACTION_MOVE)
        self.treeview.enable_model_drag_dest(self.CIBLES,
                                             gtk.gdk.ACTION_DEFAULT)

        self.treeview.connect("drag_data_get", self.donnees_du_glisser)
        self.treeview.connect("drag_data_received",
                              self.donnees_du_deposer)

        self.fen_deroule.add(self.treeview)
        self.fenetre.add(self.vboite)
        self.fenetre.show_all()

    def donnees_du_glisser(self, treeview, context, selection, id_cible,
                           etime):
        treeselection = treeview.get_selection()
        modele, iter = treeselection.get_selected()
        donnees = modele.get_value(iter, 0)
        selection.set(selection.target, 8, donnees)

    def donnees_du_deposer(self, treeview, context, x, y, selection,
                                info, etime):
        modele = treeview.get_model()
        donnees = selection.data
        info_depot = treeview.get_dest_row_at_pos(x, y)
        if info_depot:
            chemin, position = info_depot
            iter = modele.get_iter(chemin)
            if (position == gtk.TREE_VIEW_DROP_BEFORE
                or position == gtk.TREE_VIEW_DROP_INTO_OR_BEFORE):
                modele.insert_before(iter, [donnees])
            else:
                modele.insert_after(iter, [donnees])
        else:
            modele.append([donnees])
        if context.action == gtk.gdk.ACTION_MOVE:
            context.finish(True, True, etime)
        return

def main():
    gtk.main()

if __name__ == "__main__":
    treeviewdndex = TreeViewDnDExemple()
    main()
