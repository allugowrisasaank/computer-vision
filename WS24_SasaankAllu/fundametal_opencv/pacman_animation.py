import cv2
import numpy as np
window=np.zeros((500,500, 3), dtype=np.uint8)
cv2.circle(window, (250,250), 30, (255, 0,0), -1)

while (1):
    break
cv2.imshow("window", window)
cv2.waitKey(0)