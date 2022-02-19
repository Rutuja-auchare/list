# write a code ,that count the numbers between 20 and 40 them print its count
numbers=[50,40,23,70,56,12,5,10,7]
i=0
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<=40:
        print(numbers[i],"it's count")
        i+=1