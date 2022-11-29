n=int(input())
l=list(map(int,input().split()))
s=sum(l)
ss=0
for i in range(0,n+1):
    ss+=i
print(ss-s)