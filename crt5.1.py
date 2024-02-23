n=int(input("no of items:"))
d={}
for i in range(n):
    nam=input("name:")
    no=input("no:")
    d[nam]=no
m=int(input("no of search items:"))
for j in range(m):
    k=input("enter name to search:")
    if k in d:
        print(f"name:{k} ,no:{d[k]}")
    else:
        print("not found")




















