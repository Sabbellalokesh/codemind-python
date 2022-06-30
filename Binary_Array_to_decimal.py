n=int(input())
l=list(map(int,input().split()))
s=0
j=n-1
for i in range(n):
    if j>=0:
        s=s+(l[i]*(2**j))
    j=j-1
print(s)