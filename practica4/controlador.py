from modelo import *
from vista import *
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(tk.Tk())
        self.vista.get_btn_cargar().config(command=self.cargar_imagen)
        self.vista.get_btn_guardar().config(command=self.guardar_imagenes)
        self.vista.get_btn_salir().config(command=self.vista.root.quit)
        self.vista.get_btn_guardar_matriz().config(command=self.guardar_datos_a_matriz)
        self.vista.get_btn_filtro_laplaciano().config(
            command=self.aplicar_filtro_laplaciano
        )
        self.vista.get_btn_segmentacion_completa_laplaciano_minimo_histograma_UA().config(
            command=self.aplicar_segmentacion_completa_laplaciano_minimo_histograma_UA
        )
        self.vista.get_btn_segmentacion_completa_minimo_histograma_UA().config(
            command=self.aplicar_segmentacion_completa_minimo_histograma_UA
        )
        self.vista.get_btn_segmentacion_completa_laplaciano_minimo_histograma_UM().config(
            command=self.aplicar_segmentacion_completa_laplaciano_minimo_histograma_UM
        )
        self.vista.get_btn_segmentacion_completa_minimo_histograma_UM().config(
            command=self.aplicar_segmentacion_completa_minimo_histograma_UM
        )
        self.vista.get_btn_mostrar_histograma().config(command=self.mostrar_histograma)

    def cargar_imagen(self):
        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if ruta:
            self.modelo.cargar_imagen(ruta)
            self.modelo.set_label("original")
            self.vista.mostrar_imagen(
                self.modelo.img_tk, "original", self.modelo.label_info_imagen_original
            )
            self.vista.ruta_imagen = ruta
            self.vista.imagen_original = self.modelo.imagen_original
            self.modelo.img_tk = None

    def guardar_imagenes(self):
        ruta_guardar = filedialog.asksaveasfilename(
            filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp")],
        )
        if ruta_guardar:
            self.modelo.guardar_imagenes(ruta_guardar)
            messagebox.showinfo("Éxito", "Imágenes guardadas correctamente.")

    # Obtener los datos de la matriz
    def guardar_datos_a_matriz(self):
        # Comprobar si la matriz de convolución ya está definida
        if self.modelo.matriz_convolucion is None:
            # Inicializar la matriz de convolución
            self.modelo.matriz_convolucion = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                valor = self.vista.get_entry_matriz(i, j).get()
                try:
                    # Convertir el valor a entero
                    valor = int(valor)
                    # Comprobar si el valor es un número
                    if not isinstance(valor, int):
                        raise ValueError
                    # Comprobar si el valor está en el rango permitido
                    if valor < -255 or valor > 255:
                        raise ValueError
                    # Asignar el valor a la matriz de convolución
                    self.modelo.matriz_convolucion[i][j] = valor
                except ValueError:
                    messagebox.showerror(
                        "Error", f"Valor no válido en la posición ({i}, {j})"
                    )
                    return

    def aplicar_filtro_laplaciano(self):
        if self.modelo.imagen is None:
            messagebox.showerror("Error", "No hay imagen cargada.")
            return
        if self.modelo.matriz_convolucion is None:
            messagebox.showerror("Error", "No hay matriz de convolución definida.")
            return
        self.modelo.aplicar_filtro_laplaciano(self.modelo.matriz_convolucion)
        if self.modelo.imagen_procesada is None:
            messagebox.showerror("Error", "No se pudo aplicar el filtro.")
            return
        self.modelo.set_label("procesada")
        self.vista.mostrar_imagen(
            self.modelo.img_tk, "procesada", self.modelo.label_info_procesada
        )
        self.modelo.img_tk = None

    def mostrar_histograma(self):
        if self.modelo.imagen is None:
            messagebox.showerror("Error", "No hay imagen cargada.")
            return
        self.modelo.mostrar_histograma()

    def aplicar_segmentacion_completa_laplaciano_minimo_histograma_UA(self):
        if self.modelo.imagen is None:
            messagebox.showerror("Error", "No hay imagen cargada.")
            return
        self.modelo.segmentar_imagen_laplacianoUA()
        if self.modelo.imagen_segmentada_laplacianoUA is None:
            messagebox.showerror("Error", "No se pudo aplicar la segmentación.")
            return
        self.modelo.set_label("segmentada laplaciano UA")
        self.vista.mostrar_imagen(
            self.modelo.img_tk, "segmentada laplaciano UA", self.modelo.label_info_segmentada_laplacianoUA
        )
        self.modelo.img_tk = None

    def aplicar_segmentacion_completa_minimo_histograma_UA(self):
        if self.modelo.imagen is None:
            messagebox.showerror("Error", "No hay imagen cargada.")
            return
        self.modelo.segmentar_imagenUA()
        if self.modelo.imagen_segmentadaUA is None:
            messagebox.showerror("Error", "No se pudo aplicar la segmentación.")
            return
        self.modelo.set_label("segmentada UA")
        self.vista.mostrar_imagen(
            self.modelo.img_tk, "segmentada UA", self.modelo.label_info_segmentadaUA
        )
        self.modelo.img_tk = None

    def aplicar_segmentacion_completa_laplaciano_minimo_histograma_UM(self):
        if self.modelo.imagen is None:
            messagebox.showerror("Error", "No hay imagen cargada.")
            return

        # Obtener el umbral del slider
        umbral = float(self.vista.get_slider_umbral())

        self.modelo.segmentar_imagen_laplacianoUM(umbral)
        if self.modelo.imagen_segmentada_laplacianoUM is None:
            messagebox.showerror("Error", "No se pudo aplicar la segmentación.")
            return
        self.modelo.set_label("segmentada laplaciano UM")
        self.vista.mostrar_imagen(
            self.modelo.img_tk, "segmentada laplaciano UM", self.modelo.label_info_segmentada_laplacianoUM
        )
        self.modelo.img_tk = None

    def aplicar_segmentacion_completa_minimo_histograma_UM(self):
        if self.modelo.imagen is None:
            messagebox.showerror("Error", "No hay imagen cargada.")
            return

        umbral = float(self.vista.get_slider_umbral())

        self.modelo.segmentar_imagenUM(umbral)
        if self.modelo.imagen_segmentadaUM is None:
            messagebox.showerror("Error", "No se pudo aplicar la segmentación.")
            return
        self.modelo.set_label("segmentada UM")
        self.vista.mostrar_imagen(
            self.modelo.img_tk, "segmentada UM", self.modelo.label_info_segmentadaUM
        )
        self.modelo.img_tk = None