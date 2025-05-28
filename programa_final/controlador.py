from modelo import *
from vista import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


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
            "Corrección de Contraste",
            command=self.abrir_y_conectar_correcion_contraste,
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
        self.vista.get_menu_operaciones().entryconfig(
            "Not",
            command=self.abrir_y_conectar_conversion_not,
        )
        self.vista.get_menu_operaciones().entryconfig(
            "Or",
            command=self.abrir_y_conectar_conversion_or,
        )
        self.vista.get_menu_operaciones().entryconfig(
            "And",
            command=self.abrir_y_conectar_conversion_and,
        )
        self.vista.get_menu_operaciones().entryconfig(
            "Xor",
            command=self.abrir_y_conectar_conversion_xor,
        )
        self.vista.get_menu_filtros().entryconfig(
            "Filtro de gausiano",
            command=self.abrir_y_conectar_filtro_gaussiano,
        )
        self.vista.get_menu_filtros().entryconfig(
            "Filtro sal y pimienta",
            command=self.abrir_y_conectar_filtro_sal_pimienta,
        )
        self.vista.get_menu_filtros().entryconfig(
            "Filtro de laplaciano",
            command=self.abrir_y_conectar_filtro_laplaciano,
        )
        self.vista.get_menu_segmentacion().entryconfig(
            "Segmentación por minimo histograma",
            command=self.abrir_y_conectar_segmentacion_minimo,
        )
        self.vista.get_menu_segmentacion().entryconfig(
            "Segmentación por multiples umbrales",
            command=self.abrir_y_conectar_segmentacion_multi_umbral,
        )
        self.vista.get_menu_conectividades().entryconfig(
            "Etiquetado de componentes conectados-4",
            command=self.abrir_y_conectar_conectividad_4,
        )
        self.vista.get_menu_conectividades().entryconfig(
            "Etiquetado de componentes conectados-8",
            command=self.abrir_y_conectar_conectividad_8,
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

        # Limpiar todas las imágenes del modelo al cargar una nueva imagen
        self.modelo.imagen_grises = None
        self.modelo.imagen_grises_c = None
        self.modelo.imagen_umbral_manual = None
        self.modelo.imagen_umbral_automatico = None
        self.modelo.imagen_umbral_manual_c = None
        self.modelo.imagen_umbral_automatico_c = None
        self.modelo.imagen_ruido = None
        self.modelo.imagen_correccion = None
        self.modelo.imagen_filtrada = None
        self.modelo.imagen_filtrada_sal_pimienta = None
        self.modelo.imagen_laplaciana = None
        self.modelo.imagen_segmentada_um = None
        self.modelo.imagen_segmentada_lum = None
        self.modelo.imagen_segmentada_ua = None
        self.modelo.imagen_segmentada_lua = None
        self.modelo.imagen_segmentada_multi_umbral = None
        self.modelo.imagen_not = None
        self.modelo.imagen_and = None
        self.modelo.imagen_or = None
        self.modelo.imagen_xor = None
        self.modelo.imagen_conectividad_4 = None
        self.modelo.imagen_conectividad_8 = None

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
            boton_guardar = self.vista.get_boton_guardar_grises()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_grises)
                )

        boton_grises_c = self.vista.get_boton_grises_c()
        if boton_grises_c is not None:
            boton_grises_c.config(command=self.aplicar_escala_grises_c)
            boton_guardar = self.vista.get_boton_guardar_grises()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_grises_c)
                )

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
            self.vista.ventana_conversion_binario,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton_manual = self.vista.get_boton_umbralizado_manual()
        if boton_manual is not None:
            boton_manual.config(command=self.aplicar_binarizado_manual)
            boton_guardar = self.vista.get_boton_guardar_binario()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_umbral_manual
                    )
                )

        boton_auto = self.vista.get_boton_umbralizado_auto()
        if boton_auto is not None:
            boton_auto.config(command=self.aplicar_binarizado_auto)
            boton_guardar = self.vista.get_boton_guardar_binario()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_umbral_automatico
                    )
                )

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

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventanda_ruido,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_ruido_gaussiano()
        if boton is not None:
            boton.config(command=self.aplicar_ruido)
            boton_guardar = self.vista.get_boton_guardar_ruido()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_ruido)
                )

    def aplicar_ruido(self):
        if self.vista.imagen_original is not None:
            media = self.vista.get_slider_ruido_media().get()
            sigma = self.vista.get_slider_ruido_sigma().get()

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_ruido_gaussiano(imagen_seleccionada, media, sigma)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventanda_ruido
            )
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
            boton_guardar = self.vista.get_boton_guardar_contraste()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_correccion)
                )

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
            if self.vista.imagen_original is not None:
                if self.vista.imagen_original is not None:
                    self.modelo.calcular_histograma(self.modelo.imagen, "rgb")
                if self.vista.imagen_original is not None:
                    self.modelo.calcular_histograma(
                        self.modelo.imagen_correccion, "rgb"
                    )
            else:
                messagebox.showinfo("Información", "Primero cargue una imagen.")
        elif tipo == "grises":
            if self.vista.imagen_original is not None:
                self.modelo.calcular_histograma(self.modelo.imagen_grises, "grises")
                self.modelo.calcular_histograma(self.modelo.imagen_grises_c, "grises")
            else:
                messagebox.showinfo(
                    "Información", "Primero convierta la imagen a escala de grises."
                )
        elif tipo == "binario":
            if self.vista.imagen_original is not None:
                self.modelo.calcular_histograma(self.modelo.imagen_grises, "binario")
                self.modelo.calcular_histograma(self.modelo.imagen_grises_c, "binario")
                self.modelo.calcular_histograma(self.modelo.imagen_grises, "binario")
                self.modelo.calcular_histograma(self.modelo.imagen_grises_c, "binario")
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

    def abrir_y_conectar_conversion_not(self):
        self.vista.abrir_ventana_not()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_not,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_conversion_not()
        if boton is not None:
            boton.config(command=self.aplicar_conversion_not)
            boton_guardar = self.vista.get_boton_guardar_not()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_not)
                )

    def aplicar_conversion_not(self):
        if self.vista.imagen_original is not None:

            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_conversion_not(imagen_seleccionada)

            self.vista.mostrar_imagen_unica(self.modelo.img_tk1, self.vista.ventana_not)
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conversion_or(self):
        self.vista.abrir_ventana_or()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())

        # Crear dos combobox para seleccionar dos imágenes distintas
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_or,
            nombres,
            label_text="Imagen 1:",
            frame=self.vista.frame_botones,
        )
        # Guardar referencia al primer combobox
        self.combobox_imagen1 = self.vista.combobox_imagenes

        self.vista.crear_combobox_imagenes(
            self.vista.ventana_or,
            nombres,
            label_text="Imagen 2:",
            frame=self.vista.frame_botones,
        )
        # Guardar referencia al segundo combobox
        self.combobox_imagen2 = self.vista.combobox_imagenes

        boton = self.vista.get_boton_conversion_or()
        if boton is not None:
            boton.config(command=self.aplicar_conversion_or)
            boton_guardar = self.vista.get_boton_guardar_or()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_or)
                )

    def aplicar_conversion_or(self):
        if self.vista.imagen_original is not None:
            # Obtener los nombres de las dos imágenes seleccionadas
            imagen_seleccionada_nombre1 = (
                self.combobox_imagen1.get()
                if self.combobox_imagen1 is not None
                else None
            )
            imagen_seleccionada_nombre2 = (
                self.combobox_imagen2.get()
                if self.combobox_imagen2 is not None
                else None
            )

            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada1 = imagenes.get(imagen_seleccionada_nombre1)
            imagen_seleccionada2 = imagenes.get(imagen_seleccionada_nombre2)

            if imagen_seleccionada1 is None or imagen_seleccionada2 is None:
                messagebox.showwarning("Advertencia", "Seleccione dos imágenes.")
                return

            # Pasar ambas imágenes al modelo
            self.modelo.aplicar_conversion_or(
                imagen_seleccionada1, imagen_seleccionada2
            )

            self.vista.mostrar_imagen_unica(self.modelo.img_tk1, self.vista.ventana_or)
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conversion_and(self):
        self.vista.abrir_ventana_and()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())

        # Crear dos combobox para seleccionar dos imágenes distintas
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_and,
            nombres,
            label_text="Imagen 1:",
            frame=self.vista.frame_botones,
        )
        self.combobox_imagen1_and = self.vista.combobox_imagenes

        self.vista.crear_combobox_imagenes(
            self.vista.ventana_and,
            nombres,
            label_text="Imagen 2:",
            frame=self.vista.frame_botones,
        )
        self.combobox_imagen2_and = self.vista.combobox_imagenes

        boton = self.vista.get_boton_conversion_and()
        if boton is not None:
            boton.config(command=self.aplicar_conversion_and)
            boton_guardar = self.vista.get_boton_guardar_and()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_and)
                )

    def aplicar_conversion_and(self):
        if self.vista.imagen_original is not None:
            imagen_seleccionada_nombre1 = (
                self.combobox_imagen1_and.get()
                if self.combobox_imagen1_and is not None
                else None
            )
            imagen_seleccionada_nombre2 = (
                self.combobox_imagen2_and.get()
                if self.combobox_imagen2_and is not None
                else None
            )

            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada1 = imagenes.get(imagen_seleccionada_nombre1)
            imagen_seleccionada2 = imagenes.get(imagen_seleccionada_nombre2)

            if imagen_seleccionada1 is None or imagen_seleccionada2 is None:
                messagebox.showwarning("Advertencia", "Seleccione dos imágenes.")
                return

            self.modelo.aplicar_conversion_and(
                imagen_seleccionada1, imagen_seleccionada2
            )

            self.vista.mostrar_imagen_unica(self.modelo.img_tk1, self.vista.ventana_and)
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conversion_xor(self):
        self.vista.abrir_ventana_xor()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())

        self.vista.crear_combobox_imagenes(
            self.vista.ventana_xor,
            nombres,
            label_text="Imagen 1:",
            frame=self.vista.frame_botones,
        )
        self.combobox_imagen1_xor = self.vista.combobox_imagenes

        self.vista.crear_combobox_imagenes(
            self.vista.ventana_xor,
            nombres,
            label_text="Imagen 2:",
            frame=self.vista.frame_botones,
        )
        self.combobox_imagen2_xor = self.vista.combobox_imagenes

        boton = self.vista.get_boton_conversion_xor()
        if boton is not None:
            boton.config(command=self.aplicar_conversion_xor)
            boton_guardar = self.vista.get_boton_guardar_xor()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_xor)
                )

    def aplicar_conversion_xor(self):
        if self.vista.imagen_original is not None:
            imagen_seleccionada_nombre1 = (
                self.combobox_imagen1_xor.get()
                if self.combobox_imagen1_xor is not None
                else None
            )
            imagen_seleccionada_nombre2 = (
                self.combobox_imagen2_xor.get()
                if self.combobox_imagen2_xor is not None
                else None
            )

            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada1 = imagenes.get(imagen_seleccionada_nombre1)
            imagen_seleccionada2 = imagenes.get(imagen_seleccionada_nombre2)

            if imagen_seleccionada1 is None or imagen_seleccionada2 is None:
                messagebox.showwarning("Advertencia", "Seleccione dos imágenes.")
                return

            self.modelo.aplicar_conversion_xor(
                imagen_seleccionada1, imagen_seleccionada2
            )

            self.vista.mostrar_imagen_unica(self.modelo.img_tk1, self.vista.ventana_xor)
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

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
            boton_guardar = self.vista.get_boton_guardar_filtro_gaussiano()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(self.modelo.imagen_filtrada)
                )

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
            boton_guardar = self.vista.get_boton_guardar_filtro_sal_pimienta()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_filtrada_sal_pimienta
                    )
                )

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
                boton_guardar = self.vista.get_boton_guardar_filtro_laplaciano()
                if boton_guardar is not None:
                    boton_guardar.config(
                        command=lambda: self.guardar_imagen(
                            self.modelo.imagen_laplaciana
                        )
                    )

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

    def abrir_y_conectar_segmentacion_minimo(self):
        self.vista.abrir_ventana_segmentacion_minimo()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_segmentacion_minimo,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton_seg_lua = self.vista.get_boton_aplicar_segmentacion_lua()
        if boton_seg_lua is not None:
            boton_seg_lua.config(command=self.aplicar_segmentacion_lua)
            boton_guardar = self.vista.get_boton_guardar_segmentacion_minimo()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_segmentada_lua
                    )
                )
        boton_seg_lum = self.vista.get_boton_aplicar_segmentacion_lum()
        if boton_seg_lum is not None:
            boton_seg_lum.config(command=self.aplicar_segmentacion_lum)
            boton_guardar = self.vista.get_boton_guardar_segmentacion_minimo()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_segmentada_lum
                    )
                )
        boton_seg_ua = self.vista.get_boton_aplicar_segmentacion_ua()
        if boton_seg_ua is not None:
            boton_seg_ua.config(command=self.aplicar_segmentacion_ua)
            boton_guardar = self.vista.get_boton_guardar_segmentacion_minimo()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_segmentada_ua
                    )
                )
        boton_seg_um = self.vista.get_boton_aplicar_segmentacion_um()
        if boton_seg_um is not None:
            boton_seg_um.config(command=self.aplicar_segmentacion_um)
            boton_guardar = self.vista.get_boton_guardar_segmentacion_minimo()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_segmentada_um
                    )
                )

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
                self.modelo.img_tk1, self.vista.ventana_segmentacion_minimo
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

            umbral = self.vista.get_slider_segmentacion_minimo().get()

            self.modelo.aplicar_segmentacion_lum(imagen_seleccionada, umbral)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion_minimo
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
                self.modelo.img_tk1, self.vista.ventana_segmentacion_minimo
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

            umbral = self.vista.get_slider_segmentacion_minimo().get()

            self.modelo.aplicar_segmentacion_um(imagen_seleccionada, umbral)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion_minimo
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_segmentacion_multi_umbral(self):
        self.vista.abrir_ventana_segmentacion_multi_umbral()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_segmentacion_multi_umbral,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_aplicar_segmentacion_multi_umbral()
        if boton is not None:
            boton.config(command=self.aplicar_segmentacion_multi_umbral)
            boton_guardar = self.vista.get_boton_guardar_segmentacion_multi_umbral()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_segmentada_multi_umbral
                    )
                )

    def aplicar_segmentacion_multi_umbral(self):
        if self.vista.imagen_original is not None:
            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            umbral1 = self.vista.get_slider_segmentacion_multi_umbral_1().get()
            umbral2 = self.vista.get_slider_segmentacion_multi_umbral_2().get()

            self.modelo.aplicar_segmentacion_multi_umbral(
                imagen_seleccionada, umbral1, umbral2
            )
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_segmentacion_multi_umbral
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conectividad_4(self):
        self.vista.abrir_ventana_conectividad_4()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_conectividad_4,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_aplicar_conectividad_4()
        if boton is not None:
            boton.config(command=self.aplicar_conectividad_4)
            boton_guardar = self.vista.get_boton_guardar_conectividad_4()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_conectividad_4
                    )
                )

    def aplicar_conectividad_4(self):
        if self.vista.imagen_original is not None:
            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_conectividad_4(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_conectividad_4
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def abrir_y_conectar_conectividad_8(self):
        self.vista.abrir_ventana_conectividad_8()

        imagenes = self.modelo.obtener_lista_imagenes()
        nombres = list(imagenes.keys())  # Solo los nombres
        self.vista.crear_combobox_imagenes(
            self.vista.ventana_conectividad_8,
            nombres,
            frame=self.vista.frame_botones,
        )

        boton = self.vista.get_boton_aplicar_conectividad_8()
        if boton is not None:
            boton.config(command=self.aplicar_conectividad_8)
            boton_guardar = self.vista.get_boton_guardar_conectividad_8()
            if boton_guardar is not None:
                boton_guardar.config(
                    command=lambda: self.guardar_imagen(
                        self.modelo.imagen_conectividad_8
                    )
                )

    def aplicar_conectividad_8(self):
        if self.vista.imagen_original is not None:
            combobox = self.vista.get_combobox_imagenes()
            imagen_seleccionada_nombre = (
                combobox.get() if combobox is not None else None
            )
            imagenes = self.modelo.obtener_lista_imagenes()
            imagen_seleccionada = imagenes.get(imagen_seleccionada_nombre)

            self.modelo.aplicar_conectividad_8(imagen_seleccionada)
            self.vista.mostrar_imagen_unica(
                self.modelo.img_tk1, self.vista.ventana_conectividad_8
            )
            self.modelo.img_tk1 = None
        else:
            messagebox.showwarning("Advertencia", "Primero cargue una imagen.")

    def guardar_imagen(self, imagen):
        ruta_guardar = filedialog.asksaveasfilename(
            filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp")],
        )
        if ruta_guardar:
            self.modelo.guardar_imagenes(ruta_guardar, imagen)
            messagebox.showinfo("Éxito", "Imágen guardada correctamente.")
            imagen = None
