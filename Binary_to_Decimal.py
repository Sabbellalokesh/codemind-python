t=int(input())
for i in range(t):
    n=int(input())
    s=0
    i=0
    while n!=0:
        r=n%10
        s=s+(r*(2**i))
        i+=1
        n=n//10
    print(s)