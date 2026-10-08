import cv2

# 1. Cargar imagen BGR
Img = cv2.imread('modulo_14_cv_avanzado/piezas_industriales.jpg')

# 2. Escala de grises
imgGris = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)

# 3. Umbralización normal (sin invertir)
_, binarizar = cv2.threshold(imgGris, 100, 255, cv2.THRESH_BINARY)

# 4. Detectar contornos
contornos, _ = cv2.findContours(binarizar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. Dibujar caja delimitadora (Bounding Box) en CADA objeto
objetos_detectados = 0
for c in contornos:
    area = cv2.contourArea(c)
    if area > 500:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(Img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        objetos_detectados += 1

print(f"Total de objetos detectados: {objetos_detectados}")
cv2.imwrite('modulo_14_cv_avanzado/objetos_encontrados.jpg', Img)
