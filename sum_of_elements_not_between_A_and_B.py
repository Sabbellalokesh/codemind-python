n=int(input())
l=list(map(int,input().split()))
s=0
a,b=map(int,input().split())
for i in range(n):
    if l[i]<a or l[i]>b:
        s+=l[i]
print(s)