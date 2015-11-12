#!/usr/bin/env python
  
# exemple etiquettes.py

import pygtk
pygtk.require('2.0')
import gtk

class Etiquettes:
    def __init__(self):
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.fenetre.connect("destroy", gtk.main_quit)

        self.fenetre.set_title("Etiquettes")
        boite_v = gtk.VBox(False, 5)
        boite_h = gtk.HBox(False, 5)
        self.fenetre.add(boite_h)
        boite_h.pack_start(boite_v, False, False, 0)
        self.fenetre.set_border_width(5)

        cadre = gtk.Frame("Etiquette normale")
        etiquette = gtk.Label("Voici une etiquette normale")
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)
  
        cadre = gtk.Frame("Etiquette de plusieurs lignes")
        etiquette = gtk.Label("Voici une etiquette de plusieurs lignes.\nDeuxieme ligne\n"
                              "Troisieme ligne")
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)
  
        cadre = gtk.Frame("Etiquette alignee a gauche")
        etiquette = gtk.Label("Voici une etiquette de plusieurs lignes\n"
                              "dont le texte est aligne a gauche.\nTroisieme      ligne")
        etiquette.set_justify(gtk.JUSTIFY_LEFT)
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)
  
        cadre = gtk.Frame("Etiquette alignee a droite")
        etiquette = gtk.Label("Voici une etiquette de plusieurs lignes\ndont le texte est aligne a droite.\n"
                              "Quatrieme ligne, (j/k)")
        etiquette.set_justify(gtk.JUSTIFY_RIGHT)
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)

        boite_v = gtk.VBox(False, 5)
        boite_h.pack_start(boite_v, False, False, 0)
        cadre = gtk.Frame("Etiquette avec retour a la ligne auto")
        etiquette = gtk.Label("Voici un exemple d'etiquette avec retour a la ligne auto.  Elle "
                              "ne doit pas remplir l'espace qui lui est             "
                              "alloue, mais elle s'ajuste automatiquement "
                              "en renvoyant les mots a la ligne.  "
                              "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed "
                              "do eiusmod tempor incididunt ut labore et dolore magna aliqua.  "
                              "Seize jacinthes sechent dans seize sachets secs.\n"
                              "     Ces etiquettes peuvent contenir plusieurs paragraphes "
                              "et ajoutent   correctement "
                              "de nombreux          espaces supplementaires ")
        etiquette.set_line_wrap(True)
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)
  
        cadre = gtk.Frame("Etiquette justifiee avec retour a la ligne auto")
        etiquette = gtk.Label("Voici un exemple d'etiquette justifiee avec retour a la ligne auto.  "
                             "Elle doit remplir "
                             "entierement              l'espace qui lui est alloue.  "
                             "Quelques phrases pour les besoins de la "
                             "demonstration :  Voila, voila. Le lundi au soleil, "
                             "c'est une chose qu'on n'aura jamais, ta la la ta da la la...\n"
                             "    Nouveau paragraphe.\n"
                             "    Nouveau paragraphe, mais mieux que"
                             " l'autre.  Helas, il est deja fini.
                             ")
        etiquette.set_justify(gtk.JUSTIFY_FILL)
        etiquette.set_line_wrap(True)
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)
  
        cadre = gtk.Frame("Etiquette avec texte souligne")
        etiquette = gtk.Label("Cette etiquette comporte du texte souligne !\n"
                              "Cette phrase est bizarrement soulignee")
        etiquette.set_justify(gtk.JUSTIFY_LEFT)
        etiquette.set_pattern(
            "____________________________________________ _ _________ _ ______     __ _______ ___")
        cadre.add(etiquette)
        boite_v.pack_start(cadre, False, False, 0)
        self.fenetre.show_all ()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Etiquettes()
    main()
