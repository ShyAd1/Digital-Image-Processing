import numpy as np
import matplotlib.pyplot as plt
import cv2

max_val = 255
gamma = 0.5

# Carga de la imagen y pasarla a escala de grises
image = cv2.imread(
    "C:\\Users\\adhev\\Documents\\GitHub\\Digital-Image-Processing\\practica2\\Trafico.jpg",
    cv2.IMREAD_GRAYSCALE,
)
# Verificar si la imagen fue cargada correctamente
if image is None:
    print("Error al cargar la imagen.")
    exit()

# Obtener dimensiones
alto, ancho = image.shape

matriz_trans = [[0 for _ in range(ancho)] for _ in range(alto)]
# Convertir matriz_trans a un arreglo numpy para aplanar y sea compatible con ciertas funciones
matriz_trans = np.array(matriz_trans)
for i in range(alto):
    for j in range(ancho):
        pixel = image[i, j]  # Obtener el valor del píxel original
        matriz_trans[i][j] = round(max_val * ((pixel / max_val) ** gamma))

# Crear una figura con 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(image, cmap="gray")
axes[0].axis("off")
axes[0].set_title("Matriz original")

# Imagen con corrección gamma
axes[1].imshow(matriz_trans, cmap="gray")
axes[1].axis("off")
axes[1].set_title(f"Matriz con la corrección gamma de {gamma}")

# Mostrar ambas imágenes juntas
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].hist(image.ravel(), bins=256, range=(0, 256), color="blue")
axes[0].set_xlabel("Valor de intensidad")
axes[0].set_ylabel("Número de píxeles")
axes[0].set_title("Histograma de la imagen original")

axes[1].hist(matriz_trans.ravel(), bins=256, range=(0, 256), color="blue")
axes[1].set_xlabel("Valor de intensidad")
axes[1].set_ylabel("Número de píxeles")
axes[1].set_title("Histograma de la imagen con corrección gamma")

plt.tight_layout()
plt.show()
