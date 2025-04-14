import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# Variables globales
original_image1 = None
original_image2 = None
operation_image = None
img_label1 = None
img_label2 = None
img_label3 = None
max_size = 400  # Tamaño máximo para las imágenes
current_image = 1
max_val = 255
gamma = 0.5  # Valor de gamma para la corrección gamma
THRESHOLD_VALUE = 127  # Valor de umbral inicial


# Definición de funciones para las operaciones de procesamiento de imágenes


# Función para actualizar el valor del umbral
def update_threshold(value):
    global THRESHOLD_VALUE
    THRESHOLD_VALUE = value
    # Actualizar el texto del label del slider
    slider_label1.config(text=f"Ajustar valor de umbral: {THRESHOLD_VALUE}")


# Función para actualizar el valor de gamma
def update_gamma(value):
    global gamma
    gamma = float(value)
    # Actualizar el texto del label del slider
    slider_label2.config(text=f"Ajustar valor de gamma: {gamma}")


# Funciones para operaciones puntuales
# Funciones para operaciones de suma, resta y multiplicación de imágenes
def add_images():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # Sumar las dos imágenes
    # Redimensionar la segunda imagen para que coincida con la primera
    resized_image2 = cv2.resize(
        original_image2, (original_image1.shape[1], original_image1.shape[0])
    )

    # Sumar las dos imágenes
    added_image = cv2.add(original_image1, resized_image2)

    # Asegurarse de que los valores estén dentro del rango válido
    added_image = np.clip(added_image, 0, max_val).astype(np.uint8)

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(added_image)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen resultante en el label
    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine


def subtract_images():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # Restar las dos imágenes
    # Redimensionar la segunda imagen para que coincida con la primera
    resized_image2 = cv2.resize(
        original_image2, (original_image1.shape[1], original_image1.shape[0])
    )

    # Restar las dos imágenes
    subtracted_image = cv2.subtract(original_image1, resized_image2)

    # Asegurarse de que los valores estén dentro del rango válido
    subtracted_image = np.clip(subtracted_image, 0, max_val).astype(np.uint8)

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(subtracted_image)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen resultante en el label
    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine


def multiply_images():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # Multiplicar las dos imágenes
    # Redimensionar la segunda imagen para que coincida con la primera
    resized_image2 = cv2.resize(
        original_image2, (original_image1.shape[1], original_image1.shape[0])
    )

    # Multiplicar las dos imágenes
    multiplied_image = cv2.multiply(original_image1, resized_image2)

    # Asegurarse de que los valores estén dentro del rango válido
    multiplied_image = np.clip(multiplied_image, 0, max_val).astype(np.uint8)

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(multiplied_image)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen resultante en el label
    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine


# Funciones para operaciones logicas
# Funciones para operaciones de AND, OR y XOR de imágenes
def and_images():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # AND de las dos imágenes
    # Redimensionar la segunda imagen para que coincida con la primera
    resized_image2 = cv2.resize(
        original_image2, (original_image1.shape[1], original_image1.shape[0])
    )

    # AND de las dos imágenes
    and_image = cv2.bitwise_and(original_image1, resized_image2)

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(and_image)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen resultante en el label
    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine


def or_images():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # OR de las dos imágenes
    # Redimensionar la segunda imagen para que coincida con la primera
    resized_image2 = cv2.resize(
        original_image2, (original_image1.shape[1], original_image1.shape[0])
    )

    # OR de las dos imágenes
    or_image = cv2.bitwise_or(original_image1, resized_image2)

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(or_image)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen resultante en el label
    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine


def xor_images():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # XOR de las dos imágenes
    # Redimensionar la segunda imagen para que coincida con la primera
    resized_image2 = cv2.resize(
        original_image2, (original_image1.shape[1], original_image1.shape[0])
    )

    # XOR de las dos imágenes
    xor_image = cv2.bitwise_xor(original_image1, resized_image2)

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(xor_image)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen resultante en el label
    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine


