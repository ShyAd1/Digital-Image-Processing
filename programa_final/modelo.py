import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


class Modelo:
    def __init__(self):
        # Inicializar la imagen original y la imagen de salida
        self.img_tk1 = None
        self.img_tk2 = None
        self.img_tk3 = None
        self.img_tk4 = None
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
        self.max_size = 400
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

        # Redimensionar la imagen para que se ajuste al tamaño máximo
        altura, ancho, _ = self.imagen.shape
        scale_factor = 750 / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen = cv2.resize(self.imagen, (new_width, new_height))

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def convertir_RGB_a_grises(self, imagen1, imagen2):
        if imagen1 is not None:
            # Convertir la imagen de RGB a escala de grises
            self.imagen_grises = cv2.cvtColor(imagen1, cv2.COLOR_RGB2GRAY)

            # Redimensionar la imagen para que se ajuste al tamaño máximo
            altura, ancho = self.imagen_grises.shape
            scale_factor = 600 / max(altura, ancho)
            new_width = int(ancho * scale_factor)
            new_height = int(altura * scale_factor)
            self.imagen_grises = cv2.resize(self.imagen_grises, (new_width, new_height))

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_grises)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

        if imagen2 is not None:
            # Convertir la imagen de RGB a escala de grises
            self.imagen_grises_c = cv2.cvtColor(imagen2, cv2.COLOR_RGB2GRAY)

            # Redimensionar la imagen para que se ajuste al tamaño máximo
            altura, ancho = self.imagen_grises_c.shape
            scale_factor = 600 / max(altura, ancho)
            new_width = int(ancho * scale_factor)
            new_height = int(altura * scale_factor)
            self.imagen_grises_c = cv2.resize(
                self.imagen_grises_c, (new_width, new_height)
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_grises_c)
            self.img_tk2 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1, self.img_tk2

    def convertir_RGB_a_binario(self, imagen1, imagen2, umbral):
        # imagen1: sin corrección de contraste
        # imagen2: con corrección de contraste

        # Umbral manual para imagen1
        if imagen1 is not None:
            gris1 = cv2.cvtColor(imagen1, cv2.COLOR_RGB2GRAY)
            _, self.imagen_umbral_manual = cv2.threshold(
                gris1, umbral, 255, cv2.THRESH_BINARY
            )

            # Redimensionar las imagen para que se ajuste al tamaño máximo
            altura, ancho = self.imagen_umbral_manual.shape
            scale_factor = self.max_size / max(altura, ancho)
            new_width = int(ancho * scale_factor)
            new_height = int(altura * scale_factor)
            self.imagen_umbral_manual = cv2.resize(
                self.imagen_umbral_manual, (new_width, new_height)
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_umbral_manual)
            self.img_tk1 = ImageTk.PhotoImage(img_pil)

            # Umbral automático (Otsu) para imagen1
            _, self.imagen_umbral_automatico = cv2.threshold(
                gris1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Redimensionar las imagen para que se ajuste al tamaño máximo
            altura, ancho = self.imagen_umbral_automatico.shape
            scale_factor = self.max_size / max(altura, ancho)
            new_width = int(ancho * scale_factor)
            new_height = int(altura * scale_factor)
            self.imagen_umbral_automatico = cv2.resize(
                self.imagen_umbral_automatico, (new_width, new_height)
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_umbral_automatico)
            self.img_tk2 = ImageTk.PhotoImage(img_pil)

        # Umbral manual para imagen2
        if imagen2 is not None:
            gris2 = cv2.cvtColor(imagen2, cv2.COLOR_RGB2GRAY)
            _, self.imagen_umbral_manual_c = cv2.threshold(
                gris2, umbral, 255, cv2.THRESH_BINARY
            )

            # Redimensionar las imagen para que se ajuste al tamaño máximo
            altura, ancho = self.imagen_umbral_manual_c.shape
            scale_factor = self.max_size / max(altura, ancho)
            new_width = int(ancho * scale_factor)
            new_height = int(altura * scale_factor)
            self.imagen_umbral_manual_c = cv2.resize(
                self.imagen_umbral_manual_c, (new_width, new_height)
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_umbral_manual_c)
            self.img_tk3 = ImageTk.PhotoImage(img_pil)

            # Umbral automático (Otsu) para imagen2
            _, self.imagen_umbral_automatico_c = cv2.threshold(
                gris2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

            # Redimensionar las imagen para que se ajuste al tamaño máximo
            altura, ancho = self.imagen_umbral_automatico_c.shape
            scale_factor = self.max_size / max(altura, ancho)
            new_width = int(ancho * scale_factor)
            new_height = int(altura * scale_factor)
            self.imagen_umbral_automatico_c = cv2.resize(
                self.imagen_umbral_automatico_c, (new_width, new_height)
            )

            # Convertir la imagen a un formato compatible con Tkinter
            img_pil = Image.fromarray(self.imagen_umbral_automatico_c)
            self.img_tk4 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1, self.img_tk2, self.img_tk3, self.img_tk4

    def aplicar_ruido_gaussiano(self, media, sigma):
        if self.imagen_grises is None:
            raise ValueError("No se esta cargada la imagen principal")

        ruido = np.random.normal(media, sigma, self.imagen_grises.shape).astype(
            np.uint8
        )
        self.imagen_ruido = cv2.add(self.imagen_grises, ruido)

        # Redimensionar las imagen para que se ajuste al tamaño máximo
        altura, ancho = self.imagen_ruido.shape
        scale_factor = 600 / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_ruido = cv2.resize(self.imagen_ruido, (new_width, new_height))

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_ruido)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_correccion_contraste(self, gamma):
        if self.imagen_original is None:
            raise ValueError("No se esta cargada la imagen principal")

        # Aplicar corrección gamma a la imagen 1
        self.imagen_correccion = np.clip(
            255 * ((self.imagen_original / 255) ** gamma), 0, 255
        ).astype(np.uint8)

        # Redimensionar las imagen para que se ajuste al tamaño máximo
        altura, ancho, _ = self.imagen_correccion.shape
        scale_factor = 600 / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_correccion = cv2.resize(
            self.imagen_correccion, (new_width, new_height)
        )

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
        if imagen is None:
            raise ValueError("No se esta cargada la imagen principal")

        self.imagen_filtrada = cv2.GaussianBlur(
            imagen, (3, 3), sigma
        )  # Aplicar filtro gaussiano, con sigma como desviación estándar

        # Redimensionar las imagen para que se ajuste al tamaño máximo
        altura, ancho = self.imagen_filtrada.shape
        scale_factor = 600 / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_filtrada = cv2.resize(self.imagen_filtrada, (new_width, new_height))

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_filtrada)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1

    def aplicar_filtro_sal_pimienta(self, imagen):
        if imagen is None:
            raise ValueError("No se esta cargada la imagen principal")

        self.imagen_filtrada_sal_pimienta = cv2.medianBlur(imagen, 3)

        # Redimensionar las imagen para que se ajuste al tamaño máximo
        altura, ancho = self.imagen_filtrada_sal_pimienta.shape
        scale_factor = 600 / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_filtrada_sal_pimienta = cv2.resize(
            self.imagen_filtrada_sal_pimienta, (new_width, new_height)
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

        # Redimensionar la imagen procesada
        altura, ancho = self.imagen_laplaciana.shape
        scale_factor = 600 / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_laplaciana = cv2.resize(
            self.imagen_laplaciana, (new_width, new_height)
        )

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_laplaciana)
        self.img_tk1 = ImageTk.PhotoImage(img_pil)

        return self.img_tk1
