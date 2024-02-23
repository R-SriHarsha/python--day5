#find first repeating character
s=input()
l=[]
for i in s:
    if i not in l:
        l.append(i)
    else:
        print(i)
        break
else:
    print("not found")
