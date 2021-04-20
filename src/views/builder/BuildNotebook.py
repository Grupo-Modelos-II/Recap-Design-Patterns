import pgi
import matplotlib
import matplotlib.pyplot as plt
from functions import functions as f
from pgi.repository import Gtk, Gdk
from controllers.Controller import Controller

matplotlib.use("GTK3Agg")
pgi.require_version("Gtk", "3.0")

from .BuildGUI import BuildGUI

class BuildNotebook(BuildGUI):

    def __init__(self, window):
        self._window = window
        self._notebook = Gtk.Notebook()
        self._controller = Controller()

    def _buildPage1(self):
        # Label Page 1
        page1Title = Gtk.Label()
        page1Title.set_label("Analisis de equipos profesionales de  League Of Legends")

        # Boton
        self._btn_analisis = Gtk.Button(label="Analisis")

        # Combo Box Page 1
        self._combo_box_1 = Gtk.ComboBoxText()
        [self._combo_box_1.append(id=None,text=str(name)) for name in f.get_team_list()]
    

        #Configurando paginas
        self._page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        self._page1.set_border_width(10)

        #Information Page 1
        ## Label Page 1 Results
        self._label_result = Gtk.Label()


        ## Image Page 1 Results
        self._result = Gtk.Image()

        #Add Componentes
        self._page1.add(page1Title)
        self._page1.add(self._combo_box_1)
        self._page1.add(self._btn_analisis)
        self._page1.add(self._label_result)
        self._page1.add(self._result)

        self._notebook.append_page(self._page1, Gtk.Label(label="Analizar"))

    def _buildPage2(self):

        # Configurando Pagina 2
        self._page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        self._page2.set_border_width(30)

        #Combobox Page 2
        combo_box_container = Gtk.VBox(orientation=Gtk.Orientation.HORIZONTAL,spacing=100)

        self.combo_box_page21 = Gtk.ComboBoxText()
        [self.combo_box_page21.append(id=None,text=str(name)) for name in f.get_team_list()]
        combo_box_container.add(self.combo_box_page21)

        self.combo_box_page22 = Gtk.ComboBoxText()
        [self.combo_box_page22.append(id=None,text=str(name)) for name in f.get_team_list()]
        combo_box_container.add(self.combo_box_page22)

        # Button 
        self._btn_prediction = Gtk.Button(label="Realziar Prediccion")

        labels_container = Gtk.VBox(orientation=Gtk.Orientation.HORIZONTAL,spacing=100)

        self.label_prediction_team_a = Gtk.Label()
        self.label_prediction_team_b = Gtk.Label()

        self._result_page_2 = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        self._team_a_result = Gtk.LevelBar()
        self._team_b_result = Gtk.LevelBar()

        self._team_a_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65535))
        self._team_b_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 0, 0))

        self._team_a_result.set_size_request(0, 0)
        self._team_b_result.set_size_request(0, 0)

        self._result_page_2.set_opacity(0)

        self._page2.add(combo_box_container)
        self._page2.add(self._btn_prediction)
        labels_container.add(self.label_prediction_team_a)
        labels_container.add(self.label_prediction_team_b)
        self._page2.add(labels_container)
        self._result_page_2.pack1(self._team_a_result, False, False)
        self._result_page_2.pack2(self._team_b_result, False, False)
        self._page2.add(self._result_page_2)
        self._notebook.append_page(self._page2, Gtk.Label(label="Predicciones"))

    def _handleAnalysis(self,widget):
        self._controller.create_analisis()
        plt.cla()
        plt.clf()
        data = self._controller.exec_strategy(self._combo_box_1.get_active_text())

        label = data["Results"]
        label = f"Total Inhibidores: {label['inhibs']} Inhibidores Destruidos\nTotal Dragones: {label['dragons']} Dragones Asesinados\nPartidas Ganadas: {label['won']}\nTiempo Promedio: {label['average']:.6} Minutos"

        self._label_result.set_label(label)

        won = data["Graph"]["won"]
        lose = data["Graph"]["lose"]

        plt.scatter(won["time"], won["performance"], color="green")
        plt.scatter(lose["time"], lose["performance"], color="red")
        plt.xlabel("Duración de la Partida (Minutos)")
        plt.ylabel("Rendimiento del Equipo")
        plt.legend(["Partidas Ganadas", "Partidas Perdidas"])
        plt.savefig('result')
        self._result.set_from_file("result.png")

    def _handlePrediction(self,widget):
        self._controller.create_prediction()
        blue_team, red_team = (self.combo_box_page21.get_active_text(), self.combo_box_page22.get_active_text())

        if blue_team == red_team or blue_team is None or red_team is None:
            dialog = Gtk.MessageDialog(transient_for=self._window, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Debe seleccionar dos equipos diferentes, no sea imbecil")
            dialog.run()
            dialog.destroy()
        else:    
            data = self._controller.exec_strategy(blue_team, red_team)
            data = [{"team": data[0], "value": data[2]}, {"team": data[1], "value": data[3]}]

            self._team_a_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65535))
            self._team_b_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 0, 0))

            if data[0]["value"] == 0:
                self._team_a_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 0, 0))
            elif data[1]["value"] == 0:
                self._team_b_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65535))

            self.label_prediction_team_a.set_label(f'{data[0]["team"]}\n{(data[0]["value"] * 100):.4}%')
            self.label_prediction_team_b.set_label(f'{data[1]["team"]}\n{(data[1]["value"] * 100):.4}%')

            self._result_page_2.set_opacity(1)

            self._team_a_result.set_size_request(data[0]["value"]*200, 20)
            self._team_b_result.set_size_request(data[1]["value"]*200, 20)

    def _handleEvents(self):
        self._btn_analisis.connect("clicked",self._handleAnalysis)
        self._btn_prediction.connect("clicked",self._handlePrediction)

    def getGUI(self):
        self._buildPage1()
        self._buildPage2()
        self._handleEvents()
        return self._notebook