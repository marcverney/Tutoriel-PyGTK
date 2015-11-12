#!/usr/bin/env python

# exemple widgetsintervalle.py

import pygtk
pygtk.require('2.0')
import gtk

# Ces fonctions sont la pour nous faciliter les choses

def nouvelle_entree(nom, rappel, donnees=None):
    entree = gtk.MenuItem(nom)
    entree.connect("activate", rappel, donnees)
    entree.show()
    return entree

def gradateurs_valeurs_defaut(gradateur):
    gradateur.set_update_policy(gtk.UPDATE_CONTINUOUS)
    gradateur.set_digits(1)
    gradateur.set_value_pos(gtk.POS_TOP)
    gradateur.set_draw_value(True)

class WidgetsIntervalle:
    def modif_position(self, entree, position):
        # Fixe la position de la valeur pour les deux gradateurs
        self.gradateurh.set_value_pos(position)
        self.gradateurv.set_value_pos(position)

    def modif_mode_actu(self, entree, mode):
        # Fixe le mode d'actualisation pour les deux gradateurs
        self.gradateurh.set_update_policy(mode)
        self.gradateurv.set_update_policy(mode)

    def modif_decimales(self, ajust):
        # Fixe le nombre de decimales pour arrondir la valeur de ajust
        self.gradateurh.set_digits(ajust.value)
        self.gradateurv.set_digits(ajust.value)

    def modif_taille_page(self, ajust2, ajust1):
        # Les valeurs "taille de la page" et "incrementation par page" de l'ajustement 
        # exemple prennent la valeur donnee par le gradateur "Taille de la page".
        ajust1.page_size = ajust2.value
        ajust1.page_incr = ajust2.value
        # Puis on fait emettre le signal "changed" a ajust1 pour reconfigurer tous les
        # widgets qui lui sont attaches
        ajust1.emit("changed")

    def affiche_valeur(self, bouton):
        # Active ou desactive l'affichage de la valeur sur les gradateurs,
        # en fonction de l'etat du bouton a bascule
        self.gradateurh.set_draw_value(bouton.get_active())
        self.gradateurv.set_draw_value(bouton.get_active())  

    # Construction de notre fenetre exemple

    def __init__(self):
        # Creation standard d'une fenetre
        self.fenetre = gtk.Window (gtk.WINDOW_TOPLEVEL)
        self.fenetre.connect("destroy", gtk.main_quit)
        self.fenetre.set_title("Widgets d'intervalle")

        boite1 = gtk.VBox(False, 0)
        self.fenetre.add(boite1)
        boite1.show()

        boite2 = gtk.HBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        # valeur, minimale, maximale, incr/pas, incr/page, taille de la page
        # Notez que le parametre "taille de la page" n'a d'effet qu'avec les
        # barres de defilement, la plus haute valeur etant alors egale a
        # "maximale" moins "taille de la page"
        ajust1 = gtk.Adjustment(0.0, 0.0, 101.0, 0.1, 1.0, 1.0)
  
        self.gradateurv = gtk.VScale(ajust1)
        gradateurs_valeurs_defaut(self.gradateurv)
        boite2.pack_start(self.gradateurv, True, True, 0)
        self.gradateurv.show()

        boite3 = gtk.VBox(False, 10)
        boite2.pack_start(boite3, True, True, 0)
        boite3.show()

        # On reutilise le meme ajustement
        self.gradateurh = gtk.HScale(ajust1)
        self.gradateurh.set_size_request(200, 30)
        gradateurs_valeurs_defaut(self.gradateurh)
        boite3.pack_start(self.gradateurh, True, True, 0)
        self.gradateurh.show()

        # On reutilise encore le meme ajustement
        barredefil = gtk.HScrollbar(ajust1)
        # Notez que l'on demande a ce que les gradateurs soient toujours
        # actualises en continu quand la barre de defilement est manipulee
        barredefil.set_update_policy(gtk.UPDATE_CONTINUOUS)
        boite3.pack_start(barredefil, True, True, 0)
        barredefil.show()

        boite2 = gtk.HBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        # Un bouton a bascule pour afficher ou pas la valeur
        bouton = gtk.CheckButton("Afficher la valeur sur les gradateurs")
        bouton.set_active(True)
        bouton.connect("toggled", self.affiche_valeur)
        boite2.pack_start(bouton, True, True, 0)
        bouton.show()
  
        boite2 = gtk.HBox(False, 10)
        boite2.set_border_width(10)

        # Un menu deroulant pour changer la position de la valeur
        etiquette = gtk.Label("Position de la valeur :")
        boite2.pack_start(etiquette, False, False, 0)
        etiquette.show()
  
        menuderoul = gtk.OptionMenu()
        menu = gtk.Menu()

        entree = nouvelle_entree ("Au-dessus", self.modif_position, gtk.POS_TOP)
        menu.append(entree)
  
        entree = nouvelle_entree ("Au-dessous", self.modif_position,
                                  gtk.POS_BOTTOM)
        menu.append(entree)
  
        entree = nouvelle_entree ("A gauche", self.modif_position, gtk.POS_LEFT)
        menu.append(entree)
  
        entree = nouvelle_entree ("A droite", self.modif_position, gtk.POS_RIGHT)
        menu.append(entree)
  
        menuderoul.set_menu(menu)
        boite2.pack_start(menuderoul, True, True, 0)
        menuderoul.show()

        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        boite2 = gtk.HBox(False, 10)
        boite2.set_border_width(10)

        # Encore un autre menu deroulant, cette fois-ci pour le mode
        # d'actualisation des gradateurs
        etiquette = gtk.Label("Mode d'actualisation :")
        boite2.pack_start(etiquette, False, False, 0)
        etiquette.show()
  
        menuderoul = gtk.OptionMenu()
        menu = gtk.Menu()
  
        entree = nouvelle_entree("Continu", self.modif_mode_actu,
                                 gtk.UPDATE_CONTINUOUS)
        menu.append(entree)
  
        entree = nouvelle_entree ("Discontinu", self.modif_mode_actu,
                                  gtk.UPDATE_DISCONTINUOUS)
        menu.append(entree)
  
        entree = nouvelle_entree ("Differe", self.modif_mode_actu,
                                  gtk.UPDATE_DELAYED)
        menu.append(entree)
  
        menuderoul.set_menu(menu)
        boite2.pack_start(menuderoul, True, True, 0)
        menuderoul.show()
  
        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        boite2 = gtk.HBox(False, 10)
        boite2.set_border_width(10)
  
        # Creation d'un gradateur horizontal pout choisir le nombre de
        # decimales dans les gradateurs exemples.
        etiquette = gtk.Label("Decimales :")
        boite2.pack_start(etiquette, False, False, 0)
        etiquette.show()

        ajust2 = gtk.Adjustment(1.0, 0.0, 5.0, 1.0, 1.0, 0.0)
        ajust2.connect("value_changed", self.modif_decimales)
        gradateur = gtk.HScale(ajust2)
        gradateur.set_digits(0)
        boite2.pack_start(gradateur, True, True, 0)
        gradateur.show()

        boite1.pack_start(boite2, True, True, 0)
        boite2.show()
  
        boite2 = gtk.HBox(False, 10)
        boite2.set_border_width(10)
  
        # Un dernier gradateur horizontal pour choisir la taille de la page
        # de la barre de defilement.
        etiquette = gtk.Label("Taille de la page de la\nbarre de defilement :")
        boite2.pack_start(etiquette, False, False, 0)
        etiquette.show()

        ajust2 = gtk.Adjustment(1.0, 1.0, 101.0, 1.0, 1.0, 0.0)
        ajust2.connect("value_changed", self.modif_taille_page, ajust1)
        gradateur = gtk.HScale(ajust2)
        gradateur.set_digits(0)
        boite2.pack_start(gradateur, True, True, 0)
        gradateur.show()

        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        separateur = gtk.HSeparator()
        boite1.pack_start(separateur, False, True, 0)
        separateur.show()

        boite2 = gtk.VBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, False, True, 0)
        boite2.show()

        bouton = gtk.Button("Quitter")
        bouton.connect_object("clicked", gtk.main_quit, self.fenetre)
        boite2.pack_start(bouton, True, True, 0)
        bouton.set_flags(gtk.CAN_DEFAULT)
        bouton.grab_default()
        bouton.show()
        self.fenetre.show()

def main():
    gtk.main()
    return 0            

if __name__ == "__main__":
    WidgetsIntervalle()
    main()
