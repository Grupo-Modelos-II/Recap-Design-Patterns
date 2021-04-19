import matplotlib
matplotlib.use("GTK3Agg")
import matplotlib.pyplot as plt

import pgi
pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk
from controllers.Controller import Controller

class Menu(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Design Patterns")
        Gtk.Window.set_default_size (self,800,800)

        self._controller = Controller()

       
    def handle_analysis(self,widget):
        data = self._controller.exec_strategy(self._combo_box_1.get_active_text())

        label = data["Results"]
        label = f"Total Inhibidores: {label['inhibs']} Inhibidores Destruidos\nTotal Dragones: {label['dragons']} Dragones Asesinados\nPartidas Ganadas: {label['won']}\nTiempo Promedio: {label['average']} Minutos"

        self._label_result.set_label(label)

        plt.hist2d(data["Graph"]["time"], data["Graph"]["performance"])
        # plt.legend()
        plt.savefig('result', transparent=True)
        self._result.set_from_file("result.png")
        


    def handle_prediction(self,widget):
        print("Prediction")


    def init_template(self):
        #Main Container
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        #Botones
        self._btn_analisis = Gtk.Button(label="Analisis")
        self._btn_analisis.connect("clicked",self.handle_analysis)

        self._btn_prediction = Gtk.Button(label="Realziar Prediccion")
        self._btn_prediction.connect("clicked",self.handle_prediction)

        #Label Page 1
        self._label_title = Gtk.Label()
        self._label_title.set_label("Analisis de equipos profesionales de  League Of Legends")

        # Combo Box Page 1
        self._combo_box_1 = Gtk.ComboBoxText()
        [self._combo_box_1.append(id=None,text=str(name)) for name in self._controller.get_team_list()]

        #Configurando paginas
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        self.page1.set_border_width(10)
        self.page1.add(self._label_title)
        self.page1.add(self._combo_box_1)
        self.page1.add(self._btn_analisis)
    
        self.notebook.append_page(self.page1, Gtk.Label(label="Analizar"))

        self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        self.page2.set_border_width(30)

        #Contenido pagina 2
        combo_box_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=100)

        self.combo_box_page21 = Gtk.ComboBoxText()
        [self.combo_box_page21.append(id=None,text=str(name)) for name in self._controller.get_team_list()]
        combo_box_container.add(self.combo_box_page21)

        self.combo_box_page22 = Gtk.ComboBoxText()
        [self.combo_box_page22.append(id=None,text=str(name)) for name in self._controller.get_team_list()]
        combo_box_container.add(self.combo_box_page22)

        self.page2.add(combo_box_container)

        self.notebook.append_page(self.page2, Gtk.Label(label="Predicción"))

        #Information Page 1
        ## Label Page 1 Results
        self._label_result = Gtk.Label()
        self._label_result.set_label("")

        self.page1.add(self._label_result)

        ## Image Page 1 Result
        self._result = Gtk.Image()
        self.page1.add(self._result)


        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()


