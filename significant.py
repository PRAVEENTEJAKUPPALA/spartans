n=int(input())
c=0
while(n%2==0):
    n=n>>1
    c=c+1
k=1<<(c)
print(k)
