n=int(input())
i=int(input())
if(n&(1<<(i-1))==0):
    print("no it is not set")
else:
    print("yes it is set")
    
