#anagram


a,b=map(str,input().split())
print(sorted(list(a)))
print(sorted(list(b)))
if len(a)==len(b):
    if sorted(list(a))==sorted(list(b)):
        
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram")
