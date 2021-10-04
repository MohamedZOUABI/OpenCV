import cv2
import numpy as np # deal with matrix

print("package imported")

#image
'''
img= cv2.imread("../Resources/MO0jRQ.png")
cv2.imshow("image",img) # image : windowsName 
cv2.waitKey(0) # delay 0 for infinity
'''

#Video
'''
cap = cv2.VideoCapture("../Resources/AhmedZouabi.mp4")

while True:
    sucsess, img = cap.read()
    cv2.imshow("VideoShow",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
'''

#WebCam
cap = cv2.VideoCapture(0) # ID 0 for default camera
cap.set(10,100) # brightness id=10
cap.set(3,640) # Weight id=10
cap.set(4,480) # weight id=10

while True:
    sucsess, img = cap.read()
    cv2.imshow("VideoShow",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
