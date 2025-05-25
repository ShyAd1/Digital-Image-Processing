import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from scipy.signal import find_peaks


class Modelo:
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
        self.imagen_segmentada_um = None
        self.imagen_segmentada_lum = None
        self.imagen_segmentada_ua = None
        self.imagen_segmentada_lua = None
        self.imagen_negativa = None
        self.imagen_and = None
        self.imagen_or = None
        self.imagen_xor = None
        self.max_size = 600
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
            "Imagen en grises": self.imagen_grises,
            "Imagen en grises (contraste)": self.imagen_grises_c,
            "Imagen binaria (umbral manual)": self.imagen_umbral_manual,
            "Imagen binaria (umbral automático)": self.imagen_umbral_automatico,
            "Imagen binaria (umbral manual, contraste)": self.imagen_umbral_manual_c,
            "Imagen binaria (umbral automático, contraste)": self.imagen_umbral_automatico_c,
            "Imagen con ruido gaussiano": self.imagen_ruido,
            "Imagen con corrección de contraste": self.imagen_correccion,
            "Imagen filtrada gaussiana": self.imagen_filtrada,
            "Imagen filtrada sal y pimienta": self.imagen_filtrada_sal_pimienta,
            "Imagen laplaciana": self.imagen_laplaciana,
            "Imagen segmentada (umbral manual)": self.imagen_segmentada_um,
            "Imagen segmentada (laplaciano, umbral manual)": self.imagen_segmentada_lum,
            "Imagen segmentada (umbral automático)": self.imagen_segmentada_ua,
            "Imagen segmentada (laplaciano, umbral automático)": self.imagen_segmentada_lua,
            "Imagen negativa": self.imagen_negativa,
            "Imagen AND": self.imagen_and,
            "Imagen OR": self.imagen_or,
            "Imagen XOR": self.imagen_xor,
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

        # Ejemplo de uso en otros métodos:
        # self.imagen_grises = self.redimensionar_imagen(self.imagen_grises)
        # self.imagen_filtrada = self.redimensionar_imagen(self.imagen_filtrada)

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

    def aplicar_ruido_gaussiano(self, media, sigma):
        if self.imagen_grises is None:
            raise ValueError("No se esta cargada la imagen principal")

        ruido = np.random.normal(media, sigma, self.imagen_grises.shape).astype(
            np.uint8
        )
        self.imagen_ruido = cv2.add(self.imagen_grises, ruido)

        # Redimensionar las imagen para que se ajuste al tamaño máximo
        altura, ancho = self.imagen_ruido.shape
        scale_factor = self.max_size / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_ruido = cv2.resize(self.imagen_ruido, (new_width, new_height))

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

    def aplicar_segmentacion_lua(self, imagen):

        # Normalizar la imagen Laplaciana para trabajar con valores en [0, 255]
        laplacian_normalized = cv2.normalize(
            imagen, None, 0, 255, cv2.NORM_MINMAX
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
        print(f"Umbral encontrado: {threshold}")

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
        # Verificar que el umbral manual esté dentro de un rango razonable
        if umbral < 0 or umbral > 255:
            raise ValueError("El umbral manual debe estar entre 0 y 255.")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_lum = cv2.threshold(
            imagen, umbral, 255, cv2.THRESH_BINARY
        )

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_lum)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_segmentacion_ua(self, imagen):
        # Normalizar la imagen Laplaciana para trabajar con valores en [0, 255]
        imagen_normalized = cv2.normalize(imagen, None, 0, 255, cv2.NORM_MINMAX).astype(
            np.uint8
        )

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
        print(f"Umbral encontrado: {threshold}")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_ua = cv2.threshold(
            imagen_normalized, threshold, 255, cv2.THRESH_BINARY
        )

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_ua)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_segmentacion_um(self, imagen, umbral):
        # Verificar que el umbral manual esté dentro de un rango razonable
        if umbral < 0 or umbral > 255:
            raise ValueError("El umbral manual debe estar entre 0 y 255.")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_um = cv2.threshold(
            imagen, umbral, 255, cv2.THRESH_BINARY
        )

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_um)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1