# Función para binarización
def convert_to_binary():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # Convertir a escala de grises
    gray_image1 = cv2.cvtColor(original_image1, cv2.COLOR_RGB2GRAY)
    gray_image2 = cv2.cvtColor(original_image2, cv2.COLOR_RGB2GRAY)

    # Aplicar umbralización
    _, binary_image1 = cv2.threshold(
        gray_image1, THRESHOLD_VALUE, max_val, cv2.THRESH_BINARY
    )
    _, binary_image2 = cv2.threshold(
        gray_image2, THRESHOLD_VALUE, max_val, cv2.THRESH_BINARY
    )

    # Mostrar las imágenes originales y binarizadas
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image1)
    plt.title("Imagen Original 1")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(binary_image1, cmap="gray")
    plt.title("Imagen Binarizada - Imagen 1")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image2)
    plt.title("Imagen Original 2")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(binary_image2, cmap="gray")
    plt.title("Imagen Binarizada - Imagen 2")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Función para convertir a escala de grises
def convert_grayscale():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # Convertir a escala de grises
    gray_image1 = cv2.cvtColor(original_image1, cv2.COLOR_RGB2GRAY)
    gray_image2 = cv2.cvtColor(original_image2, cv2.COLOR_RGB2GRAY)

    # Mostrar las imágenes originales y en escala de grises
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image1)
    plt.title("Imagen Original 1")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(gray_image1, cmap="gray")
    plt.title("Escala de Grises - Imagen 1")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image2)
    plt.title("Imagen Original 2")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(gray_image2, cmap="gray")
    plt.title("Escala de Grises - Imagen 2")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Función para aplicar corrección gamma a las imágenes
def gamma_correction():
    global original_image1, original_image2, gamma
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return

    # Aplicar corrección gamma a la imagen 1
    corrected_image1 = np.clip(
        max_val * ((original_image1 / max_val) ** gamma), 0, max_val
    ).astype(np.uint8)
    # Aplicar corrección gamma a la imagen 2
    corrected_image2 = np.clip(
        max_val * ((original_image2 / max_val) ** gamma), 0, max_val
    ).astype(np.uint8)

    # Mostrar las imágenes originales y corregidas
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image1)
    plt.title("Imagen Original 1")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(corrected_image1)
    plt.title(f"Corrección Gamma (gamma={gamma}) - Imagen 1")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image2)
    plt.title("Imagen Original 2")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(corrected_image2)
    plt.title(f"Corrección Gamma (gamma={gamma}) - Imagen 2")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Función para extraer los canales RGB de las imágenes
def extract_channels():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return
    # Extraer los canales RGB de la imagen 1
    b_channel1, g_channel1, r_channel1 = cv2.split(original_image1)
    # Extraer los canales RGB de la imagen 2
    b_channel2, g_channel2, r_channel2 = cv2.split(original_image2)

    # Mostrar los canales en subplots
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 3, 1)
    plt.imshow(
        cv2.merge([b_channel1, np.zeros_like(b_channel1), np.zeros_like(b_channel1)])
    )
    plt.title("Canal Azul - Imagen 1")
    plt.axis("off")
    plt.subplot(2, 3, 2)
    plt.imshow(
        cv2.merge([np.zeros_like(g_channel1), g_channel1, np.zeros_like(g_channel1)])
    )
    plt.title("Canal Verde - Imagen 1")
    plt.axis("off")
    plt.subplot(2, 3, 3)
    plt.imshow(
        cv2.merge([np.zeros_like(r_channel1), np.zeros_like(r_channel1), r_channel1])
    )
    plt.title("Canal Rojo - Imagen 1")
    plt.axis("off")
    plt.subplot(2, 3, 4)
    plt.imshow(
        cv2.merge([b_channel2, np.zeros_like(b_channel2), np.zeros_like(b_channel2)])
    )
    plt.title("Canal Azul - Imagen 2")
    plt.axis("off")
    plt.subplot(2, 3, 5)
    plt.imshow(
        cv2.merge([np.zeros_like(g_channel2), g_channel2, np.zeros_like(g_channel2)])
    )
    plt.title("Canal Verde - Imagen 2")
    plt.axis("off")
    plt.subplot(2, 3, 6)
    plt.imshow(
        cv2.merge([np.zeros_like(r_channel2), np.zeros_like(r_channel2), r_channel2])
    )
    plt.title("Canal Rojo - Imagen 2")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Función para mostrar el histograma de las imágenes
