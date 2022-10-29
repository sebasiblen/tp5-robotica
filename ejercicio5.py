import cv2

vc = cv2.VideoCapture(0)

if vc.isOpened(): # intenta obtener el primer frame 
    rval, frames = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("En VIVO", frames)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: #  ESC para salir
        break

vc.release()
cv2.destroyAllWindows()