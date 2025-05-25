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
            "Mostrar Histograma de Color",
            command=lambda: self.mostrar_histograma("rgb"),
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Mostrar Histograma de Escala de Grises",
            command=lambda: self.mostrar_histograma("grises"),
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Mostrar Histograma de Binario",
            command=lambda: self.mostrar_histograma("binario"),
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Extraer Canal Rojo",
            command=lambda: self.extraer_canales("r"),
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Extraer Canal Verde",
            command=lambda: self.extraer_canales("g"),
        )
        self.vista.get_menu_histogramas_canales().entryconfig(
            "Extraer Canal Azul",
            command=lambda: self.extraer_canales("b"),
        )
        self.vista.get_menu_filtros().entryconfig(
            "Filtro de gausiano", command=self.abrir_y_conectar_filtro_gaussiano
        )
        self.vista.get_menu_filtros().entryconfig(
            "Filtro sal y pimienta", command=self.abrir_y_conectar_filtro_sal_pimienta
        )
        self.vista.get_menu_filtros().entryconfig(
            "Filtro de laplaciano", command=self.abrir_y_conectar_filtro_laplaciano
        )
        self.vista.get_menu_segmetacion().entryconfig(
            "Segmentación por minimo histograma",
            command=self.abrir_y_conectar_segmentacion,
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

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_conversion_grises,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton_grises = self.vista.get_boton_grises()
        if boton_grises is not None:
            boton_grises.config(command=self.aplicar_escala_grises)

        boton_grises_c = self.vista.get_boton_grises_c()
        if boton_grises_c is not None:
            boton_grises_c.config(command=self.aplicar_escala_grises_c)

    def aplicar_escala_grises(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.convertir_RGB_a_grises(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_conversion_grises
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def aplicar_escala_grises_c(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.convertir_RGB_a_grises_c(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_conversion_grises
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conversion_binario(self):
        self.vista.abrir_ventana_conversion_binario()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_conversion_grises,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton_manual = self.vista.get_boton_umbralizado_manual()
        if boton_manual is not None:
            boton_manual.config(command=self.aplicar_binarizado_manual)

        boton_auto = self.vista.get_boton_umbralizado_auto()
        if boton_auto is not None:
            boton_auto.config(command=self.aplicar_binarizado_auto)

    def aplicar_binarizado_manual(self):
        if self.vista.imagen_original is not None:
            umbral = self.vista.get_slider_binario().get()

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.convertir_RGB_a_binario(imagen_seleccionada, umbral)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_conversion_binario
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def aplicar_binarizado_auto(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.convertir_RGB_a_binario_a(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_conversion_binario
            )
            self.modelo.img_tk1 = None
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

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventanda_correcion,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_correccion_gamma()
        if boton is not None:
            boton.config(command=self.aplicar_contraste)

    def aplicar_contraste(self):
        if self.vista.imagen_original is not None:
            gamma = self.vista.get_slider_contraste_gamma().get()

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_correccion_contraste(imagen_seleccionada, gamma)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventanda_correcion
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def mostrar_histograma(self, tipo):
        if tipo == "rgb":
            if (
                self.vista.imagen_original is not None
                or self.vista.imagen_correccion is not None
            ):
                if self.vista.imagen_original is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen, "rgb")
                if self.vista.imagen_original is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_correccion, "rgb"
                    )
            else:
                messagebox.showinfo("Información", "Primero cargue una imagen.")
        elif tipo == "grises":
            if (
                self.vista.imagen_grises is not None
                or self.vista.imagen_grises_c is not None
            ):
                if self.vista.imagen_grises is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen_grises, "grises")
                if self.vista.imagen_grises_c is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_grises_c, "grises"
                    )
            else:
                messagebox.showinfo(
                    "Información", "Primero convierta la imagen a escala de grises."
                )
        elif tipo == "binario":
            if (
                self.vista.imagen_umbral_manual is not None
                or self.vista.imagen_umbral_manual_c is not None
                or self.vista.imagen_umbral_automatico is not None
                or self.vista.imagen_umbral_automatico_c is not None
            ):
                if self.vista.imagen_umbral_manual is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_grises, "binario"
                    )
                if self.vista.imagen_umbral_manual_c is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_grises_c, "binario"
                    )
                if self.vista.imagen_umbral_automatico is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_grises, "binario"
                    )
                if self.vista.imagen_umbral_automatico_c is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_grises_c, "binario"
                    )
            else:
                messagebox.showinfo(
                    "Información", "Primero convierta la imagen a binario."
                )

    def extraer_canales(self, tipo):
        if tipo == "r" and self.vista.imagen_original is not None:
            self.modelo.extrae_canales(self.modelo.imagen_original, tipo)
        elif tipo == "g" and self.vista.imagen_original is not None:
            self.modelo.extrae_canales(self.modelo.imagen_original, tipo)
        elif tipo == "b" and self.vista.imagen_original is not None:
            self.modelo.extrae_canales(self.modelo.imagen_original, tipo)
        else:
            messagebox.showinfo("Información", "Primero cargue una imagen.")

    def abrir_y_conectar_filtro_gaussiano(self):
        self.vista.abrir_ventana_filtro_gaussiano()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_filtro_gaussiano,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_aplicar_filtro_gaussiano()
        if boton is not None:
            boton.config(command=self.aplicar_filtro_gaussiano)

    def aplicar_filtro_gaussiano(self):
        if self.vista.imagen_original is not None:
            sigma = self.vista.get_slider_filtro_gaussiano_sigma().get()

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_filtro_gaussiano(imagen_seleccionada, sigma)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_filtro_gaussiano
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_filtro_sal_pimienta(self):
        self.vista.abrir_ventana_filtro_sal_pimienta()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_filtro_sal_pimienta,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_aplicar_filtro_sal_pimienta()
        if boton is not None:
            boton.config(command=self.aplicar_filtro_sal_pimienta)

    def aplicar_filtro_sal_pimienta(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_filtro_sal_pimienta(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_filtro_sal_pimienta
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_filtro_laplaciano(self):
        self.vista.abrir_ventana_filtro_laplaciano()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_filtro_laplaciano,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton_guardar = self.vista.get_boton_guardar_matriz()
        if boton_guardar is not None:
            boton_guardar.config(command=self.guardar_matriz)
            boton_aplicar = self.vista.get_boton_aplicar_filtro_laplaciano()
            if boton_aplicar is not None:
                boton_aplicar.config(command=self.aplicar_filtro_laplaciano)

    def guardar_matriz(self):
        self.matriz_laplaciana_temp = self.vista.get_matriz_convolucion()

    def aplicar_filtro_laplaciano(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            matriz = getattr(self, "matriz_laplaciana_temp", None)
            if matriz is not None:
                self.modelo.aplicar_filtro_laplaciano(imagen_seleccionada, matriz)
                self.vista.mostrar_imagen_unica(
                    self.modelo.img_tk1, self.vista.ventana_filtro_laplaciano
                )
                self.modelo.img_tk1 = None
            else:
                messagebox.showwarning(
                    "Advertencia", "Primero guarde la matriz de convolución."
                )
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_segmentacion(self):
        self.vista.abrir_ventana_segmentacion()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_segmentacion,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton_seg_lua = self.vista.get_boton_aplicar_segmentacion_lua()
        if boton_seg_lua is not None:
            boton_seg_lua.config(command=self.aplicar_segmentacion_lua)
        boton_seg_lum = self.vista.get_boton_aplicar_segmentacion_lum()
        if boton_seg_lum is not None:
            boton_seg_lum.config(command=self.aplicar_segmentacion_lum)
        boton_seg_ua = self.vista.get_boton_aplicar_segmentacion_ua()
        if boton_seg_ua is not None:
            boton_seg_ua.config(command=self.aplicar_segmentacion_ua)
        boton_seg_um = self.vista.get_boton_aplicar_segmentacion_um()
        if boton_seg_um is not None:
            boton_seg_um.config(command=self.aplicar_segmentacion_um)

    def aplicar_segmentacion_lua(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_segmentacion_lua(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def aplicar_segmentacion_lum(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            umbral = self.vista.get_slider_segmentacion().get()

            self.modelo.aplicar_segmentacion_lum(imagen_seleccionada, umbral)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def aplicar_segmentacion_ua(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_segmentacion_ua(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def aplicar_segmentacion_um(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_segmentacion_um(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")
