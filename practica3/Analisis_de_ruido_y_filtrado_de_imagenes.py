import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from scipy import stats
from scipy.ndimage import generic_filter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# Variables globales
original_image = None
gaussian_image = None
salt_pepper_image = None
img_label1 = None
img_label2 = None
img_label3 = None
label1 = None
label2 = None
label3 = None
max_size = 400  # Tamaño máximo para las imágenes
RUIDO_SAL_PIMIENTA = 0.05
MEDIA = 0 # Media para ruido gaussiano
SIGMA = 25 # Desviacion estandar para ruido gaussiano

# Definicion de funciones para las operaciones del procesamiento de imagenes

# Funcion para actualizar el ruido gaussiano (media)
def update_noise_gauss_media(value):
    global MEDIA
    MEDIA = value
    # Actualizar el texto del label del slider
    slider_media.config(text=f"Ajustar valor de media (ruido gaussiano): {MEDIA}")

# Funcion para actualizar el ruido gaussiano (sigma)
def update_noise_gauss_sigma(value):
    global SIGMA
    SIGMA = value
    # Actualizar el texto del label del slider
    slider_sigma.config(text=f"Ajustar valor de sigma (ruido gaussiano): {SIGMA}")

# Funcion para actualizar el ruido de sal y pimienta
def update_noise_s_p(value):
    global RUIDO_SAL_PIMIENTA
    RUIDO_SAL_PIMIENTA = value
    # Actualizar el texto del label del slider
    slider_label1.config(text=f"Ajustar valor de ruido sal y pimienta: {RUIDO_SAL_PIMIENTA}")




# Funciones para aplicar filtrados a las imágenes

# Funcion para aplicar filtro promedio
def apply_filter_average():
    global gaussian_image
    if gaussian_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    salida = cv2.blur(gaussian_image, (5, 5))  # Aplicar filtro promedio con un kernel de 5x5

    # Mostrar la imagen filtrada
    plt.imshow(salida, cmap='gray')
    plt.title("Filtro Promedio")
    plt.axis('off')
    plt.show()

# Funcion para aplicar filtro promedio pesado
def apply_filter_average_heavy():
    global gaussian_image
    if gaussian_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    kernel = np.array([[1,1,1],[1,5,1], [1,1,1]]) / 13  # Definir el kernel del filtro promedio pesado, normalizado a 1 y con un peso mayor en el centro, con un tamaño de 3x3 y suma 13
    salida = cv2.filter2D(gaussian_image, -1, kernel)  # Aplicar filtro promedio pesado

    # Mostrar la imagen filtrada
    plt.imshow(salida, cmap='gray')
    plt.title("Filtro Promedio Pesado")
    plt.axis('off')
    plt.show()

# Funcion para aplicar filtro gaussiano
def apply_filter_gaussian():
    global gaussian_image, SIGMA
    if gaussian_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    salida = cv2.GaussianBlur(gaussian_image, (5, 5), SIGMA)  # Aplicar filtro gaussiano, con sigma como desviación estándar

    # Mostrar la imagen filtrada
    plt.imshow(salida, cmap='gray')
    plt.title("Filtro Gaussiano")
    plt.axis('off')
    plt.show()




# Funcion para aplicar filtro de mediana
def apply_filter_median():
    global salt_pepper_image
    if salt_pepper_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    salida = cv2.medianBlur(salt_pepper_image, 5)  # Aplicar filtro de mediana, con un tamaño de 5x5

    # Mostrar la imagen filtrada
    plt.imshow(salida, cmap='gray')
    plt.title("Filtro Mediana")
    plt.axis('off')
    plt.show()

# Funcion para aplicar filtro de moda
def apply_filter_mode():
    global salt_pepper_image
    if salt_pepper_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    # Definir la función de moda
    def mode_filter(arr):
        mode = stats.mode(arr, axis=None)[0][0]
        return mode

    salida = generic_filter(salt_pepper_image, mode_filter, size=5)  # Aplicar filtro de moda, con un tamaño de 5x5

    # Mostrar la imagen filtrada
    plt.imshow(salida, cmap='gray')
    plt.title("Filtro Moda")
    plt.axis('off')
    plt.show()


