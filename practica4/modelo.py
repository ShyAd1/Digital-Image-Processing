import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
from scipy.signal import find_peaks


class Modelo:
    def __init__(self):
        self.imagen = None
        self.imagen_original = None
        self.imagen_procesada = None
        self.imagen_segmentadaUA = None
        self.imagen_segmentada_laplacianoUA = None
        self.imagen_segmentadaUM = None
        self.imagen_segmentada_laplacianoUM = None
        self.max_size = 300
        self.tamaño_original = None
        self.label_info_imagen_original = None
        self.label_info_procesada = None
        self.label_info_segmentadaUA = None
        self.label_info_segmentada_laplacianoUA = None
        self.label_info_segmentadaUM = None
        self.label_info_segmentada_laplacianoUM = None
        self.img_tk = None
        self.matriz_convolucion = None

    def set_label(self, option):
        if option == "original":
            self.label_info_imagen_original = f"Imagen Original - tamaño: {self.imagen.shape[0]}x{self.imagen.shape[1]}"
        elif option == "procesada":
            self.label_info_procesada = f"Imagen Procesada - tamaño: {self.imagen_procesada.shape[0]}x{self.imagen_procesada.shape[1]}"
        elif option == "segmentada laplaciano UA":
            self.label_info_segmentada_laplacianoUA = f"Imagen Segmentada laplaciano umbral automatico - tamaño: {self.imagen_segmentada_laplacianoUA.shape[0]}x{self.imagen_segmentada_laplacianoUA.shape[1]}"
        elif option == "segmentada UA":
            self.label_info_segmentadaUA = f"Imagen Segmentada umbral automatico - tamaño: {self.imagen_segmentadaUA.shape[0]}x{self.imagen_segmentadaUA.shape[1]}"
        elif option == "segmentada laplaciano UM":
            self.label_info_segmentada_laplacianoUM = f"Imagen Segmentada laplaciano umbral manual - tamaño: {self.imagen_segmentada_laplacianoUM.shape[0]}x{self.imagen_segmentada_laplacianoUM.shape[1]}"
        elif option == "segmentada UM":
            self.label_info_segmentadaUM = f"Imagen Segmentada umbral manual - tamaño: {self.imagen_segmentadaUM.shape[0]}x{self.imagen_segmentadaUM.shape[1]}"
        else:
            raise ValueError("Opción no válida para establecer la etiqueta.")

    def cargar_imagen(self, ruta):
        self.imagen = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        self.tamaño_original = self.imagen.shape
        if self.imagen is None:
            raise ValueError("No se pudo cargar la imagen.")

        self.imagen_original = self.imagen.copy()

        # Redimensionar la imagen para que se ajuste al tamaño máximo
        altura, ancho = self.imagen.shape
        scale_factor = self.max_size / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen = cv2.resize(self.imagen, (new_width, new_height))

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        return self.img_tk

    def guardar_imagenes(self, ruta_guardar):
        # Guardar la imagen procesada
        if self.imagen_procesada is not None:
            # Redimensionar la imagen procesada al tamaño original
            self.imagen_procesada = cv2.resize(
                self.imagen_procesada,
                (self.tamaño_original[1], self.tamaño_original[0]),
            )

            cv2.imwrite(ruta_guardar + "_procesada.jpg", self.imagen_procesada)

        # Guardar la imagen segmentada laplaciano umbral automático
        if self.imagen_segmentada_laplacianoUA is not None:
            # Redimensionar la imagen segmentada laplaciano al tamaño original
            self.imagen_segmentada_laplacianoUA = cv2.resize(
                self.imagen_segmentada_laplacianoUA,
                (self.tamaño_original[1], self.tamaño_original[0]),
            )

            cv2.imwrite(ruta_guardar + "_segmentada_laplaciano_automatico.jpg", self.imagen_segmentada_laplacianoUA)

        # Guardar la imagen segmentada umbral automático
        if self.imagen_segmentadaUA is not None:
            # Redimensionar la imagen segmentada al tamaño original
            self.imagen_segmentadaUA = cv2.resize(
                self.imagen_segmentadaUA,
                (self.tamaño_original[1], self.tamaño_original[0]),
            )

            cv2.imwrite(ruta_guardar + "_segmentada_automatico.jpg", self.imagen_segmentadaUA)

        # Guardar la imagen segmentada laplaciano umbral manual
        if self.imagen_segmentada_laplacianoUM is not None:
            # Redimensionar la imagen segmentada laplaciano al tamaño original
            self.imagen_segmentada_laplacianoUM = cv2.resize(
                self.imagen_segmentada_laplacianoUM,
                (self.tamaño_original[1], self.tamaño_original[0]),
            )

            cv2.imwrite(ruta_guardar + "_segmentada_laplaciano_manual.jpg", self.imagen_segmentada_laplacianoUM)

        # Guardar la imagen segmentada umbral manual
        if self.imagen_segmentadaUM is not None:
            # Redimensionar la imagen segmentada al tamaño original
            self.imagen_segmentadaUM = cv2.resize(
                self.imagen_segmentadaUM,
                (self.tamaño_original[1], self.tamaño_original[0]),
            )

            cv2.imwrite(ruta_guardar + "_segmentada_manual.jpg", self.imagen_segmentadaUM)

    def aplicar_filtro_laplaciano(self, matriz):
        # Converir la matriz de convolución a un array de numpy
        laplaciano = np.array(matriz, dtype=np.float32)

        # Aplicar el filtro Laplaciano a la imagen
        self.imagen_procesada = cv2.filter2D(self.imagen, -1, laplaciano)

        # Redimensionar la imagen procesada
        altura, ancho = self.imagen.shape
        scale_factor = self.max_size / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        self.imagen_procesada = cv2.resize(
            self.imagen_procesada, (new_width, new_height)
        )

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_procesada)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        return self.img_tk

    def mostrar_histograma(self):
        # Mostrar el histograma de la imagen original
        plt.hist(self.imagen.flatten(), bins=256, range=[0, 256], color="gray")
        plt.title("Histograma de la Imagen Original")
        plt.xlabel("Intensidad de píxel")
        plt.ylabel("Frecuencia")
        plt.show()

    def segmentar_imagen_laplacianoUA(self):
        # Asegurarse de que haya una imagen procesada (Laplaciana)
        if self.imagen_procesada is None:
            raise ValueError("No hay una imagen procesada (Laplaciana) para segmentar.")

        # Normalizar la imagen Laplaciana para trabajar con valores en [0, 255]
        laplacian_normalized = cv2.normalize(
            self.imagen_procesada, None, 0, 255, cv2.NORM_MINMAX
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
        _, self.imagen_segmentada_laplacianoUA = cv2.threshold(
            laplacian_normalized, threshold, 255, cv2.THRESH_BINARY
        )

        # Actualizar la etiqueta de la imagen segmentada
        self.set_label("segmentada laplaciano UA")

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_laplacianoUA)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        return self.img_tk

    def segmentar_imagenUA(self):
        # Asegurarse de que haya una imagen procesada (Laplaciana)
        if self.imagen is None:
            raise ValueError("No hay una imagen procesada (Laplaciana) para segmentar.")

        # Normalizar la imagen Laplaciana para trabajar con valores en [0, 255]
        imagen_normalized = cv2.normalize(
            self.imagen, None, 0, 255, cv2.NORM_MINMAX
        ).astype(np.uint8)

        # Calcular el histograma de la imagen normalizada
        hist = cv2.calcHist(
            [imagen_normalized], [0], None, [256], [0, 256]
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
        _, self.imagen_segmentadaUA = cv2.threshold(
            imagen_normalized, threshold, 255, cv2.THRESH_BINARY
        )

        # Actualizar la etiqueta de la imagen segmentada
        self.set_label("segmentada UA")

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentadaUA)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        return self.img_tk

    def segmentar_imagen_laplacianoUM(self, umbral):
        # Asegurarse de que haya una imagen procesada (Laplaciana)
        if self.imagen_procesada is None:
            raise ValueError("No hay una imagen procesada (Laplaciana) para segmentar.")

        print(umbral)

        # Verificar que el umbral manual esté dentro de un rango razonable
        if umbral < 0 or umbral > 255:
            raise ValueError("El umbral manual debe estar entre 0 y 255.")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentada_laplacianoUM = cv2.threshold(
            self.imagen_procesada, umbral, 255, cv2.THRESH_BINARY
        )

        # Actualizar la etiqueta de la imagen segmentada
        self.set_label("segmentada laplaciano UM")

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentada_laplacianoUM)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        return self.img_tk

    def segmentar_imagenUM(self, umbral):
        # Asegurarse de que haya una imagen procesada (Laplaciana)
        if self.imagen is None:
            raise ValueError("No hay una imagen procesada (Laplaciana) para segmentar.")

        print(umbral)

        # Verificar que el umbral manual esté dentro de un rango razonable
        if umbral < 0 or umbral > 255:
            raise ValueError("El umbral manual debe estar entre 0 y 255.")

        # Aplicar umbralización para segmentar la imagen
        _, self.imagen_segmentadaUM = cv2.threshold(
            self.imagen, umbral, 255, cv2.THRESH_BINARY
        )

        # Actualizar la etiqueta de la imagen segmentada
        self.set_label("segmentada UM")

        # Convertir la imagen segmentada a un formato compatible con Tkinter
        img_pil = Image.fromarray(self.imagen_segmentadaUM)
        self.img_tk = ImageTk.PhotoImage(img_pil)

        return self.img_tk