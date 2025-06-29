import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from scipy.signal import find_peaks


class Modelo:
    WINDOW_NAME = "image"  # Define window name as a constant

    def __init__(self):
        # Inicializar la imagen original y la imagen de salida
        self.img_tk1 = None
        self.imagen = None
        self.imagen_original = None
        self.imagen_grises = None
        self.imagen_grises_c = None
        self.imagen_umbral_manual = None
        self.imagen_umbral_automatico = None
        self.imagen_umbral_manual_c = None
        self.imagen_umbral_automatico_c = None
        self.imagen_ruido = None
        self.imagen_correccion = None
        self.imagen_filtrada = None
        self.imagen_filtrada_sal_pimienta = None
        self.imagen_laplaciana = None
        self.imagen_recortada = None
        self.imagen_segmentada_um = None
        self.imagen_segmentada_lum = None
        self.imagen_segmentada_ua = None
        self.imagen_segmentada_lua = None
        self.imagen_segmentada_multi_umbral = None
        self.imagen_not = None
        self.imagen_and = None
        self.imagen_or = None
        self.imagen_xor = None
        self.imagen_conectividad_4 = None
        self.imagen_conectividad_8 = None
        self.imagen_etiquetado_conectividad_4 = None
        self.imagen_etiquetado_conectividad_8 = None
        self.max_size = 750
        self.tamaño_original = None
        self.matriz_convolucion = None

    def cargar_imagen(self, ruta):
        # Leer la imagen apartir de la ruta
        self.imagen = cv2.imread(ruta)

        if self.imagen is None:
            raise ValueError("No se pudo cargar la imagen.")

        # Guardar el tamaño original de la imagen
        self.tamaño_original = self.imagen.shape

        # Convertir la imagen de BGR a RGB
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)

        self.imagen_original = self.imagen.copy()

        self.imagen = self.redimensionar_imagen(self.imagen, 750)

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def obtener_lista_imagenes(self):
        # Devuelve un diccionario con los nombres y referencias de todas las imágenes procesadas
        imagenes = {
            "Imagen original": self.imagen_original,
            "Imagen con corrección de contraste": self.imagen_correccion,
            "Imagen en grises": self.imagen_grises,
            "Imagen en grises (contraste)": self.imagen_grises_c,
            "Imagen binaria (umbral manual)": self.imagen_umbral_manual,
            "Imagen binaria (umbral automático)": self.imagen_umbral_automatico,
            "Imagen con ruido gaussiano": self.imagen_ruido,
            "Imagen filtrada gaussiana": self.imagen_filtrada,
            "Imagen filtrada sal y pimienta": self.imagen_filtrada_sal_pimienta,
            "Imagen laplaciana": self.imagen_laplaciana,
            "Imagen segmentada (umbral manual)": self.imagen_segmentada_um,
            "Imagen segmentada (laplaciano, umbral manual)": self.imagen_segmentada_lum,
            "Imagen segmentada (umbral automático)": self.imagen_segmentada_ua,
            "Imagen segmentada (laplaciano, umbral automático)": self.imagen_segmentada_lua,
            "Imagen segmentada multi umbral": self.imagen_segmentada_multi_umbral,
            "Imagen NOT": self.imagen_not,
            "Imagen AND": self.imagen_and,
            "Imagen OR": self.imagen_or,
            "Imagen XOR": self.imagen_xor,
            "Imagen conectivida 4": self.imagen_conectividad_4,
            "Imagen conectivida 8": self.imagen_conectividad_8,
            "Imagen etiquetado conectivida 4": self.imagen_etiquetado_conectividad_4,
            "Imagen etiquetado conectivida 8": self.imagen_etiquetado_conectividad_8,
        }
        # Filtrar solo las imágenes que no son None
        return {k: v for k, v in imagenes.items() if v is not None}

    def redimensionar_imagen(self, imagen, max_size=None):
        if imagen is None:
            return None

        if max_size is None:
            max_size = self.max_size

        # Detectar si la imagen es RGB (3 canales) o escala de grises (2D)
        if len(imagen.shape) == 3:
            altura, ancho = imagen.shape[:2]
        else:
            altura, ancho = imagen.shape

        scale_factor = max_size / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        return cv2.resize(imagen, (new_width, new_height))

    def convertir_RGB_a_grises(self, imagen):
        if imagen is not None:
            # Convertir la imagen de RGB a escala de grises
            self.imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)

            self.imagen_grises = self.redimensionar_imagen(self.imagen_grises)

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_grises)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def convertir_RGB_a_grises_c(self, imagen):
        if imagen is not None:
            # Convertir la imagen de RGB a escala de grises
            self.imagen_grises_c = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)

            self.imagen_grises_c = self.redimensionar_imagen(self.imagen_grises_c)

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_grises_c)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def convertir_RGB_a_binario(self, imagen, umbral=None):
        if imagen is not None:
            gris1 = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
            _, self.imagen_umbral_manual = cv2.threshold(
                gris1, umbral, 255, cv2.THRESH_BINARY
            )

            self.imagen_umbral_manual = self.redimensionar_imagen(
                self.imagen_umbral_manual
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_umbral_manual)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def convertir_RGB_a_binario_a(self, imagen):
        if imagen is not None:
            gris1 = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
            # Umbral automático usando Otsu
            _, self.imagen_umbral_automatico = cv2.threshold(
                gris1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            self.imagen_umbral_automatico = self.redimensionar_imagen(
                self.imagen_umbral_automatico
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_umbral_automatico)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_ruido_gaussiano(self, imagen, media, sigma):
        if imagen is not None:
            ruido = np.random.normal(media, sigma, imagen.shape).astype(np.uint8)
            self.imagen_ruido = cv2.add(imagen, ruido)

            self.imagen_ruido = self.redimensionar_imagen(self.imagen_ruido)

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_ruido)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)
        return self.img_tk1

    def aplicar_correccion_contraste(self, imagen, gamma):
        if imagen is not None:
            # Aplicar corrección gamma a la imagen 1
            self.imagen_correccion = np.clip(
                255 * ((imagen / 255) ** gamma), 0, 255
            ).astype(np.uint8)

            self.imagen_correccion = self.redimensionar_imagen(self.imagen_correccion)

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_correccion)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def calcular_histograma(self, imagen, tipo):
        if imagen is not None:
            if tipo == "rgb":
                plt.figure(figsize=(10, 5))
                plt.hist(
                    imagen.ravel(),
                    bins=256,
                    range=(0, 256),
                    color="blue",
                    alpha=0.5,
                    label="Canal Azul",
                )
                plt.hist(
                    imagen[:, :, 1].ravel(),
                    bins=256,
                    range=(0, 256),
                    color="green",
                    alpha=0.5,
                    label="Canal Verde",
                )
                plt.hist(
                    imagen[:, :, 2].ravel(),
                    bins=256,
                    range=(0, 256),
                    color="red",
                    alpha=0.5,
                    label="Canal Rojo",
                )
                plt.title("Histograma de la imagen en RGB")
                plt.xlabel("Valor de intensidad")
                plt.ylabel("Número de píxeles")
                plt.legend()
                plt.grid()
                plt.tight_layout()
                plt.show()
            elif tipo == "grises":
                plt.figure(figsize=(10, 5))
                plt.hist(
                    imagen.ravel(), bins=256, range=(0, 256), color="gray", alpha=0.7
                )
                plt.title("Histograma de la imagen en escala de grises")
                plt.xlabel("Valor de intensidad")
                plt.ylabel("Número de píxeles")
                plt.grid()
                plt.tight_layout()
                plt.show()
            elif tipo == "binario":
                plt.figure(figsize=(6, 4))
                plt.hist(
                    imagen.ravel(), bins=2, range=(0, 256), color="black", alpha=0.7
                )
                plt.title("Histograma de la imagen binaria")
                plt.xlabel("Valor de intensidad (0=negro, 255=blanco)")
                plt.ylabel("Número de píxeles")
                plt.xticks([0, 255])
                plt.grid()
                plt.tight_layout()
                plt.show()
            else:
                raise ValueError("No se puede calcular ese histograma")

    def extrae_canales(self, imagen, tipo):
        if imagen is not None:
            if tipo == "r":
                plt.figure(figsize=(6, 4))
                canal = imagen[:, :, 0]
                canal_rgb = np.zeros_like(imagen)
                canal_rgb[:, :, 0] = canal
                plt.imshow(canal_rgb)
                plt.title("Canal Rojo")
                plt.axis("off")
                plt.show()
            elif tipo == "g":
                plt.figure(figsize=(6, 4))
                canal = imagen[:, :, 1]
                canal_rgb = np.zeros_like(imagen)
                canal_rgb[:, :, 1] = canal
                plt.imshow(canal_rgb)
                plt.title("Canal Verde")
                plt.axis("off")
                plt.show()
            elif tipo == "b":
                plt.figure(figsize=(6, 4))
                canal = imagen[:, :, 2]
                canal_rgb = np.zeros_like(imagen)
                canal_rgb[:, :, 2] = canal
                plt.imshow(canal_rgb)
                plt.title("Canal Azul")
                plt.axis("off")
                plt.show()
            else:
                raise ValueError("Tipo de canal no válido. Usa 'r', 'g' o 'b'.")

    def aplicar_conversion_not(self, imagen):
        if imagen is not None:
            self.imagen_not = cv2.bitwise_not(imagen)

            self.imagen_not = self.redimensionar_imagen(self.imagen_not)

            img_pil = Image.fromarray(self.imagen_not)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)
        return self.img_tk1

    def aplicar_conversion_or(self, imagen1, imagen2):
        if imagen1 is not None and imagen2 is not None:

            # Redimensionar imagen2 si es necesario
            if imagen1.shape[:2] != imagen2.shape[:2]:
                imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

            # Convertir a 3 canales si uno es de 1 canal y el otro de 3
            if len(imagen1.shape) == 2 and len(imagen2.shape) == 3:
                imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_GRAY2RGB)
            elif len(imagen1.shape) == 3 and len(imagen2.shape) == 2:
                imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_GRAY2RGB)

            # Igualar tipos de datos
            if imagen1.dtype != imagen2.dtype:
                imagen2 = imagen2.astype(imagen1.dtype)

            self.imagen_or = cv2.bitwise_or(imagen1, imagen2)

            self.imagen_or = self.redimensionar_imagen(self.imagen_or)

            img_pil = Image.fromarray(self.imagen_or)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)
        return self.img_tk1

    def aplicar_conversion_and(self, imagen1, imagen2):
        if imagen1 is not None and imagen2 is not None:

            # Redimensionar imagen2 si es necesario
            if imagen1.shape[:2] != imagen2.shape[:2]:
                imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

            # Convertir a 3 canales si uno es de 1 canal y el otro de 3
            if len(imagen1.shape) == 2 and len(imagen2.shape) == 3:
                imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_GRAY2RGB)
            elif len(imagen1.shape) == 3 and len(imagen2.shape) == 2:
                imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_GRAY2RGB)

            # Igualar tipos de datos
            if imagen1.dtype != imagen2.dtype:
                imagen2 = imagen2.astype(imagen1.dtype)

            self.imagen_and = cv2.bitwise_and(imagen1, imagen2)

            self.imagen_and = self.redimensionar_imagen(self.imagen_and)

            img_pil = Image.fromarray(self.imagen_and)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)
        return self.img_tk1

    def aplicar_conversion_xor(self, imagen1, imagen2):
        if imagen1 is not None and imagen2 is not None:

            # Redimensionar imagen2 si es necesario
            if imagen1.shape[:2] != imagen2.shape[:2]:
                imagen2 = cv2.resize(imagen2, (imagen1.shape[1], imagen1.shape[0]))

            # Convertir a 3 canales si uno es de 1 canal y el otro de 3
            if len(imagen1.shape) == 2 and len(imagen2.shape) == 3:
                imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_GRAY2RGB)
            elif len(imagen1.shape) == 3 and len(imagen2.shape) == 2:
                imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_GRAY2RGB)

            # Igualar tipos de datos
            if imagen1.dtype != imagen2.dtype:
                imagen2 = imagen2.astype(imagen1.dtype)

            self.imagen_xor = cv2.bitwise_xor(imagen1, imagen2)

            self.imagen_xor = self.redimensionar_imagen(self.imagen_xor)

            img_pil = Image.fromarray(self.imagen_xor)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)
        return self.img_tk1

    def aplicar_filtro_gaussiano(self, imagen, sigma):
        if imagen is not None:

            self.imagen_filtrada = cv2.GaussianBlur(
                imagen, (3, 3), sigma
            )  # Aplicar filtro gaussiano, con sigma como desviación estándar

            self.imagen_filtrada = self.redimensionar_imagen(self.imagen_filtrada)

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_filtrada)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_filtro_sal_pimienta(self, imagen):
        if imagen is None:
            raise ValueError("No se esta cargada la imagen principal")

        self.imagen_filtrada_sal_pimienta = cv2.medianBlur(imagen, 3)

        self.imagen_filtrada_sal_pimienta = self.redimensionar_imagen(
            self.imagen_filtrada_sal_pimienta
        )

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_filtrada_sal_pimienta)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_filtro_laplaciano(self, imagen, matriz):
        # Converir la matriz de convolución a un array de numpy
        laplaciano = np.array(matriz, dtype=np.float32)

        # Aplicar el filtro Laplaciano a la imagen
        self.imagen_laplaciana = cv2.filter2D(imagen, -1, laplaciano)

        self.imagen_laplaciana = self.redimensionar_imagen(self.imagen_laplaciana)

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_laplaciana)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def obtener_region_interes(self, imagen):
        # Permite seleccionar una región de interés (ROI) de la imagen con el mouse
        # Devuelve la ROI seleccionada redimensionada y en formato compatible con Tkinter

        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        img = imagen.copy()
        # Redimensionar para mostrar (máx 600 px)
        max_dim = 600
        h, w = img.shape[:2]
        scale = min(max_dim / h, max_dim / w, 1.0)
        dim = (int(w * scale), int(h * scale))
        resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        pt1 = None
        pt2 = None
        roi = None
        cropped = False

        def select_region(event, x, y, _, __):
            nonlocal pt1, pt2, roi, cropped
            if event == cv2.EVENT_LBUTTONDOWN:
                pt1 = (x, y)
                pt2 = None
                cropped = False
            elif event == cv2.EVENT_LBUTTONUP:
                pt2 = (x, y)
                cv2.rectangle(resized_img, pt1, pt2, (0, 255, 0), 2)
                cv2.imshow(self.WINDOW_NAME, resized_img)
                cropped = True
                # Recortar la región en la imagen original usando la escala
                x1 = int(pt1[0] * img.shape[1] / resized_img.shape[1])
                y1 = int(pt1[1] * img.shape[0] / resized_img.shape[0])
                x2 = int(pt2[0] * img.shape[1] / resized_img.shape[1])
                y2 = int(pt2[1] * img.shape[0] / resized_img.shape[0])
                x1, x2 = sorted([x1, x2])
                y1, y2 = sorted([y1, y2])
                # Validar que la ROI tenga tamaño válido
                if (x2 - x1) > 0 and (y2 - y1) > 0:
                    roi = img[y1:y2, x1:x2].copy()
                    self.imagen_recortada = roi
                    # Redimensionar la ROI para mostrarla, proporcionalmente y mantener la relación de aspecto
                    roi_height, roi_width = roi.shape[:2]
                    aspect_ratio = roi_width / roi_height if roi_height > 0 else 1
                    new_width = 300
                    new_height = (
                        int(new_width / aspect_ratio) if aspect_ratio > 0 else 300
                    )
                    roi_show = cv2.resize(
                        roi, (new_width, new_height), interpolation=cv2.INTER_AREA
                    )
                    cv2.imshow("ROI", roi_show)
                    cv2.moveWindow("ROI", 500, 100)
                else:
                    roi = None
                    self.imagen_recortada = None

        cv2.namedWindow(self.WINDOW_NAME)
        cv2.setMouseCallback(self.WINDOW_NAME, select_region)
        cv2.moveWindow(self.WINDOW_NAME, 100, 100)

        # Mostrar la imagen la primera vez
        cv2.imshow(self.WINDOW_NAME, resized_img)

        running = True
        while running:
            temp_img = resized_img.copy()
            if pt1 and pt2:
                cv2.imshow(self.WINDOW_NAME, temp_img)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                running = False
            elif key == ord("r"):
                # Reiniciar selección
                pt1 = None
                pt2 = None
                cropped = False
                roi = None
                self.imagen_recortada = None
                resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow(self.WINDOW_NAME, resized_img)
            # Cerrar ventana ROI si está abierta y se cierra manualmente
            if cropped and roi is not None:
                try:
                    if cv2.getWindowProperty("ROI", cv2.WND_PROP_VISIBLE) < 1:
                        cropped = False
                        roi = None
                        self.imagen_recortada = None
                except cv2.error:
                    pass  # Ignore if the window does not exist
                # ROI seleccionada correctamente, salir del bucle y devolver la imagen
                cv2.destroyAllWindows()
                self.imagen_recortada = roi.copy()
                roi_redim = self.redimensionar_imagen(self.imagen_recortada)
                img_pil = Image.fromarray(roi_redim)
                self.img_tk1 = ImageTk.PhotoImage(img_pil)
                return self.img_tk1

        # Si no se seleccionó ROI válida
        cv2.destroyAllWindows()
        return None

    def aplicar_segmentacion_lua(self, imagen):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Convertir a escala de grises si es RGB o binaria de 3 canales
        if len(imagen.shape) == 3:
            imagen_proc = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            imagen_proc = imagen.copy()

        # Normalizar la imagen Laplaciana para trabajar con valores en [0, 255]
        laplacian_normalized = cv2.normalize(
            imagen_proc, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Calcular el histograma de la imagen normalizada
        hist = cv2.calcHist(
            [laplacian_normalized], [0], None, [256], [0, 256]
        ).flatten()

        # Suavizar el histograma con un filtro de promedio móvil para reducir ruido
        window_size = 5
        smoothed_hist = np.convolve(
            hist, np.ones(window_size) / window_size, mode="valid"
        )
        pad_size = (window_size - 1) // 2
        smoothed_hist = np.pad(smoothed_hist, (pad_size, pad_size), mode="edge")

        # Encontrar picos en el histograma suavizado
        peaks, _ = find_peaks(smoothed_hist, distance=20)

        # Verificar que se encontraron al menos dos picos
        if len(peaks) < 2:
            raise ValueError(
                "No se encontraron suficientes picos en el histograma para determinar el umbral."
            )

        # Seleccionar los dos picos más prominentes
        peak_heights = smoothed_hist[peaks]
        top_peaks = peaks[np.argsort(peak_heights)[-2:]]
        top_peaks = sorted(top_peaks)

        # Encontrar el mínimo (valle) entre los dos picos
        valley_region = smoothed_hist[top_peaks[0] : top_peaks[1]]
        valley_idx = np.argmin(valley_region) + top_peaks[0]
        threshold = int(valley_idx)

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_lua = cv2.threshold(
            laplacian_normalized, threshold, 255, cv2.THRESH_BINARY
        )

        self.imagen_segmentada_lua = self.redimensionar_imagen(
            self.imagen_segmentada_lua
        )

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_lua)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_segmentacion_lum(self, imagen, umbral):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Convertir a escala de grises si es RGB o binaria de 3 canales
        if len(imagen.shape) == 3:
            imagen_proc = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            imagen_proc = imagen.copy()

        # Normalizar la imagen Laplaciana para trabajar con valores en [0, 255]
        laplacian_normalized = cv2.normalize(
            imagen_proc, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Verificar que el umbral manual esté dentro de un rango razonable
        if umbral < 0 or umbral > 255:
            raise ValueError("El umbral manual debe estar entre 0 y 255.")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_lum = cv2.threshold(
            laplacian_normalized, umbral, 255, cv2.THRESH_BINARY
        )

        self.imagen_segmentada_lum = self.redimensionar_imagen(
            self.imagen_segmentada_lum
        )

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_lum)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_segmentacion_ua(self, imagen):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Convertir a escala de grises si es RGB o binaria de 3 canales
        if len(imagen.shape) == 3:
            imagen_proc = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            imagen_proc = imagen.copy()

        # Normalizar la imagen para trabajar con valores en [0, 255]
        imagen_normalized = cv2.normalize(
            imagen_proc, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Calcular el histograma de la imagen normalizada
        hist = cv2.calcHist([imagen_normalized], [0], None, [256], [0, 256]).flatten()

        # Suavizar el histograma con un filtro de promedio móvil para reducir ruido
        window_size = 5
        smoothed_hist = np.convolve(
            hist, np.ones(window_size) / window_size, mode="valid"
        )
        pad_size = (window_size - 1) // 2
        smoothed_hist = np.pad(smoothed_hist, (pad_size, pad_size), mode="edge")

        # Encontrar picos en el histograma suavizado
        peaks, _ = find_peaks(smoothed_hist, distance=20)

        # Verificar que se encontraron al menos dos picos
        if len(peaks) < 2:
            raise ValueError(
                "No se encontraron suficientes picos en el histograma para determinar el umbral."
            )

        # Seleccionar los dos picos más prominentes
        peak_heights = smoothed_hist[peaks]
        top_peaks = peaks[np.argsort(peak_heights)[-2:]]
        top_peaks = sorted(top_peaks)

        # Encontrar el mínimo (valle) entre los dos picos
        valley_region = smoothed_hist[top_peaks[0] : top_peaks[1]]
        valley_idx = np.argmin(valley_region) + top_peaks[0]
        threshold = int(valley_idx)

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_ua = cv2.threshold(
            imagen_normalized, threshold, 255, cv2.THRESH_BINARY
        )

        self.imagen_segmentada_ua = self.redimensionar_imagen(self.imagen_segmentada_ua)

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_ua)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_segmentacion_um(self, imagen, umbral):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Convertir a escala de grises si es RGB o binaria de 3 canales
        if len(imagen.shape) == 3:
            imagen_proc = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            imagen_proc = imagen.copy()

        # Normalizar la imagen para trabajar con valores en [0, 255]
        imagen_normalized = cv2.normalize(
            imagen_proc, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Verificar que el umbral manual esté dentro de un rango razonable
        if umbral < 0 or umbral > 255:
            raise ValueError("El umbral manual debe estar entre 0 y 255.")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_um = cv2.threshold(
            imagen_normalized, umbral, 255, cv2.THRESH_BINARY
        )

        self.imagen_segmentada_um = self.redimensionar_imagen(self.imagen_segmentada_um)

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_um)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_segmentacion_multi_umbral(self, imagen, umbral1, umbral2):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Convertir a escala de grises si es RGB o binaria de 3 canales
        if len(imagen.shape) == 3:
            imagen_proc = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            imagen_proc = imagen.copy()

        # Normalizar la imagen para trabajar con valores en [0, 255]
        imagen_normalized = cv2.normalize(
            imagen_proc, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Segmentación con dos umbrales (tres categorías)
        imagen_multi_umbrales = np.zeros_like(imagen_normalized)
        imagen_multi_umbrales[imagen_normalized < umbral1] = 0
        imagen_multi_umbrales[
            (imagen_normalized >= umbral1) & (imagen_normalized < umbral2)
        ] = 127
        imagen_multi_umbrales[imagen_normalized >= umbral2] = 255

        self.imagen_segmentada_multi_umbral = imagen_multi_umbrales
        self.imagen_segmentada_multi_umbral = self.redimensionar_imagen(
            self.imagen_segmentada_multi_umbral
        )

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_multi_umbral)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_conectividad_4(self, imagen):
        if imagen is not None:
            # Convertir a binario si no lo está
            if len(imagen.shape) == 3:
                img_bin = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
            else:
                img_bin = imagen.copy()
            _, img_bin = cv2.threshold(
                img_bin, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Etiquetado de componentes conectados (conectividad 4)
            num_labels, labels = cv2.connectedComponents(img_bin, connectivity=4)

            # Asignar colores a cada etiqueta
            label_hue = (
                np.uint8(179 * labels / np.max(labels))
                if np.max(labels) > 0
                else labels
            )
            blank_ch = 255 * np.ones_like(label_hue)
            labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
            labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2RGB)
            labeled_img[label_hue == 0] = 0  # Fondo en negro

            self.imagen_conectividad_4 = self.redimensionar_imagen(labeled_img)

            img_pil = Image.fromarray(self.imagen_conectividad_4)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_conectividad_8(self, imagen):
        if imagen is not None:
            # Convertir a binario si no lo está
            if len(imagen.shape) == 3:
                img_bin = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
            else:
                img_bin = imagen.copy()
            _, img_bin = cv2.threshold(
                img_bin, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Etiquetado de componentes conectados (conectividad 8)
            num_labels, labels = cv2.connectedComponents(img_bin, connectivity=8)

            # Asignar colores a cada etiqueta
            label_hue = (
                np.uint8(179 * labels / np.max(labels))
                if np.max(labels) > 0
                else labels
            )
            blank_ch = 255 * np.ones_like(label_hue)
            labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
            labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2RGB)
            labeled_img[label_hue == 0] = 0  # Fondo en negro

            self.imagen_conectividad_8 = self.redimensionar_imagen(labeled_img)

            img_pil = Image.fromarray(self.imagen_conectividad_8)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)
        return self.img_tk1

    def aplicar_etiquetado_conectividad_4(self, imagen):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Asegurarse de que la imagen sea binaria (1 canal)
        if len(imagen.shape) == 3:
            img_bin = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            img_bin = imagen.copy()
        _, img_bin = cv2.threshold(img_bin, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Encontrar contornos
        contours, _ = cv2.findContours(
            img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Convertir a color para dibujar
        image_color = cv2.cvtColor(img_bin, cv2.COLOR_GRAY2BGR)

        # Dibujar y numerar los contornos
        for i, contour in enumerate(contours):
            cv2.drawContours(image_color, [contour], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(
                image_color,
                f"{i + 1}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

        # Imprimir numero de componentes encontrados
        print(f"Número de componentes encontrados (conectividad 4): {len(contours)}")

        # Redimensionar la imagen para mostrarla en la interfaz
        self.imagen_etiquetado_conectividad_4 = self.redimensionar_imagen(image_color)

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_etiquetado_conectividad_4)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_etiquetado_conectividad_8(self, imagen):
        if imagen is None:
            raise ValueError("No se ha proporcionado una imagen.")

        # Asegurarse de que la imagen sea binaria (1 canal)
        if len(imagen.shape) == 3:
            img_bin = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
        else:
            img_bin = imagen.copy()
        _, img_bin = cv2.threshold(img_bin, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Encontrar contornos
        contours, _ = cv2.findContours(
            img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Convertir a color para dibujar
        image_color = cv2.cvtColor(img_bin, cv2.COLOR_GRAY2BGR)

        # Dibujar y numerar los contornos
        for i, contour in enumerate(contours):
            cv2.drawContours(image_color, [contour], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.putText(
                image_color,
                f"{i + 1}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

        # Imprimir numero de componentes encontrados
        print(f"Número de componentes encontrados (conectividad 8): {len(contours)}")

        # Redimensionar la imagen para mostrarla en la interfaz
        self.imagen_etiquetado_conectividad_8 = self.redimensionar_imagen(image_color)

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_etiquetado_conectividad_8)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def guardar_imagenes(self, ruta_guardar, imagen):
        # Guardar la imagen procesada
        if imagen is not None:
            # Redimensionar la imagen al tamaño original si es necesario
            if self.tamaño_original is not None and (
                imagen.shape[0] != self.tamaño_original[0]
                or imagen.shape[1] != self.tamaño_original[1]
            ):
                imagen_a_guardar = cv2.resize(
                    imagen, (self.tamaño_original[1], self.tamaño_original[0])
                )
            else:
                imagen_a_guardar = imagen

            # Si la imagen es RGB, convertir a BGR para guardar correctamente con OpenCV
            if len(imagen_a_guardar.shape) == 3 and imagen_a_guardar.shape[2] == 3:
                imagen_a_guardar = cv2.cvtColor(imagen_a_guardar, cv2.COLOR_RGB2BGR)

            # Si la ruta no tiene una extensión válida, agregar ".png" por defecto
            extensiones_validas = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif")
            if not ruta_guardar.lower().endswith(extensiones_validas):
                ruta_guardar += ".png"

            cv2.imwrite(ruta_guardar, imagen_a_guardar)
