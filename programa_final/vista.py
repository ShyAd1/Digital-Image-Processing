import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Vista:
    def __init__(self, root):
        # Inicializar la ventana principal
        self.root = root
        self.root.title("Procesador de Imágenes")
        self.root.geometry("1400x800")

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
        self.menubar.add_cascade(label="Segmentaciónes", menu=self.segmentation_menu)

        # Crear el menú "Etiquetado"
        self.labeling_menu = tk.Menu(self.menubar, tearoff=0)
        self.labeling_menu.add_command(
            label="Etiquetado de componentes conectados-4",
            command=None,
        )
        self.labeling_menu.add_separator()
        self.labeling_menu.add_command(
            label="Etiquetado de componentes conectados-8",
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

        # Crear label para la visualización de la imagen original
        self.label_original = tk.Label(self.frame_imagen, text="Imagen original")
        self.label_original.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_original = tk.Label(self.frame_imagen)
        self.imagen_original.grid(row=1, column=0, padx=10, pady=5)

        # Asignar la barra de menús a la ventana
        self.root.config(menu=self.menubar)

    def abrir_ventana_conversion_grises(self):
        # Crear una ventana para la conversion de RGB a Escala de grises
        self.ventana_conversion_grises = tk.Toplevel(self.root)
        self.ventana_conversion_grises.title("Conversión de RGB a Escala de grises")
        self.ventana_conversion_grises.geometry("1600x900")

        # Crear marco para las imagenes de resultado
        self.frame_resultados = tk.Frame(self.ventana_conversion_grises)
        self.frame_resultados.pack(pady=20)

        # Crear label para la visualización de la imagen en escala de grises
        self.label_grises = tk.Label(
            self.frame_resultados, text="Imagen en escala de grises"
        )
        self.label_grises.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_grises = tk.Label(self.frame_resultados)
        self.imagen_grises.grid(row=1, column=0, padx=10, pady=5)

        # Crear label para la visualización de la imagen en escala de grises con ajuste de contraste
        self.label_grises_c = tk.Label(
            self.frame_resultados, text="Imagen en escala de grises"
        )
        self.label_grises_c.grid(row=0, column=1, padx=10, pady=5)
        self.imagen_grises_c = tk.Label(self.frame_resultados)
        self.imagen_grises_c.grid(row=1, column=1, padx=10, pady=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_conversion_grises)
        self.frame_botones.pack(pady=10)

        # Crear botón para convertir a escala de grises
        self.boton_grises = ttk.Button(
            self.frame_botones, text="Aplicar conversión a Escala de grises"
        )
        self.boton_grises.pack(side=tk.LEFT, padx=5)

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

        # Crear Canvas y Scrollbar para las imágenes (desplazable)
        self.canvas = tk.Canvas(self.ventana_conversion_binario, borderwidth=0)
        self.scrollbar = tk.Scrollbar(
            self.ventana_conversion_binario,
            orient="vertical",
            command=self.canvas.yview,
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Posicionar Canvas y Scrollbar
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(pady=20, fill="both", expand=True)

        # Crear marco desplazable para las imágenes
        self.frame_resultados = tk.Frame(self.canvas)
        # Centrar el frame_resultados dentro del Canvas
        self.canvas_frame = self.canvas.create_window(
            (0, 0), window=self.frame_resultados, anchor="n"
        )

        # Vincular eventos para actualizar la región desplazable y centrar el contenido
        self.frame_resultados.bind("<Configure>", self.actualizar_scrollregion)
        self.canvas.bind("<Configure>", self.centrar_contenido)

        # Crear label para la visualización de la imagen de umbral manual
        self.label_umbral_manual = tk.Label(self.frame_resultados, text="Umbral manual")
        self.label_umbral_manual.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_umbral_manual = tk.Label(self.frame_resultados)
        self.imagen_umbral_manual.grid(row=1, column=0, padx=10, pady=5)

        # Crear label para la visualización de la imagen de umbral automático
        self.label_umbral_automatico = tk.Label(
            self.frame_resultados, text="Umbral automático"
        )
        self.label_umbral_automatico.grid(row=0, column=1, padx=10, pady=5)
        self.imagen_umbral_automatico = tk.Label(self.frame_resultados)
        self.imagen_umbral_automatico.grid(row=1, column=1, padx=10, pady=5)

        # Crear label para la visualización de la imagen de umbral manual con corrección de contraste
        self.label_umbral_manual_c = tk.Label(
            self.frame_resultados, text="Umbral manual con corrección de contraste"
        )
        self.label_umbral_manual_c.grid(row=2, column=0, padx=10, pady=5)
        self.imagen_umbral_manual_c = tk.Label(self.frame_resultados)
        self.imagen_umbral_manual_c.grid(row=3, column=0, padx=10, pady=5)

        # Crear label para la visualización de la imagen de umbral automático con corrección de contraste
        self.label_umbral_automatico_c = tk.Label(
            self.frame_resultados, text="Umbral automático con corrección de contraste"
        )
        self.label_umbral_automatico_c.grid(row=2, column=1, padx=10, pady=5)
        self.imagen_umbral_automatico_c = tk.Label(self.frame_resultados)
        self.imagen_umbral_automatico_c.grid(row=3, column=1, padx=10, pady=5)

        # Crear un marco para los botones y acomodarlos horizontalmente (fijo en la parte inferior)
        self.frame_botones = tk.Frame(self.ventana_conversion_binario)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar umbralizado
        self.boton_umbralizado = ttk.Button(
            self.frame_botones, text="Aplicar umbralizado"
        )
        self.boton_umbralizado.pack(side=tk.LEFT, padx=5)

        # Crear botón para guardar resultados
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultados")
        self.boton_guardar.pack(side=tk.LEFT, padx=5)

    def actualizar_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Centrar el contenido después de actualizar la región desplazable
        self.centrar_contenido(None)

    def centrar_contenido(self, event):
        if event:
            canvas_width = event.width
        else:
            canvas_width = self.canvas.winfo_width()

        # Obtener el ancho del frame_resultados
        frame_width = self.frame_resultados.winfo_reqwidth()

        # Calcular la posición x para centrar el frame_resultados
        x_position = max(0, (canvas_width - frame_width) // 2)

        # Actualizar la posición del frame_resultados en el Canvas
        self.canvas.coords(self.canvas_frame, x_position, 0)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.ventana_conversion_binario.bind_all("<MouseWheel>", self._on_mousewheel)

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

        # Crear marco para las imagen de resultado
        self.frame_resultado = tk.Frame(self.ventanda_ruido)
        self.frame_resultado.pack(pady=20)

        # Crear label para la visualización de la imagen con ruido
        self.label_ruido = tk.Label(
            self.frame_resultado, text="Imagen con el ruido aplicado"
        )
        self.label_ruido.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_ruido = tk.Label(self.frame_resultado)
        self.imagen_ruido.grid(row=1, column=0, padx=10, pady=5)

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

        # Crear marco para las imagen de resultado
        self.frame_resultado = tk.Frame(self.ventanda_correcion)
        self.frame_resultado.pack(pady=20)

        # Crear label para la visualización de la imagen ya corregida
        self.label_correccion = tk.Label(
            self.frame_resultado, text="Imagen con el contraste corregido"
        )
        self.label_correccion.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_correccion = tk.Label(self.frame_resultado)
        self.imagen_correccion.grid(row=1, column=0, padx=10, pady=5)

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

        # Crear marco para la imagen de resultado
        self.frame_resultado = tk.Frame(self.ventana_filtro_gaussiano)
        self.frame_resultado.pack(pady=20)

        # Crear label para la visualización de la imagen filtrada
        self.label_filtrada = tk.Label(
            self.frame_resultado, text="Imagen con filtro gaussiano"
        )
        self.label_filtrada.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_filtrada = tk.Label(self.frame_resultado)
        self.imagen_filtrada.grid(row=1, column=0, padx=10, pady=5)

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

        # Crear marco para la imagen de resultado
        self.frame_resultado = tk.Frame(self.ventana_filtro_sal_pimienta)
        self.frame_resultado.pack(pady=20)

        # Crear label para la visualización de la imagen filtrada
        self.label_filtrada_sal_pimienta = tk.Label(
            self.frame_resultado, text="Imagen con filtro sal y pimienta"
        )
        self.label_filtrada_sal_pimienta.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_filtrada_sal_pimienta = tk.Label(self.frame_resultado)
        self.imagen_filtrada_sal_pimienta.grid(row=1, column=0, padx=10, pady=5)

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

        # Crear marco para la imagen de resultado
        self.frame_resultado = tk.Frame(self.ventana_filtro_laplaciano)
        self.frame_resultado.pack(pady=20)

        # Crear label para la visualización de la imagen con filtro laplaciano
        self.label_laplaciana = tk.Label(
            self.frame_resultado, text="Imagen con filtro laplaciano"
        )
        self.label_laplaciana.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_laplaciana = tk.Label(self.frame_resultado)
        self.imagen_laplaciana.grid(row=1, column=0, padx=10, pady=5)

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

    def abrir_ventana_segmentacion(self):
        # Crear una ventana para la segmentación por mínimo de histograma
        self.ventana_segmentacion = tk.Toplevel(self.root)
        self.ventana_segmentacion.title("Segmentación por mínimo de histograma")
        self.ventana_segmentacion.geometry("1600x900")

        # Crear marco para el slider de umbral
        self.frame_slider = tk.Frame(self.ventana_segmentacion)
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

        # Crear marco para la imagen de resultado
        self.frame_resultado = tk.Frame(self.ventana_segmentacion)
        self.frame_resultado.pack(pady=20)

        # Crear label para la visualización de la imagen segmentada por umbral manual
        self.label_segmentada_um = tk.Label(
            self.frame_resultado, text="Imagen segmentada por umbral manual"
        )
        self.label_segmentada_um.grid(row=0, column=0, padx=10, pady=5)
        self.imagen_segmentada_um = tk.Label(self.frame_resultado)
        self.imagen_segmentada_um.grid(row=1, column=0, padx=10, pady=5)

        # Crear label para la visualización de la imagen segmentada laplaciana por umbral manual
        self.label_segmentada_lum = tk.Label(
            self.frame_resultado, text="Imagen segmentada laplaciana por umbral manual"
        )
        self.label_segmentada_lum.grid(row=0, column=1, padx=10, pady=5)
        self.imagen_segmentada_lum = tk.Label(self.frame_resultado)
        self.imagen_segmentada_lum.grid(row=1, column=1, padx=10, pady=5)

        # Crear label para la visualización de la imagen segmentada por umbral automatico
        self.label_segmentada_ua = tk.Label(
            self.frame_resultado, text="Imagen segmentada por umbral automatico"
        )
        self.label_segmentada_ua.grid(row=2, column=0, padx=10, pady=5)
        self.imagen_segmentada_ua = tk.Label(self.frame_resultado)
        self.imagen_segmentada_ua.grid(row=3, column=0, padx=10, pady=5)

        # Crear label para la visualización de la imagen segmentada laplaciana por umbral automatico
        self.label_segmentada_lua = tk.Label(
            self.frame_resultado,
            text="Imagen segmentada laplaciana por umbral automatico",
        )
        self.label_segmentada_lua.grid(row=2, column=1, padx=10, pady=5)
        self.imagen_segmentada_lua = tk.Label(self.frame_resultado)
        self.imagen_segmentada_lua.grid(row=3, column=1, padx=10, pady=5)

        # Crear un marco para los botones y acomodarlos horizontalmente
        self.frame_botones = tk.Frame(self.ventana_segmentacion)
        self.frame_botones.pack(pady=10)

        # Crear botón para aplicar la segmentación umbral manual
        self.boton_aplicar_segmentacion_um = ttk.Button(
            self.frame_botones, text="Aplicar segmentación umbral manual"
        )
        self.boton_aplicar_segmentacion_um.grid(row=0, column=0, padx=5, pady=5)

        # Crear botón para aplicar la segmentación laplaciana umbral manual
        self.boton_aplicar_segmentacion_lum = ttk.Button(
            self.frame_botones, text="Aplicar segmentación laplaciana umbral manual"
        )
        self.boton_aplicar_segmentacion_lum.grid(row=0, column=1, padx=5, pady=5)

        # Crear botón para aplicar la segmentación umbral automático
        self.boton_aplicar_segmentacion_ua = ttk.Button(
            self.frame_botones, text="Aplicar segmentación umbral automatico"
        )
        self.boton_aplicar_segmentacion_ua.grid(row=1, column=0, padx=5, pady=5)

        # Crear botón para aplicar la segmentación laplaciana umbral automático
        self.boton_aplicar_segmentacion_lua = ttk.Button(
            self.frame_botones, text="Aplicar segmentación laplaciana umbral automatico"
        )
        self.boton_aplicar_segmentacion_lua.grid(row=1, column=1, padx=5, pady=5)

        # Crear botón para guardar resultados (abajo de los de segmentación)
        self.boton_guardar = ttk.Button(self.frame_botones, text="Guardar resultado")
        self.boton_guardar.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    # Getters para los botones
    def get_boton_grises(self):
        return getattr(self, "boton_grises", None)

    def get_boton_guardar_grises(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_conversion_grises")
            else None
        )

    def get_boton_umbralizado(self):
        return getattr(self, "boton_umbralizado", None)

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

    def get_boton_guardar_segmentacion(self):
        return (
            getattr(self, "boton_guardar", None)
            if hasattr(self, "ventana_segmentacion")
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

    def get_slider_segmentacion(self):
        return (
            getattr(self, "slider4", None)
            if hasattr(self, "ventana_segmentacion")
            else None
        )

    # Getters de los menús de abrir, guardar, mostrar histogramas y canales
    def get_menu_abrir(self):
        return self.file_menu

    def get_menu_conversion(self):
        return self.convert_menu

    def get_menu_histogramas_canales(self):
        return self.histogram_menu

    def get_menu_correcciones(self):
        return self.correction_menu

    def get_menu_filtros(self):
        return self.filter_menu

    def get_menu_segmetacion(self):
        return self.segmentation_menu

    def mostrar_imagen(self, imagen, tipo):
        if tipo == "original":
            self.imagen_original.config(image=imagen)
            self.imagen_original.image = imagen
        elif tipo == "grises":
            if hasattr(self, "imagen_grises"):
                self.imagen_grises.config(image=imagen)
                self.imagen_grises.image = imagen
        elif tipo == "grises_c":
            if hasattr(self, "imagen_grises_c"):
                self.imagen_grises_c.config(image=imagen)
                self.imagen_grises_c.image = imagen
        elif tipo == "umbral_manual":
            if hasattr(self, "imagen_umbral_manual"):
                self.imagen_umbral_manual.config(image=imagen)
                self.imagen_umbral_manual.image = imagen
        elif tipo == "umbral_automatico":
            if hasattr(self, "imagen_umbral_automatico"):
                self.imagen_umbral_automatico.config(image=imagen)
                self.imagen_umbral_automatico.image = imagen
        elif tipo == "umbral_manual_c":
            if hasattr(self, "imagen_umbral_manual_c"):
                self.imagen_umbral_manual_c.config(image=imagen)
                self.imagen_umbral_manual_c.image = imagen
        elif tipo == "umbral_automatico_c":
            if hasattr(self, "imagen_umbral_automatico_c"):
                self.imagen_umbral_automatico_c.config(image=imagen)
                self.imagen_umbral_automatico_c.image = imagen
        elif tipo == "ruido":
            if hasattr(self, "imagen_ruido"):
                self.imagen_ruido.config(image=imagen)
                self.imagen_ruido.image = imagen
        elif tipo == "correccion":
            if hasattr(self, "imagen_correccion"):
                self.imagen_correccion.config(image=imagen)
                self.imagen_correccion.image = imagen
        elif tipo == "filtro_gaussiano":
            if hasattr(self, "imagen_filtrada"):
                self.imagen_filtrada.config(image=imagen)
                self.imagen_filtrada.image = imagen
        elif tipo == "filtro_sal_pimienta":
            if hasattr(self, "imagen_filtrada_sal_pimienta"):
                self.imagen_filtrada_sal_pimienta.config(image=imagen)
                self.imagen_filtrada_sal_pimienta.image = imagen
        elif tipo == "filtro_laplaciano":
            if hasattr(self, "imagen_laplaciana"):
                self.imagen_laplaciana.config(image=imagen)
                self.imagen_laplaciana.image = imagen
        elif tipo == "segmentada_um":
            if hasattr(self, "imagen_segmentada_um"):
                self.imagen_segmentada_um.config(image=imagen)
                self.imagen_segmentada_um.image = imagen
        elif tipo == "segmentada_lum":
            if hasattr(self, "imagen_segmentada_lum"):
                self.imagen_segmentada_lum.config(image=imagen)
                self.imagen_segmentada_lum.image = imagen
        elif tipo == "segmentada_ua":
            if hasattr(self, "imagen_segmentada_ua"):
                self.imagen_segmentada_ua.config(image=imagen)
                self.imagen_segmentada_ua.image = imagen
        elif tipo == "segmentada_lua":
            if hasattr(self, "imagen_segmentada_lua"):
                self.imagen_segmentada_lua.config(image=imagen)
                self.imagen_segmentada_lua.image = imagen

    # Bucle principal
    def mainloop(self):
        self.root.mainloop()
