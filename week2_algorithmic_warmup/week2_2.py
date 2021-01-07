x=int(input())
a=[0]*61
def fn(n):
    a[0]=0
    a[1]=1
    for i in range(2,61):
        a[i]=(a[i-2]+a[i-1])%10
fn(x)
print(a[x%60])