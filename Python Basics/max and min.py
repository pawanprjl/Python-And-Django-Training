def maxAndMin(list):
    max= min = list[0]
    
    for i in list:
        if(max<i):
            max = i
        elif(min > i):
            min = i

    return (max,min)

mylist = [44, 35,46,22,78,95,34,22]

maximum, minimum = maxAndMin(mylist)
print("Maximum: ", maximum, "\nMinimum: ", minimum)