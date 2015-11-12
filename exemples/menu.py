#!/usr/bin/env python
   
# exemple menu.py
  
import pygtk
pygtk.require('2.0')
import gtk

class ExempleMenu:
    def __init__(self):
        # Creation d'une fenetre
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_size_request(200, 100)
        fenetre.set_title("Test menu GTK")
        fenetre.connect("delete_event", gtk.main_quit)

        # Initialisation du widget. Souvenez-vous : on n'affiche jamais
        # (avec show()) le widget menu !
        # Il s'agit du menu qui contiendra les commandes, celui qui apparaitra
        # apres un clic sur le "Menu racine" de l'application.
        menu = gtk.Menu()

        # Ensuite, on ecrit une petite boucle qui cree trois entrees pour le menu.
        # Notez l'appel a gtk_menu_append. Ici, nous ajoutons une liste de commandes
        # a notre menu. Nous devrions aussi nous debrouiller pour capter le signal
        # "clicked" de chacune des commandes et mettre en place une fonction de rappel
        # pour le traiter, mais pour ne pas faire trop long on s'en passera ici.
        for i in range(3):
            # On copie les noms dans une variable "tampon".
            tampon = "Sous-menu test - %d" % i

            # On cree une nouvelle commande , avec un nom...
            commandes = gtk.MenuItem(tampon)

            # ... et on l'ajoute au menu
            menu.append(commandes)

	    # On reagit a la selection de la commande
	    commandes.connect("activate", self.reponse_commande, tampon)

            # On affiche le widget
            commandes.show()

        # Voici le menu racine. Ce sera aussi l'etiquette visible dans la barre de
        # menus. On ne lui connecte pas de gestionnaire de signal, son role etant
        # seulement de faire apparaitre le reste du menu lorsqu'on le clique.
        menu_racine = gtk.MenuItem("Menu racine")

        menu_racine.show()

        # Ici on indique que notre "menu" cree plus haut doit etre le menu de 
        # "Menu racine"
        menu_racine.set_submenu(menu)

        # Une boite verticale pour y placer un menu et un bouton :
        boitev = gtk.VBox(False, 0)
        fenetre.add(boitev)
        boitev.show()

        # On cree une barre pour contenir les menus, et on la place dans notre fenetre
        barre_menus = gtk.MenuBar()
        boitev.pack_start(barre_menus, False, False, 2)
        barre_menus.show()

        # Creation d'un bouton, auquel on attache le menu comme popup
        bouton = gtk.Button("Cliquez-moi")
        bouton.connect_object("event", self.evnmt_button_press, menu)
        boitev.pack_end(bouton, True, True, 2)
        bouton.show()

        # Enfin, on rattache la commande a la barre de menus -- il s'agit de la commande
        # "Menu racine" sur laquelle je me suis emballe =)
        barre_menus.append (menu_racine)

        # Toujours afficher la fenetre en dernier, afin qu'elle soit complete lors de
        # son apparition a l'ecran.
        fenetre.show()

    # On repond a l'evenement "button-press" en affichant un menu, qui est
    # transmis comme "widget".
    # Notez que l'argument "widget" N'EST PAS le bouton qui a ete enfonce,
    # mais bien le menu a afficher
    def evnmt_button_press(self, widget, evenement):
        if evenement.type == gtk.gdk.BUTTON_PRESS:
            widget.popup(None, None, None, evenement.button, evenement.time)
            # On fait savoir au code appelant que l'on a traite l'evenement. Son
            # histoire s'arrete ici.
            return True
        # On fait savoir au code appelant que l'evenement n'a pas ete traite. Il continue.
        return False

    # Affiche une chaine de caracteres lorsqu'une commande est selectionnee.
    def reponse_commande(self, widget, chaine):
        print "%s" % chaine

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleMenu()
    main()
