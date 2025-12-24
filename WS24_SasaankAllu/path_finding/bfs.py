arr=[[2,3],[1,3,4],[1,2,4,5],[2,5,6],[3,4],[4]]
flag=[1,0,0,0,0,0]
start=1
end=6
current_layer=[1]
while 1:
    next_layer=[]
    for i in current_layer:
        neighbours=arr[i-1]   
        check=0
        for j in neighbours:
            if flag[j-1]==0:
                print(i, "to", j)
                next_layer.append(j)
                check=1
                flag[j-1]=1
    current_layer=next_layer
    if(check==0):
        break