#!/usr/bin/env python

# exemple boite.py

import pygtk
pygtk.require('2.0')
import gtk
import sys, string

# Cette fonction nous aide a creer une nouvelle HBox remplie de boutons+etiquettes.
# Des arguments pour les variables qui nous interessent lui sont transmis. On n'affiche 
# pas la boite (avec show()), mais on affiche tout ce qui se trouve a l'interieur.

def creer_boite(homogeneous, spacing, expand, fill, padding):

    # On cree une nouvelle boite avec les valeurs
    # transmises pour "homogeneous" et "spacing"
    boite = gtk.HBox(homogeneous, spacing)

    # On cree une serie de boutons, toujours avec les valeurs transmises.
    bouton = gtk.Button("boite.pack")
    boite.pack_start(bouton, expand, fill, padding)
    bouton.show()

    bouton = gtk.Button("(bouton,")
    boite.pack_start(bouton, expand, fill, padding)
    bouton.show()

    # On cree un bouton dont l'etiquette dependra de la valeur
    # de "expand".
    if expand == True:
        bouton = gtk.Button("True,")
    else:
        bouton = gtk.Button("False,")

    boite.pack_start(bouton, expand, fill, padding)
    bouton.show()

    # Meme principe que ci-dessus, mais cette fois avec la
    # formulation abregee
    bouton = gtk.Button(("False,", "True,")[fill==True])
    boite.pack_start(bouton, expand, fill, padding)
    bouton.show()

    chaine_pad = "%d)" % padding

    bouton = gtk.Button(chaine_pad)
    boite.pack_start(bouton, expand, fill, padding)
    bouton.show()
    return boite

