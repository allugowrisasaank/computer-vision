import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def convert_to_pencil_sketch(frame):
    img=frame
    img=cv2.GaussianBlur(img, (3, 3), 0)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height,width=img.shape[:2]
    threshold=25


    def minmax(canny):
        min=max=canny[1,1]
        for i in range(1,height-1):
            for j in range(1,width-1):
                if canny[i,j]>max:
                    max=canny[i,j]
                if canny[i,j]<min:
                    min=canny[i,j]
        return min,max


    sobelx1=np.zeros((height,width))
    sobely1=np.zeros((height,width))


    for i in range(1,height-1):
        for j in range(1,width-1):
            a=int(img[i-1,j+1])
            a1=int(img[i-1,j-1])
            b=int(img[i,j+1])
            b1=int(img[i,j-1])
            c=int(img[i+1,j+1])
            c1=int(img[i+1,j-1])
            sobelx1[i,j]=a-a1+2*(b-b1)+c-c1


    for i in range(1,height-1):
        for j in range(1,width-1):
            a=int(img[i+1,j+1])
            a1=int(img[i-1,j+1])
            b=int(img[i+1,j])
            b1=int(img[i-1,j])
            c=int(img[i+1,j-1])
            c1=int(img[i-1,j-1])
            sobely1[i,j]=a-a1+2*(b-b1)+c-c1

            
    sobel1=np.zeros((height,width))


    for i in range(1,height-1):
        for j in range(1,width-1):
            sobel1[i,j]=math.sqrt(sobelx1[i,j]**2+sobely1[i,j]**2)


    canny1=np.zeros((height, width), dtype=np.uint8)


    for i in range(2,height-2):
        for j in range(2,width-2):
            if(sobelx1[i,j]>0):
                if(sobely1[i,j]>0):
                    if(sobel1[i,j]>sobel1[i+1, j-1] and sobel1[i,j]>sobel1[i-1, j+1]):
                        if(sobel1[i,j]>threshold):
                            canny1[i,j]=255
                else:
                    if(sobely1[i,j]==0):
                        if(sobel1[i,j]>sobel1[i,j-1] and sobel1[i,j]>sobel1[i,j+1]):
                            if(sobel1[i,j]>threshold):
                                canny1[i,j]=255
                    else:
                        if(sobel1[i,j]>sobel1[i+1, j+1] and sobel1[i,j]>sobel1[i-1,j-1]):
                            if(sobel1[i,j]>threshold):
                                canny1[i,j]=255
            else:
                if(sobelx1[i,j]==0):
                    if(sobel1[i,j]>sobel1[i-1,j] and sobel1[i,j]>sobel1[i+1, j]):
                        if(sobel1[i,j]>threshold):
                            canny1[i,j]=255
                else:
                    if(sobely1[i,j]<0):
                        if(sobel1[i,j]>sobel1[i+1, j-1] and sobel1[i,j]>sobel1[i-1, j+1]):
                            if(sobel1[i,j]>threshold):
                                canny1[i,j]=255
                    else:
                        if(sobely1[i,j]==0):
                            if(sobel1[i,j]>sobel1[i,j-1] and sobel1[i,j]>sobel1[i,j+1]):
                                if(sobel1[i,j]>threshold):
                                    canny1[i,j]=255
                        else:
                            if(sobel1[i,j]>sobel1[i+1, j+1] and sobel1[i,j]>sobel1[i-1,j-1]):
                                if(sobel1[i,j]>threshold):
                                    canny1[i,j]=255
    for i in range(height):
        for j in range(width):            #for black pen on white backdrop
            canny1[i][j]=255-canny1[i][j]
    return canny1

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
while(1):
    ret, frame=cap.read()
    if not ret:
        print("Failed to capture image")
        break
    cv2.imshow('pencil', convert_to_pencil_sketch(frame))
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