def show_histogram():
    global original_image1, original_image2
    if original_image1 is None or original_image2 is None:
        messagebox.showerror("Error", "Por favor, carga dos imágenes primero.")
        return
    # mostrar el histograma de los canales RGB de la imagen 1
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(
        original_image1.ravel(),
        bins=256,
        range=(0, 256),
        color="blue",
        alpha=0.5,
        label="Canal Azul",
    )
    plt.hist(
        original_image1[:, :, 1].ravel(),
        bins=256,
        range=(0, 256),
        color="green",
        alpha=0.5,
        label="Canal Verde",
    )
    plt.hist(
        original_image1[:, :, 2].ravel(),
        bins=256,
        range=(0, 256),
        color="red",
        alpha=0.5,
        label="Canal Rojo",
    )
    plt.title("Histograma de la imagen 1")
    plt.xlabel("Valor de intensidad")
    plt.ylabel("Número de píxeles")
    plt.legend()
    plt.grid()
    plt.subplot(1, 2, 2)
    plt.hist(
        original_image2.ravel(),
        bins=256,
        range=(0, 256),
        color="blue",
        alpha=0.5,
        label="Canal Azul",
    )
    plt.hist(
        original_image2[:, :, 1].ravel(),
        bins=256,
        range=(0, 256),
        color="green",
        alpha=0.5,
        label="Canal Verde",
    )
    plt.hist(
        original_image2[:, :, 2].ravel(),
        bins=256,
        range=(0, 256),
        color="red",
        alpha=0.5,
        label="Canal Rojo",
    )
    plt.title("Histograma de la imagen 2")
    plt.xlabel("Valor de intensidad")
    plt.ylabel("Número de píxeles")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


# Función para cargar la imagen
def load_image():
    global original_image1, original_image2, img_label1, img_label2, current_image
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.bmp *.png *.jpg")]
    )
    if file_path:
        image = cv2.imread(file_path)
        if image is None:
            messagebox.showerror("Error", "No se pudo cargar la imagen.")
            return

        # Convertir la imagen de BGR a RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        altura, ancho, _ = image.shape
        scale_factor = max_size / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        image = cv2.resize(image, (new_width, new_height))

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(image)
        img_tk = ImageTk.PhotoImage(img_pil)

        # Alternar entre las dos imágenes
        if current_image == 1:
            original_image1 = image
            img_label1.config(image=img_tk)
            img_label1.image = img_tk  # Guardar referencia para evitar que se elimine
            current_image = 2  # Cambiar a la segunda imagen
        else:
            original_image2 = image
            img_label2.config(image=img_tk)
            img_label2.image = img_tk  # Guardar referencia para evitar que se elimine
            current_image = 1  # Cambiar a la primera imagen


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesamiento de Imágenes - operaciones puntuales")
ventana.geometry("1400x800")
ventana.configure(bg="#adadad")

# Marco para los botones (centrado en la parte superior)
button_frame = tk.Frame(ventana, bg="#adadad")
button_frame.pack(pady=20)

# Marco para slider (centrado en la parte superior)
scroll_frame = tk.Frame(ventana, bg="#adadad")
scroll_frame.pack(pady=20)

# Marco para las imágenes (centrado en la parte inferior)
image_frame = tk.Frame(ventana, bg="#adadad")
image_frame.pack(pady=20)

