num = int(input("Enter a number: "))

def reverse(x):
	rev = 0
	while(x>0):
		rev = rev * 10 + x % 10
		x = x // 10
	return rev

if(reverse(num) == num):
	print(num, "is a palindrome number")
else:
	print(num, "is not a palindrome number")