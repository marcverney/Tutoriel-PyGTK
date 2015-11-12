# !/usr/bin/env python
# coding: utf8
# exemple helloworld.py

import pygtk
pygtk.require('2.0')
import gtk

class SalutMonde:

    # Ceci est une fonction de rappel. Les arguments sont ignorés dans
    # cet exemple. Plus de précisions sur ces fonctions plus bas.
    def salut(self, widget, donnees=None):
        print "Salut tout le monde !"

    def evnmt_delete(self, widget, evenement, donnees=None):
        # Si on renvoie FALSE dans le gestionnaire du signal "evnmt_delete",
        # GTK émettra le signal "destroy". Renvoyer TRUE signifie que l'on
        # ne veut pas que la fenêtre soit détruite.
        # Ceci peut être utile pour faire apparaître des fenêtres
        # du type "Êtes vous sûr de vouloir quitter ?"
        print "Évènement delete survenu."

        # Changez FALSE par TRUE et la fenêtre principale ne 
        # sera pas détruite par un "delete_event"
        return False

    def destroy(self, widget, donnees=None):
        print "Évènement destroy survenu."
        gtk.main_quit()

    def __init__(self):
        # création d'une nouvelle fenêtre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # Quand la fenêtre reçoit le signal "delete_event" (donné par le
        # gestionnaire de fenêtres, généralement par l'option "fermer" ou
        # la croix de la barre de titre), on lui demande d'appeler la
        # fonction evnmt_delete() définie plus haut. On lui passe l'argument
        # NULL, qui est ignoré.
        self.fenetre.connect("delete_event", self.evnmt_delete)

        # Ici on connecte l'évènement "destroy" à un gestionnaire de signal.
        # Cet évènement se produit lorsqu'on invoque gtk_widget_destroy() sur
        # la fenêtre ou lorsque le gestionnaire du signal "delete" renvoie FALSE.
        self.fenetre.connect("destroy", self.destroy)

        # On fixe la largeur des bordures de la fenêtre.
        self.fenetre.set_border_width(10)

        # On crée un nouveau bouton avec l'étiquette "Salut tout le monde !".
        self.bouton = gtk.Button("Salut tout le monde !")

        # Lorsque le bouton reçoit le signal "clicked", il appelle la
        # fonction salut() et lui passe None comme argument. La fonction
        # salut() est définie plus haut.
        self.bouton.connect("clicked", self.salut, None)

        # Ceci entrainera la destruction de la fenêtre par l'appel de
        # gtk_widget_destroy(fenetre) si l'on clique le bouton. Encore une fois,
        # le signal "destroy" peut venir d'ici ou du gestionnaire de fenêtres.
        self.bouton.connect_object("clicked", gtk.Widget.destroy, self.fenetre)

        # On place le bouton dans la fenêtre (un conteneur GTK).
        self.fenetre.add(self.bouton)

        # La dernière étape consiste à afficher ce nouveau widget...
        self.bouton.show()

        # ...ainsi que la fenêtre
        self.fenetre.show()

    def boucle(self):
        # Toutes les applications PyGTK doivent avoir un gtk.main(). Arrivé à ce point,
        # le programme se met en attente d'un évènement (clic, appui d'une touche, etc.)
        gtk.main()

# Si le programme est lancé directement ou passé en argument à l'interpréteur 
# Python, ceci crée une instance de la classe SalutMonde et l'affiche
if __name__ == "__main__":
    salut = SalutMonde()
    salut.boucle()
