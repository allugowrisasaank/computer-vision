import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
img=cv2.imread("chill_guy.webp")
img = cv2.GaussianBlur(img, (3, 3), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height,width=img.shape[:2]
t=10


def minmax(sobel):
    min=max=sobel[1,1]
    for i in range(1,height-1):
        for j in range(1,width-1):
            if sobel[i,j]>max:
                max=sobel[i,j]
            if sobel[i,j]<min:
                min=sobel[i,j]
    return min,max
sobelx1=np.zeros((height,width))
sobelx=np.zeros((height,width), dtype=np.uint8)
sobely1=np.zeros((height,width))
sobely=np.zeros((height,width), dtype=np.uint8)


for i in range(1,height-1):
    for j in range(1,width-1):
        a=int(img[i-1,j+1])
        a1=int(img[i-1,j-1])
        b=int(img[i,j+1])
        b1=int(img[i,j-1])
        c=int(img[i+1,j+1])
        c1=int(img[i+1,j-1])
        sobelx1[i,j]=a-a1+2*(b-b1)+c-c1
        
min,max=minmax(sobelx1)

for i in range(1,height-1):
    for j in range(1,width-1):
        sobelx[i,j]=int(255*(sobelx1[i,j]-min)/(max-min))


for i in range(1,height-1):
    for j in range(1,width-1):
        a=int(img[i+1,j+1])
        a1=int(img[i-1,j+1])
        b=int(img[i+1,j])
        b1=int(img[i-1,j])
        c=int(img[i+1,j-1])
        c1=int(img[i-1,j-1])
        sobely1[i,j]=a-a1+2*(b-b1)+c-c1

min,max=minmax(sobely1)

for i in range(1,height-1):
    for j in range(1,width-1):
        sobely[i,j]=int(255*(sobely1[i,j]-min)/(max-min))
        
sobel=np.zeros((height,width), dtype=np.uint8)
sobel1=np.zeros((height,width))


for i in range(1,height-1):
    for j in range(1,width-1):
        sobel1[i,j]=math.sqrt(sobelx1[i,j]**2+sobely1[i,j]**2)
min,max=minmax(sobel1)
for i in range(1,height-1):
    for j in range(1,width-1):
        x=int(255*(sobel1[i,j]-min)/(max-min))
        if(x>100):
                sobel[i,j]=int(255*(sobel1[i,j]-min)/(max-min))
cv2.imshow("sobel", sobel)
cv2.waitKey(0)
plt.subplot(221), plt.imshow(img)
plt.subplot(222), plt.imshow(sobelx)
plt.subplot(223), plt.imshow(sobely)
plt.subplot(224), plt.imshow(sobel)
plt.show()