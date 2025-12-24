import numpy as np
import cv2

img =cv2.imread("pngtree-winter-scenery-aesthetic-snow-mountain-creative-book-cover-image_711481.webp")
cv2.imshow("window", img)
cv2.waitKey(5000)
print(img[10,10])
height, width = img.shape[:2]
for i in range(height):
    for j in range(width):
        a,b,c=int(img[i,j])
        if((a+b+c)/3>255/10):
            img[i,j]=[255,255,255]
        else:
            img[i,j]=[0,0,0]
cv2.destroyAllWindows()
cv2.imshow("binary", img)
cv2.waitKey(0)



