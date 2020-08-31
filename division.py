n=int(input())
d=int(input())
value=0
q=0
for i in range(31,-1,-1):
    if(value+(d<<i)<=n):
        value=value+(d<<i)
        q=q|(1<<i)
print(q)
