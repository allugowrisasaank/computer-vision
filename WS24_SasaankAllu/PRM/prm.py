import cv2
import numpy as np


def bresenham(x1, y1, x2, y2):
    points = [] 
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append([y1, x1])  
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points


o=img = cv2.imread("maze2.png")
o=img=cv2.resize(img, (625, 625))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img=cv2.threshold(img, 70, 255, 0)
cv2.imshow("binary", img)
cv2.waitKey(0)


start=[14,282]
end=[617,280]


height, width=img.shape[:2]


nodes=[]
node_count=0
nc=200


while 1:
    if node_count==nc:
        break
    i=np.random.randint(0, height)
    j=np.random.randint(0,width)
    if img[i,j]>150:
        nodes.append([i,j])
        node_count+=1


nodes.insert(0,start)
nodes.append(end)


k=10
temp=[]
neighbours=[[] for _ in range(nc+2)]


# print(img[458, 516])
# img[458,516]=255

node_count=0
for node in nodes:
    node_count+=1
    neigh_count=0
    max=10000000
    max_ind=-1
    for neigh in nodes:
        if node[0]!=neigh[0] or node[1]!=neigh[1]:
            x1=int(node[1])
            x2=int(neigh[1])
            y1=int(node[0])
            y2=int(neigh[0])
            obst=0
            points=bresenham(x1,y1,x2,y2)
            for point in points:
                if img[point[1], point[0]]==0:
                    obst=1
                    break
            if obst==1:
                continue

            if (x1-x2)**2+(y1-y2)**2<max:
                if neigh_count!=k:
                    neigh_count+=1
                    neighbours[node_count-1].append(neigh)
                    cv2.line(o, node, neigh, (0,0,255), 1)
                else:
                    neighbours[node_count-1][max_ind]=neigh
                    cv2.line(o, node, neigh, (0,0,255), 1)
                max=(x1-x2)**2+(y1-y2)**2
                for count in range(neigh_count):
                    x1=int(node[0])
                    x2=int(neighbours[node_count-1][count][0])
                    y1=int(node[1])
                    y2=int(neighbours[node_count-1][count][1])
                    if (x1-x2)**2+(y1-y2)**2>max:
                        max=(x1-x2)**2+(y1-y2)**2
                        max_ind=count
o[start[0], start[1]]=[0,255,0]
o[end[0], end[1]]=[0,255,0]

cv2.imshow("final", o)
cv2.waitKey(0)


cv2.destroyAllWindows()