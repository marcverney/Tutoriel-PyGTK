#!/usr/bin/env python

# exemple treemodelfilter.py

import pygtk
pygtk.require('2.0')
import gtk

bugdata="""120595 NEW Custom GtkTreeModelFilter wrappers need
121339 RESO dsextras.py installation directory is incorrect
121611 RESO argument is guint, should be guint32
121943 RESO gtk.mainiteration and gtk.mainloop defeat the caller's ex...
122260 RESO Could not compile
122569 NEW gtk.Window derived class segfaults
122591 RESO cannot return None from CellRenderer.on_start_editing
122755 RESO _wrap_gdk_window_new needs to ref return value
122786 RESO don't import Numeric until it is first used
123014 NEW PyGtk build problem on Win32 using the 'distutils' approach.
123037 NEW gtk.ListStore.set_column_types is missing
123456 RESO ItemFactory.create_items and <ImageItem> bug
123458 NEED pygtk does not wrap all of gdk-pixbuf
123891 NEW gobject.PARAM_CONSTRUCT problem
124181 NEED Python Shell inside a gtk GUI
124338 RESO Memleak when using pixbuf
124593 RESO TreeModel.iter_children should accept None as parent
125172 RESO gtk.TreeModelSort returns an unusable object
125272 RESO error in gtk_widget_translate_coordinates wrapping
125445 NEW pygtk gives no acces to PangoLayoutIter's
125533 RESO set_skip_taskbar_hint and set_skip_pager_hint not wrapped
126109 RESO gtk.Entry focus_out event core
126323 RESO gtk_disable_setlocale cannot be used
126406 RESO gtk.TreeView.expand_row() should return gboolean not None
126479 RESO None iter's in custom TreeModel cause SystemException's
127083 RESO Binding generation of methods which use gpointer does not...
127178 RESO gtk.Widget color modify methods do not allow None for col...
127504 NEW wrap GtkTreeViewColumnDropFunc
128623 RESO Allow NULL as set_tip argument
128988 RESO missing space in prototype confuses h2def.py
129032 NEW GObject Interfaces (GInterface) support
129414 RESO h2def.py doesn't see gda_log_enable()
129490 RESO Provide hardware_keycode to python
129754 RESO memory leak with gtk.gdk.pixmap_foreign_new()
129843 NEW Make all constructors work through g_object_new()
129966 RESO convert GValue containing GValueArray to PyObject
131837 RESO Cannot set or get \"markup\" property from CellRendererText
132040 NEW abusing setdefaultencoding()
132058 RESO gtkgl bus error on constructor to gtk.gl.Area
132507 RESO gtk_accel_group_connect seems to be missing
132837 NEW set_from_pixmap creates a different gtk.Image than set_fr...
133681 RESO memory leak in gdk.drawable.get_image
134462 RESO pygtk2 segfaults
134491 RESO OverflowError occurs when menu pops up.
134494 RESO The Definition of argument for gtk.gdk.Pixbuf.fill should...
135279 RESO codegen is using private functions
135439 RESO Integrate SDL into pygtk widgets
135963 RESO gc of gtk.ListStore aborts intrepeter after gtk.threads_i...
136204 RESO GtkTextSearchFlags warning
136205 RESO GdkPixbuf.fill passed arg changed type originating crash
136297 RESO Explanatory additions to gtk.DrawingArea
136597 RESO gtkgl still referenced in build files
136688 RESO installation directory of pygtk 2.2
136705 RESO mainquit vs. main_quit usage
136707 RESO gtk.gdk.Window.raise uses reserved keyword.
136731 RESO setup.py should not install the libglade DLL
136811 RESO h2def ignores some functions
136984 RESO Seemingly Invalid Flag for gtk.MessageDialog
136989 NEW should pixbufloader throw two GErrors?
137086 NEW gtk.gdk.window_lookup assertion
137091 RESO \"constants\" for selection atoms
137935 RESO description of gtk.gdk.atom_intern() should be in gtk.gdk...
137969 NEW GenericTreeModel/TreeSelection returning GtkTreeIter inst...
138104 RESO gtk_widget_style_get_property is not wrapped
138163 VERI NOTA gtk.main_iteration(TRUE) unblocks every .1 seconds
138476 RESO gtk.Layout is needed by gnome.canvas but is missing from ...
138487 RESO PyGTK Tutorial: in Calendar sample date string is 1 day b...
138576 RESO gtk.IconSet now has 2 constructors in gtk.defs, while on...
138619 UNCO codegen/definitions.py could use some refactoring
138772 RESO Callback parameters to input_add are incorrect
138804 UNCO In gtk2.4, gdk_font_get_display and gdk_pixmap_lookup is ...
138944 UNCO Cannot import gtk when pygtk installed using 'make install'
139128 UNCO All constructors should be defined as constructors
139130 NEW GtkEntry's constructor needs to be rewritten
139312 NEED gtk.gdk.Window.get_screen method undocumented.
139921 RESO Support tp_new
140071 NEW Register custom widget classes.
140665 RESO TypeError when creating user defined signals having third...
140718 UNCO Enhance codegen with user defined type wrapper.
140946 UNCO filechooser example broken
141042 RESO Garbage collection causes lossage in Pango
141886 UNCO Add a PyGEnum_Type
142030 RESO Possible ref count error in gtk.GC
142738 RESO Fatal error with multi-depth menus
142997 UNCO require() breaks sys.path if libs found in /usr/local/r/local"""

