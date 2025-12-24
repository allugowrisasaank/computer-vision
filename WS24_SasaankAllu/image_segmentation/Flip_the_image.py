import numpy as np
import cv2

img =cv2.imread("pngtree-winter-scenery-aesthetic-snow-mountain-creative-book-cover-image_711481.webp")
cv2.imshow("window", img)
cv2.waitKey(5000)
height, width = img.shape[:2]
img_rot = np.full((width,height, 3), (0,0,0), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        img_rot[j,height-i-1]=img[i,j]
        cv2.destroyAllWindows()
cv2.imshow("window", img_rot)
cv2.waitKey(0)
