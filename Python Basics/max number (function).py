def max(x, y, z):
	if(x > y and x > z):
		return 'x is greatest'
	elif (y > x and y > z):
		return 'y is greatest'
	else:
		return 'z is greatest'

ans = max(5,4,8)
print(ans)