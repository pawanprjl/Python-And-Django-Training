#input
num = int(input("Enter a number: "))

#conditional branching
if(num%2==0 and num%3 ==0):
	print(num, "is divisible by 2 and 3")
elif(num%2==0):
	print(num, "is divisible by 2 only")
elif(num%3==0):
	print(num, "is divisible by 3 only")
else:
	print(num, "is not divisible by 2 and 3")