# Botones centrados
# Crear un botón para cargar la imagen
btn_load = tk.Button(
    button_frame,
    text="Cargar Imagen",
    command=load_image,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_load.grid(row=0, column=0, padx=5)

# Crear un botón para mostrar el histograma
btn_show = tk.Button(
    button_frame,
    text="Calcular histograma",
    command=show_histogram,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_show.grid(row=0, column=1, padx=5)

# Crear un botón para extraer los canales
btn_extract = tk.Button(
    button_frame,
    text="Extraer Canales",
    command=extract_channels,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_extract.grid(row=0, column=2, padx=5)

# Crear un botón para aplicar la corrección gamma
btn_gamma = tk.Button(
    button_frame,
    text="Corrección Gamma",
    command=gamma_correction,
    bg="#FF5722",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_gamma.grid(row=0, column=3, padx=5)

# Crear un botón para convertir a escala de grises
btn_grayscale = tk.Button(
    button_frame,
    text="Convertir a Escala de Grises",
    command=convert_grayscale,
    bg="#673AB7",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_grayscale.grid(row=0, column=4, padx=5)

# Crear un botón para convertir a binarizada
btn_binarize = tk.Button(
    button_frame,
    text="Convertir a Binarizada",
    command=convert_to_binary,
    bg="#3F51B5",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_binarize.grid(row=0, column=5, padx=5)

# Crear un botón para sumar imágenes
btn_add = tk.Button(
    button_frame,
    text="Sumar Imágenes",
    command=add_images,
    bg="#009688",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_add.grid(row=1, column=0, padx=5)

# Crear un botón para restar imágenes
btn_subtract = tk.Button(
    button_frame,
    text="Restar Imágenes",
    command=subtract_images,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_subtract.grid(row=1, column=1, padx=5)

# Crear un botón para multiplicar imágenes
btn_multiply = tk.Button(
    button_frame,
    text="Multiplicar Imágenes",
    command=multiply_images,
    bg="#FF5722",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_multiply.grid(row=1, column=2, padx=5)

# Crear un botón para AND de imágenes
btn_and = tk.Button(
    button_frame,
    text="AND Imágenes",
    command=and_images,
    bg="#673AB7",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_and.grid(row=1, column=3, padx=5)

# Crear un botón para OR de imágenes
btn_or = tk.Button(
    button_frame,
    text="OR Imágenes",
    command=or_images,
    bg="#3F51B5",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_or.grid(row=1, column=4, padx=5)

# Crear un botón para XOR de imágenes
btn_xor = tk.Button(
    button_frame,
    text="XOR Imágenes",
    command=and_images,
    bg="#009688",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_xor.grid(row=1, column=5, padx=5)

# Crear slider para ajustar el valor de umbral
slider_label1 = tk.Label(
    scroll_frame,
    text="Ajustar valor de umbral:",
    bg="#adadad",
    font=("Arial", 10, "bold"),
)
slider_label1.grid(row=0, column=0, padx=5)

slider_threshold = tk.Scale(
    scroll_frame,
    from_=0,
    to=255,
    orient=tk.HORIZONTAL,
    bg="#adadad",
    fg="black",
    font=("Arial", 10, "bold"),
    command=lambda value: update_threshold(int(value)),
)
slider_threshold.set(THRESHOLD_VALUE)  # Establecer el valor inicial del slider
slider_threshold.grid(row=0, column=1, padx=5)

# Crear slider para ajustar el valor de gamma
slider_label2 = tk.Label(
    scroll_frame,
    text="Ajustar valor de gamma:",
    bg="#adadad",
    font=("Arial", 10, "bold"),
)
slider_label2.grid(row=0, column=2, padx=5)

slider_gamma = tk.Scale(
    scroll_frame,
    from_=0.1,
    to=5.0,
    orient=tk.HORIZONTAL,
    bg="#adadad",
    fg="black",
    font=("Arial", 10, "bold"),
    resolution=0.1,
    command=lambda value: update_gamma(float(value)),
)
slider_gamma.set(gamma)  # Establecer el valor inicial del slider
slider_gamma.grid(row=0, column=3, padx=5)

# Crear Labels para mostrar las imágenes
img_label1 = tk.Label(image_frame, bg="#adadad")
img_label1.grid(row=0, column=0, padx=5, pady=5)

img_label2 = tk.Label(image_frame, bg="#adadad")
img_label2.grid(row=0, column=1, padx=5, pady=5)

img_label3 = tk.Label(image_frame, bg="#adadad")
img_label3.grid(row=0, column=3, padx=5, pady=5)

# Centrar el marco de botones
button_frame.grid_columnconfigure((0, 1, 2), weight=1)

# Centrar el marco de imágenes
image_frame.grid_rowconfigure(0, weight=1)
image_frame.grid_columnconfigure((0, 1, 2), weight=1)

# Centrar el marco del slider
scroll_frame.grid_rowconfigure(0, weight=1)
scroll_frame.grid_columnconfigure((0, 1), weight=1)

# Iniciar la aplicación
ventana.mainloop()
