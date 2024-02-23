def prime(i):
    for k in range(2,i):
        if i%k==0:
            return False
    return True




d={}
n=int(input())
d[1]="not defined"
for i in range(2,n+1):
    if prime(i):
        d[i]="prime"
    else:
        d[i]="composite"
print(d)
