import pgi
import matplotlib
import matplotlib.pyplot as plt
from functions import functions as f
from pgi.repository import Gtk, Gdk
from controllers.Controller import Controller

matplotlib.use("GTK3Agg")
pgi.require_version("Gtk", "3.0")

from .builder.BuildNotebook import BuildNotebook

class Menu(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Design Patterns")
        Gtk.Window.set_default_size (self,800,800)

    def initTemplate(self):

        #Main Container
        self.set_resizable(False)
        self.set_border_width(3)

        builder = BuildNotebook(self)
        self._notebook = builder.getGUI()
        self.add(self._notebook)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()