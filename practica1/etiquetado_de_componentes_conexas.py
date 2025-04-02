import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2

ruta_imagen = None

MAX_SIZE = 400

THRESHOLD_VALUE = 127


def resize_image_preserve_aspect(image, max_size=MAX_SIZE):
    width, height = image.size
    scale = min(max_size / width, max_size / height)
    new_width = int(width * scale)
    new_height = int(height * scale)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)


def cargar_imagen(label_imagen):
    global ruta_imagen
    ruta_archivo = filedialog.askopenfilename(
        initialdir="/",
        title="Selecciona una imagen",
        filetypes=(
            ("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("Todos los archivos", "*.*"),
        ),
    )
    if ruta_archivo:
        imagen_original = Image.open(ruta_archivo).convert("RGB")
        imagen_mostrar = resize_image_preserve_aspect(imagen_original)
        foto = ImageTk.PhotoImage(imagen_mostrar)
        label_imagen.config(image=foto)
        label_imagen.image = foto
        ruta_imagen = ruta_archivo


def binarizar_imagen(label_imagen_modificada):
    global ruta_imagen
    if ruta_imagen is None:
        print("No se ha cargado ninguna imagen.")
        return

    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        print("Error al cargar la imagen.")
        return

    _, binary_image = cv2.threshold(imagen, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    imagen_pil = Image.fromarray(binary_image)
    imagen_mostrar = resize_image_preserve_aspect(imagen_pil)
    foto = ImageTk.PhotoImage(imagen_mostrar)
    label_imagen_modificada.config(image=foto)
    label_imagen_modificada.image = foto


def etiquetar_componentes(label_imagen_modificada, connectivity):
    global ruta_imagen
    if ruta_imagen is None:
        print("No se ha cargado ninguna imagen.")
        return

    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        print("Error al cargar la imagen.")
        return

    _, binary_image = cv2.threshold(imagen, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    num_labels, labels = cv2.connectedComponents(
        binary_image, connectivity=connectivity
    )
    print(f"Número de objetos detectados con vecindad-{connectivity}: {num_labels - 1}")

    labels_normalized = (
        (labels * 255 / (num_labels - 1)).astype(np.uint8) if num_labels > 1 else labels
    )
    imagen_pil = Image.fromarray(labels_normalized)
    imagen_mostrar = resize_image_preserve_aspect(imagen_pil)
    foto = ImageTk.PhotoImage(imagen_mostrar)
    label_imagen_modificada.config(image=foto)
    label_imagen_modificada.image = foto


def dibujar_contornos(label_imagen_modificada):
    global ruta_imagen
    if ruta_imagen is None:
        print("No se ha cargado ninguna imagen.")
        return

    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        print("Error al cargar la imagen.")
        return

    _, binary_image = cv2.threshold(imagen, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)

    image_color = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    contours, _ = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    print(f"Número de contornos detectados: {len(contours)}")
    if len(contours) == 0:
        print("No se detectaron contornos. Revisa la binarización o ajusta el umbral.")

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

    imagen_pil = Image.fromarray(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
    imagen_mostrar = resize_image_preserve_aspect(imagen_pil)
    foto = ImageTk.PhotoImage(imagen_mostrar)
    label_imagen_modificada.config(image=foto)
    label_imagen_modificada.image = foto


def comparar_vecindades():
    global ruta_imagen
    if ruta_imagen is None:
        print("No se ha cargado ninguna imagen.")
        return

    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        print("Error al cargar la imagen.")
        return

    _, binary_image = cv2.threshold(imagen, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    num_labels_4, _ = cv2.connectedComponents(binary_image, connectivity=4)
    num_labels_8, _ = cv2.connectedComponents(binary_image, connectivity=8)

    diferencia = abs(num_labels_4 - num_labels_8)
    print(f"Número de objetos con vecindad-4: {num_labels_4 - 1}")
    print(f"Número de objetos con vecindad-8: {num_labels_8 - 1}")
    print(f"Diferencia entre vecindad-4 y vecindad-8: {diferencia}")


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Procesador de Imágenes")
    ventana.geometry("1200x700")
    ventana.configure(bg="#f0f0f0")

    frame_controles = tk.Frame(ventana, bg="#e0e0e0", padx=10, pady=10)
    frame_controles.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

    titulo = tk.Label(
        frame_controles,
        text="Editor de Imágenes",
        font=("Arial", 16, "bold"),
        bg="#e0e0e0",
    )
    titulo.grid(row=0, column=0, columnspan=5, pady=10)

    boton_cargar = tk.Button(
        frame_controles,
        text="Cargar Imagen",
        command=lambda: cargar_imagen(label_imagen_original),
        width=15,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    boton_cargar.grid(row=1, column=0, padx=5, pady=5)

    boton_binarizar = tk.Button(
        frame_controles,
        text="Binarizar",
        command=lambda: binarizar_imagen(label_imagen_modificada),
        width=15,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    boton_binarizar.grid(row=1, column=1, padx=5, pady=5)

    boton_vecindad_4 = tk.Button(
        frame_controles,
        text="Vecindad-4",
        command=lambda: etiquetar_componentes(label_imagen_modificada, 4),
        width=15,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    boton_vecindad_4.grid(row=1, column=2, padx=5, pady=5)

    boton_vecindad_8 = tk.Button(
        frame_controles,
        text="Vecindad-8",
        command=lambda: etiquetar_componentes(label_imagen_modificada, 8),
        width=15,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    boton_vecindad_8.grid(row=1, column=3, padx=5, pady=5)

    boton_contornos = tk.Button(
        frame_controles,
        text="Contornos",
        command=lambda: dibujar_contornos(label_imagen_modificada),
        width=15,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    boton_contornos.grid(row=1, column=4, padx=5, pady=5)

    boton_comparar = tk.Button(
        frame_controles,
        text="Comparar",
        command=comparar_vecindades,
        width=15,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),
    )
    boton_comparar.grid(row=2, column=2, padx=5, pady=5)

    frame_imagenes = tk.Frame(ventana, bg="#f0f0f0")
    frame_imagenes.grid(row=1, column=0, columnspan=2, pady=20, sticky="nsew")

    frame_imagen_original = tk.Frame(
        frame_imagenes,
        bg="white",
        bd=2,
        relief="groove",
        width=MAX_SIZE,
        height=MAX_SIZE,
    )
    frame_imagen_original.grid(row=0, column=0, padx=10, pady=10)
    frame_imagen_original.grid_propagate(False)
    label_imagen_original = tk.Label(frame_imagen_original, bg="white")
    label_imagen_original.place(relx=0.5, rely=0.5, anchor="center")

    frame_imagen_modificada = tk.Frame(
        frame_imagenes,
        bg="white",
        bd=2,
        relief="groove",
        width=MAX_SIZE,
        height=MAX_SIZE,
    )
    frame_imagen_modificada.grid(row=0, column=1, padx=10, pady=10)
    frame_imagen_modificada.grid_propagate(False)
    label_imagen_modificada = tk.Label(frame_imagen_modificada, bg="white")
    label_imagen_modificada.place(relx=0.5, rely=0.5, anchor="center")

    ventana.grid_rowconfigure(0, weight=0)
    ventana.grid_rowconfigure(1, weight=1)
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    frame_imagenes.grid_rowconfigure(0, weight=1)
    frame_imagenes.grid_columnconfigure(0, weight=1)
    frame_imagenes.grid_columnconfigure(1, weight=1)

    ventana.mainloop()
