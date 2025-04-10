import numpy as np
import matplotlib.pyplot as plt
#Creación de constantes que indican el rango del valor de los pixeles 
max_val = 100
gamma = 0.2

#Se crea una matriz de 10x10
matriz = np.random.randint(0, max_val + 1, size=(10, 10))

#Se inicializa la matriz con la corrección gamma y se le aplica la formula
matriz_trans = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        matriz_trans[i][j] = round(max_val * ((matriz[i][j] / max_val) ** gamma))

# Crear una figura con 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(matriz, cmap='gray')
axes[0].axis('off')
axes[0].set_title("Matriz original")

# Imagen con corrección gamma
axes[1].imshow(matriz_trans, cmap='gray')
axes[1].axis('off')
axes[1].set_title(f"Matriz con la corrección gamma de {gamma}")

# Mostrar ambas imágenes juntas
plt.tight_layout()
plt.show()

# Imprimir matrices
print("Matriz original:")
print(matriz)
print("\nMatriz con corrección gamma:")
print(matriz_trans)
