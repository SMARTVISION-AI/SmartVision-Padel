import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_homography(image_path):
    # Cargar la imagen
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image at path {image_path} not found.")
    
    # Puntos de la imagen original (cuatro esquinas de la cancha en la imagen)
    # Se obtienen con el script get_points.py
    pts_src = np.array([
        [407, 198],  # esquina superior izquierda
        [937, 198],  # esquina superior derecha
        [1220, 657],  # esquina inferior derecha
        [133, 651]  # esquina inferior izquierda
    ])

    # Puntos de destino (donde queremos mapear los puntos de la imagen original)
    pts_dst = np.array([
        [0, 0],      # esquina superior izquierda
        [300, 0],    # esquina superior derecha
        [300, 400],  # esquina inferior derecha
        [0, 400]     # esquina inferior izquierda
    ])

    output_size = (300, 400)  # Tamaño de la imagen transformada

    # Calcular la matriz de homografía
    h, status = cv2.findHomography(pts_src, pts_dst)
    if h is None:
        raise ValueError("Error calculating homography matrix.")

    # Aplicar la homografía a la imagen
    img_out = cv2.warpPerspective(img, h, output_size)

    # Mostrar la imagen original y la transformada
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Transformada')
    plt.show()

    return img_out
