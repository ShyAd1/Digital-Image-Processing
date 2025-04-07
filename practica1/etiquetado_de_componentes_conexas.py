import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Variables globales
original_image = None
binary_image = None
negative_image = None
gaussian_binary_image = None
gaussian_negative_image = None
THRESHOLD_VALUE = 100  # Valor de umbral inicial

def load_image():
    global original_image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.bmp *.png *.jpg")])
    if file_path:
        original_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if original_image is None:
            messagebox.showerror("Error", "No se pudo cargar la imagen.")
            return
        plt.figure(figsize=(6, 6))
        plt.imshow(original_image, cmap='gray')
        plt.title('Imagen Original')
        plt.axis('off')
        plt.show()

def process_connectivity_and_contours(image, title_prefix):
    # Conectividad 4
    num_labels_4, labels_4 = cv2.connectedComponents(image, connectivity=4)
    num_objects_4 = num_labels_4 - 1
    print(f"Número de objetos detectados con vecindad-4 ({title_prefix}): {num_objects_4}")
    messagebox.showinfo(f"Conectividad 4 ({title_prefix})", 
                        f"Número de objetos detectados con vecindad-4 ({title_prefix}): {num_objects_4}")
    plt.figure(figsize=(6, 6))
    plt.imshow(labels_4, cmap='jet')
    plt.title(f'Etiquetado con Vecindad-4 ({title_prefix})')
    plt.colorbar()
    plt.axis('off')
    plt.show()

    # Conectividad 8
    num_labels_8, labels_8 = cv2.connectedComponents(image, connectivity=8)
    num_objects_8 = num_labels_8 - 1
    print(f"Número de objetos detectados con vecindad-8 ({title_prefix}): {num_objects_8}")
    messagebox.showinfo(f"Conectividad 8 ({title_prefix})", 
                        f"Número de objetos detectados con vecindad-8 ({title_prefix}): {num_objects_8}")
    plt.figure(figsize=(6, 6))
    plt.imshow(labels_8, cmap='jet')
    plt.title(f'Etiquetado con Vecindad-8 ({title_prefix})')
    plt.colorbar()
    plt.axis('off')
    plt.show()

    # Diferencia
    diferencia = abs(num_labels_4 - num_labels_8)
    print(f"Diferencia entre vecindad-4 y vecindad-8 ({title_prefix}): {diferencia}")
    messagebox.showinfo(f"Diferencia de Conectividades ({title_prefix})", 
                        f"Diferencia entre vecindad-4 y vecindad-8 ({title_prefix}): {diferencia}")

    # Contornos
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv2.drawContours(image_color, [contour], -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(image_color, f'{i + 1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
    plt.title(f'Objetos Detectados y Numerados ({title_prefix})')
    plt.axis('off')
    plt.show()

def binarize_image():
    global original_image, binary_image, negative_image
    if original_image is None:
        messagebox.showwarning("Advertencia", "Primero carga una imagen.")
        return
    # Binarización
    _, binary_image = cv2.threshold(original_image, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    plt.figure(figsize=(6, 6))
    plt.imshow(binary_image, cmap='gray')
    plt.title('Imagen Binarizada')
    plt.axis('off')
    plt.show()

    # Negativa
    negative_image = cv2.bitwise_not(binary_image)
    plt.figure(figsize=(6, 6))
    plt.imshow(negative_image, cmap='gray')
    plt.title('Imagen Negativa (desde Binarizada)')
    plt.axis('off')
    plt.show()

    # Procesar conectividad y contornos para ambas
    process_connectivity_and_contours(binary_image, "Binarizada")
    process_connectivity_and_contours(negative_image, "Negativa desde Binarizada")

def apply_gaussian_blur():
    global original_image, gaussian_binary_image, gaussian_negative_image
    if original_image is None:
        messagebox.showwarning("Advertencia", "Primero carga una imagen.")
        return
    # GaussianBlur y binarización
    gaussian_image = cv2.GaussianBlur(original_image, (5, 5), 0)
    _, gaussian_binary_image = cv2.threshold(gaussian_image, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
    plt.figure(figsize=(6, 6))
    plt.imshow(gaussian_binary_image, cmap='gray')
    plt.title('Imagen Binarizada con GaussianBlur')
    plt.axis('off')
    plt.show()

    # Negativa
    gaussian_negative_image = cv2.bitwise_not(gaussian_binary_image)
    plt.figure(figsize=(6, 6))
    plt.imshow(gaussian_negative_image, cmap='gray')
    plt.title('Imagen Negativa (desde GaussianBlur)')
    plt.axis('off')
    plt.show()

    # Procesar conectividad y contornos para ambas
    process_connectivity_and_contours(gaussian_binary_image, "GaussianBlur + Binarizada")
    process_connectivity_and_contours(gaussian_negative_image, "Negativa desde GaussianBlur")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesamiento de Imágenes - Etiquetado de Componentes")
ventana.geometry("600x200")
ventana.configure(bg="#f0f0f0")

# Marco para los botones (centrado en la parte superior)
button_frame = tk.Frame(ventana, bg="#f0f0f0")
button_frame.pack(pady=20)

# Botones centrados
btn_load = tk.Button(button_frame, text="Cargar Imagen", command=load_image, 
                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
btn_load.grid(row=0, column=0, padx=5)

btn_binarize = tk.Button(button_frame, text="Binarizar", command=binarize_image, 
                         bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
btn_binarize.grid(row=0, column=1, padx=5)

btn_gaussian = tk.Button(button_frame, text="GaussianBlur + Binarizar", command=apply_gaussian_blur, 
                         bg="#FF9800", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
btn_gaussian.grid(row=0, column=2, padx=5)

# Centrar el marco de botones
button_frame.grid_columnconfigure((0, 1, 2), weight=1)

# Iniciar la aplicación
ventana.mainloop()