# Codigo para extrar manualmente las posiciones de las esquinas de la cancha

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Variable global para almacenar los puntos seleccionados
points = []

# Callback de ratón para obtener los puntos
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        points.append((int(event.xdata), int(event.ydata)))
        plt.plot(event.xdata, event.ydata, 'ro')
        plt.draw()

# Cargar la imagen
image = cv2.imread('../utils/cancha-base.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots()
ax.imshow(image_rgb)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

print("Seleccione las cuatro esquinas de la cancha y cierre la ventana cuando haya terminado.")
plt.show()

print("Puntos seleccionados:", points)
