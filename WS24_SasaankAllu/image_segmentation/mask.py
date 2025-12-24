import numpy as np
import cv2
img=cv2.imread("coin.jpg")
cv2.imshow("No Mask", img)
cv2.waitKey(0)
height, width=img.shape[:2]
threshold=10
for i in range(height):
    for j in range(width):
        if(img[i,j,0]>threshold and img[i,j,1]>threshold and img[i,j,2]>threshold):
            img[i,j]=[255,255,255]
cv2.imshow("Mask", img)
cv2.waitKey(0)
cv2.destroyAllWindows()