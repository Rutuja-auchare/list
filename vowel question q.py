# sentence = input("enter your word:")
# for letter in sentence:
#     if letter in "aeiou":
#         print(letter)
# for letter in sentence :
#     if letter not in "aeiou":
#         print(letter)




# a='rutuja'
# v='aeiou'
# count=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j] in v:
#             count+=1
#             print(a[i][j])
#         j=j+1
#     i+=1
#     print(count)    


# a=[12,"alpana",12.32,"neha",12+0j,12]
# i=0
# c=[]
# while i<len(a)
#   if type(a[i])==str:
#       c.append(a[i])
#   i+=1
# print(c)

num1=input("enter any number:")
l1=list(num1)
l=len(l1)
i=0
n={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
while (i<l):
    print(n[int(l1[i])],end="")
    i=i+1
