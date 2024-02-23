#write a python program to print the average of each student marks given in nested dictionary
n,m=map(int,input("enter no of students and no of subjects:").split())
d={}
avg=0
d2={}
for i in range(n):
    regno=int(input("roll no:"))
    d[regno]={}
    sum=0
    for j in range(m):
        subj=input("subject:")
        mar=int(input("marks:"))
        d[regno][subj]=mar
        sum+=mar
    avg=sum/m
    d2[regno]=avg
print(d)
print(d2)
    



        
