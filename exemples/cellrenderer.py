#!/usr/bin/env python
# vim: ts=4:sw=4:tw=78:nowrap
""" Exemple avec Cellrenderer modifiables et activables """
import pygtk
pygtk.require("2.0")
import gtk, gobject

taches =  {
    "Faire les courses": "Acheter une baguette",
    "Programmer": "Mettre a jour le programme",
    "Cuisiner": "Allumer le four",
    "Regarder la TV": "Enregistrer \"Urgences\""
    } 

class GUI_Controleur:
    """ La classe GUI est le controleur de l'application """
    def __init__(self):
        # Creation de la fenetre principale
        self.fenetre = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
        self.fenetre.set_title("Exemple de CellRenderer")
        self.fenetre.connect("destroy", self.evnmt_destroy)
        # On recupere le modele et on le relie a la vue
        self.modele = Ranger.recup_modele()
        self.vue = Afficher.cree_vue( self.modele )
        # Ajouter la vue a la fenetre principale
        self.fenetre.add(self.vue)
        self.fenetre.show_all()
        return
    def evnmt_destroy(self, *kw):
        """ Fonction de rappel pour fermer l'application """
        gtk.main_quit()
        return
    def lance(self):
        """ La fonction est appelee pour lancer la boucle principale GTK """
        gtk.main()
        return  

class InfoModele:
    """ La classe du modele contient l'information que nous voulons afficher """
    def __init__(self):
        """ Creation et remplissage du gtk.TreeStore """
        self.tree_store = gtk.TreeStore( gobject.TYPE_STRING,
                                         gobject.TYPE_BOOLEAN )
        # on place les donnees utilisateur globales dans une liste
        # on cree une arborescence simple.
        for item in taches.keys():
            lignemere = self.tree_store.append( None, (item, None) )
            self.tree_store.append( lignemere, (taches[item],None) )
        return
    def recup_modele(self):
        """ Renvoie le modele """
        if self.tree_store:
            return self.tree_store 
        else:
            return None

class AfficheModele:
    """ Affiche le modele InfoModele dans un treeview """
    def cree_vue( self, modele ):
        """ Cree une vue pour le Tree Model """
        self.vue = gtk.TreeView( modele )
        # Cree le CellRendererText et permet aux cellules
        # d'etre editees.
        self.renderer = gtk.CellRendererText()
        self.renderer.set_property( 'editable', True )
        self.renderer.connect( 'edited', self.rappel_edited_col0, modele )

        # Cree le CellRendererToggle et permet sa 
        # modification (toggled) par l'utilisateur.
        self.renderer1 = gtk.CellRendererToggle()
        self.renderer1.set_property('activatable', True)
        self.renderer1.connect( 'toggled', self.rappel_toggled_col1, modele )

        # On connecte la colonne 0 de l'affichage a la colonne 0 du modele
        # Le cellrenderer va alors afficher tout ce qui est en colonne 0 de
        # notre modele .
        self.colonne0 = gtk.TreeViewColumn("Nom", self.renderer, text=0)

        # L'etat actif des colonnes est relie a la seconde colonne
        # du modele. Ainsi, quand le modele indique True, le bouton
        # apparaitra comme actif.
        self.colonne1 = gtk.TreeViewColumn("Fait", self.renderer1 )
        self.colonne1.add_attribute( self.renderer1, "active", 1)
        self.vue.append_column( self.colonne0 )
        self.vue.append_column( self.colonne1 )
        return self.vue
    def rappel_edited_col0( self, cellrenderer, chemin, nouveau_texte, modele ):
        """
        Appele quand un texte est modifie. Il inscrit le nouveau texte
        dans le modele pour qu'il puisse etre affiche correctement.
        """
        print "Change '%s' en '%s'" % (modele[chemin][0], nouveau_texte)
        modele[chemin][0] = nouveau_texte
        return
    def rappel_toggled_col1( self, cellrenderer, chemin, modele ):
        """
        Fixe l'etat du bouton a bascule sur true ou false.
        """
        modele[chemin][1] = not modele[chemin][1]
        print "Valeur de '%s'  : %s" % (modele[chemin][0], modele[chemin][1],)
        return

if __name__ == '__main__':
    Ranger = InfoModele()	
    Afficher = AfficheModele()
    monGUI = GUI_Controleur()
    monGUI.lance()
