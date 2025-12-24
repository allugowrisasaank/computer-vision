x=float(input("Enter x: "))
n=int(input("Enter n: "))
sum=0
denom=1
for i in range(n):
    sum=sum+denom
    denom=denom*x/(i+1)
print(sum)