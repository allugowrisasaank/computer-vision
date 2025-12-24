arr=[[2,3],[1,3,4],[1,2,4,5],[2,5,6],[3,4],[4]]
flag=[1,0,0,0,0,0]
current=0
parent=[0,0,0,0,0,0]
neighbours=arr[current]
while 1:
    check=0
    for i in neighbours:
        if(flag[i-1]==0):
            print(current+1, "to", i)
            parent[i-1]=current
            current=i-1
            flag[i-1]=1
            check=1
            break
    if(current==0):
        break
    if(check==0):
        print(current+1, "to", 1+parent[current])
        current=parent[current]
    neighbours=arr[current]