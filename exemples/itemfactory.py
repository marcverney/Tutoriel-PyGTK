#!/usr/bin/env python
  
# exemple itemfactory.py
  
import pygtk
pygtk.require('2.0')
import gtk
  
class ExempleItemFactory:
    # L'inevitable petite fonction de rappel
    def affiche_hello(self, w, donnees):
        print "Salut tout le monde !"

    # Voici la structure d'ItemFactoryEntry utilisee pour generer de nouveaux menus
    # Element 1: Le chemin du menu. la lettre qui suit le caractere "_" indique un 
    #            raccourci clavier actif une fois le menu ouvert.
    # Element 2: Le raccourci clavier pour cette entree.
    # Element 3: La fonction de rappel.
    # Element 4: L'action de la fonction de rappel. Modifie les parametres avec
    #            lesquels la fonction de rappel est appelee. 0 par defaut.
    # Element 5: Le type d'entree. Indique quelle sorte d'entree l'on souhaite creer.
    #            Voici les differentes valeurs possibles :

    #       NULL               -> "<Item>"
    #       ""                 -> "<Item>"
    #       "<Title>"          -> cree une entree titre
    #       "<Item>"           -> cree une entree simple
    #       "<CheckItem>"      -> cree une entree a cocher
    #       "<ToggleItem>"     -> cree une entree a bascule
    #       "<RadioItem>"      -> cree une entree radio
    #       <chemin>           -> chemin d'une entree radio a laquelle attacher celle-ci
    #       "<Separator>"      -> cree un separateur
    #       "<Branch>"         -> cree une entree pouvant contenir des sous-entrees (optionel)
    #       "<LastBranch>"     -> cree une entree "Branch" alignee a droite

    def menu_principal(self, fenetre):
        racc_clavier = gtk.AccelGroup()

        # Cette fonction initialise l'ItemFactory.
        # Param 1: Le type de menu - peut etre MenuBar, Menu,
        #          ou OptionMenu.
        # Param 2: Le chemin du menu.
        # Param 3: une reference a un AccelGroup. L'ItemFactory configure
        #          la table des raccourcis en generant les menus.
        item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", racc_clavier)

        # Cette methode genere les entrees du menu. On transmet a l'ItemFactory
        # la liste des entrees de menu.
        item_factory.create_items(self.entrees_menu)

        # On attache le nouveau groupe de raccourcis clavier a la fenetre.
        fenetre.add_accel_group(racc_clavier)

        # On a besoin de garder une reference a item_factory pour empecher sa destruction
        self.item_factory = item_factory
        # Enfin, on renvoie la barre de menus creee par l'ItemFactory.
        return item_factory.get_widget("<main>")

    def __init__(self):
        self.entrees_menu = (
            ( "/_Fichier",         None,         None, 0, "<Branch>" ),
            ( "/Fichier/_Nouveau",     "<control>N", self.affiche_hello, 0, None ),
            ( "/Fichier/_Ouvrir",    "<control>O", self.affiche_hello, 0, None ),
            ( "/Fichier/_Enregistrer",    "<control>S", self.affiche_hello, 0, None ),
            ( "/Fichier/Enregistrer _sous", None,         None, 0, None ),
            ( "/Fichier/sep1",     None,         None, 0, "<Separator>" ),
            ( "/Fichier/Quitter",     "<control>Q", gtk.main_quit, 0, None ),
            ( "/_Options",      None,         None, 0, "<Branch>" ),
            ( "/Options/Test",  None,         None, 0, None ),
            ( "/_Aide",         None,         None, 0, "<LastBranch>" ),
            ( "/_Aide/A propos",   None,         None, 0, None ),
            )
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.connect("destroy", gtk.main_quit, "WM destroy")
        fenetre.set_title("ItemFactory")
        fenetre.set_size_request(300, 200)

        boitev_princ = gtk.VBox(False, 1)
        boitev_princ.set_border_width(1)
        fenetre.add(boitev_princ)
        boitev_princ.show()

        barremenus = self.menu_principal(fenetre)

        boitev_princ.pack_start(barremenus, False, True, 0)
        barremenus.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleItemFactory()
    main()
