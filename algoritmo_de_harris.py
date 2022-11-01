!wget https://raw.githubusercontent.com/DRMiguelAR/UP_Interpretacion/master/orillas/figura1.png

import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy import pi, floor, cos, sin, sqrt, zeros


figuras = cv2.imread("figura1.png", 0)
plt.title("Imagen Original") 
plt.imshow(figuras)
plt.show()

s_x = cv2.Sobel(figuras, cv2.CV_16S, 1, 0)  
s_y = cv2.Sobel(figuras, cv2.CV_64F, 0, 1)

sobel_x = cv2.convertScaleAbs(s_x)
sobel_y = cv2.convertScaleAbs(s_y)

plt.title("Gradiente X") 
plt.imshow(sobel_x)  
plt.show()

plt.title("Gradiente Y") 
plt.imshow(sobel_y)
plt.show()

M = [[[[0,0], [0,0]]]*width for j in range (height)]
for i in range(height):
  for j in range(width):
    aux = np.zeros((2,2))
    for u in range (i-2,(i+3)):
      for v in range (j-2,(j+3)):
        u%=height
        v%=width
        aux+=momentos[u][v]
    M[i][j] = aux

esquinas = np.zeros((height, width))
for i in range (height):
  for j in range(width):
    esquinas[i][j] = np.linalg.det(M[i][j])-np.trace(M[i][j])**2

plt.imshow(esquinas)

R= np.zeros((height,width))
for i in range(height):
    for j in range(width):
        aux= M[i][j]
        determinante= np.linalg.det(aux)
        traza = np.trace(aux)
        k=0.04
        R[i][j]= determinante- k*traza**2

maximo=np.max(R)
umbral= 0.02*maximo
esquinas= np.zeros((height,width))
for i in range(height):
    for j in range(width):
        if R[i,j]> umbral:
            esquinas[i,j]=1
esquinas[120:130, 210:220]
plt.imshow(esquinas)
