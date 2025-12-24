import numpy as np
import cv2
import random
k=4
img=cv2.imread("baboon_k_means.jpg")
# img = cv2.resize(img, (500,500))
height, width=img.shape[:2]
img1=np.zeros((height, width, 3), dtype=np.uint8)
centroids=np.zeros((k,3))
for i in range(k):
    centroids[i]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
cluster_colour=np.zeros((k,3))
count=np.zeros((k))
for i in range(5):
    count=np.zeros((k))
    for i1 in range(height):
        for i2 in range(width):
            min=195077
            ind=-1
            for i3 in range(k):
                if((centroids[i3][0]-int(img[i1][i2][0]))**2+(centroids[i3][1]-int(img[i1][i2][1]))**2+(centroids[i3][2]-int(img[i1][i2][2]))**2<=min):
                    min=(centroids[i3][0]-int(img[i1][i2][0]))**2+(centroids[i3][1]-int(img[i1][i2][1]))**2+(centroids[i3][2]-int(img[i1][i2][2]))**2
                    ind=i3
            count[ind]=count[ind]+1
            cluster_colour[ind][0]=cluster_colour[ind][0]+int(img[i1][i2][0])
            cluster_colour[ind][1]=cluster_colour[ind][1]+int(img[i1][i2][1])
            cluster_colour[ind][2]=cluster_colour[ind][2]+int(img[i1][i2][2])
    for i3 in range(k):
        if(count[i3]!=0):
            centroids[i3]=cluster_colour[i3]/count[i3]
        else:
            centroids[i3]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    cluster_colour=np.zeros((k,3))
for i1 in range(height):
    for i2 in range(width):
        min=195077
        ind=-1
        for i3 in range(k):
            if((centroids[i3][0]-int(img[i1][i2][0]))**2+(centroids[i3][1]-int(img[i1][i2][1]))**2+(centroids[i3][2]-int(img[i1][i2][2]))**2<=min):
                min=(centroids[i3][0]-int(img[i1][i2][0]))**2+(centroids[i3][1]-int(img[i1][i2][1]))**2+(centroids[i3][2]-int(img[i1][i2][2]))**2
                ind=i3
        img1[i1][i2][0]=centroids[ind][0]=int(centroids[ind][0])
        img1[i1][i2][1]=centroids[ind][1]=int(centroids[ind][1])
        img1[i1][i2][2]=centroids[ind][2]=int(centroids[ind][2])
print(centroids)
cv2.imshow("before", img)
cv2.imshow("segment", img1)
cv2.waitKey(0)
            


