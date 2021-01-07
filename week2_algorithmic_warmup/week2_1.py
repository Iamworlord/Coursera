x=int(input())
a=[0]*(x+1)
for i in range(x+1):
    if i<=1:
        a[i]=i
    else:
        a[i]=a[i-1]+a[i-2]
print(a[-1])