n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,2**n):
    p=[]
    for j in range(1,n+1):
        if((i &(1<<(j-1)))!=0):
            p.append(l[j-1])
    k.append(p)
print(k)
    
        
    
