num = int(input("Enter a number: "))

def fibonacci(x):
	if x==0:
		return 0
	elif x == 1:
		return 1
	else:
		return fibonacci(x-1) + fibonacci(x-2)

print(num, "th fibonacci number is: ", fibonacci(num))