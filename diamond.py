import numpy as np
import matplotlib.pyplot as plt

# Algoritmo diamante cuadrado
def diamond_square(size, roughness):
    n = size - 1
    terrain = np.zeros((size, size), dtype=float)
    terrain[0, 0] = np.random.uniform(0, 1)
    terrain[0, n] = np.random.uniform(0, 1)
    terrain[n, 0] = np.random.uniform(0, 1)
    terrain[n, n] = np.random.uniform(0, 1)

    step = n
    scale = 1.0

    while step > 1:
        half = step // 2

        for y in range(half, n, step):
            for x in range(half, n, step):
                avg = (terrain[y - half, x - half] + terrain[y - half, x + half] +
                       terrain[y + half, x - half] + terrain[y + half, x + half]) / 4
                terrain[y, x] = avg + np.random.uniform(-scale, scale)

        for y in range(0, n + 1, step):
            for x in range(half, n, step):
                avg = (terrain[y, x - half] + terrain[y, x + half]) / 2
                terrain[y, x] = avg + np.random.uniform(-scale, scale)

        for y in range(half, n, step):
            for x in range(0, n + 1, step):
                avg = (terrain[y - half, x] + terrain[y + half, x]) / 2
                terrain[y, x] = avg + np.random.uniform(-scale, scale)

        step = half
        scale *= roughness

    return terrain


size = 9  # Tamaño de la matriz (debe ser 2^n + 1)
roughness = 0.5 # Rugosidad del terreno

terrain = diamond_square(size, roughness)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(size)
y = np.arange(size)
x, y = np.meshgrid(x, y)

ax.plot_surface(x, y, terrain, cmap='viridis')

plt.show()

