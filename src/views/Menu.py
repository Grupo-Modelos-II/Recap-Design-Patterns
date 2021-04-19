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

        self._label_result.set_label(str(data["Graph"]))
        


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

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label(label="A page with an image for a Title."))
        self.notebook.append_page(self.page2, Gtk.Label(label="Predicción"))

        #Label Page 1 Results
        self._label_result = Gtk.Label()
        self._label_result.set_label("")

        self.page1.add(self._label_result)


        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()


