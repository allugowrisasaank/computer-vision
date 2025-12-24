from ctypes import sizeof
import cv2
import numpy as np
import math
import tkinter
A=B=0

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print("Dope")
#         B=x
#         A=y
#         print(A,B)


orig=img=cv2.imread("MAP for BFS.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height,width=img.shape[:2]
for i in range(height):
    for j in range(width):
        if img[i][j]<120:
            img[i][j]=255
        else:
            img[i][j]=0
# cv2.imshow("map", orig)
# cv2.setMouseCallback("map", click_event)
# start=[A, B]
# cv2.setMouseCallback("map", click_event)
# end=[A, B]
# cv2.waitKey(0) 
img1=img
for i in range(1,height-1):
    for j in range(1,width-1):
        if(img1[i-1,j-1]==255 and img1[i,j-1]==255 and img1[i+1,j-1]==255 and img1[i-1,j]==255 and img1[i,j]==255 and img1[i+1,j]==255 and img1[i-1,j+1]==255 and img1[i,j+1]==255 and img1[i+1,j+1]==255):
            img[i,j]=0
graph=[]
for i in range(1,height-1):
    for j in range(1,width-1):
        graph.append([])
        for a in (-1, 0, 1):
            for b in (-1, 0, 1):
                if (a==0 and b==1) or (a==0 and b==-1) or (a==-1 and b==0) or (a==1 and b==-0):
                    if(img[i+a, j+b]==255):
                        graph[(i-1)*(width-2)+(j-1)].append((width)*(i+a)+(j+b))


start=[74,152]
end=[223, 347]


layers=[[]]
count=0
flag=np.zeros((height)*(width))
flag[start[0]*width+start[1]]=1
current_layer=[start]
layers.append(current_layer)
count+=1
found=0
while 1:
    next_layer=[]
    check=0
    for i in current_layer:
        neighbours=graph[(i[0]-1)*(width-2)+i[1]-1]
        for j in neighbours:
            if j==end[0]*width+end[1]:
                found=1
                print("found")
                flag[j]=1
                break

            if flag[j]<0.5:
                next_layer.append([j//width, j%width])
                check=1
                flag[j]=1
        if found==1:
            break
    if found==1:
        break
    if(check==0):
        break
    current_layer=next_layer
    layers.append(current_layer)
    count+=1    
if found==0:
    print("No route")
else:
    orig[i[0], i[1]]=[255,0,0]
    while(count>=0):
        if(end[0]==start[0] and end[1]==start[1]):
            break
        for i in layers[count]:
            check=0
            for j in graph[(end[0]-1)*(width-2)+(end[1]-1)]:
                if i[0]*width+i[1]==j:
                    check=1
                    break
            if check==1:
                orig[i[0], i[1]]=[0,255,0]
                break
        count-=1
        end=[i[0], i[1]]
cv2.imshow("original", orig)
cv2.imshow("map", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

    
