# sum-of-n-digits
i=int(input())
if 1<=i<=10000:
    s=0
    for x in range(1,i+1):
        s=x+s
    print(s)
