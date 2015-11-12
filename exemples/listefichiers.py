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

class ExplListeFichiersFoncDonnees:
    noms_colonnes = ['Nom', 'Taille', 'Mode', 'Derniere modification']

    def evnmt_delete(self, widget, evnmt, donnees=None):
        gtk.main_quit()
        return False
 
    def __init__(self, dossier = None):
        fonct_donnees_cell = (None, self.taille_fichier, self.mode_fichier,
                              self.modif_fichier)
 
        # Creation d'une nouvelle fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
 
        self.fenetre.set_size_request(400, 300)
 
        self.fenetre.connect("delete_event", self.evnmt_delete)
 
        modeleliste = self.creer_liste(dossier)
 
        # Creation du TreeView
        self.treeview = gtk.TreeView()
 
        # Creation des TreeViewColumn pour afficher les donnees
        self.tvcolumn = [None] * len(self.noms_colonnes)
        cellpb = gtk.CellRendererPixbuf()
        self.tvcolumn[0] = gtk.TreeViewColumn(self.noms_colonnes[0], cellpb)
        self.tvcolumn[0].set_cell_data_func(cellpb, self.fichier_pixbuf)
        cell = gtk.CellRendererText()
        self.tvcolumn[0].pack_start(cell, False)
        self.tvcolumn[0].set_cell_data_func(cell, self.nom_fichier)
        self.treeview.append_column(self.tvcolumn[0])
        for n in range(1, len(self.noms_colonnes)):
            cell = gtk.CellRendererText()
            self.tvcolumn[n] = gtk.TreeViewColumn(self.noms_colonnes[n], cell)
            if n == 1:
                cell.set_property('xalign', 1.0)
            self.tvcolumn[n].set_cell_data_func(cell, fonct_donnees_cell[n])
            self.treeview.append_column(self.tvcolumn[n])

        self.treeview.connect('row-activated', self.ouvrir_fichier)
        self.fenetredefilmt = gtk.ScrolledWindow()
        self.fenetredefilmt.add(self.treeview)
        self.fenetre.add(self.fenetredefilmt)
        self.treeview.set_model(modeleliste)
 
        self.fenetre.show_all()
        return

    def creer_liste(self, dossier=None):
        if not dossier:
            self.nomrep = os.path.expanduser('~')
        else:
            self.nomrep = os.path.abspath(dossier)
        self.fenetre.set_title(self.nomrep)
        fichiers = [f for f in os.listdir(self.nomrep) if f[0] <> '.']
        fichiers.sort()
        fichiers = ['..'] + fichiers
        modeleliste = gtk.ListStore(object)
        for f in fichiers:
            modeleliste.append([f])
        return modeleliste

    def ouvrir_fichier(self, treeview, chemin, colonne):
        modele = treeview.get_model()
        iter = modele.get_iter(chemin)
        nomfichier = os.path.join(self.nomrep, modele.get_value(iter, 0))
        statsfichier = os.stat(nomfichier)
        if stat.S_ISDIR(statsfichier.st_mode):
            nouvmodele = self.creer_liste(nomfichier)
            treeview.set_model(nouvmodele)
        return

    def fichier_pixbuf(self, colonne, cell, modele, iter):
        nomfichier = os.path.join(self.nomrep, modele.get_value(iter, 0))
        statsfichier = os.stat(nomfichier)
        if stat.S_ISDIR(statsfichier.st_mode):
            pb = dossierpb
        else:
            pb = fichierpb
        cell.set_property('pixbuf', pb)
        return

    def nom_fichier(self, colonne, cell, modele, iter):
        cell.set_property('text', modele.get_value(iter, 0))
        return

    def taille_fichier(self, colonne, cell, modele, iter):
        nomfichier = os.path.join(self.nomrep, modele.get_value(iter, 0))
        statsfichier = os.stat(nomfichier)
        cell.set_property('text', statsfichier.st_size)
        return

    def mode_fichier(self, colonne, cell, modele, iter):
        nomfichier = os.path.join(self.nomrep, modele.get_value(iter, 0))
        statsfichier = os.stat(nomfichier)
        cell.set_property('text', oct(stat.S_IMODE(statsfichier.st_mode)))
        return


    def modif_fichier(self, colonne, cell, modele, iter):
        nomfichier = os.path.join(self.nomrep, modele.get_value(iter, 0))
        statsfichier = os.stat(nomfichier)
        cell.set_property('text', time.ctime(statsfichier.st_mtime))
        return

def main():
    gtk.main()

if __name__ == "__main__":
    exemple = ExplListeFichiersFoncDonnees()
    main()
