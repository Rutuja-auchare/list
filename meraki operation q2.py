# names_list=["shivam","neha","alpnana","harshad"]
# print (names_list[1])

# marks_list=[40,60,50,60,70]
# print(marks_list[4])

# temprecture_list=[70.5,14.1,60.5,89.6]
# print (temprecture_list[2])



list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,1,0,6,7]
i=0
a=[]
while i<len(list1):
    m=list1(i)
    if m not in list2:
        a.append(m)
    i=i+1
print(a)