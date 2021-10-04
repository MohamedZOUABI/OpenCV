import cv2

img = cv2.imread("../Resources/MO0jRQ.png")
print(img.shape)

#********* Resize **************

imgResize = cv2.resize(img,(840,525))
cv2.imshow("image resize", imgResize)
#cv2.waitKey(0)

#********* Croppe **************

imgCropped = imgResize[200:400,100:250]
cv2.imshow("image cropped", imgCropped)
cv2.waitKey(0)