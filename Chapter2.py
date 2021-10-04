import cv2
import numpy as np

#******************** someFn(Blur,graycolor,Canny,Dialition,Eroded) *******************

img= cv2.imread("../Resources/MO0jRQ.png")
kernel = np.ones((5,5),np.uint8) # we want all the values to be one and the size of matrix (5,5)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(111,111),0) # (111,111) : PERCENTAGE OF BLUR & MUST BE ODD NUMBER || 0 IS SIGMA IDICATOR
imgCanny = cv2.Canny(img,150,200)
imgDialiation = cv2.dilate(img,kernel, iterations=5)
imgEroded = cv2.erode(img,kernel,iterations=5) #Eroded is the opposide of Dialiation

cv2.imshow("Blur image",imgBlur)
cv2.imshow("Gray image", imgGray)
cv2.imshow("canny image", imgCanny)
cv2.imshow("Dialited image", imgDialiation)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0) # delay 0 for infinity OR can be 1000 milisecond