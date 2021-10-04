import cv2
import numpy as np

#WebCam
cap = cv2.VideoCapture(0) # ID 0 for default camera
cap.set(10,150) # brightness id=10
cap.set(3,640) # Weight id=10
cap.set(4,480) # weight id=10

#***  define list max min of hue
myColors = [[103,101,38,137,255,255],
            [47,53,75,98,219,255],
            [0,141,0,26,255,255]]

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)  # -1 for draw all the contours
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
        #cv2.imshow(str(color[0]),mask)

while True:
    sucsess, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors)
    cv2.imshow("VideoShow",imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

