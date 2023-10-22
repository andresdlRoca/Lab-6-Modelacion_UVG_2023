"""
Generación de Fractales usando el Sistema Iterativo de Funciones (IFS) propuesto por M. Barnsley

Teoría:
El método IFS de Barnsley se basa en la idea de construir un fractal a través de la aplicación iterativa
de transformaciones afines sobre un punto inicial. Cada transformación se elige aleatoriamente de un conjunto
de funciones posibles. Con el tiempo, al aplicar estas transformaciones repetidamente, se forma un fractal.

Pasos del método:
1. Comenzar con un punto inicial p.
2. Elegir aleatoriamente una función de transformación del conjunto de funciones.
3. Aplicar la función elegida al punto para obtener un nuevo punto.
4. Dibujar el nuevo punto.
5. Repetir los pasos 2-4 un gran número de veces.

En este código, usamos dos funciones de transformación definidas como:
f1(x, y) = (1/2 * (x - y), 1/2 * (x + y))
f2(x, y) = (1/2 * (-x - y) + 1, 1/2 * (x - y))

Ejecución:
Al correr este código, se generará y mostrará un fractal basado en las funciones f1 y f2.

"""

import numpy as np
import matplotlib.pyplot as plt

# Define las funciones f1 y f2
def f1(x, y):
    return (0.5*(x - y), 0.5*(x + y))

def f2(x, y):
    return (0.5*(-x - y) + 1, 0.5*(x - y))

# Inicializa el punto de partida
x, y = [0.5], [0.5]

# Número de iteraciones
num_iterations = 100000

# Genera los puntos usando las funciones
for _ in range(num_iterations):
    # Elige aleatoriamente entre f1 y f2
    choice = np.random.choice([f1, f2])
    
    new_x, new_y = choice(x[-1], y[-1])
    x.append(new_x)
    y.append(new_y)

# Dibuja el fractal
plt.figure(figsize=(10, 10))
plt.scatter(x, y, s=0.1, color='black')
plt.title("Fractal con Funciones Corregidas")
plt.axis('off')
plt.tight_layout()

# Guarda la figura si es necesario
# plt.savefig("final_fractal_graph.png")

plt.show()
