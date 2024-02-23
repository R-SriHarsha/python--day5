#write a python program to maintain students marks database using nested dictionary
n=int(input("no of items:"))
m=int(input("no of subjects"))
d={}
for i in range(n):
    regno=int(input("roll no:"))
    d[regno]={}
    for j in range(m):
        subj=input("subject:")
        d[regno][subj]=int(input("marks:"))
print(d)

