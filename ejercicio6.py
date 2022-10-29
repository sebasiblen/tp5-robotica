import cv2 as cv

captura = cv.VideoCapture("P.mp4")

while(captura.isOpened()):
    ret,img = captura.read()
    if ret == True:
        fps = 'FPS:  ' + str(int(captura.get(cv.CAP_PROP_FPS)))
        cv.putText(img, fps, (100,50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
        cv.imshow("video", img)
        
        if cv.waitKey(1) == 27:
            break;
    else:
        break;
captura.release()
cv.destroyAllWindows()