# Funcion para aplicar ruido de sal y pimienta
def apply_noice_s_p():
    global original_image, salt_pepper_image, img_label2, RUIDO_SAL_PIMIENTA, label2
    if original_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    salida = np.copy(original_image)
    num_pixeles = int(RUIDO_SAL_PIMIENTA * original_image.size)
    # Añadir ruido sal
    coords = [np.random.randint(0, i-1, num_pixeles) for i in original_image.shape]
    salida[coords[0], coords[1]] = 255
    # Añadir ruido pimienta
    coords = [np.random.randint(0, i-1, num_pixeles) for i in original_image.shape]
    salida[coords[0], coords[1]] = 0

    salt_pepper_image = salida # Guardar la imagen con ruido de sal y pimienta

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(salida)
    img_tk = ImageTk.PhotoImage(img_pil)

    img_label2.config(image=img_tk)
    img_label2.image = img_tk  # Guardar referencia para evitar que se elimine

    # Update el label de la imagen
    label2.config(text="Imagen con Ruido (sal y pimienta)")
    label2.grid(row=1, column=1, padx=5, pady=5)

# Funcion para aplicar ruido gaussiano
def apply_noice_gauss():
    global original_image, gaussian_image, img_label3, MEDIA, SIGMA, label3
    if original_image is None:
        messagebox.showerror("Error", "Por favor, carga la imagen primero.")
        return

    ruido = np.random.normal(MEDIA, SIGMA, original_image.shape).astype(np.uint8)
    salida = cv2.add(original_image, ruido)

    gaussian_image = salida # Guardar la imagen con ruido gaussiano

    # Convertir la imagen a un formato compatible con Tkinter
    img_pil = Image.fromarray(salida)
    img_tk = ImageTk.PhotoImage(img_pil)

    img_label3.config(image=img_tk)
    img_label3.image = img_tk  # Guardar referencia para evitar que se elimine

    # Update el label de la imagen
    label3.config(text="Imagen con Ruido (gaussiano)")
    label3.grid(row=1, column=2, padx=5, pady=5)




# Función para cargar la imagen
def load_image():
    global original_image, img_label1, label1, max_size
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.bmp *.png *.jpg")]
    )
    if file_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            messagebox.showerror("Error", "No se pudo cargar la imagen.")
            return

        altura, ancho = image.shape
        scale_factor = max_size / max(altura, ancho)
        new_width = int(ancho * scale_factor)
        new_height = int(altura * scale_factor)
        image = cv2.resize(image, (new_width, new_height))

        # Convertir la imagen a un formato compatible con Tkinter
        img_pil = Image.fromarray(image)
        img_tk = ImageTk.PhotoImage(img_pil)

        original_image = image
        img_label1.config(image=img_tk)
        img_label1.image = img_tk  # Guardar referencia para evitar que se elimine

        # Update el label de la imagen
        label1.config(text="Imagen Original")
        label1.grid(row=1, column=0, padx=5, pady=5)


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

