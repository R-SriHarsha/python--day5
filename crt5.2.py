n,m=map(int,input().split())
d={}
for i in range(n):
    k,v=map(str,input().split())
    d[k]=v

for j in range(m):
    s,sv=map(str,input().split())
    for i in d:
        if d[i]==sv[:-1]:
            print(f"{s} {sv} #{i}")
            break

    


    
