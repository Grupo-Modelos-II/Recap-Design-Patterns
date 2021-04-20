import pgi
import matplotlib
import matplotlib.pyplot as plt
from functions import functions as f
from pgi.repository import Gtk, Gdk
from controllers.Controller import Controller

matplotlib.use("GTK3Agg")
pgi.require_version("Gtk", "3.0")

class Menu(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Design Patterns")
        Gtk.Window.set_default_size (self,800,800)

        self._controller = Controller()

       
    def handle_analysis(self,widget):
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
        


    def handle_prediction(self,widget):
        self._controller.create_prediction()
        blue_team, red_team = (self.combo_box_page21.get_active_text(), self.combo_box_page22.get_active_text())

        if blue_team == red_team or blue_team is None or red_team is None:
            dialog = Gtk.MessageDialog(transient_for=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="No sea imbecil")
            dialog.run()
            dialog.destroy()
        else:    
            data = self._controller.exec_strategy(blue_team, red_team)
            data = [{"team": data[0], "value": data[2]}, {"team": data[1], "value": data[3]}]

            self._team_a_result.set_opacity(1)
            self._team_b_result.set_opacity(1)

            if data[0]["value"] == 0:
                self._team_a_result.set_opacity(0)
            elif data[1]["value"] == 0:
                self._team_b_result.set_opacity(0)

            self.label_prediction_team_a.set_label(f'{data[0]["team"]}\n{(data[0]["value"] * 100):.4}%')
            self.label_prediction_team_b.set_label(f'{data[1]["team"]}\n{(data[1]["value"] * 100):.4}%')

            self._result_page_2.set_opacity(1)

            self._team_a_result.set_size_request(data[0]["value"]*200, 20)
            self._team_b_result.set_size_request(data[1]["value"]*200, 20)


    def init_template(self):
        self.set_resizable(False)
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
        [self._combo_box_1.append(id=None,text=str(name)) for name in f.get_team_list()]

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
        combo_box_container = Gtk.VBox(orientation=Gtk.Orientation.HORIZONTAL,spacing=100)

        self.combo_box_page21 = Gtk.ComboBoxText()
        [self.combo_box_page21.append(id=None,text=str(name)) for name in f.get_team_list()]
        combo_box_container.add(self.combo_box_page21)

        self.combo_box_page22 = Gtk.ComboBoxText()
        [self.combo_box_page22.append(id=None,text=str(name)) for name in f.get_team_list()]
        combo_box_container.add(self.combo_box_page22)

        self.page2.add(combo_box_container)
        self.page2.add(self._btn_prediction)

        self.notebook.append_page(self.page2, Gtk.Label(label="Predicción"))

        #Information Page 1
        ## Label Page 1 Results
        self._label_result = Gtk.Label()
        self._label_result.set_label("")

        self.page1.add(self._label_result)

        ## Image Page 1 Results
        self._result = Gtk.Image()
        self.page1.add(self._result)

        #Information Page 2
        ## LevelBar Page 2 Results

        labels_container = Gtk.VBox(orientation=Gtk.Orientation.HORIZONTAL,spacing=100)

        self.label_prediction_team_a = Gtk.Label()
        self.label_prediction_team_b = Gtk.Label()

        labels_container.add(self.label_prediction_team_a)
        labels_container.add(self.label_prediction_team_b)

        self.page2.add(labels_container)

        self._result_page_2 = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        self._team_a_result = Gtk.LevelBar()
        self._team_b_result = Gtk.LevelBar()

        self._team_a_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65535))
        self._team_b_result.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 0, 0))

        self._team_a_result.set_size_request(0, 0)
        self._team_b_result.set_size_request(0, 0)

        self._result_page_2.pack1(self._team_a_result, False, False)
        self._result_page_2.pack2(self._team_b_result, False, False)

        self._result_page_2.set_opacity(0)

        self.page2.add(self._result_page_2)

        

        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()


