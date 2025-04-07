# Importar librerías
import cv2
import numpy as np
import matplotlib.pyplot as plt

THRESHOLD_VALUE = 150  # Valor de umbral para binarización

# ----- 1. Cargar y binarizar la imagen -----
# Cargar imagen en escala de grises
image = cv2.imread('practica1\\Imagenes\\figurasgeometricas.bmp', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen fue cargada correctamente
if image is None:
    print("Error al cargar la imagen.")
    exit()

# Mostrar imagen original
plt.figure(figsize=(6, 6))
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')
plt.show()

# Umbralización para binarizar la imagen
# Se utiliza un valor de umbral fijo para convertir la imagen a binaria
_, binary_image = cv2.threshold(image, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY)
# binary_image = cv2.adaptiveThreshold(
#     image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
# )

out_gaussian = cv2.GaussianBlur(binary_image, (5, 5), 0)

# Invertir la imagen binarizada para obtener la imagen negativa
negative_image = cv2.bitwise_not(out_gaussian)

# Mostrar imagen binarizada
plt.figure(figsize=(6, 6))
plt.imshow(binary_image, cmap='gray')
plt.title('Imagen Binarizada')
plt.axis('off')
plt.show()

plt.figure(figsize=(6, 6))
plt.imshow(out_gaussian, cmap='gray')
plt.title('Imagen Suavizada')
plt.axis('off')
plt.show()

# Mostrar imagen negativa
plt.figure(figsize=(6, 6))
plt.imshow(negative_image, cmap='gray')
plt.title('Imagen Negativa')
plt.axis('off')
plt.show()

# ----- 2. Etiquetado de componentes conexas -----
# Vecindad-4
num_labels1_4, labels1_4 = cv2.connectedComponents(binary_image, connectivity=4)

# Vecindad-8
num_labels1_8, labels1_8 = cv2.connectedComponents(binary_image, connectivity=8)
print(f"Número de objetos detectados con vecindad-4: {num_labels1_4 - 1}")
print(f"Número de objetos detectados con vecindad-8: {num_labels1_8 - 1}")

# Vecindad-4 en imagen negativa
num_labels2_4, labels2_4 = cv2.connectedComponents(negative_image, connectivity=4)

# Vecindad-8 en imagen negativa
num_labels2_8, labels2_8 = cv2.connectedComponents(negative_image, connectivity=8)
print(f"Número de objetos detectados con vecindad-4: {num_labels2_4 - 1}")
print(f"Número de objetos detectados con vecindad-8: {num_labels2_8 - 1}")

# Mostrar resultados de vecindad-4
plt.figure(figsize=(6, 6))
plt.imshow(labels1_4, cmap='jet')
plt.title('Etiquetado con Vecindad-4 (Binarizada)')
plt.colorbar()
plt.axis('off')
plt.show()

# Mostrar resultados de vecindad-8
plt.figure(figsize=(6, 6))
plt.imshow(labels1_8, cmap='jet')
plt.title('Etiquetado con Vecindad-8 (Binarizada)')
plt.colorbar()
plt.axis('off')
plt.show()

# Mostrar resultados de vecindad-4 en imagen negativa
plt.figure(figsize=(6, 6))
plt.imshow(labels2_4, cmap='jet')
plt.title('Etiquetado con Vecindad-4 (Negativa)')
plt.colorbar()
plt.axis('off')
plt.show()

# Mostrar resultados de vecindad-8 en imagen negativa
plt.figure(figsize=(6, 6))
plt.imshow(labels2_8, cmap='jet')
plt.title('Etiquetado con Vecindad-8 (Negativa)')
plt.colorbar()
plt.axis('off')
plt.show()

# ----- 3. Dibujar contornos y numerar los objetos -----
# Convertir imagen binaria a imagen en color para dibujar contornos
image_color = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)

# Encontrar contornos en la imagen
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos y numerar los objetos
for i, contour in enumerate(contours):
    # Dibujar contorno (color verde)
    cv2.drawContours(image_color, [contour], -1, (0, 255, 0), 2)
    # Encontrar el centro del objeto y colocar el número
    x, y, w, h = cv2.boundingRect(contour)
    cv2.putText(image_color, f'{i + 1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,
    255, 0), 2)

# Mostrar la imagen con los contornos y etiquetas
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title('Objetos Detectados y Numerados (Binarizada)')
plt.axis('off')
plt.show()

# Convertir imagen binaria a imagen en color para dibujar contornos en la imagen negativa
image_color = cv2.cvtColor(negative_image, cv2.COLOR_GRAY2BGR)

# Encontrar contornos en la imagen negativa
contours, _ = cv2.findContours(negative_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos y numerar los objetos en la imagen negativa
for i, contour in enumerate(contours):
    # Dibujar contorno (color verde)
    cv2.drawContours(image_color, [contour], -1, (0, 255, 0), 2)
    # Encontrar el centro del objeto y colocar el número
    x, y, w, h = cv2.boundingRect(contour)
    cv2.putText(image_color, f'{i + 1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,
    255, 0), 2)

# Mostrar la imagen con los contornos y etiquetas en la imagen negativa
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title('Objetos Detectados y Numerados (Negativa)')
plt.axis('off')
plt.show()

# ----- 4. Comparación entre vecindad-4 y vecindad-8 -----
# Calcular la diferencia entre el número de etiquetas detectadas
# en la imagen original y la imagen negativa
diferencia = abs(num_labels1_4 - num_labels1_8)
print(f"Diferencia entre vecindad-4 y vecindad-8 (Binarizada): {diferencia}")

diferencia = abs(num_labels2_4 - num_labels2_8)
print(f"Diferencia entre vecindad-4 y vecindad-8 (Negativa): {diferencia}")