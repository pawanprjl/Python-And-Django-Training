#input
num = int(input("Enter a num: "))

#initialization of total
total = 0

#while loop terminates when num becomes zero or less than zero
while(num > 0):
	total = total + num
	num = num - 1

#output
print("the total is ", total)


#alternative way


num = int(input("Enter a num: "))

total = 0
count = 0

while(count<=num):
	total = total + count

print("the total is ", total)