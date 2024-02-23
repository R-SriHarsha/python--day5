a=list(map(int,input().split()))
k=int(input())
flag=0
for i in a:
    for j in a:
        if i-j==k:
            flag=1
    
print(flag==1)
        
