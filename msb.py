#to find the msb in o(1)
n=int(input())
print((n^(n-1)&n))
