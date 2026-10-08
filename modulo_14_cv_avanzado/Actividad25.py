import cv2

# 1 Cargar imagen
Img = cv2.imread('modulo_14_cv_avanzado/piezas_industriales.jpg')
print("Imagen convertida  BGA", Img.shape)

# 2 Convertir en escalas de grises

imgGris = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
print("Imagen en escala de grises:", imgGris.shape)

# 3 Umbralizacion (tresholding)

_, binarizar = cv2.threshold(imgGris, 200, 255, cv2.THRESH_BINARY)

# 4 Detectar los contornos  (Canny)

contornos, _ = cv2.findContours(binarizar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5 Recorrer contornos y dibujar bounding boxes
objetos_detectados = 0
for c in contornos:
    area = cv2.contourArea(c)
    if area > 500:
        x,y,w,h= cv2.boundingRect(c)
        cv2.rectangle(Img, (x,y), (x+w, y+h), (0,255,0),3)
        objetos_detectados +=1

print(f"Total de objetos detectados: {objetos_detectados}")
cv2.imwrite('modulo_14_cv_avanzado/objetos_encontrados.jpg', Img)
