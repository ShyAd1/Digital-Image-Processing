from modelo import *
from vista import *
import tkinter as tk
from tkinter import filedialog, messagebox


class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(tk.Tk())
        self.vista.get_menu_abrir().entryconfig(
            "Abrir",
            command=self.cargar_imagen,
        )
        self.vista.get_menu_conversion().entryconfig(
            "Convertir de RGB a Escala de Grises",
            command=self.abrir_y_conectar_conversion_grises,
        )
        self.vista.get_menu_conversion().entryconfig(
            "Convertir de RGB a Binario",
            command=self.abrir_y_conectar_conversion_binario,
        )
        self.vista.get_menu_correcciones().entryconfig(
            "Aplicar Ruido Gaussiano",
            command=self.abrir_y_conectar_aplicar_ruido,
        )
        self.vista.get_menu_correcciones().entryconfig(
            "Corrección de Contraste", command=self.abrir_y_conectar_correcion_contraste
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Mostrar Histograma de Color", command=lambda: self.mostrar_histograma("rgb")
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Mostrar Histograma de Escala de Grises", command=lambda: self.mostrar_histograma("grises")
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Mostrar Histograma de Binario", command=lambda: self.mostrar_histograma("binario")
        )

    def cargar_imagen(self):
        # Aquí llamas al método de modelo para cargar la imagen
        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if ruta:
            self.modelo.cargar_imagen(ruta)
            self.vista.mostrar_imagen(self.modelo.img_tk1, "original")
            self.vista.ruta_imagen = ruta
            self.modelo.img_tk1 = None

    def abrir_y_conectar_conversion_grises(self):
        self.vista.abrir_ventana_conversion_grises()
        boton = self.vista.get_boton_grises()
        if boton is not None:
            boton.config(command=self.aplicar_escala_grises)

    def aplicar_escala_grises(self):
        if self.vista.imagen_original is not None:
            self.modelo.convertir_RGB_a_grises(
                self.modelo.imagen_original, self.modelo.imagen_correccion
            )
            self.vista.mostrar_imagen(self.modelo.img_tk1, "grises")
            self.vista.mostrar_imagen(self.modelo.img_tk2, "grises_c")
            self.modelo.img_tk1 = None
            self.modelo.img_tk2 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conversion_binario(self):
        self.vista.abrir_ventana_conversion_binario()
        boton = self.vista.get_boton_umbralizado()
        if boton is not None:
            boton.config(command=self.aplicar_binarizado)

    def aplicar_binarizado(self):
        if self.vista.imagen_original is not None:
            umbral = self.vista.get_slider_binario().get()
            self.modelo.convertir_RGB_a_binario(
                self.modelo.imagen_original,
                self.modelo.imagen_correccion,
                umbral,
            )
            self.vista.mostrar_imagen(self.modelo.img_tk1, "umbral_manual")
            self.vista.mostrar_imagen(self.modelo.img_tk2, "umbral_automatico")
            self.vista.mostrar_imagen(self.modelo.img_tk3, "umbral_manual_c")
            self.vista.mostrar_imagen(self.modelo.img_tk4, "umbral_automatico_c")
            self.modelo.img_tk1 = None
            self.modelo.img_tk2 = None
            self.modelo.img_tk3 = None
            self.modelo.img_tk4 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_aplicar_ruido(self):
        self.vista.abrir_ventana_aplicar_ruido()
        boton = self.vista.get_boton_ruido_gaussiano()
        if boton is not None:
            boton.config(command=self.aplicar_ruido)

    def aplicar_ruido(self):
        if self.vista.imagen_original is not None:
            media = self.vista.get_slider_ruido_media().get()
            sigma = self.vista.get_slider_ruido_sigma().get()
            self.modelo.aplicar_ruido_gaussiano(media, sigma)
            self.vista.mostrar_imagen(self.modelo.img_tk1, "ruido")
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_correcion_contraste(self):
        self.vista.abrir_ventana_correcion_contraste()
        boton = self.vista.get_boton_correccion_gamma()
        if boton is not None:
            boton.config(command=self.aplicar_contraste)

    def aplicar_contraste(self):
        if self.vista.imagen_original is not None:
            gamma = self.vista.get_slider_contraste_gamma().get()
            self.modelo.aplicar_correccion_contraste(gamma)
            self.vista.mostrar_imagen(self.modelo.img_tk1, "correccion")
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def mostrar_histograma(self, tipo):
        if tipo == "rgb":
            if self.vista.imagen_original is not None:
                self.modelo.calcular_histograma(self.modelo.imagen, "rgb")
            else:
                messagebox.showinfo("Información", "Primero cargue una imagen.")
        elif tipo == "grises":
            if self.vista.imagen_grises is not None or self.vista.imagen_grises_c is not None:
                if self.vista.imagen_grises is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises, "grises")
                if self.vista.imagen_grises_c is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises_c, "grises")
            else:
                messagebox.showinfo("Información", "Primero convierta la imagen a escala de grises.")
        elif tipo == "binario":
            if (
                self.vista.imagen_umbral_manual is not None
                or self.vista.imagen_umbral_manual_c is not None
                or self.vista.imagen_umbral_automatico is not None
                or self.vista.imagen_umbral_automatico_c is not None
            ):
                if self.vista.imagen_umbral_manual is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises, "binario")
                if self.vista.imagen_umbral_manual_c is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises_c, "binario")
                if self.vista.imagen_umbral_automatico is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises, "binario")
                if self.vista.imagen_umbral_automatico_c is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises_c, "binario")
            else:
                messagebox.showinfo("Información", "Primero convierta la imagen a binario.")