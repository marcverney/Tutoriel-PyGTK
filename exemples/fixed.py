#!/usr/bin/env python
# -*- coding:utf-8 -*-
# exemple fixed.py

import pygtk
pygtk.require('2.0')
import gtk

class ExemplePlace:
    # Cette méthode de rappel déplace le bouton dans
    # le conteneur Place vers une nouvelle position
    def deplace_bouton(self, widget):
        self.x = (self.x+30)%300
        self.y = (self.y+50)%300
        self.Place.move(widget, self.x, self.y) 

    def __init__(self):
        self.x = 50
        self.y = 50

        # On crée une nouvelle fenêtre
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Conteneur Place")

        # On connecte l'évènement "destroy" au gestionnaire de signal 
        fenetre.connect("destroy", lambda w: gtk.main_quit())
 
        # On indique la largeur des bordures de la fenêtre
        fenetre.set_border_width(10)

        # On crée le conteneur Place
        self.Place = gtk.Fixed()
        fenetre.add(self.Place)
        self.Place.show()
  
        for i in range(1, 4):
            # On crée un bouton avec un label "Appuyez !"
            bouton = gtk.Button("Appuyez !")
  
           # Lorsque le bouton reçoit le signal "clicked", 
            # il appelle la méthode deplace_bouton().
            bouton.connect("clicked", self.deplace_bouton)
  
            # Ceci place le bouton dans la fenêtre du conteneur
            self.Place.put(bouton, i*50, i*50)
  
            # La dernière tâche est d'afficher ce nouveau bouton.
            bouton.show()

        # On affiche la fenêtre
        fenetre.show()

def main():
    # Boucle principale
    gtk.main()
    return 0

if __name__ == "__main__":
    ExemplePlace()
    main()
