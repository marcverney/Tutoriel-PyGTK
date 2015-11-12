#!/usr/bin/env python

import os, stat, time
import pygtk
pygtk.require('2.0')
import gtk

dossierxpm = [
    "17 16 7 1",
    "  c #000000",
    ". c #808000",
    "X c yellow",
    "o c #808080",
    "O c #c0c0c0",
    "+ c white",
    "@ c None",
    "@@@@@@@@@@@@@@@@@",
    "@@@@@@@@@@@@@@@@@",
    "@@+XXXX.@@@@@@@@@",
    "@+OOOOOO.@@@@@@@@",
    "@+OXOXOXOXOXOXO. ",
    "@+XOXOXOXOXOXOX. ",
    "@+OXOXOXOXOXOXO. ",
    "@+XOXOXOXOXOXOX. ",
    "@+OXOXOXOXOXOXO. ",
    "@+XOXOXOXOXOXOX. ",
    "@+OXOXOXOXOXOXO. ",
    "@+XOXOXOXOXOXOX. ",
    "@+OOOOOOOOOOOOO. ",
    "@                ",
    "@@@@@@@@@@@@@@@@@",
    "@@@@@@@@@@@@@@@@@"
    ]
dossierpb = gtk.gdk.pixbuf_new_from_xpm_data(dossierxpm)

fichierxpm = [
    "12 12 3 1",
    "  c #000000",
    ". c #ffff04",
    "X c #b2c0dc",
    "X        XXX",
    "X ...... XXX",
    "X ......   X",
    "X .    ... X",
    "X ........ X",
    "X .   .... X",
    "X ........ X",
    "X .     .. X",
    "X ........ X",
    "X .     .. X",
    "X ........ X",
    "X          X"
    ]
fichierpb = gtk.gdk.pixbuf_new_from_xpm_data(fichierxpm)

class Fichmodeleliste(gtk.GenericTreeModel):
    types_colonnes = (gtk.gdk.Pixbuf, str, long, str, str)
    noms_colonnes = ['Nom', 'Taille', 'Mode', 'Derniere modification']

    def __init__(self, dname=None):
        gtk.GenericTreeModel.__init__(self)
        if not dname:
            self.nomrep = os.path.expanduser('~')
        else:
            self.nomrep = os.path.abspath(dname)
        self.fichiers = [f for f in os.listdir(self.nomrep) if f[0] <> '.']
        self.fichiers.sort()
        self.fichiers = ['..'] + self.fichiers
        return

    def recup_nomchemin(self, chemin):
        nomfichier = self.fichiers[chemin[0]]
        return os.path.join(self.nomrep, nomfichier)

    def est_rep(self, chemin):
        nomfichier = self.fichiers[chemin[0]]
        nomchemin = os.path.join(self.nomrep, nomfichier)
        statutfich = os.stat(nomchemin)
        if stat.S_ISDIR(statutfich.st_mode):
            return True
        return False

    def recup_noms_colonnes(self):
        return self.noms_colonnes[:]

    def on_get_flags(self):
        return gtk.TREE_MODEL_LIST_ONLY|gtk.TREE_MODEL_ITERS_PERSIST

    def on_get_n_columns(self):
        return len(self.types_colonnes)

    def on_get_column_type(self, n):
        return self.types_colonnes[n]

    def on_get_iter(self, chemin):
        return self.fichiers[chemin[0]]

    def on_get_chemin(self, refligne):
        return self.fichiers.index(refligne)

    def on_get_value(self, refligne, colonne):
        fname = os.path.join(self.nomrep, refligne)
        try:
            statutfich = os.stat(fname)
        except OSError:
            return None
        mode = statutfich.st_mode
        if colonne is 0:
            if stat.S_ISDIR(mode):
                return dossierpb
            else:
                return fichierpb
        elif colonne is 1:
            return refligne
        elif colonne is 2:
            return statutfich.st_size
        elif colonne is 3:
            return oct(stat.S_IMODE(mode))
        return time.ctime(statutfich.st_mtime)

    def on_iter_next(self, refligne):
        try:
            i = self.fichiers.index(refligne)+1
            return self.fichiers[i]
        except IndexError:
            return None

    def on_iter_children(self, refligne):
        if refligne:
            return None
        return self.fichiers[0]

    def on_iter_has_child(self, refligne):
        return False

    def on_iter_n_children(self, refligne):
        if refligne:
            return 0
        return len(self.fichiers)

    def on_iter_nth_child(self, refligne, n):
        if refligne:
            return None
        try:
            return self.fichiers[n]
        except IndexError:
            return None

    def on_iter_parent(child):
        return None

class ExpModeleArbreGeneric:
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
 
    def __init__(self):
        # Creation d'une nouvelle fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
 
        self.fenetre.set_size_request(300, 200)
 
        self.fenetre.connect("delete_event", self.delete_event)
 
        self.modeleliste = Fichmodeleliste()
 
        # Creation du TreeView
        self.treeview = gtk.TreeView()
 
        # Creation des TreeViewColumn pour afficher les donnees
        noms_colonnes = self.modeleliste.recup_noms_colonnes()
        self.tvcolonne = [None] * len(noms_colonnes)
        cellpb = gtk.CellRendererPixbuf()
        self.tvcolonne[0] = gtk.TreeViewColumn(noms_colonnes[0],
                                              cellpb, pixbuf=0)
        cell = gtk.CellRendererText()
        self.tvcolonne[0].pack_start(cell, False)
        self.tvcolonne[0].add_attribute(cell, 'text', 1)
        self.treeview.append_column(self.tvcolonne[0])
        for n in range(1, len(noms_colonnes)):
            cell = gtk.CellRendererText()
            if n == 1:
                cell.set_property('xalign', 1.0)
            self.tvcolonne[n] = gtk.TreeViewColumn(noms_colonnes[n],
                                                  cell, text=n+1)
            self.treeview.append_column(self.tvcolonne[n])

        self.treeview.connect('row-activated', self.ouvrir_fichier)
        self.fenetredefilmt = gtk.ScrolledWindow()
        self.fenetredefilmt.add(self.treeview)
        self.fenetre.add(self.fenetredefilmt)
        self.treeview.set_model(self.modeleliste)
        self.fenetre.set_title(self.modeleliste.nomrep)
        self.fenetre.show_all()

    def ouvrir_fichier(self, treeview, chemin, colonne):
        modele = treeview.get_model()
        if modele.est_rep(chemin):
            nomchemin = modele.recup_nomchemin(chemin)
            nouv_modele = Fichmodeleliste(nomchemin)
            self.fenetre.set_title(nouv_modele.nomrep)
            treeview.set_model(nouv_modele)
        return
 
def main():
    gtk.main()

if __name__ == "__main__":
    exemplegtm = ExpModeleArbreGeneric()
    main()
