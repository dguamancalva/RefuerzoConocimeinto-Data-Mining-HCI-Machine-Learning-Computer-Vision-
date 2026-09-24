import cv2
import numpy as np


#Converitr imagen a BGR
cargaImg = cv2.imread('modulo_11_computer_vision/figuras.jpg')
print("DImensiones de la imagen BGR (3D): ", cargaImg.shape)

# Convertir a escala de grises

imagenGris = cv2.cvtColor(cargaImg, cv2.COLOR_BGR2GRAY)
print("Dimensiones en escala de grises (2D): ", imagenGris.shape)

# Umbralización (Thresholding)

_, binarizada = cv2.threshold(imagenGris, 200, 255, cv2.THRESH_BINARY_INV)

#Deteccion de bordes Canny

bordes = cv2.Canny(imagenGris, 100, 200)

# Guardar imagenes procesadas

cv2.imwrite('modulo_11_computer_vision/figuras_grises.jpg', imagenGris)
cv2.imwrite('modulo_11_computer_vision/figuras_bordes.jpg', bordes)

print("Imagenes procesadas y guardas con exito")