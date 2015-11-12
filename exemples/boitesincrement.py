#!/usr/bin/env python

# exemple boiteincrement.py

import pygtk
pygtk.require('2.0')
import gtk

class ExempleBoiteIncrement:
    def modif_arrondi(self, widget, boiteincr):
        boiteincr.set_snap_to_ticks(widget.get_active())

    def modif_numerique(self, widget, boiteincr):
        boiteincr.set_numeric(widget.get_active())

    def modif_decimales(self, widget, boiteincr, boiteincr1):
        boiteincr1.set_digits(boiteincr.get_value_as_int())

    def recup_valeur(self, widget, donnees, boiteincr, boiteincr2, etiquette):
        if donnees == 1:
            tampon = "%d" % boiteincr.get_value_as_int()
        else:
            tampon = "%0.*f" % (boiteincr2.get_value_as_int(),
                                boiteincr.get_value())
        etiquette.set_text(tampon)

    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.connect("destroy", gtk.main_quit)
        fenetre.set_title("Boites d'increment")

        boite_v0 = gtk.VBox(False, 5)
        boite_v0.set_border_width(10)
        fenetre.add(boite_v0)

        cadre = gtk.Frame("Sans acceleration")
        boite_v0.pack_start(cadre, True, True, 0)
  
        boite_v1 = gtk.VBox(False, 0)
        boite_v1.set_border_width(5)
        cadre.add(boite_v1)

        # Boites d'increment pour le jour, le mois et l'annee
        boite_h = gtk.HBox(False, 0)
        boite_v1.pack_start(boite_h, True, True, 5)
  
        boite_v2 = gtk.VBox(False, 0)
        boite_h.pack_start(boite_v2, True, True, 5)

        etiquette = gtk.Label("Jour :")
        etiquette.set_alignment(0, 0.5)
        boite_v2.pack_start(etiquette, False, True, 0)
  
        ajustement = gtk.Adjustment(1.0, 1.0, 31.0, 1.0, 5.0, 0.0)
        boiteincr = gtk.SpinButton(ajustement, 0, 0)
        boiteincr.set_wrap(True)
        boite_v2.pack_start(boiteincr, False, True, 0)
  
        boite_v2 = gtk.VBox(False, 0)
        boite_h.pack_start(boite_v2, True, True, 5)
  
        etiquette = gtk.Label("Mois :")
        etiquette.set_alignment(0, 0.5)
        boite_v2.pack_start(etiquette, False, True, 0)

        ajustement = gtk.Adjustment(1.0, 1.0, 12.0, 1.0, 5.0, 0.0)
        boiteincr = gtk.SpinButton(ajustement, 0, 0)
        boiteincr.set_wrap(True)
        boite_v2.pack_start(boiteincr, False, True, 0)
  
        boite_v2 = gtk.VBox(False, 0)
        boite_h.pack_start(boite_v2, True, True, 5)
  
        etiquette = gtk.Label("Annee :")
        etiquette.set_alignment(0, 0.5)
        boite_v2.pack_start(etiquette, False, True, 0)
  
        ajustement = gtk.Adjustment(1998.0, 0.0, 2100.0, 1.0, 100.0, 0.0)
        boiteincr = gtk.SpinButton(ajustement, 0, 0)
        boiteincr.set_wrap(False)
        boiteincr.set_size_request(55, -1)
        boite_v2.pack_start(boiteincr, False, True, 0)
  
        cadre = gtk.Frame("Avec acceleration")
        boite_v0.pack_start(cadre, True, True, 0)
  
        boite_v1 = gtk.VBox(False, 0)
        boite_v1.set_border_width(5)
        cadre.add(boite_v1)
  
        boite_h = gtk.HBox(False, 0)
        boite_v1.pack_start(boite_h, False, True, 5)
  
        boite_v2 = gtk.VBox(False, 0)
        boite_h.pack_start(boite_v2, True, True, 5)
  
        etiquette = gtk.Label("Valeur :")
        etiquette.set_alignment(0, 0.5)
        boite_v2.pack_start(etiquette, False, True, 0)
  
        ajustement = gtk.Adjustment(0.0, -10000.0, 10000.0, 0.5, 100.0, 0.0)
        boiteincr1 = gtk.SpinButton(ajustement, 1.0, 2)
        boiteincr1.set_wrap(True)
        boiteincr1.set_size_request(100, -1)
        boite_v2.pack_start(boiteincr1, False, True, 0)
  
        boite_v2 = gtk.VBox(False, 0)
        boite_h.pack_start(boite_v2, True, True, 5)
  
        etiquette = gtk.Label("Decimales :")
        etiquette.set_alignment(0, 0.5)
        boite_v2.pack_start(etiquette, False, True, 0)
  
        ajustement = gtk.Adjustment(2, 1, 5, 1, 1, 0)
        boiteincr2 = gtk.SpinButton(ajustement, 0.0, 0)
        boiteincr2.set_wrap(True)
        ajustement.connect("value_changed", self.modif_decimales, boiteincr2, boiteincr1)
        boite_v2.pack_start(boiteincr2, False, True, 0)
  
        boite_h = gtk.HBox(False, 0)
        boite_v1.pack_start(boite_h, False, True, 5)

        bouton = gtk.CheckButton("Deplacement tous les 0,5")
        bouton.connect("clicked", self.modif_arrondi, boiteincr1)
        boite_v1.pack_start(bouton, True, True, 0)
        bouton.set_active(True)
  
        bouton = gtk.CheckButton("Saisie numerique seulement")
        bouton.connect("clicked", self.modif_numerique, boiteincr1)
        boite_v1.pack_start(bouton, True, True, 0)
        bouton.set_active(True)
  
        etiquette_valeur = gtk.Label("")
  
        boite_h = gtk.HBox(False, 0)
        boite_v1.pack_start(boite_h, False, True, 5)
        bouton = gtk.Button("Valeur entiere")
        bouton.connect("clicked", self.recup_valeur, 1, boiteincr1, boiteincr2,
                       etiquette_valeur)
        boite_h.pack_start(bouton, True, True, 5)
  
        bouton = gtk.Button("Valeur decimale")
        bouton.connect("clicked", self.recup_valeur, 2, boiteincr1, boiteincr2,
                       etiquette_valeur)
        boite_h.pack_start(bouton, True, True, 5)
  
        boite_v1.pack_start(etiquette_valeur, True, True, 0)
        etiquette_valeur.set_text("0")
  
        boite_h = gtk.HBox(False, 0)
        boite_v0.pack_start(boite_h, False, True, 0)
  
        bouton = gtk.Button("Fermer")
        bouton.connect("clicked", gtk.main_quit)
        boite_h.pack_start(bouton, True, True, 5)
        fenetre.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleBoiteIncrement()
    main()
