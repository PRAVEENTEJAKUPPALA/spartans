#reach the feild
n=int(input())
#max size of the bag be m
m=int(input())
l=list(map(int,input().split()))
c=1
sumy=0
i=0
while(i<n):
    if(sumy==m):
        sumy=0
        c=c+1
    elif(sumy>m):
        sumy=0
        i=i-1
        c=c+1
    else:
        sumy=sumy+l[i]
        i=i+1
if(sumy>m):
    print(c+1)
else:
    print(c)


        
        
    
    
        
    
    
    
