i=0
s=[]
num=int(input("no of items"))
for i in range (num):
    val=int(input('"enter elements:"))
    s.append(val)
    i=i-1
print(s)
sum=0
for i in range(num):
    val=int(input("enter items:"))
    s.append(val)
    i=i-1
print(s)
pro=1
for i in range(num):
    pro=pro*s[i]