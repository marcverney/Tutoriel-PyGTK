#!/usr/bin/env python

# exemple pixmap.py

import pygtk
pygtk.require('2.0')
import gtk

# Donnees XPM d'une icone "Ouvrir Fichier"
donnees_xpm = [
"16 16 3 1",
"       c None",
".      c #000000000000",
"X      c #FFFFFFFFFFFF",
"                ",
"   ......       ",
"   .XXX.X.      ",
"   .XXX.XX.     ",
"   .XXX.XXX.    ",
"   .XXX.....    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .XXXXXXX.    ",
"   .........    ",
"                ",
"                "
]

class ExemplePixmap:
    # Si elle est invoquee (via le "delete_event"), cette fonction ferme l'application
    def fermer_application(self, widget, evnmt, data=None):
        gtk.main_quit()
        return False

    # Fonction invoquee par un clic sur le bouton. Elle affiche juste un message.
    def clic_bouton(self, widget, data=None):
        print "Clic sur le bouton"

    def __init__(self):
        # creation de la fenetre principale, et connexion du signal
        # delete_event a la fermeture de l'application
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.connect("delete_event", self.fermer_application)
        fenetre.set_border_width(10)
        fenetre.show()

        # venons-en a la creation du pixmap a partir des donnees XPM
        pixmap, masque = gtk.gdk.pixmap_create_from_xpm_d(fenetre.window,
                                                          None,
                                                          donnees_xpm)

        # Creation d'un widget gtk.Image pour contenir le pixmap
        image = gtk.Image()
        image.set_from_pixmap(pixmap, masque)
        image.show()

        # Creation d'un bouton pour contenir le gtk.Image
        bouton = gtk.Button()
        bouton.add(image)
        fenetre.add(bouton)
        bouton.show()

        bouton.connect("clicked", self.clic_bouton)

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExemplePixmap()
    main()
