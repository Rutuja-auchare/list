# name=input("enter the name ")
# a=[]
# i=0
# while i<len(name):
#     a.append(name[i])
#     i=i+1
# print(a)
# name1=[]
# i=1
# length=len(a)
# while i<=length:
#     name1.append(a[-i])
#     i=i+1
# print(a)
# print(name1)
# if a==name1:
#     print("yes i is palindrom")
# else:
#     print("not palindrom number")


name=input("enter the name ")
a=[]
i=0
while i<len(name):
    a.append(name[i])
    i=i+1
print(a)
j=0
while j<len(a):
    j+=1
print(a[::-1])
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not")


    # i enjoy being alone my soul is at peace in the silence