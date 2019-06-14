num = int(input("Enter a num: "))
ans = 0

while(ans**3 < num):
	ans +=1

if(ans**3 != num):
	print(num, "is not a perfect cube number")
else:
    print(ans, "is cube root of ", num)
