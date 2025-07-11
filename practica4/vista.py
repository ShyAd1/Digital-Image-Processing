import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tkinter import ttk


class Vista:
    def __init__(self, root):
        # Inicializar la ventana principal
        self.root = root
        self.root.title("Procesador de Imágenes")
        self.root.geometry("1400x800")

        # Crear pestañas para la interfaz
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both")
        self.btns_CGS = ttk.Frame(self.notebook)
        self.btns_FlS = ttk.Frame(self.notebook)
        self.ajustes = ttk.Frame(self.notebook)
        self.notebook.add(self.btns_CGS, text="Cargar y Guardar")
        self.notebook.add(self.ajustes, text="Ajustes adicionales")
        self.notebook.add(self.btns_FlS, text="Filtros y Segmentación")

        # Crear variables para almacenar las imágenes
        self.imagen_original = None
        self.ruta_imagen = None
        self.imagen_procesada = None
        self.imagen_segmentadaUA = None
        self.imagen_segmentada_laplacianoUA = None
        self.imagen_segmentadaUM = None
        self.imagen_segmentada_laplacianoUM = None
        self.threshold = 128

        # Crear botones para cargar y guardar imágenes
        self.btn_cargar = ttk.Button(self.btns_CGS, text="Cargar Imagen", width=15)
        self.btn_cargar.grid(row=0, column=0, padx=10, pady=10)
        self.btn_guardar = ttk.Button(self.btns_CGS, text="Guardar Imagen", width=15)
        self.btn_guardar.grid(row=0, column=1, padx=10, pady=10)
        self.btn_salir = ttk.Button(self.btns_CGS, text="Salir", width=15)
        self.btn_salir.grid(row=0, column=2, padx=10, pady=10)

        # Crear ventana para la matriz de convolución
        self.label_matriz = ttk.Label(self.ajustes, text="Matriz de Convolución")
        self.label_matriz.grid(row=0, column=1, padx=10, pady=10)
        for i in range(3):
            for j in range(3):
                self.entry_matriz = ttk.Entry(self.ajustes, width=5)
                self.entry_matriz.grid(row=i + 1, column=j, padx=10, pady=10)

        # Crear botón para guardar la matriz de convolución
        self.btn_guardar_matriz = ttk.Button(self.ajustes, text="Guardar Matriz")
        self.btn_guardar_matriz.grid(row=4, column=1, padx=10, pady=10)

        # Crear slider para ajustar el umbral
        self.label_umbral = tk.Label(self.ajustes, text="Ajuste de umbral")
        self.label_umbral.grid(row=3, column=3, padx=10, pady=10)
        self.slider_umbral = tk.Scale(
            self.ajustes, from_=0, to=255, orient="horizontal", length=200
        )
        self.slider_umbral.set(self.threshold)
        self.slider_umbral.grid(row=2, column=3, padx=10, pady=10)

        # Crear botones para aplicar filtros y segmentación
        self.btn_filtro_laplaciano = ttk.Button(self.btns_FlS, text="Filtro Laplaciano")
        self.btn_filtro_laplaciano.grid(row=0, column=0, padx=10, pady=10)

        self.btn_segmentacion_completa_minimo_histograma_UA = ttk.Button(
            self.btns_FlS, text="Segmentación Completa del por Mínimo Histograma (Umbral automático)"
        )
        self.btn_segmentacion_completa_minimo_histograma_UA.grid(
            row=0, column=1, padx=10, pady=10
        )

        self.btn_segmentacion_completa_laplaciano_minimo_histograma_UA = ttk.Button(
            self.btns_FlS, text="Segmentación Completa del lapalaciano por Mínimo Histograma (Umbral automático)"
        )
        self.btn_segmentacion_completa_laplaciano_minimo_histograma_UA.grid(
            row=0, column=2, padx=10, pady=10
        )

        self.btn_segmentacion_completa_minimo_histograma_UM = ttk.Button(
            self.btns_FlS, text="Segmentación Completa del por Mínimo Histograma (Umbral manual)"
        )
        self.btn_segmentacion_completa_minimo_histograma_UM.grid(
            row=1, column=0, padx=10, pady=10
        )

        self.btn_segmentacion_completa_laplaciano_minimo_histograma_UM = ttk.Button(
            self.btns_FlS, text="Segmentación Completa del lapalaciano por Mínimo Histograma (Umbral manual)"
        )
        self.btn_segmentacion_completa_laplaciano_minimo_histograma_UM.grid(
            row=1, column=1, padx=10, pady=10
        )

        self.mostrar_histograma = ttk.Button(self.btns_FlS, text="Mostrar Histograma")
        self.mostrar_histograma.grid(row=1, column=2, padx=10, pady=10)


        # Crear área de visualización de imágenes
        self.frame_imagen = ttk.Frame(self.root)
        self.frame_imagen.pack(pady=20)
        self.label_imagen_original = ttk.Label(self.frame_imagen)
        self.label_imagen_original.grid(row=0, column=0, padx=10, pady=10)
        self.label_imagen_procesada = ttk.Label(self.frame_imagen)
        self.label_imagen_procesada.grid(row=0, column=1, padx=10, pady=10)
        self.label_imagen_segmentada_laplacianoUA = ttk.Label(self.frame_imagen)
        self.label_imagen_segmentada_laplacianoUA.grid(row=0, column=2, padx=10, pady=10)

        self.label_imagen_segmentadaUA = ttk.Label(self.frame_imagen)
        self.label_imagen_segmentadaUA.grid(row=2, column=0, padx=10, pady=10)
        self.label_imagen_segmentada_laplacianoUM = ttk.Label(self.frame_imagen)
        self.label_imagen_segmentada_laplacianoUM.grid(row=2, column=1, padx=10, pady=10)
        self.label_imagen_segmentadaUM = ttk.Label(self.frame_imagen)
        self.label_imagen_segmentadaUM.grid(row=2, column=2, padx=10, pady=10)

        #  Crear etiquetas para mostrar información
        self.label_info_imagen_original = ttk.Label(self.frame_imagen, text="")
        self.label_info_imagen_original.grid(row=1, column=0, padx=10, pady=10)
        self.label_info_procesada = ttk.Label(self.frame_imagen, text="")
        self.label_info_procesada.grid(row=1, column=1, padx=10, pady=10)
        self.label_info_segmentada_laplacianoUA = ttk.Label(self.frame_imagen, text="")
        self.label_info_segmentada_laplacianoUA.grid(row=1, column=2, padx=10, pady=10)
        self.label_info_segmentadaUA = ttk.Label(self.frame_imagen, text="")
        self.label_info_segmentadaUA.grid(row=3, column=0, padx=10, pady=10)
        self.label_info_segmentada_laplacianoUM = ttk.Label(self.frame_imagen, text="")
        self.label_info_segmentada_laplacianoUM.grid(row=3, column=1, padx=10, pady=10)
        self.label_info_segmentadaUM = ttk.Label(self.frame_imagen, text="")
        self.label_info_segmentadaUM.grid(row=3, column=2, padx=10, pady=10)

    # getters para los botones
    def get_btn_cargar(self):
        return self.btn_cargar

    def get_btn_guardar(self):
        return self.btn_guardar

    def get_btn_salir(self):
        return self.btn_salir

    def get_btn_guardar_matriz(self):
        return self.btn_guardar_matriz

    def get_entry_matriz(self, i, j):
        return self.ajustes.grid_slaves(row=i + 1, column=j)[0]

    def get_btn_filtro_laplaciano(self):
        return self.btn_filtro_laplaciano

    def get_btn_segmentacion_completa_laplaciano_minimo_histograma_UA(self):
        return self.btn_segmentacion_completa_laplaciano_minimo_histograma_UA

    def get_btn_segmentacion_completa_minimo_histograma_UA(self):
        return self.btn_segmentacion_completa_minimo_histograma_UA

    def get_btn_segmentacion_completa_laplaciano_minimo_histograma_UM(self):
        return self.btn_segmentacion_completa_laplaciano_minimo_histograma_UM

    def get_btn_segmentacion_completa_minimo_histograma_UM(self):
        return self.btn_segmentacion_completa_minimo_histograma_UM

    def get_label_imagen_original(self):
        return self.label_imagen_original

    def get_label_imagen_procesada(self):
        return self.label_imagen_procesada

    def get_label_imagen_segmentada_UA(self):
        return self.label_imagen_segmentadaUA

    def get_label_imagen_segmentada_laplaciano_UA(self):
        return self.label_imagen_segmentada_laplacianoUA

    def get_label_imagen_segmentada_UM(self):
        return self.label_imagen_segmentadaUM

    def get_label_imagen_segmentada_laplaciano_UM(self):
        return self.label_imagen_segmentada_laplacianoUM

    def get_slider_umbral(self):
        return self.slider_umbral.get()

    def get_btn_mostrar_histograma(self):
        return self.mostrar_histograma

    def get_ruta_imagen(self):
        return self.ruta_imagen

    def mostrar_imagen(self, imagen, tipo, info):
        if tipo == "original":
            self.imagen_original = imagen
            self.label_imagen_original.config(image=self.imagen_original)
            self.label_imagen_original.image = imagen
            self.label_info_imagen_original.config(text=info)
        elif tipo == "procesada":
            self.imagen_procesada = imagen
            self.label_imagen_procesada.config(image=imagen)
            self.label_imagen_procesada.image = imagen
            self.label_info_procesada.config(text=info)
        elif tipo == "segmentada laplaciano UA":
            self.imagen_segmentada_laplacianoUA = imagen
            self.label_imagen_segmentada_laplacianoUA.config(image=imagen)
            self.label_imagen_segmentada_laplacianoUA.image = imagen
            self.label_info_segmentada_laplacianoUA.config(text=info)
        elif tipo == "segmentada UA":
            self.imagen_segmentadaUA = imagen
            self.label_imagen_segmentadaUA.config(image=imagen)
            self.label_imagen_segmentadaUA.image = imagen
            self.label_info_segmentadaUA.config(text=info)
        elif tipo == "segmentada laplaciano UM":
            self.imagen_segmentada_laplacianoUM = imagen
            self.label_imagen_segmentada_laplacianoUM.config(image=imagen)
            self.label_imagen_segmentada_laplacianoUM.image = imagen
            self.label_info_segmentada_laplacianoUM.config(text=info)
        elif tipo == "segmentada UM":
            self.imagen_segmentadaUM = imagen
            self.label_imagen_segmentadaUM.config(image=imagen)
            self.label_imagen_segmentadaUM.image = imagen
            self.label_info_segmentadaUM.config(text=info)

    def mainloop(self):
        self.root.mainloop()
