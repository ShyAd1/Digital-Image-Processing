import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Vista:
    def __init__(self, root):
        # Inicializar la ventana principal
        self.root = root
        self.root.title("Procesador de Imágenes")
        self.root.geometry("1600x900")

        # Ruta orginal
        self.ruta_imagen = None

        # Crear la barra de menú
        self.menubar = tk.Menu(self.root)

        # Crear el menú "Archivo"
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(
            label="Abrir",
            command=None,
        )
        self.menubar.add_cascade(label="Archivo", menu=self.file_menu)

        # Crear el menú "Conversión"
        self.convert_menu = tk.Menu(self.menubar, tearoff=0)
        self.convert_menu.add_command(
            label="Convertir de RGB a Escala de Grises",
            command=None,
        )
        self.convert_menu.add_separator()
        self.convert_menu.add_command(
            label="Convertir de RGB a Binario",
            command=None,
        )
        self.menubar.add_cascade(label="Conversiónes", menu=self.convert_menu)

        # Crear el menú "Mostrar Histograma y Extracción de canales"
        self.histogram_menu = tk.Menu(self.menubar, tearoff=0)
        self.histogram_menu.add_command(
            label="Mostrar Histograma de Color",
            command=None,
        )
        self.histogram_menu.add_separator()
        self.histogram_menu.add_command(
            label="Mostrar Histograma de Escala de Grises",
            command=None,
        )
        self.histogram_menu.add_separator()
        self.histogram_menu.add_command(
            label="Mostrar Histograma de Binario",
            command=None,
        )
        self.histogram_menu.add_separator()
        self.histogram_menu.add_command(
            label="Extraer Canal Rojo",
            command=None,
        )
        self.histogram_menu.add_separator()
        self.histogram_menu.add_command(
            label="Extraer Canal Verde",
            command=None,
        )
        self.histogram_menu.add_separator()
        self.histogram_menu.add_command(
            label="Extraer Canal Azul",
            command=None,
        )
        self.menubar.add_cascade(
            label="Mostrar Histogramas y Canales", menu=self.histogram_menu
        )

        # Crear el menú "Operaciones"
        self.operation_menu = tk.Menu(self.menubar, tearoff=0)
        self.operation_menu.add_command(
            label="Not",
            command=None,
        )
        self.operation_menu.add_separator()
        self.operation_menu.add_command(
            label="Or",
            command=None,
        )
        self.operation_menu.add_separator()
        self.operation_menu.add_command(
            label="And",
            command=None,
        )
        self.operation_menu.add_separator()
        self.operation_menu.add_command(
            label="Xor",
            command=None,
        )
        self.menubar.add_cascade(label="Operaciones", menu=self.operation_menu)

        # Crear el menú "Correcciones de ruido y contraste"
        self.correction_menu = tk.Menu(self.menubar, tearoff=0)
        self.correction_menu.add_command(
            label="Aplicar Ruido Gaussiano",
            command=None,
        )
        self.correction_menu.add_separator()
        self.correction_menu.add_command(
            label="Corrección de Contraste",
            command=None,
        )
        self.menubar.add_cascade(label="Correcciones", menu=self.correction_menu)

        # Crear el menú "Filtros"
        self.filter_menu = tk.Menu(self.menubar, tearoff=0)
        self.filter_menu.add_command(
            label="Filtro de gausiano",
            command=None,
        )
        self.filter_menu.add_separator()
        self.filter_menu.add_command(
            label="Filtro sal y pimienta",
            command=None,
        )
        self.filter_menu.add_separator()
        self.filter_menu.add_command(
            label="Filtro de laplaciano",
            command=None,
        )
        self.menubar.add_cascade(label="Filtros", menu=self.filter_menu)

        # Crear el menú "Segmentación"
        self.segmentation_menu = tk.Menu(self.menubar, tearoff=0)
        self.segmentation_menu.add_command(
            label="Segmentación por minimo histograma",
            command=None,
        )
        self.segmentation_menu.add_separator()
        self.segmentation_menu.add_command(
            label="Segmentación por multiples umbrales",
            command=None,
        )
        self.menubar.add_cascade(label="Segmentaciónes", menu=self.segmentation_menu)

        # Crear el menú "Etiquetado"
        self.labeling_menu = tk.Menu(self.menubar, tearoff=0)
        self.labeling_menu.add_command(
            label="Conectividad 4",
            command=None,
        )
        self.labeling_menu.add_separator()
        self.labeling_menu.add_command(
            label="Conectividad 8",
            command=None,
        )
        self.labeling_menu.add_separator()
        self.labeling_menu.add_command(
            label="Etiquetado Conectividad 4",
            command=None,
        )
        self.labeling_menu.add_separator()
        self.labeling_menu.add_command(
            label="Etiquetado Conectividad 8",
            command=None,
        )
        self.menubar.add_cascade(label="Etiquetado", menu=self.labeling_menu)

        # Crear el menú "Calculo de los etiquetados"
        self.calculation_menu = tk.Menu(self.menubar, tearoff=0)
        self.calculation_menu.add_command(
            label="Calculo de area",
            command=None,
        )
        self.calculation_menu.add_separator()
        self.calculation_menu.add_command(
            label="Calculo de perimetro",
            command=None,
        )
        self.menubar.add_cascade(
            label="Calculo de los etiquetados", menu=self.calculation_menu
        )

        # Crear el menú "Ayuda"
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(
            label="Acerca de",
            command=None,
        )
        self.menubar.add_cascade(label="Ayuda", menu=self.help_menu)

        # Crear área de visualización de la imagen original
        self.frame_imagen = ttk.Frame(self.root)
        self.frame_imagen.pack(pady=20)

        self.imagen_original = tk.Label(self.frame_imagen)
        self.imagen_original.grid(row=1, column=0, padx=10, pady=5)

        # Asignar la barra de menús a la ventana
        self.root.config(menu=self.menubar)

    def abrir_ventana_conversion_grises(self):
        # Crear una ventana para la conversion de RGB a Escala de grises
        self.ventana_conversion_grises = tk.Toplevel(self.root)
        self.ventana_conversion_grises.title("Conversión de RGB a Escala de grises")
        self.ventana_conversion_grises.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_conversion_grises)
        self.frame_botones.pack(pady=10)

        # Crear botón para convertir a escala de grises
        self.boton_grises = ttk.Button(
            self.frame_botones, text="Aplicar conversión a Escala de grises"
        )
        self.boton_grises.pack(side=tk.LEFT, padx=5)

        # Crear botón para convertir a escala de grises con correcion de contraste
        self.boton_grises_c = ttk.Button(
            self.frame_botones, text="Aplicar conversión a Escala de grises (contraste)"
        )
        self.boton_grises_c.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_conversion_binario(self):
        # Crear una ventana para la conversión de RGB a Binario
        self.ventana_conversion_binario = tk.Toplevel(self.root)
        self.ventana_conversion_binario.title("Conversión de RGB a Binario")
        self.ventana_conversion_binario.geometry("1600x900")

        # Crear marco para el slider (fijo en la parte superior)
        self.frame_slider = tk.Frame(self.ventana_conversion_binario)
        self.frame_slider.pack(pady=20)

        # Crear label para el slider
        self.label_slider = tk.Label(
            self.frame_slider, text="Umbral de conversión (0-255):"
        )
        self.label_slider.pack(side=tk.LEFT, padx=5)

        # Crear slider para el umbral
        self.slider = tk.Scale(
            self.frame_slider,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            length=200,
        )
        self.slider.set(128)
        self.slider.pack(side=tk.LEFT, padx=5)

        # Crear un marco para los botones y acomodarlos horizontalmente (fijo en la parte inferior)
        self.frame_botones = tk.Frame(self.ventana_conversion_binario)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar umbralizado
        self.boton_umbralizado_manual = ttk.Button(
            self.frame_botones, text="Aplicar umbralizado manual"
        )
        self.boton_umbralizado_manual.pack(side=tk.LEFT, padx=5)

        self.boton_umbralizado_auto = ttk.Button(
            self.frame_botones, text="Aplicar umbralizado automatico"
        )
        self.boton_umbralizado_auto.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultados")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_aplicar_ruido(self):
        # Crear una ventana para la correcion_contraste
        self.ventanda_ruido = tk.Toplevel(self.root)
        self.ventanda_ruido.title("Aplicar ruido gaussiano")
        self.ventanda_ruido.geometry("1600x900")

        # Crear marco para los sliders
        self.frame_sliders = tk.Frame(self.ventanda_ruido)
        self.frame_sliders.pack(pady=20)

        # Crear label para el slider de media
        self.label_slider1 = tk.Label(
            self.frame_sliders, text="Ajustar valor de media (0-100):"
        )
        self.label_slider1.pack(side=tk.LEFT, padx=5)

        # Crear slider para la media
        self.slider1 = tk.Scale(
            self.frame_sliders,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=200,
        )
        self.slider1.set(0)
        self.slider1.pack(side=tk.LEFT, padx=5)

        # Crear label para el slider de sigma
        self.label_slider2 = tk.Label(
            self.frame_sliders, text="Ajustar valor de sigma (0-100):"
        )
        self.label_slider2.pack(side=tk.LEFT, padx=5)

        # Crear slider para el sigma
        self.slider2 = tk.Scale(
            self.frame_sliders,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=200,
        )
        self.slider2.set(25)
        self.slider2.pack(side=tk.LEFT, padx=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventanda_ruido)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar el ruido gaussiano
        self.boton_ruido_gaussiano = ttk.Button(
            self.frame_botones, text="Aplicar ruido gaussiano"
        )
        self.boton_ruido_gaussiano.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_correcion_contraste(self):
        # Crear una ventana para la correcion_contraste
        self.ventanda_correcion = tk.Toplevel(self.root)
        self.ventanda_correcion.title("Correccion de contraste")
        self.ventanda_correcion.geometry("1600x900")

        # Crear marco para el slider
        self.frame_slider = tk.Frame(self.ventanda_correcion)
        self.frame_slider.pack(pady=20)

        # Crear label para el slider
        self.label_slider3 = tk.Label(
            self.frame_slider, text="Ajustar valor de gamma (0.1-2):"
        )
        self.label_slider3.pack(side=tk.LEFT, padx=5)

        # Crear slider para el gamma
        self.slider3 = tk.Scale(
            self.frame_slider,
            from_=0.1,
            to=2,
            orient=tk.HORIZONTAL,
            length=200,
            resolution=0.1,
        )
        self.slider3.set(0.5)
        self.slider3.pack(side=tk.LEFT, padx=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventanda_correcion)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la correccion gamma
        self.boton_correccion_gamma = ttk.Button(
            self.frame_botones, text="Aplicar corrección gamma"
        )
        self.boton_correccion_gamma.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_not(self):
        # Crear una ventana para la not
        self.ventana_not = tk.Toplevel(self.root)
        self.ventana_not.title("Convercion Inversa")
        self.ventana_not.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_not)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la conversion not
        self.boton_conversion_not = ttk.Button(
            self.frame_botones, text="Aplicar conversion Not"
        )
        self.boton_conversion_not.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_or(self):
        # Crear una ventana para la or
        self.ventana_or = tk.Toplevel(self.root)
        self.ventana_or.title("Conversion Or")
        self.ventana_or.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_or)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la correccion gamma
        self.boton_conversion_or = ttk.Button(
            self.frame_botones, text="Aplicar conversion Or"
        )
        self.boton_conversion_or.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_and(self):
        # Crear una ventana para la and
        self.ventana_and = tk.Toplevel(self.root)
        self.ventana_and.title("Conversion And")
        self.ventana_and.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_and)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la correccion gamma
        self.boton_conversion_and = ttk.Button(
            self.frame_botones, text="Aplicar conversion And"
        )
        self.boton_conversion_and.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_xor(self):
        # Crear una ventana para la xor
        self.ventana_xor = tk.Toplevel(self.root)
        self.ventana_xor.title("Conversion Xor")
        self.ventana_xor.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_xor)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la correccion gamma
        self.boton_conversion_xor = ttk.Button(
            self.frame_botones, text="Aplicar conversion Xor"
        )
        self.boton_conversion_xor.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_filtro_gaussiano(self):
        # Crear una ventana para el filtro gaussiano
        self.ventana_filtro_gaussiano = tk.Toplevel(self.root)
        self.ventana_filtro_gaussiano.title("Filtro Gaussiano")
        self.ventana_filtro_gaussiano.geometry("1600x900")

        # Crear marco para el slider de sigma
        self.frame_slider = tk.Frame(self.ventana_filtro_gaussiano)
        self.frame_slider.pack(pady=20)

        # Crear label para el slider de sigma
        self.label_sigma = tk.Label(
            self.frame_slider, text="Ajustar valor de sigma (0.01-1):"
        )
        self.label_sigma.pack(side=tk.LEFT, padx=5)

        # Crear slider para sigma
        self.slider_sigma = tk.Scale(
            self.frame_slider,
            from_=0.01,
            to=1,
            orient=tk.HORIZONTAL,
            length=200,
            resolution=0.01,
        )
        self.slider_sigma.set(0.50)
        self.slider_sigma.pack(side=tk.LEFT, padx=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_filtro_gaussiano)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar el filtro gaussiano
        self.boton_aplicar_filtro_gaussiano = ttk.Button(
            self.frame_botones, text="Aplicar filtro gaussiano"
        )
        self.boton_aplicar_filtro_gaussiano.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_filtro_sal_pimienta(self):
        # Crear una ventana para el filtro sal y pimienta
        self.ventana_filtro_sal_pimienta = tk.Toplevel(self.root)
        self.ventana_filtro_sal_pimienta.title("Filtro Sal y Pimienta")
        self.ventana_filtro_sal_pimienta.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_filtro_sal_pimienta)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar el filtro sal y pimienta
        self.boton_aplicar_filtro_sal_pimienta = ttk.Button(
            self.frame_botones, text="Aplicar filtro sal y pimienta"
        )
        self.boton_aplicar_filtro_sal_pimienta.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_filtro_laplaciano(self):
        # Crear una ventana para el filtro Laplaciano
        self.ventana_filtro_laplaciano = tk.Toplevel(self.root)
        self.ventana_filtro_laplaciano.title("Filtro Laplaciano")
        self.ventana_filtro_laplaciano.geometry("1600x900")

        # Crear frame para la matriz de convolucion
        self.frame_matriz = tk.Frame(self.ventana_filtro_laplaciano)
        self.frame_matriz.pack(pady=20)

        # Crear la matriz de convolución en forma de tabla 3x3
        self.label_matriz = ttk.Label(self.frame_matriz, text="Matriz de Convolución")
        self.label_matriz.grid(row=0, column=0, columnspan=3, pady=5)
        self.entries_matriz = []
        for i in range(3):
            fila = []
            for j in range(3):
                entry = ttk.Entry(self.frame_matriz, width=5)
                entry.grid(row=i + 1, column=j, padx=5, pady=5)
                fila.append(entry)
            self.entries_matriz.append(fila)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_filtro_laplaciano)
        self.frame_botones.pack(pady=10)

        # Crear botón para guardar la matriz de convolución
        self.boton_guardar_matriz = ttk.Button(
            self.frame_botones, text="Guardar Matriz"
        )
        self.boton_guardar_matriz.pack(side=tk.LEFT, padx=5)

        # Crear botón para aplicar el filtro laplaciano
        self.boton_aplicar_filtro_laplaciano = ttk.Button(
            self.frame_botones, text="Aplicar filtro laplaciano"
        )
        self.boton_aplicar_filtro_laplaciano.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_segmentacion_minimo(self):
        # Crear una ventana para la segmentación por mínimo de histograma
        self.ventana_segmentacion_minimo = tk.Toplevel(self.root)
        self.ventana_segmentacion_minimo.title("Segmentación por mínimo de histograma")
        self.ventana_segmentacion_minimo.geometry("1600x900")

        # Crear marco para el slider de umbral
        self.frame_slider = tk.Frame(self.ventana_segmentacion_minimo)
        self.frame_slider.pack(pady=20)

        # Crear label para el slider
        self.label_slider4 = tk.Label(
            self.frame_slider, text="Umbral de segmentación (0-255):"
        )
        self.label_slider4.pack(side=tk.LEFT, padx=5)

        # Crear slider para el umbral
        self.slider4 = tk.Scale(
            self.frame_slider,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            length=200,
        )
        self.slider4.set(128)
        self.slider4.pack(side=tk.LEFT, padx=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_segmentacion_minimo)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la segmentación umbral manual
        self.boton_aplicar_segmentacion_um = ttk.Button(
            self.frame_botones, text="Aplicar segmentación umbral manual"
        )
        self.boton_aplicar_segmentacion_um.pack(side=tk.LEFT, padx=5)

        # Crear botón para aplicar la segmentación laplaciana umbral manual
        self.boton_aplicar_segmentacion_lum = ttk.Button(
            self.frame_botones, text="Aplicar segmentación laplaciana umbral manual"
        )
        self.boton_aplicar_segmentacion_lum.pack(side=tk.LEFT, padx=5)

        # Crear botón para aplicar la segmentación umbral automático
        self.boton_aplicar_segmentacion_ua = ttk.Button(
            self.frame_botones, text="Aplicar segmentación umbral automatico"
        )
        self.boton_aplicar_segmentacion_ua.pack(side=tk.LEFT, padx=5)

        # Crear botón para aplicar la segmentación laplaciana umbral automático
        self.boton_aplicar_segmentacion_lua = ttk.Button(
            self.frame_botones, text="Aplicar segmentación laplaciana umbral automatico"
        )
        self.boton_aplicar_segmentacion_lua.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados (abajo de los de segmentación)
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_segmentacion_multi_umbral(self):
        # Crear una ventana para la segmentación por múltiples umbrales
        self.ventana_segmentacion_multi_umbral = tk.Toplevel(self.root)
        self.ventana_segmentacion_multi_umbral.title(
            "Segmentación por múltiples umbrales"
        )
        self.ventana_segmentacion_multi_umbral.geometry("1600x900")

        # Crear marco para los sliders
        self.frame_slider = tk.Frame(self.ventana_segmentacion_multi_umbral)
        self.frame_slider.pack(pady=20)

        # Crear label para el slider
        self.label_slider5 = tk.Label(
            self.frame_slider, text="Umbral de segmentación (0-255):"
        )
        self.label_slider5.pack(side=tk.LEFT, padx=5)

        # Crear slider para el umbral
        self.slider5 = tk.Scale(
            self.frame_slider,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            length=200,
        )
        self.slider5.set(128)
        self.slider5.pack(side=tk.LEFT, padx=5)

        # Crear segundo label para el slider
        self.label_slider6 = tk.Label(
            self.frame_slider, text="Umbral de segmentación (0-255):"
        )
        self.label_slider6.pack(side=tk.LEFT, padx=5)

        # Crear segundo slider para el umbral
        self.slider6 = tk.Scale(
            self.frame_slider,
            from_=0,
            to=255,
            orient=tk.HORIZONTAL,
            length=200,
        )
        self.slider6.set(128)
        self.slider6.pack(side=tk.LEFT, padx=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_segmentacion_multi_umbral)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la segmentación por múltiples umbrales
        self.boton_aplicar_segmentacion_multi_umbral = ttk.Button(
            self.frame_botones, text="Aplicar segmentación por múltiples umbrales"
        )
        self.boton_aplicar_segmentacion_multi_umbral.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_conectividad_4(self):
        # Crear una ventana para mostrar la conectividad 4
        self.ventana_conectividad_4 = tk.Toplevel(self.root)
        self.ventana_conectividad_4.title("Conectividad 4")
        self.ventana_conectividad_4.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_conectividad_4)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar conectividad 4
        self.boton_aplicar_conectividad_4 = ttk.Button(
            self.frame_botones, text="Aplicar conectividad 4"
        )
        self.boton_aplicar_conectividad_4.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_conectividad_8(self):
        # Crear una ventana para mostrar la conectividad 8
        self.ventana_conectividad_8 = tk.Toplevel(self.root)
        self.ventana_conectividad_8.title("Conectividad 8")
        self.ventana_conectividad_8.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_conectividad_8)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar conectividad 8
        self.boton_aplicar_conectividad_8 = ttk.Button(
            self.frame_botones, text="Aplicar conectividad 8"
        )
        self.boton_aplicar_conectividad_8.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_etiquetado_conectividad_4(self):
        # Crear una ventana para el etiquetado con conectividad 4
        self.ventana_etiquetado_conectividad_4 = tk.Toplevel(self.root)
        self.ventana_etiquetado_conectividad_4.title("Etiquetado Conectividad 4")
        self.ventana_etiquetado_conectividad_4.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_etiquetado_conectividad_4)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar etiquetado conectividad 4
        self.boton_aplicar_etiquetado_conectividad_4 = ttk.Button(
            self.frame_botones, text="Aplicar etiquetado conectividad 4"
        )
        self.boton_aplicar_etiquetado_conectividad_4.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def abrir_ventana_etiquetado_conectividad_8(self):
        # Crear una ventana para el etiquetado con conectividad 8
        self.ventana_etiquetado_conectividad_8 = tk.Toplevel(self.root)
        self.ventana_etiquetado_conectividad_8.title("Etiquetado Conectividad 8")
        self.ventana_etiquetado_conectividad_8.geometry("1600x900")

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_etiquetado_conectividad_8)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar etiquetado conectividad 8
        self.boton_aplicar_etiquetado_conectividad_8 = ttk.Button(
            self.frame_botones, text="Aplicar etiquetado conectividad 8"
        )
        self.boton_aplicar_etiquetado_conectividad_8.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def mostrar_imagen(self, imagen, tipo):
        if tipo == "original":
            self.imagen_original.config(image=imagen)
            self.imagen_original.image = imagen

    def mostrar_imagen_unica(self, imagen, ventana, label_attr="imagen_unica"):
        # Crea el label si no existe o si fue destruido
        label = getattr(self, label_attr, None)
        if label is None or not str(label):
            frame = ttk.Frame(ventana)
            frame.pack(pady=20)
            label = tk.Label(frame)
            label.pack()
            setattr(self, label_attr, label)
        try:
            label.config(image=imagen)
            label.image = imagen
        except tk.TclError:
            # El label fue destruido, crearlo de nuevo
            frame = ttk.Frame(ventana)
            frame.pack(pady=20)
            label = tk.Label(frame)
            label.pack()
            setattr(self, label_attr, label)
            label.config(image=imagen)
            label.image = imagen

    def crear_combobox_imagenes(
        self, ventana, imagenes, label_text="Selecciona una imagen:", frame=None
    ):
        # Usa el frame proporcionado o crea uno nuevo en la ventana
        parent = frame if frame is not None else ventana
        self.frame_combobox = ttk.Frame(parent)
        self.frame_combobox.pack(side=tk.LEFT, padx=5)

        # Label descriptivo
        self.label_combobox = ttk.Label(self.frame_combobox, text=label_text)
        self.label_combobox.pack(side=tk.LEFT, padx=5)

        # Combobox con la lista de nombres de imágenes
        max_length = max((len(str(nombre)) for nombre in imagenes), default=20)
        width = min(
            max_length, 80
        )  # Limita el ancho máximo para evitar que sea demasiado grande
        self.combobox_imagenes = ttk.Combobox(
            self.frame_combobox, values=imagenes, state="readonly", width=width
        )
        self.combobox_imagenes.pack(side=tk.LEFT, padx=5)

    # Getters para los botones
    def get_boton_grises(self):
        return getattr(self, "boton_grises", None)

    def get_boton_grises_c(self):
        return getattr(self, "boton_grises_c", None)

    def get_boton_guardar_grises(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_conversion_grises")
            else None
        )

    def get_boton_umbralizado_manual(self):
        return getattr(self, "boton_umbralizado_manual", None)

    def get_boton_umbralizado_auto(self):
        return getattr(self, "boton_umbralizado_auto", None)

    def get_boton_guardar_binario(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_conversion_binario")
            else None
        )

    def get_boton_ruido_gaussiano(self):
        return getattr(self, "boton_ruido_gaussiano", None)

    def get_boton_guardar_ruido(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventanda_ruido")
            else None
        )

    def get_boton_correccion_gamma(self):
        return getattr(self, "boton_correccion_gamma", None)

    def get_boton_guardar_contraste(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventanda_correcion")
            else None
        )

    def get_boton_conversion_not(self):
        return getattr(self, "boton_conversion_not", None)

    def get_boton_guardar_not(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventanda_not")
            else None
        )

    def get_boton_conversion_or(self):
        return getattr(self, "boton_conversion_or", None)

    def get_boton_guardar_or(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_or")
            else None
        )

    def get_boton_conversion_and(self):
        return getattr(self, "boton_conversion_and", None)

    def get_boton_guardar_and(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_and")
            else None
        )

    def get_boton_conversion_xor(self):
        return getattr(self, "boton_conversion_xor", None)

    def get_boton_guardar_xor(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_xor")
            else None
        )

    def get_boton_aplicar_filtro_gaussiano(self):
        return getattr(self, "boton_aplicar_filtro_gaussiano", None)

    def get_boton_guardar_filtro_gaussiano(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_filtro_gaussiano")
            else None
        )

    def get_boton_aplicar_filtro_sal_pimienta(self):
        return getattr(self, "boton_aplicar_filtro_sal_pimienta", None)

    def get_boton_guardar_filtro_sal_pimienta(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_filtro_sal_pimienta")
            else None
        )

    def get_boton_guardar_matriz(self):
        return getattr(self, "boton_guardar_matriz", None)

    def get_matriz_convolucion(self):
        if hasattr(self, "entries_matriz"):
            matriz = []
            for i in range(3):
                fila = []
                for j in range(3):
                    entry = self.entries_matriz[i][j]
                    valor = entry.get()
                    try:
                        fila.append(float(valor))
                    except ValueError:
                        fila.append(0.0)
                matriz.append(fila)
            return matriz
        return None

    def get_boton_aplicar_filtro_laplaciano(self):
        return getattr(self, "boton_aplicar_filtro_laplaciano", None)

    def get_boton_guardar_filtro_laplaciano(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_filtro_laplaciano")
            else None
        )

    def get_boton_aplicar_segmentacion_um(self):
        return getattr(self, "boton_aplicar_segmentacion_um", None)

    def get_boton_aplicar_segmentacion_lum(self):
        return getattr(self, "boton_aplicar_segmentacion_lum", None)

    def get_boton_aplicar_segmentacion_ua(self):
        return getattr(self, "boton_aplicar_segmentacion_ua", None)

    def get_boton_aplicar_segmentacion_lua(self):
        return getattr(self, "boton_aplicar_segmentacion_lua", None)

    def get_boton_guardar_segmentacion_minimo(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_segmentacion")
            else None
        )

    def get_boton_aplicar_segmentacion_multi_umbral(self):
        return getattr(self, "boton_aplicar_segmentacion_multi_umbral", None)

    def get_boton_guardar_segmentacion_multi_umbral(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_segmentacion_multi_umbral")
            else None
        )

    def get_boton_aplicar_conectividad_4(self):
        return getattr(self, "boton_aplicar_conectividad_4", None)

    def get_boton_guardar_conectividad_4(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_conectividad_4")
            else None
        )

    def get_boton_aplicar_conectividad_8(self):
        return getattr(self, "boton_aplicar_conectividad_8", None)

    def get_boton_guardar_conectividad_8(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_conectividad_8")
            else None
        )

    def get_boton_aplicar_etiquetado_conectividad_4(self):
        return getattr(self, "boton_aplicar_etiquetado_conectividad_4", None)

    def get_boton_guardar_etiquetado_conectividad_4(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_etiquetado_conectividad_4")
            else None
        )

    def get_boton_aplicar_etiquetado_conectividad_8(self):
        return getattr(self, "boton_aplicar_etiquetado_conectividad_8", None)

    def get_boton_guardar_etiquetado_conectividad_8(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_etiquetado_conectividad_8")
            else None
        )

    # Getters para los sliders
    def get_slider_binario(self):
        return (
            getattr(self, "slider", None)
            if hasattr(self, "ventana_conversion_binario")
            else None
        )

    def get_slider_ruido_media(self):
        return (
            getattr(self, "slider1", None) if hasattr(self, "ventanda_ruido") else None
        )

    def get_slider_ruido_sigma(self):
        return (
            getattr(self, "slider2", None) if hasattr(self, "ventanda_ruido") else None
        )

    def get_slider_contraste_gamma(self):
        return (
            getattr(self, "slider3", None)
            if hasattr(self, "ventanda_correcion")
            else None
        )

    def get_slider_filtro_gaussiano_sigma(self):
        return (
            getattr(self, "slider_sigma", None)
            if hasattr(self, "ventana_filtro_gaussiano")
            else None
        )

    def get_slider_segmentacion_minimo(self):
        return (
            getattr(self, "slider4", None)
            if hasattr(self, "ventana_segmentacion_minimo")
            else None
        )

    def get_slider_segmentacion_multi_umbral_1(self):
        return (
            getattr(self, "slider5", None)
            if hasattr(self, "ventana_segmentacion_multi_umbral")
            else None
        )

    def get_slider_segmentacion_multi_umbral_2(self):
        return (
            getattr(self, "slider6", None)
            if hasattr(self, "ventana_segmentacion_multi_umbral")
            else None
        )

    # Getters de los menús de abrir, guardar, mostrar histogramas y canales
    def get_menu_abrir(self):
        return self.file_menu

    def get_menu_conversion(self):
        return self.convert_menu

    def get_menu_histogramas_canales(self):
        return self.histogram_menu

    def get_menu_operaciones(self):
        return self.operation_menu

    def get_menu_correcciones(self):
        return self.correction_menu

    def get_menu_filtros(self):
        return self.filter_menu

    def get_menu_segmentacion(self):
        return self.segmentation_menu

    def get_menu_conectividades(self):
        return self.labeling_menu

    def get_combobox_imagenes(self):
        return getattr(self, "combobox_imagenes", None)

    # Bucle principal
    def mainloop(self):
        self.root.mainloop()
