#!/usr/bin/env python

# exemple selectfichier.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleSelecteurFichier:
    # On recupere le nom du fichier choisi et on l'affiche dans la console
    def ok_fichier(self, w):
        print "%s" % self.selectfichier.get_filename()

    def destroy(self, widget):
        gtk.main_quit()

    def __init__(self):
        # Creation d'un nouveau widget de selection de fichier
        self.selectfichier = gtk.FileSelection("Selection de fichier")

        self.selectfichier.connect("destroy", self.destroy)
        # Connexion du bouton OK a la methode ok_fichier()
        self.selectfichier.ok_button.connect("clicked", self.ok_fichier)
    
        # Connexion du bouton Annuler a la destruction du widget
        self.selectfichier.cancel_button.connect("clicked",
                                         lambda w: self.selectfichier.destroy())
    
        # Definissons le fichier, comme s'il s'agissait d'une boite de dialogue
        # d'enregistrement de fichier et que nous donnions un fichier par defaut
        self.selectfichier.set_filename("pingouin.png")
    
        self.selectfichier.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleSelecteurFichier()
    main()
