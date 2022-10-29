import cv2
import numpy as np

img = cv2.imread('vehiculo.jpg')
imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

blueB = np.array([100,50,50], np.uint8)
blueA = np.array([130,255,255], np.uint8)
#blueB = np.array([100,100,20], np.uint8)
#blueA = np.array([125,255,255], np.uint8)

maskBlue1 = cv2.inRange(imgHSV, blueB, blueA)


maskRedVis = cv2.bitwise_and(img, img, mask=maskBlue1)

cv2.imshow('Original', img)
cv2.imshow("maskRed", maskBlue1)
cv2.imshow('maskRojoVis', maskRedVis)

cv2.waitKey(0)
cv2.destroyAllWindows()