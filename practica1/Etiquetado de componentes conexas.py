import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen_original = None

def escoger_imagen():
    global imagen_original
    ruta_archivo = filedialog.askopenfilename(initialdir="/", title="Selecciona una imagen", filetypes=(("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp"), ("Todos los archivos", "*.*")))

    if ruta_archivo:
        imagen_original = Image.open(ruta_archivo).convert("RGB")

        imagen_mostrar = imagen_original.resize((400,400), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagen_mostrar)

        label_imagen_original.config(image=foto)
        label_imagen_original.image = foto

def binarizar_imagen():
    global imagen_original
    # Verificar si la imagen fue cargada correctamente
    if imagen_original is None:
        print("Error al cargar la imagen.")
        exit()

    imagen_cv2 = np.array(imagen_original)
    imagen_cv2 = cv2.cvtColor(imagen_cv2, cv2.COLOR_RGB2BGR)

    imagen_grey = cv2.cvtColor(imagen_cv2, cv2.COLOR_BGR2GRAY)
    # Umbralización para binarizar la imagen
    _, binary_image = cv2.threshold(imagen_grey, 127, 255, cv2.THRESH_BINARY)

    binarizada_rgb = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2RGB)
    imagen_pil = Image.fromarray(binarizada_rgb)

    # Redimensionar para mostrar
    imagen_mostrar = imagen_pil.resize((400, 400), Image.Resampling.NEAREST)
    foto = ImageTk.PhotoImage(imagen_mostrar)

    # Actualizar el label
    label_imagen_binarizada.config(image=foto)
    label_imagen_binarizada.image = foto

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Practica 1")
    ventana.geometry("1080x720")

    # Frame para los controles
    frame_controles = tk.Frame(ventana, bg="#e0e0e0", padx=10, pady=10)
    frame_controles.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    # Título
    titulo = tk.Label(frame_controles, text="Editor de Imágenes", font=("Arial", 16, "bold"), bg="#e0e0e0")
    titulo.grid(row=0, column=0, columnspan=2, pady=10)

    boton_abrir_img = tk.Button(frame_controles, text="Escoger imagen", command=escoger_imagen)
    boton_abrir_img.grid(row=1, column=0, padx=5, pady=5)

    boton_binarizar = tk.Button(frame_controles, text="Binariza Imagen", command=binarizar_imagen)
    boton_binarizar.grid(row=1, column=1, padx=5, pady=5)

    # Frame para la imagen con borde
    frame_imagen = tk.Frame(ventana, bg="white", bd=2, relief="groove")
    frame_imagen.grid(row=0, column=1, padx=20, pady=20)

    # Label para la imagen original
    label_imagen_original = tk.Label(frame_imagen, bg="white")
    label_imagen_original.pack(side="left", padx=10, pady=10)

    # Label para la imagen binarizada
    label_imagen_binarizada = tk.Label(frame_imagen, bg="white")
    label_imagen_binarizada.pack(side="right", padx=10, pady=10)

    # Configurar el grid
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_rowconfigure(0, weight=1)

    ventana.mainloop()