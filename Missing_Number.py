n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,n+1):
    s+=i
print(s-sum(l))