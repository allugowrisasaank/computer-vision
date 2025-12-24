import numpy as np
import cv2
import random
import math

img = cv2.imread('maze_image.jpg')
img = cv2.resize(img, (500,500) )
img = cv2.GaussianBlur(img, (5, 5), 0) 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img1 = np.full((500,500), 0, dtype = np.uint8)
img2 = np.full((500,500), 0, dtype = np.uint8)
for i in range(500):#path  possible
    for j in range(500):
        if img[i][j] <150:
            img1[i][j] = 0
        else:
            img1[i][j] = 255
# cv2.imshow("Image", img)
cv2.imshow("path", img1) 

# for i in range(2, 498):
#     for j in range(2, 498):
#         if (i%100 == 0) or (j%100==0):
#             for k in range (-2,3):
#                 for l in range (-2, 3):
#                     img1[i+k][j+l] = 255
        

# cv2.imshow("p", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

n=5
#n*n matrix
adj_list=[[] for _ in range(n*n)]
for i in range(n):
    for j in range(n):
        x=(2*j+1)*250/n
        y=(2*i+1)*250/n
        # print(x, y)
        while 1:
            if x==(2*j+3)*250/n or x==499:
                break
            x=x+1
            if img1[int(y)][int(x)]==255:
                break
        if x==(2*j+3)*250/n:
            adj_list[i*n+j].append(i*n+(j+1))
        x=(2*j+1)*250/n
        y=(2*i+1)*250/n
        while 1:
            if x==(2*j-1)*250/n or x==1:
                break
            x=x-1
            if img1[int(y)][int(x)]==255:
                break
        if x==(2*j-1)*250/n:
            adj_list[i*n+j].append(i*n+j-1)
        x=(2*j+1)*250/n
        y=(2*i+1)*250/n
        while 1:
            if y==(2*i+3)*250/n or y==499:
                break
            y=y+1
            if img1[int(y)][int(x)]==255:
                break
        if y==(2*i+3)*250/n:
            adj_list[i*n+j].append((i+1)*n+j)
        x=(2*j+1)*250/n
        y=(2*i+1)*250/n
        while 1:
            if y==(2*i-1)*250/n or y==1:
                break
            y=y-1
            if img1[int(y)][int(x)]==255:
                break
        if y==(2*i-1)*250/n:
            adj_list[i*n+j].append(j+(i-1)*n)
A = adj_list

lis = [0 for _ in range (n**2)]
# print(lis)
# print(A)
end =14
c = 10
que = [c]
que1 = []
que1label = [-1]
print("BFS")
while(len(que)):
    c = que[0]
    if( c== end):
        
        que1.append(end)
        break
    
    lis[c] = 1
    for i in range(len(A[c])):
        t = A[c][i]
        if lis[t] == 0:
            que1label.append(c)
            que.append(t)
            lis[t] =1
    
    que1.append(c)
    
    que.remove(c)
print(que1)
print("LABELS")
que1label.pop()

print(que1label)
quefinal = []
c = end
while(1):
    quefinal.append(c)
    i = que1.index(c)
    c1 = que1label[i]
    if c1 == -1:
        break
    c = c1

quefinal.reverse()
print('FINAl:', quefinal)