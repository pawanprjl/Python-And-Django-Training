word = input("Enter a word: ")

def reverse(word):
	temp = ''
	for i in range(len(word)):
		temp = temp+word[-1]
		word = word[:-1]
	return temp

if(reverse(word)==word):
	print(word, "is a palindrome")
else:
	print(word, "is not a palindrome")
