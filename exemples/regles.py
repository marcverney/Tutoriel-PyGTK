#!/usr/bin/env python

# exemple regles.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleRegles:
    TAILLE_X = 400
    TAILLE_Y = 400

    # Cette routine prend le controle lorsque on clique sur le bouton fermer
    def fermer_application(self, widget, evnmt, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.connect("delete_event", self.fermer_application)
        fenetre.set_border_width(10)

        # Creation d'un tableau pour le placement des regles et de la zone de dessin
        tableau = gtk.Table(3, 2, False)
        fenetre.add(tableau)

        zonedess = gtk.DrawingArea()
        zonedess.set_size_request(self.TAILLE_X, self.TAILLE_Y)
        tableau.attach(zonedess, 1, 2, 1, 2,
                       gtk.EXPAND|gtk.FILL, gtk.FILL, 0, 0)
        zonedess.set_events(gtk.gdk.POINTER_MOTION_MASK |
                            gtk.gdk.POINTER_MOTION_HINT_MASK )

        # La regle horizontale va en haut. Quand la souris passe dans la zone de dessin,
        # un "motion_notify-event" est transmis au gestionnaire d'evenement approprie,
        # qui le passe a son tour a la regle.
        regle_h = gtk.HRuler()
        regle_h.set_metric(gtk.PIXELS)
        regle_h.set_range(7, 13, 0, 20)
        def notif_mouvmt(regle, evnmt):
            return regle.emit("motion_notify_event", evnmt)
        zonedess.connect_object("motion_notify_event", notif_mouvmt, regle_h)
        tableau.attach(regle_h, 1, 2, 0, 1,
                       gtk.EXPAND|gtk.SHRINK|gtk.FILL, gtk.FILL, 0, 0 )

        # La regle verticale va a gauche. Quand la souris passe dans la zone de dessin,
        # un "motion_notify-event" est transmis au gestionnaire d'evenement approprie,
        # qui le passe a son tour a la regle.
        regle_v = gtk.VRuler()
        regle_v.set_metric(gtk.PIXELS)
        regle_v.set_range(0, self.TAILLE_Y, 10, self.TAILLE_Y)
        zonedess.connect_object("motion_notify_event", notif_mouvmt, regle_v)
        tableau.attach(regle_v, 0, 1, 1, 2,
                       gtk.FILL, gtk.EXPAND|gtk.SHRINK|gtk.FILL, 0, 0 )

        # On affiche tout
        zonedess.show()
        regle_h.show()
        regle_v.show()
        tableau.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleRegles()
    main()
