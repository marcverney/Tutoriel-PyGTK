#!/usr/bin/env python

# exemple calendrier.py
#
# Copyright (C) 1998 Cesar Miquel, Shawn T. Amundson, Mattias Gronlund
# Copyright (C) 2000 Tony Gale
# Copyright (C) 2001-2002 John Finlay
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import pygtk
pygtk.require('2.0')
import gtk, pango
import time

class ExempleCalendrier:
    DEF_ESP = 10
    DEF_PETIT_ESP = 5
    ANNEE_BASE = 1900

    calendrier_affich_entete = 0
    calendrier_affich_jours = 1
    calendrier_change_mois = 2 
    calendrier_affich_semaine = 3

    def calendrier_date_chaine(self):
        annee, mois, jour = self.fenetre.get_date()
        date = time.mktime((annee, mois+1, jour, 0, 0, 0, 0, 0, -1))
        return time.strftime("%x", time.localtime(date))

    def calendrier_chaines_signaux(self, chaine_signal):
        penult_sig = self.penult_sig.get()
        self.apenult_sig.set_text(penult_sig)

        penult_sig = self.dern_sig.get()
        self.penult_sig.set_text(penult_sig)
        self.dern_sig.set_text(chaine_signal)

    def calendrier_change_mois(self, widget):
        tampon = "month_changed : %s" % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

    def calendrier_selec_jour(self, widget):
        tampon = "day_selected : %s" % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

    def calendrier_selec_jour_dbleclic(self, widget):
        tampon = "day_selected_double_click : %s"
        tampon = tampon % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

        annee, mois, jour = self.fenetre.get_date()

        if self.date_marquee[jour-1] == 0:
            self.fenetre.mark_day(jour)
            self.date_marquee[jour-1] = 1
        else:
            self.fenetre.unmark_day(jour)
            self.date_marquee[jour-1] = 0

    def calendrier_mois_prec(self, widget):
        tampon = "prev_month : %s" % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

    def calendrier_mois_suiv(self, widget):
        tampon = "next_month : %s" % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

    def calendrier_annee_prec(self, widget):
        tampon = "prev_year : %s" % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

    def calendrier_annee_suiv(self, widget):
        tampon = "next_year : %s" % self.calendrier_date_chaine()
        self.calendrier_chaines_signaux(tampon)

    def calendrier_def_drapeaux(self):
        options = 0
        for i in range(5):
            if self.reglages[i]:
                options = options + (1<<i)
        if self.fenetre:
            self.fenetre.display_options(options)

    def calendrier_drapeau_coche(self, caseacocher):
        j = 0
        for i in range(5):
            if self.cases_drapeaux[i] == caseacocher:
                j = i

        self.reglages[j] = not self.reglages[j]
        self.calendrier_def_drapeaux()

    def calendrier_police_selection_ok(self, bouton):
        self.police = self.dialogue_police.get_font_name()
        if self.fenetre:
            desc_police = pango.FontDescription(self.police)
            if desc_police: 
                self.fenetre.modify_font(desc_police)

    def calendrier_selec_police(self, bouton):
        if not self.dialogue_police:
            fenetre = gtk.FontSelectionDialog("Selection d'une police")
            self.dialogue_police = fenetre
    
            fenetre.set_position(gtk.WIN_POS_MOUSE)
    
            fenetre.connect("destroy", self.dialogue_police_destroy)
    
            fenetre.ok_button.connect("clicked",
                                     self.calendrier_police_selection_ok)
            fenetre.cancel_button.connect_object("clicked",
                                                lambda wid: wid.destroy(),
                                                self.dialogue_police)
        fenetre = self.dialogue_police
        if not (fenetre.flags() & gtk.VISIBLE):
            fenetre.show()
        else:
            fenetre.destroy()
            self.dialogue_police = None

    def dialogue_police_destroy(self, donnees=None):
        self.dialogue_police = None

    def __init__(self):
        drapeaux = [
            "Afficher en-tete",
            "Afficher nom des jours",
            "Pas de changement de mois",
            "Afficher numeros de semaines",
            ]
        self.fenetre = None
        self.police = None
        self.dialogue_police = None
        self.cases_drapeaux = 5*[None]
        self.reglages = 5*[0]
        self.date_marquee = 31*[0]

        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Exemple de calendrier")
        fenetre.set_border_width(5)
        fenetre.connect("destroy", lambda x: gtk.main_quit())

        fenetre.set_resizable(False)

        boite_v = gtk.VBox(False, self.DEF_ESP)
        fenetre.add(boite_v)

        # La partie du haut de la fenetre : calendrier, drapeaux et police
        boite_h = gtk.HBox(False, self.DEF_ESP)
        boite_v.pack_start(boite_h, True, True, self.DEF_ESP)
        boiteboutons_h = gtk.HButtonBox()
        boite_h.pack_start(boiteboutons_h, False, False, self.DEF_ESP)
        boiteboutons_h.set_layout(gtk.BUTTONBOX_SPREAD)
        boiteboutons_h.set_spacing(5)

        # Le calendrier
        cadre = gtk.Frame("Calendrier")
        boiteboutons_h.pack_start(cadre, False, True, self.DEF_ESP)
        calendrier = gtk.Calendar()
        self.fenetre = calendrier
        self.calendrier_def_drapeaux()
        calendrier.mark_day(19)
        self.date_marquee[19-1] = 1
        cadre.add(calendrier)
        calendrier.connect("month_changed", self.calendrier_change_mois)
        calendrier.connect("day_selected", self.calendrier_selec_jour)
        calendrier.connect("day_selected_double_click",
                         self.calendrier_selec_jour_dbleclic)
        calendrier.connect("prev_month", self.calendrier_mois_prec)
        calendrier.connect("next_month", self.calendrier_mois_suiv)
        calendrier.connect("prev_year", self.calendrier_annee_prec)
        calendrier.connect("next_year", self.calendrier_annee_suiv)

        separateur = gtk.VSeparator()
        boite_h.pack_start(separateur, False, True, 0)

        boite_v2 = gtk.VBox(False, self.DEF_ESP)
        boite_h.pack_start(boite_v2, False, False, self.DEF_ESP)
  
        # Construction du cadre de droite contenant les drapeaux
        cadre = gtk.Frame("Drapeaux")
        boite_v2.pack_start(cadre, True, True, self.DEF_ESP)
        boite_v3 = gtk.VBox(True, self.DEF_PETIT_ESP)
        cadre.add(boite_v3)

        for i in range(len(drapeaux)):
            caseacocher = gtk.CheckButton(drapeaux[i])
            caseacocher.connect("toggled", self.calendrier_drapeau_coche)
            boite_v3.pack_start(caseacocher, True, True, 0)
            self.cases_drapeaux[i] = caseacocher

        # Construction du bouton "Police..." a droite
        bouton = gtk.Button("Police...")
        bouton.connect("clicked", self.calendrier_selec_police)
        boite_v2.pack_start(bouton, False, False, 0)

        # Construction de la partie Evenements-Signaux.
        cadre = gtk.Frame("Evenements-signaux")
        boite_v.pack_start(cadre, True, True, self.DEF_ESP)

        boite_v2 = gtk.VBox(True, self.DEF_PETIT_ESP)
        cadre.add(boite_v2)
  
        boite_h = gtk.HBox (False, 3)
        boite_v2.pack_start(boite_h, False, True, 0)
        etiquette = gtk.Label("Dernier :")
        boite_h.pack_start(etiquette, False, True, 0)
        self.dern_sig = gtk.Label("")
        boite_h.pack_start(self.dern_sig, False, True, 0)

        boite_h = gtk.HBox (False, 3)
        boite_v2.pack_start(boite_h, False, True, 0)
        etiquette = gtk.Label("Penultieme :")
        boite_h.pack_start(etiquette, False, True, 0)
        self.penult_sig = gtk.Label("")
        boite_h.pack_start(self.penult_sig, False, True, 0)

        boite_h = gtk.HBox (False, 3)
        boite_v2.pack_start(boite_h, False, True, 0)
        etiquette = gtk.Label("Antepenultieme :")
        boite_h.pack_start(etiquette, False, True, 0)
        self.apenult_sig = gtk.Label("")
        boite_h.pack_start(self.apenult_sig, False, True, 0)

        boiteboutons = gtk.HButtonBox ()
        boite_v.pack_start(boiteboutons, False, False, 0)
        boiteboutons.set_layout(gtk.BUTTONBOX_END)

        bouton = gtk.Button("Fermer")
        bouton.connect("clicked", lambda w: gtk.main_quit())
        boiteboutons.add(bouton)
        bouton.set_flags(gtk.CAN_DEFAULT)
        bouton.grab_default()

        fenetre.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleCalendrier()
    main()
