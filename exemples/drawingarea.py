#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example drawingzone_dessin.py

import pygtk
pygtk.require('2.0')
import gtk
import operator
import time
import string

class ExempleZoneDessin:
    def __init__(self):
        fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        fenetre.set_title("Exemple de zone de dessin")
        fenetre.connect("destroy", lambda w: gtk.main_quit())
        self.zone_dessin = gtk.DrawingArea()
        self.zone_dessin.set_size_request(400, 300)
        self.stylepango = self.zone_dessin.create_pango_layout("")
        self.fenetre_defil = gtk.ScrolledWindow()
        self.fenetre_defil.add_with_viewport(self.zone_dessin)
        self.table = gtk.Table(2,2)
        self.reglehoriz = gtk.HRuler()
        self.reglevert = gtk.VRuler()
        self.reglehoriz.set_range(0, 400, 0, 400)
        self.reglevert.set_range(0, 300, 0, 300)
        self.table.attach(self.reglehoriz, 1, 2, 0, 1, yoptions=0)
        self.table.attach(self.reglevert, 0, 1, 1, 2, xoptions=0)
        self.table.attach(self.fenetre_defil, 1, 2, 1, 2)
        fenetre.add(self.table)
        self.zone_dessin.set_events(gtk.gdk.POINTER_MOTION_MASK |
                             gtk.gdk.POINTER_MOTION_HINT_MASK )
        self.zone_dessin.connect("expose-event", self.rappel_zone_dessin_expose)
        def a_bouge(ruler, event):
            return ruler.emit("motion_notify_event", event)
        self.zone_dessin.connect_object("motion_notify_event", a_bouge,
                                 self.reglehoriz)
        self.zone_dessin.connect_object("motion_notify_event", a_bouge,
                                 self.reglevert)
        self.ajuste_hor = self.fenetre_defil.get_hadjustment()
        self.ajuste_ver = self.fenetre_defil.get_vadjustment()
        def rappel_valeur(ajuste, regle, horiz):
            if horiz:
                span = self.fenetre_defil.get_allocation()[3]
            else:
                span = self.fenetre_defil.get_allocation()[2]
            l,u,p,m = regle.get_range()
            v = ajuste.value
            regle.set_range(v, v+span, p, m)
            while gtk.events_pending():
                gtk.main_iteration()
        self.ajuste_hor.connect('value-changed', rappel_valeur, self.reglehoriz, True)
        self.ajuste_ver.connect('value-changed', rappel_valeur, self.reglevert, False)
        def rappel_taille_fixee(wid, allocation):
            x, y, w, h = allocation
            l,u,p,m = self.reglehoriz.get_range()
            m = max(m, w)
            self.reglehoriz.set_range(l, l+w, p, m)
            l,u,p,m = self.reglevert.get_range()
            m = max(m, h)
            self.reglevert.set_range(l, l+h, p, m)
        self.fenetre_defil.connect('size-allocate', rappel_taille_fixee)
        self.zone_dessin.show()
        self.reglehoriz.show()
        self.reglevert.show()
        self.fenetre_defil.show()
        self.table.show()
        fenetre.show()

    def rappel_zone_dessin_expose(self, zone_dessin, event):
        self.style = self.zone_dessin.get_style()
        self.contexte_graph = self.style.fg_gc[gtk.STATE_NORMAL]
        self.trace_point(10,10)
        self.trace_points(110, 10)
        self.trace_ligne(210, 10)
        self.trace_lignes(310, 10)
        self.trace_segments(10, 100)
        self.trace_rectangles(110, 100)
        self.trace_arcs(210, 100)
        self.trace_pixmap(310, 100)
        self.trace_polygone(10, 200)
        self.trace_image_rgb(110, 200)
        return True

    def trace_point(self, x, y):
        self.zone_dessin.window.draw_point(self.contexte_graph, x+30, y+30)
        self.stylepango.set_text("Point")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+50, self.stylepango)
        return

    def trace_points(self, x, y):
        points = [(x+10,y+10), (x+10,y), (x+40,y+30),
                  (x+30,y+10), (x+50,y+10)]
        self.zone_dessin.window.draw_points(self.contexte_graph, points)
        self.stylepango.set_text("Points")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+50, self.stylepango)
        return

    def trace_ligne(self, x, y):
        self.zone_dessin.window.draw_line(self.contexte_graph, x+10, y+10, x+20, y+30)
        self.stylepango.set_text("Ligne")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+50, self.stylepango)
        return

    def trace_lignes(self, x, y):
        points = [(x+10,y+10), (x+10,y), (x+40,y+30),
                  (x+30,y+10), (x+50,y+10)]
        self.zone_dessin.window.draw_lines(self.contexte_graph, points)
        self.stylepango.set_text("Lignes")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+50, self.stylepango)
        return

    def trace_segments(self, x, y):
        segments = ((x+20,y+10, x+20,y+70), (x+60,y+10, x+60,y+70),
            (x+10,y+30 , x+70,y+30), (x+10, y+50 , x+70, y+50))
        self.zone_dessin.window.draw_segments(self.contexte_graph, segments)
        self.stylepango.set_text("Segments")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+80, self.stylepango)
        return

    def trace_rectangles(self, x, y):
        self.zone_dessin.window.draw_rectangle(self.contexte_graph, False, x, y, 80, 70)
        self.zone_dessin.window.draw_rectangle(self.contexte_graph, True, x+10, y+10, 20, 20)
        self.zone_dessin.window.draw_rectangle(self.contexte_graph, True, x+50, y+10, 20, 20)
        self.zone_dessin.window.draw_rectangle(self.contexte_graph, True, x+20, y+50, 40, 10)
        self.stylepango.set_text("Rectangles")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+80, self.stylepango)
        return

    def trace_arcs(self, x, y):
        self.zone_dessin.window.draw_arc(self.contexte_graph, False, x+10, y, 70, 70,
                                  0, 360*64)
        self.zone_dessin.window.draw_arc(self.contexte_graph, True, x+30, y+20, 10, 10,
                                  0, 360*64)
        self.zone_dessin.window.draw_arc(self.contexte_graph, True, x+50, y+20, 10, 10,
                                  0, 360*64)
        self.zone_dessin.window.draw_arc(self.contexte_graph, True, x+30, y+10, 30, 50,
                                  210*64, 120*64)
        self.stylepango.set_text("Arcs")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+30, y+80, self.stylepango)
        return

    def trace_pixmap(self, x, y):
        pixmap, mask = gtk.gdk.pixmap_create_from_xpm(
            self.zone_dessin.window, self.style.bg[gtk.STATE_NORMAL], "gtk.xpm")

        self.zone_dessin.window.draw_drawable(self.contexte_graph, pixmap, 0, 0, x+15, y+25,
                                       -1, -1)
        self.stylepango.set_text("Pixmap")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+80, self.stylepango)
        return

    def trace_polygone(self, x, y):
        points = [(x+10,y+60), (x+10,y+20), (x+40,y+70),
                  (x+30,y+30), (x+50,y+40)]
        self.zone_dessin.window.draw_polygon(self.contexte_graph, True, points)
        self.stylepango.set_text("Polygone")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+80, self.stylepango)
        return

    def trace_image_rgb(self, x, y):
        b = 80*3*80*['\0']
        for i in range(80):
            for j in range(80):
                b[3*80*i+3*j] = chr(255-3*i)
                b[3*80*i+3*j+1] = chr(255-3*abs(i-j))
                b[3*80*i+3*j+2] = chr(255-3*j)
        buff = string.join(b, '')
        self.zone_dessin.window.draw_rgb_image(self.contexte_graph, x, y, 80, 80,
                                 gtk.gdk.RGB_DITHER_NONE, buff, 80*3)
        self.stylepango.set_text("Image RGB")
        self.zone_dessin.window.draw_layout(self.contexte_graph, x+5, y+80, self.stylepango)
        return

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ExempleZoneDessin()
    main()