# Crear un boton para aplicar el ruido de sal y pimienta
btn_s_p = tk.Button(
    button_frame,
    text="Aplicar ruido (sal y pimienta)",
    command=apply_noice_s_p,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_s_p.grid(row=0, column=1, padx=5)

# Crear un botón para aplicar el ruido gaussiano
btn_gauss = tk.Button(
    button_frame,
    text="Aplicar ruido (gaussiano)",
    command=apply_noice_gauss,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_gauss.grid(row=0, column=2, padx=5)

# Crear un botón para aplicar el filtro promedio
btn_p_filter = tk.Button(
    button_frame,
    text="Aplicar filtro promedio (gaussiano)",
    command=apply_filter_average,
    bg="#9C27B0",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_p_filter.grid(row=0, column=3, padx=5)

# Crear un botón para aplicar el filtro promedio pesado
btn_p_h_filter = tk.Button(
    button_frame,
    text="Aplicar filtro promedio pesado (gaussiano)",
    command=apply_filter_average_heavy,
    bg="#FF5722",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_p_h_filter.grid(row=0, column=4, padx=5)

# Crear un botón para aplicar el filtro gaussiano
btn_g_filter = tk.Button(
    button_frame,
    text="Aplicar filtro gaussiano (gaussiano)",
    command=apply_filter_gaussian,
    bg="#FFEB3B",
    fg="black",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_g_filter.grid(row=0, column=5, padx=5)

# Crear un botón para aplicar el filtro de mediana
btn_m_filter = tk.Button(
    button_frame,
    text="Aplicar filtro mediana (sal y pimienta)",
    command=apply_filter_median,
    bg="#8BC34A",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_m_filter.grid(row=1, column=0, padx=5)

# Crear un botón para aplicar el filtro de moda
btn_mode_filter = tk.Button(
    button_frame,
    text="Aplicar filtro moda (sal y pimienta)",
    command=apply_filter_mode,
    bg="#607D8B",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
)
btn_mode_filter.grid(row=1, column=1, padx=5)

# Crear slider para ajustar el valor de umbral
slider_label1 = tk.Label(
    scroll_frame,
    text="Ajustar valor de ruido:",
    bg="#adadad",
    font=("Arial", 10, "bold"),
)
slider_label1.grid(row=0, column=0, padx=5)

slider_ruido_s_p = tk.Scale(
    scroll_frame,
    from_=0.01,
    to=0.50,
    orient=tk.HORIZONTAL,
    bg="#adadad",
    fg="black",
    font=("Arial", 10, "bold"),
    resolution=0.01,
    command=lambda value: update_noise_s_p(float(value)),
)
slider_ruido_s_p.set(RUIDO_SAL_PIMIENTA)  # Establecer el valor inicial del slider
slider_ruido_s_p.grid(row=0, column=1, padx=5)

# Crear slider para ajustar el valor de media
slider_media = tk.Label(
    scroll_frame,
    text="Ajustar valor de media (ruido gaussiano):",
    bg="#adadad",
    font=("Arial", 10, "bold"),
)
slider_media.grid(row=0, column=2, padx=5)

slider_ruido_gauss_media = tk.Scale(
    scroll_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    bg="#adadad",
    fg="black",
    font=("Arial", 10, "bold"),
    resolution=1,
    command=lambda value: update_noise_gauss_media(float(value)),
)
slider_ruido_gauss_media.set(MEDIA)  # Establecer el valor inicial del slider
slider_ruido_gauss_media.grid(row=0, column=3, padx=5)

# Crear slider para ajustar el valor de sigma
slider_sigma = tk.Label(
    scroll_frame,
    text="Ajustar valor de sigma (gaussiano):",
    bg="#adadad",
    font=("Arial", 10, "bold"),
)
slider_sigma.grid(row=0, column=4, padx=5)

slider_ruido_gauss_sigma = tk.Scale(
    scroll_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    bg="#adadad",
    fg="black",
    font=("Arial", 10, "bold"),
    resolution=1,
    command=lambda value: update_noise_gauss_sigma(float(value)),
)
slider_ruido_gauss_sigma.set(SIGMA)  # Establecer el valor inicial del slider
slider_ruido_gauss_sigma.grid(row=0, column=5, padx=5)

# Crear Labels para mostrar las imágenes
img_label1 = tk.Label(image_frame, bg="#adadad")
img_label1.grid(row=0, column=0, padx=5, pady=5)

img_label2 = tk.Label(image_frame, bg="#adadad")
img_label2.grid(row=0, column=1, padx=5, pady=5)

img_label3 = tk.Label(image_frame, bg="#adadad")
img_label3.grid(row=0, column=2, padx=5, pady=5)

# Crear Labels para mostrar los nombres de las imágenes
label1 = tk.Label(image_frame, text="", bg="#adadad", font=("Arial", 10, "bold"))
label1.grid(row=1, column=0, padx=5, pady=5)

label2 = tk.Label(image_frame, text="", bg="#adadad", font=("Arial", 10, "bold"))
label2.grid(row=1, column=1, padx=5, pady=5)

label3 = tk.Label(image_frame, text="", bg="#adadad", font=("Arial", 10, "bold"))
label3.grid(row=1, column=2, padx=5, pady=5)

# Centrar el marco de botones
button_frame.grid_columnconfigure((0, 1, 2), weight=1)

# Centrar el marco de imágenes
image_frame.grid_rowconfigure(0, weight=1)
image_frame.grid_columnconfigure((0, 1, 2), weight=1)

# Iniciar la aplicación
ventana.mainloop()