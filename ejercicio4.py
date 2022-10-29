import cv2

img = cv2.imread('ruta.jpg')

bordes = cv2.Canny(img,340,890)
bordes = cv2.dilate(bordes, None, iterations=1)
bordes = cv2.erode(bordes,None,iterations=1)

c,j = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, c, -1, (255,0,250),2)
cv2.putText(img,'Alerta al Conductor', (250,200), cv2.FONT_HERSHEY_COMPLEX, 1, (124,252,0), 2)
cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