class TreeModelFilterExemple:

    # ferme la fenetre et quitte
    def delete_event(self, widget, event, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self):
        # Cree une nouvelle fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.fenetre.set_title("Exemple TreeModelFilter")

        self.fenetre.set_size_request(400, 400)

        self.fenetre.connect("delete_event", self.delete_event)

        # creea un liststore avec une colonne de type chaine comme modele
        self.liststore = gtk.ListStore(int, str, str)

        self.filtremodele = self.liststore.filter_new()

        # cree le TreeView
        self.treeview = gtk.TreeView()

        # cree les colonnes du TreeView pour afficher les donnees
        self.treeview.colonnes = [None]*3
        self.treeview.colonnes[0] = gtk.TreeViewColumn('Bug No.')
        self.treeview.colonnes[1] = gtk.TreeViewColumn('Statut')
        self.treeview.colonnes[2] = gtk.TreeViewColumn('Description')

        # ajoute les donnees de bug
        self.etats = []
        for line in bugdata.split('\n'):
            l = line.split()
            self.liststore.append([int(l[0]), l[1], ' '.join(l[2:])])
            if not l[1] in self.etats:
                self.etats.append(l[1])

        self.montre_etats = self.etats[:]
        self.filtremodele.set_visible_func(self.visible_cb, self.montre_etats)

        self.treeview.set_model(self.filtremodele)

        for n in range(3):
            # ajoute les colonnes au treeview
            self.treeview.append_column(self.treeview.colonnes[n])
            # cree un CellRenderers pour formater les donnees
            self.treeview.colonnes[n].cell = gtk.CellRendererText()
            # ajoute les cellules aux colonnes
            self.treeview.colonnes[n].pack_start(self.treeview.colonnes[n].cell,
                                                True)
            # fixe les attibuts de cellule a la colonne adequate
            self.treeview.colonnes[n].set_attributes(
                self.treeview.colonnes[n].cell, text=n)


        # autorise la recherche dans le treeview
        self.treeview.set_search_column(3)

        # cree l'interface utilisateur
        self.boitever = gtk.VBox()
        self.fen_deroule = gtk.ScrolledWindow()
        self.boite_bouton = gtk.HButtonBox()
        self.boitever.pack_start(self.fen_deroule)
        self.boitever.pack_start(self.boite_bouton, False)
        # cree un bouton bascule pour choisir les filtres utilises
        # selon l'etat des bugs et rend les boutons actifs
        for state in self.etats:
            bouton = gtk.ToggleButton(state)
            self.boite_bouton.pack_start(bouton)
            bouton.set_active(True)
            bouton.connect('toggled', self.verif_boutons)

        self.fen_deroule.add(self.treeview)
        self.fenetre.add(self.boitever)

        self.fenetre.show_all()
        return

    # determine la visibilite des donnees selon l'etat des boutons de filtre
    def visible_cb(self, modele, iter, donnees):
        return modele.get_value(iter, 1) in donnees

    # construit la liste des etats de bug a afficher et les filtre
    def verif_boutons(self, tb):
        del self.montre_etats[:]
        for bouton in self.boite_bouton.get_children():
            if bouton.get_active():
                self.montre_etats.append(bouton.get_label())
        self.filtremodele.refilter()
        return

def main():
    gtk.main()

if __name__ == "__main__":
    exempletmf = TreeModelFilterExemple()
    main()
