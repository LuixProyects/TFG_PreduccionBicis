from Backend import Constantes
from Backend.Manipuladores import Agrupador
from Backend.estadisticasOcupacionHorarias import estadisticasOcupacionHorarias
from Frontend.Ventana import Ventana
import customtkinter as tk


class VentanaEstadisticas(Ventana):

    def __init__(self, matrices: dict):
        super().__init__("Generador de Mapas")
        self.matrices = matrices
        self.listaMatrices = []
        ventana = super().getVentanaAttribute()
        self.delta_media = tk.BooleanVar()
        self.textbox_deltasActuales = tk.CTkTextbox(master=ventana, height=5, width=135)
        self.textbox_deltasTransformar = tk.CTkTextbox(master=ventana, height=5, width=135)
        self.textbox_dias = tk.CTkTextbox(master=ventana, height=5, width=135)
        self.textbox_estacion = tk.CTkTextbox(master=ventana, height=5, width=135)
        self.combobox = tk.CTkOptionMenu(master=ventana,
                                         values=["Histograma Acumulado de una estación",
                                                 "Histograma Medio de una estación",
                                                 "Histograma Medio de todas las estaciones"],
                                         command=donothing(),
                                         )
        self.__titulo(ventana)
        self.__seleccionMatrices(ventana)
        self.__boton(ventana)
        self.__seleccionPeriodo(ventana)
        self.__seleccionarEstadisticas(ventana)
        self.__cambiarDeltas(ventana)
        super().ejecutarVentana()

    def __titulo(self, ventana):
        titulo = tk.CTkLabel(
            master=ventana,
            text="Estadisticas",
            font=("Arial", 70),
        )
        descripcion = tk.CTkLabel(
            master=ventana,
            text="Matrices a representar",
            font=("Arial", 20),
        )
        # titulo.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
        titulo.pack()
        descripcion.pack(side=tk.TOP, pady=5, padx=1, anchor="w")

    def __boton(self, ventana):
        boton = tk.CTkButton(master=ventana, text="Generar Mapa",
                             command=lambda: self.__getBotonesPulsados())
        boton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def __seleccionMatrices(self, ventana):
        check_ocupacion = tk.BooleanVar()
        check_kms_coger = tk.BooleanVar()
        check_kms_dejar = tk.BooleanVar()
        check_peticionesResueltas_coger = tk.BooleanVar()
        check_peticionesResueltas_dejar = tk.BooleanVar()
        check_peticionesNoResueltas_coger = tk.BooleanVar()
        check_peticionesNoResueltas_dejar = tk.BooleanVar()
        check_peticionesFicticias_NoResueltas_coger = tk.BooleanVar()
        check_peticionesFicticias_NoResueltas_dejar = tk.BooleanVar()
        check_ocupacionRelativa = tk.BooleanVar()
        check_kmsFicticios_coger = tk.BooleanVar()
        check_kmsFicticios_dejar = tk.BooleanVar()
        check_NoResueltas_ficticias_coger = tk.BooleanVar()
        check_NoResueltas_ficticias_dejar = tk.BooleanVar()

        self.listaMatrices = [check_ocupacion, check_ocupacionRelativa, check_kms_coger, check_kms_dejar,
                              check_peticionesResueltas_coger,
                              check_peticionesResueltas_dejar, check_peticionesNoResueltas_coger,
                              check_peticionesNoResueltas_dejar
            , check_peticionesFicticias_NoResueltas_coger, check_peticionesFicticias_NoResueltas_dejar,
                              check_kmsFicticios_coger, check_kmsFicticios_dejar, check_NoResueltas_ficticias_coger,
                              check_NoResueltas_ficticias_dejar]

        # Creamos el checkbox
        check_button1 = tk.CTkCheckBox(ventana, text="Ocupaciones", variable=check_ocupacion)
        check_button2 = tk.CTkCheckBox(ventana, text="Kilometros coger bicicleta", variable=check_kms_coger)
        check_button3 = tk.CTkCheckBox(ventana, text="Kilometros dejar bicicleta", variable=check_kms_dejar)
        check_button4 = tk.CTkCheckBox(ventana, text="Peticiones Resueltas coger bicicleta",
                                       variable=check_peticionesResueltas_coger)
        check_button5 = tk.CTkCheckBox(ventana, text="Peticiones Resueltas dejar bicicleta",
                                       variable=check_peticionesResueltas_dejar)
        check_button6 = tk.CTkCheckBox(ventana, text="Peticiones no resueltas coger bicicleta",
                                       variable=check_peticionesNoResueltas_coger)
        check_button7 = tk.CTkCheckBox(ventana, text="Peticiones no resueltas dejar bicicleta",
                                       variable=check_peticionesNoResueltas_dejar)
        check_button8 = tk.CTkCheckBox(ventana, text="Peticiones ficticias no resueltas coger",
                                       variable=check_peticionesFicticias_NoResueltas_coger)
        check_button9 = tk.CTkCheckBox(ventana, text="Peticiones ficticias no resueltas dejar",
                                       variable=check_peticionesFicticias_NoResueltas_dejar)
        check_button10 = tk.CTkCheckBox(ventana, text="Ocupación relativa", variable=check_ocupacionRelativa)
        check_button11 = tk.CTkCheckBox(ventana, text="Kilometros ficticios coger", variable=check_kmsFicticios_coger)
        check_button12 = tk.CTkCheckBox(ventana, text="Kilometros ficticios dejar", variable=check_kmsFicticios_dejar)
        check_button13 = tk.CTkCheckBox(ventana, text="Peticiones no resueltas ficticias coger",
                                        variable=check_NoResueltas_ficticias_coger)
        check_button14 = tk.CTkCheckBox(ventana, text="Peticiones no resueltas ficticias dejar",
                                        variable=check_NoResueltas_ficticias_dejar)

        # Colocamos el checkbox en la ventana
        check_button1.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button2.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button3.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button4.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button5.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button6.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button7.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button8.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button9.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button10.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button11.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button12.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button13.pack(side=tk.TOP, pady=5, padx=1, anchor="w")
        check_button14.pack(side=tk.TOP, pady=5, padx=1, anchor="w")

    # Función perteneciente del bloque encargado de cambiar las deltas times de los datos
    def __cambiarDeltas(self, ventana):
        titulo = tk.CTkLabel(
            master=ventana,
            text="Seleccione los deltas a trasformar:",
            font=("Arial", 20),
        )
        titulo.place(relx=0.6, rely=0.5)

        self.textbox_deltasActuales.place(relx=0.6, rely=0.6)
        self.textbox_deltasTransformar.place(relx=0.7, rely=0.6)
        check_mediaOacumulada = tk.CTkCheckBox(ventana, text="Media/Acumulada", variable=self.delta_media)
        check_mediaOacumulada.place(relx=0.8, rely=0.5)

    def __seleccionPeriodo(self, ventana):
        titulo = tk.CTkLabel(
            master=ventana,
            text="Seleccione los periodos que deasea:",
            font=("Arial", 20),
        )
        titulo.place(relx=0.6, rely=0.3)
        textbox_periodo_inicio = tk.CTkTextbox(master=ventana, height=5, width=135)
        textbox_periodo_inicio.place(relx=0.6, rely=0.4)

        textbox_periodo_final = tk.CTkTextbox(master=ventana, height=5, width=135)
        textbox_periodo_final.place(relx=0.7, rely=0.4)


        titulo2 = tk.CTkLabel(
            master=ventana,
            text="Selecciona la estación y días que desees en el caso de representaciones diarias:",
            font=("Arial", 20),
        )
        titulo2.place(relx=0.6, rely=0.65)

        self.textbox_estacion.place(relx=0.6,rely=0.7)
        self.textbox_dias.place(relx=0.7, rely=0.7)

    def __seleccionarEstadisticas(self, ventana):

        self.combobox.place(relx=0.3, rely=0.3)
        self.combobox.set("Selecciona la estadistica")

    def generarMapa(self):
        print()

    def __getBotonesPulsados(self):
        seleccionados = []
        for i in range(len(self.listaMatrices)):
            if self.listaMatrices[i].get():
                seleccionados.append(Constantes.LISTA_MATRICES[i])

        ###Selección de matrices:

        # En la lista seleccionados tenemos todas las matrices seleccionadas para su unificación.
        matrizDeseada = self.matrices[seleccionados[0]].matrix
        if len(seleccionados) > 1:
            for i in range(1, len(seleccionados)):
                matrizDeseada = Agrupador.agruparMatrices(matrizDeseada, self.matrices[seleccionados[i]].matrix)

        ###Configuración de deltas:
        # Compruebo que exista texto.
        delta = Constantes.DELTA_TIME
        if not self.textbox_deltasActuales.get("0.0", 'end-1c') == "" or not self.textbox_deltasActuales.get("0.0",
                                                                                                             'end-1c') == "":
            aux_deltaInicial = int(self.textbox_deltasActuales.get("0.0", 'end-1c'))
            aux_deltaFinal = int(self.textbox_deltasActuales.get("0.0", 'end-1c'))
            delta = aux_deltaFinal
            if self.delta_media.get():  # Si el usuario quiere agrupar por media:
                matrizDeseada = Agrupador.colapsarDeltasMedia(matrizDeseada, aux_deltaInicial, aux_deltaFinal)
            else:
                matrizDeseada = Agrupador.colapsarDeltasAcumulacion(matrizDeseada, aux_deltaInicial, aux_deltaFinal)

        matrizDeseada = Agrupador.colapsarDeltasMedia(matrizDeseada,15,60)

        dias_escogidos = list(map(int, self.textbox_dias.get("0.0", 'end-1c').split(',')))
        estacion_elegida = int(self.textbox_estacion.get("0.0", 'end-1c'))

        eOH = estadisticasOcupacionHorarias(matrizDeseada, delta)
        if self.combobox.get() == "Histograma Acumulado de una estación":
            eOH.HistogramaAcumulacion(estacion_elegida,dias_escogidos)
        else:
            if self.combobox.get() == "Histograma Medio de una estación":
                eOH.HistogramaPorEstacion(estacion_elegida,dias_escogidos)
            else:
                if self.combobox.get() == "Histograma Medio de todas las estaciones":
                    eOH.HistogramaOcupacionMedia(dias_escogidos)


def donothing():
    x = 0
