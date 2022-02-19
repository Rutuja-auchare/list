numbers=[50,40,23,22,21,70,56,12,5,10,7]
i=0
a=[]
count=0
while i< len(numbers):
    if numbers[i]>=20 and numbers[i]<=40:
        a.append(numbers[i])
        count=count+1
    i=i+1
print(count)
print(a)


