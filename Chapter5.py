import cv2
import numpy as np

img = cv2.imread("../Resources/perspective.jpg")

wight,height = 750,500
pts1 = np.float32([[241,135],[900,320],[310,780],[1045,720]])
pts2 = np.float32([[0,0],[wight,0],[0,height],[wight,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(wight,height))

cv2.imshow("image" , img)
cv2.imshow("image OutPut" , imgOutput)

cv2.waitKey(0)
