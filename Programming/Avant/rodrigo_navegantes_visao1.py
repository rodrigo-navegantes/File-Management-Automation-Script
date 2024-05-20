import cv2
import numpy as np
from matplotlib import pyplot as plt

#Importamos as imagens  e convertemos a imagem de referência para grayscale
img = cv2.imread('ref.png')
template = cv2.imread('waldo.png',0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Obtemos a largura e altura da imagem de referência
w, h = template.shape[::-1]

#Esta função retorna outra imagem(array 2d) com cada entrada(pixel) representando a porcentagem de semelhanca a imagem que estamos buscando
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

#O array 2d loc são todas as pixels em que a semelhança é superior à 60%
threshold = 0.6
loc = np.where( res >= threshold)

#Desenha um retangulo sobre a região e exibe a imagem
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
cv2.imshow('Waldo Detectado!', img)

#Garante que a imagem será fechada corretamente após o usuário apertar uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

