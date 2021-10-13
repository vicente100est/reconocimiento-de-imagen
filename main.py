from cv2 import cv2
readimg=cv2.imread('contorno.jpg')
grises=cv2.cvtColor(readimg,cv2.COLOR_BGR2GRAY)
_,umbral=cv2.threshold(grises,16,255,cv2.THRESH_BINARY)
contornos,jerarquia = cv2.findContours(umbral, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(readimg,contornos,-1,(245, 245, 245),3)

#Salida de data
cv2.imshow('lEYENDO IMAGEN EN ORIGINA',readimg)
#cv2.imshow('LEYENDO IMAGEN EN GRISES', grises)
#cv2.imshow('LEYENDO UMBRAL', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()