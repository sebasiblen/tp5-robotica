import cv2

img = cv2.imread('vehiculo.jpg')
cv2.imshow("",img)

patente = img[130:170, 90:180]
cv2.imshow("",patente)
cv2.imwrite("patente.png", patente)

cv2.waitKey(0)
cv2.destroyAllWindows()