class BoitesPLacement:
    def evnmt_delete(self, widget, evenement, donnees=None):
        gtk.main_quit()
        return False

    def __init__(self, numero):

        # Creation de notre fenetre
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)

        # N'oubliez pas de connecter le signal "delete_event"
        # a la fenetre principale. Cela donne au programme
        # un comportement plus intuitif.
        self.fenetre.connect("delete_event", self.evnmt_delete)
        self.fenetre.set_border_width(10)
    
        # On cree une boite verticale (VBox) pour y placer nos boites
        # horizontales. Ainsi on peut empiler les boites horizontales
        # remplies de boutons les unes sur les autre dans la VBox.
        boite1 = gtk.VBox(False, 0)
    
        # Sur quel scenario partons-nous ? (cf. images de la section 4.2)
        if numero == 1:
            # Creation d'une nouvelle etiquette.
            etiquette = gtk.Label("HBox(False, 0)")
	
            # On aligne l'etiquette a gauche. Nous verrons cette methode
            # ainsi que d'autres dans la section sur les attributs des widgets.
            etiquette.set_alignment(0, 0)

            # On place l'etiquette dans la boite verticale (la VBox boite1).
            # Souvenez-vous que les widgets ajoutes a une VBox seront places
            # les uns sur les autres, dans l'ordre.
            boite1.pack_start(etiquette, False, False, 0)
	
            # On affiche l'etiquette.
            etiquette.show()
	
            # On appelle notre fonction creer_boite en lui transmettant :
            # homogeneous=False, spacing=0, expand=False, fill=False, padding=0
            boite2 = creer_boite(False, 0, False, False, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()

            # On appelle notre fonction creer_boite en lui transmettant :
            # homogeneous=False, spacing=0, expand=True, fill=False, padding=0
            boite2 = creer_boite(False, 0, True, False, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # homogeneous=False, spacing=0, expand=True, fill=True, padding=0
            boite2 = creer_boite(False, 0, True, True, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # Creation d'un separateur. On en apprendra plus sur ce widget
            # ulterieurement mais il est assez simple.
            separateur = gtk.HSeparator()
	
            # On place le separateur dans la VBox. Gardez bien a l'esprit que
            # tout ces widgets sont places dans une VBox, ils sont donc
            # empiles les uns sur les autres.
            boite1.pack_start(separateur, False, True, 5)
            separateur.show()
	
            # On cree une autre etiquette, et on l'affiche.
            etiquette = gtk.Label("HBox(True, 0)")
            etiquette.set_alignment(0, 0)
            boite1.pack_start(etiquette, False, False, 0)
            etiquette.show()
	
            # homogeneous=True, spacing=0, expand=True, fill=False, padding=0
            boite2 = creer_boite(True, 0, True, False, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # homogeneous=True, spacing=0, expand=True, fill=True, padding=0
            boite2 = creer_boite(True, 0, True, True, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # Un autre separateur.
            separateur = gtk.HSeparator()
            # Les trois derniers arguments de pack_start() sont :
            # expand, fill, padding.
            boite1.pack_start(separateur, False, True, 5)
            separateur.show()
        elif numero == 2:
            # On cree une etiquette, souvenez-vous que boite1 est une VBox,
            # creee vers le debut de __init__()
            etiquette = gtk.Label("HBox(False, 10)")
            etiquette.set_alignment( 0, 0)
            boite1.pack_start(etiquette, False, False, 0)
            etiquette.show()
	
            # homogeneous=False, spacing=10, expand=True, fill=False, padding=0
            boite2 = creer_boite(False, 10, True, False, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # homogeneous=False, spacing=10, expand=True, fill=True, padding=0
            boite2 = creer_boite(False, 10, True, True, 0)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            separateur = gtk.HSeparator()
            # Les trois derniers arguments de pack_start() sont :
            # expand, fill, padding.
            boite1.pack_start(separateur, False, True, 5)
            separateur.show()
	
            etiquette = gtk.Label("HBox(False, 0)")
            etiquette.set_alignment(0, 0)
            boite1.pack_start(etiquette, False, False, 0)
            etiquette.show()
	
            # homogeneous=False, spacing=0, expand=True, fill=False, padding=10
            boite2 = creer_boite(False, 0, True, False, 10)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # homogeneous=False, spacing=0, expand=True, fill=True, padding=10
            boite2 = creer_boite(False, 0, True, True, 10)
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            separateur = gtk.HSeparator()
            # Les trois derniers arguments de pack_start() sont :
            # expand, fill, padding.
            boite1.pack_start(separateur, False, True, 5)
            separateur.show()

        elif numero == 3:

            # Ce scenario est la pour montrer qu'avec pack_end() on peut aligner
            # les widgets a droite. D'abord, creons une boite, comme avant.
            boite2 = creer_boite(False, 0, False, False, 0)

            # on cree l'etiquette que l'on alignera a droite.
            etiquette = gtk.Label("fin")
            # On la place avec pack_end(), elle va se placer a l'extremite
            # droite de la HBox creee par l'appel a creer_boite().
            boite2.pack_end(etiquette, False, False, 0)
            # On affiche l'etiquette.
            etiquette.show()
	
            # On place boite2 dans boite1
            boite1.pack_start(boite2, False, False, 0)
            boite2.show()
	
            # Un separateur pour le bas.
            separateur = gtk.HSeparator()
            
            # Cette methode fixe les dimensions du separateur (400 pixels de large
            # pour 5 pixels de haut). C'est pour que la HBox qu'on vient de creer
            # fasse aussi 400 de large, et que l'etiquette "fin" soit bien separee
            # des autres widgets de la HBox. Autrement, tous les widgets de la 
            # HBox seraient places aussi pres l'un de l'autre que possible.
            separateur.set_size_request(400, 5)
            # On place le separateur dans la HBox (boite1) creee vers le debut 
            # de __init__()
            boite1.pack_start(separateur, False, True, 5)
            separateur.show()
    
        # On cree une autre HBox. On peut en utiliser autant qu'on veut !
        boitequitter = gtk.HBox(False, 0)
    
        # Notre bouton "Quitter".
        bouton = gtk.Button("Quitter")
    
        # Lorsqu'on clique sur le bouton, le signal emis doit terminer le programme.
        bouton.connect_object("clicked", gtk.main_quit, self.fenetre)
        # On place le bouton dans la HBox boitequitter.
        # Les trois derniers arguments de pack_start() sont :
        # expand, fill, padding.
        boitequitter.pack_start(bouton, True, False, 0)
        # On place boitequitter dans la VBox (boite1)
        boite1.pack_start(boitequitter, False, False, 0)
    
        # On place la VBox boite1 (qui contient maintenant tous nos widgets)
        # dans la fenetre principale.
        self.fenetre.add(boite1)
    
        # Et on affiche ce qui reste a afficher.
        bouton.show()
        boitequitter.show()
    
        boite1.show()
        # La fenetre en dernier, afin que tout s'affiche d'un coup.
        self.fenetre.show()

def main():
    # Et bien sur, notre boucle principale.
    gtk.main()
    # Le controle revient ici lorsque main_quit() est appelee.
    return 0         

if __name__ =="__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("La commande doit etre de la forme \"boite.py num\", avec num = 1 ou 2 ou 3\n")
        sys.exit(1)
    BoitesPLacement(string.atoi(sys.argv[1]))
    main()
