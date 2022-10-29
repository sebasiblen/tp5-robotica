import cv2

img = cv2.imread('cara_dado.png',0)

bordes = cv2.Canny(img, 100,500)
bordes = cv2.dilate(bordes, None, iterations=1)
bordes = cv2.erode(bordes, None, iterations=1)

# contorno
contorno, jerarq = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contorno, -1, (0,0,0),2)

cv2.imshow("dados",img)

cv2.waitKey(0)
cv2.destroyAllWindows()