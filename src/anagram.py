str1=raw_input("Enter string 1")
str2=raw_input("Enter string 2")
l1=len(str1)
l2=len(str2)
a=[]
b=[]
count=0

if(l1==l2):
    for i in range(0,l1):
        a.append(str1[i])
        b.append(str2[i])
    a.sort()
    b.sort()
    for i in range(0,l1):
        if(a==b):
            count+=1
    if(count==l1):
        print("Anagram")

    else:
        print("Not an Anagram")

else:
    print("Not an anagram")
