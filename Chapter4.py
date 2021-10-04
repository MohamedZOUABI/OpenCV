import cv2
import numpy as np

#********** Shape ********************
img = np.zeros((525,840,3),np.uint8) # zeros is black color || in matrix 525 BY 840
img[100:200,50:500] = 255,255,0 # COLOR 255,255,0 IN 100:200,50:500 SECTION


#********** line ********************
cv2.line(img,(0,0),(300,300),(255,0,0),3)
cv2.rectangle(img,(700,500),(70,50),(102, 102, 153)) #we can add ,cv2.FILLED) to make it all color
cv2.circle(img,(400,300),150,(153, 0, 0),4) #we can add ,cv2.FILLED) to make it all color


#********** line ********************
cv2.putText(img,"OpenCV tuto",(500,200),cv2.FONT_ITALIC,1,(255, 198, 0),3)


cv2.imshow("image",img)
cv2.waitKey(0)