#!/usr/bin/env python
# coding: utf8
# exemple filechooser.py

import pygtk
pygtk.require('2.0')

import gtk

# Vérification du nouveau PyGtk : c'est une nouvelle classe de PyGtk 2.4
if gtk.pygtk_version < (2,3,90):
   print "Cet exemple nécessite PyGtk 2.3.90 ou ultérieur"
   raise SystemExit

dialogue = gtk.FileChooserDialog("Ouvrir..",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
dialogue.set_default_response(gtk.RESPONSE_OK)

filtre = gtk.FileFilter()
filtre.set_name("All files")
filtre.add_pattern("*")
dialogue.add_filter(filtre)

filtre = gtk.FileFilter()
filtre.set_name("Images")
filtre.add_mime_type("image/png")
filtre.add_mime_type("image/jpeg")
filtre.add_mime_type("image/gif")
filtre.add_pattern("*.png")
filtre.add_pattern("*.jpg")
filtre.add_pattern("*.gif")
filtre.add_pattern("*.tif")
filtre.add_pattern("*.xpm")
dialogue.add_filter(filtre)

reponse = dialogue.run()
if reponse == gtk.RESPONSE_OK:
    print dialogue.get_filename(), 'choisi'
elif reponse == gtk.RESPONSE_CANCEL:
    print 'On ferme, pas de fichier sélectionné.'
dialogue.destroy()
