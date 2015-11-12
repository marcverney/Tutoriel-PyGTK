#!/usr/bin/env python

# exemple textview-basic.py
  
import pygtk
pygtk.require('2.0')
import gtk

class ExempleTextView:
    def change_editable(self, case, textview):
        textview.set_editable(case.get_active())

    def change_curseur_visible(self, case, textview):
        textview.set_cursor_visible(case.get_active())

    def change_marge_gauche(self, case, textview):
        if case.get_active():
            textview.set_left_margin(50)
        else:
            textview.set_left_margin(0)

    def change_marge_droite(self, case, textview):
        if case.get_active():
            textview.set_right_margin(50)
        else:
             textview.set_right_margin(0)

    def change_retour_ligne(self, boutonradio, textview, val):
        if boutonradio.get_active():
            textview.set_wrap_mode(val)

    def change_alignement(self, boutonradio, textview, val):
        if boutonradio.get_active():
            textview.set_justification(val)

    def fermer_application(self, widget):
        gtk.main_quit()

    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_resizable(True)
        fenetre.connect("destroy", self.fermer_application)
        fenetre.set_title("Exemple de widget TextView simple")
        fenetre.set_border_width(0)

        boite1 = gtk.VBox(False, 0)
        fenetre.add(boite1)
        boite1.show()

        boite2 = gtk.VBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, True, True, 0)
        boite2.show()

        fd = gtk.ScrolledWindow()
        fd.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        buffertexte = textview.get_buffer()
        fd.add(textview)
        fd.show()
        textview.show()

        boite2.pack_start(fd)
        # Chargement du fichier textview-basic.py dans la fenetre
        fichier = open("textview-basic.py", "r")

        if fichier:
            chaine = fichier.read()
            fichier.close()
            buffertexte.set_text(chaine)

        boiteH = gtk.HButtonBox()
        boite2.pack_start(boiteH, False, False, 0)
        boiteH.show()

        boiteV = gtk.VBox()
        boiteV.show()
        boiteH.pack_start(boiteV, False, False, 0)
        # case a cocher pour autoriser l'edition du texte
        case = gtk.CheckButton("Editable")
        boiteV.pack_start(case, False, False, 0)
        case.connect("toggled", self.change_editable, textview)
        case.set_active(True)
        case.show()
        # case a cocher pour afficher le curseur
        case = gtk.CheckButton("Curseur visible")
        boiteV.pack_start(case, False, False, 0)
        case.connect("toggled", self.change_curseur_visible, textview)
        case.set_active(True)
        case.show()
        # case a cocher pour afficher une marge gauche
        case = gtk.CheckButton("Marge gauche")
        boiteV.pack_start(case, False, False, 0)
        case.connect("toggled", self.change_marge_gauche, textview)
        case.set_active(False)
        case.show()
        # case a cocher pour afficher une marge droite
        case = gtk.CheckButton("Marge droite")
        boiteV.pack_start(case, False, False, 0)
        case.connect("toggled", self.change_marge_droite, textview)
        case.set_active(False)
        case.show()
        # boutons radio pour definir le type de retour a la ligne automatique
        boiteV = gtk.VBox()
        boiteV.show()
        boiteH.pack_start(boiteV, False, False, 0)
        radio = gtk.RadioButton(None, "WRAP__NONE")
        boiteV.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.change_retour_ligne, textview, gtk.WRAP_NONE)
        radio.set_active(True)
        radio.show()
        radio = gtk.RadioButton(radio, "WRAP__CHAR")
        boiteV.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.change_retour_ligne, textview, gtk.WRAP_CHAR)
        radio.show()
        radio = gtk.RadioButton(radio, "WRAP__WORD")
        boiteV.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.change_retour_ligne, textview, gtk.WRAP_WORD)
        radio.show()

        # boutons radio pour definir l'alignement
        boiteV = gtk.VBox()
        boiteV.show()
        boiteH.pack_start(boiteV, False, False, 0)
        radio = gtk.RadioButton(None, "JUSTIFY__LEFT")
        boiteV.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.change_alignement, textview,
                      gtk.JUSTIFY_LEFT)
        radio.set_active(True)
        radio.show()
        radio = gtk.RadioButton(radio, "JUSTIFY__RIGHT")
        boiteV.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.change_alignement, textview,
                      gtk.JUSTIFY_RIGHT)
        radio.show()
        radio = gtk.RadioButton(radio, "JUSTIFY__CENTER")
        boiteV.pack_start(radio, False, True, 0)
        radio.connect("toggled", self.change_alignement, textview,
                      gtk.JUSTIFY_CENTER)
        radio.show()

        separateur = gtk.HSeparator()
        boite1.pack_start(separateur, False, True, 0)
        separateur.show()

        boite2 = gtk.VBox(False, 10)
        boite2.set_border_width(10)
        boite1.pack_start(boite2, False, True, 0)
        boite2.show()

        bouton = gtk.Button("Fermer")
        bouton.connect("clicked", self.fermer_application)
        boite2.pack_start(bouton, True, True, 0)
        bouton.set_flags(gtk.CAN_DEFAULT)
        bouton.grab_default()
        bouton.show()
        fenetre.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleTextView()
    main()
